import os
from openai import OpenAI
import pandas as pd
import io

# Set your OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = "My_API_KEY"

# Initialize the OpenAI client
client = OpenAI()

# Load the dataset
df = pd.read_csv('C:\\temp_files\\shopping_behavior_updated.csv')

# Get column names
columns = df.columns.tolist()

# Prepare a summary of the data
data_summary = df.describe().to_string()
buffer = io.StringIO()
df.info(buf=buffer)
data_info = buffer.getvalue()
data_head = df.head().to_string()

# Combine the information into a prompt
prompt = f"""
You are a data analyst tasked with exploring trends and gathering insights from a real e-commerce dataset. This is actual data, not hypothetical. Here's the information about the dataset:

Columns present in the dataset: {', '.join(columns)}

Data Description:
{data_summary}

Data Info:
{data_info}

First few rows of the data:
{data_head}

Based ONLY on this information and the columns actually present in the dataset, please provide:
1. Key trends you observe in the data
2. Interesting insights about customer behavior
3. Suggestions for further analysis or visualizations

Please be concise but informative in your response. Do NOT make assumptions about data that isn't present. If you can't answer something because the data is not available, please state that clearly.
"""

# Function to interact with ChatGPT
def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful data analyst working with real data. Only make statements about data that is actually present in the dataset."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Get insights from ChatGPT
insights = chat_with_gpt(prompt)
print("ChatGPT's Analysis:")
print(insights)

# You can add more specific questions or analysis requests here
follow_up_questions = [
    "What are the top 5 product categories by sales volume?",
    "Is there a correlation between age and spending habits?",
    "What day of the week sees the highest sales?"
]

for question in follow_up_questions:
    follow_up_prompt = f"{prompt}\n\nBased ONLY on the data actually present in the dataset, please answer the following question. If the data needed to answer is not available, please state that clearly:\n{question}"
    answer = chat_with_gpt(follow_up_prompt)
    print(f"\nQ: {question}")
    print(f"A: {answer}")