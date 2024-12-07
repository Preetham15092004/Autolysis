# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pandas",
#   "matplotlib",
#   "seaborn",
#   "requests",
#   "pillow",
# ]
# ///

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from PIL import Image

# Validate command-line arguments
if len(sys.argv) != 2:
    print("Usage: uv run autolysis.py <dataset.csv>")
    sys.exit(1)

# Dataset file passed as argument
dataset_file = sys.argv[1]
dataset_name = os.path.splitext(os.path.basename(dataset_file))[0]
output_dir = dataset_name

# Check if the file exists
if not os.path.isfile(dataset_file):
    print(f"File {dataset_file} not found.")
    sys.exit(1)

import os
import sys

try:
    ai_proxy_token = os.environ["AIPROXY_TOKEN"]
    print(f"AIPROXY_TOKEN detected: {ai_proxy_token[:10]}...")  # Only print part of the token for security
except KeyError:
    print("Error: AIPROXY_TOKEN environment variable is not set.")
    sys.exit(1)

# Load the dataset
try:
    data = pd.read_csv(dataset_file)
    print(f"Dataset {dataset_file} loaded successfully.")
except Exception as e:
    print(f"Error loading dataset: {e}")
    sys.exit(1)

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Perform generic analysis
def perform_generic_analysis(data):
    analysis = {
        "shape": data.shape,
        "missing_values": data.isnull().sum().to_dict(),
        "dtypes": data.dtypes.astype(str).to_dict(),
        "head": data.head().to_dict(orient="list"),
    }
    numeric_cols = data.select_dtypes(include=["number"])
    if not numeric_cols.empty:
        analysis["correlations"] = numeric_cols.corr().to_dict()
    return analysis

# Generate visualizations
def visualize_correlation_matrix(corr_matrix, filename):
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True, square=True)
    plt.title("Correlation Matrix Heatmap")
    plt.savefig(filename)
    plt.close()

def visualize_numeric_distributions(data, column, filename):
    plt.figure(figsize=(8, 6))
    sns.histplot(data[column].dropna(), kde=True, bins=30, color="blue")
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.savefig(filename)
    plt.close()

def visualize_categorical_counts(data, column, filename):
    plt.figure(figsize=(10, 6))
    sns.barplot(
    x=data[column].value_counts().index[:10],
    y=data[column].value_counts().values[:10],
    palette="viridis",
    hue=None  # Explicitly set hue to None
)
    plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels
    plt.title(f"Top 10 Categories in {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.savefig(filename)
    plt.close()

def create_visualizations(data, data_summary, output_dir):
    charts = []
    numeric_cols = data.select_dtypes(include=["number"]).columns
    categorical_cols = data.select_dtypes(include=["object", "category"]).columns

    if "correlations" in data_summary:
        corr_matrix = pd.DataFrame(data_summary["correlations"])
        if not corr_matrix.empty:
            filename = os.path.join(output_dir, "correlation_matrix.png")
            visualize_correlation_matrix(corr_matrix, filename)
            charts.append(filename)

    for col in numeric_cols[:3]:
        filename = os.path.join(output_dir, f"{col}_distribution.png")
        visualize_numeric_distributions(data, col, filename)
        charts.append(filename)

    for col in categorical_cols[:3]:
        filename = os.path.join(output_dir, f"{col}_bar_chart.png")
        visualize_categorical_counts(data, col, filename)
        charts.append(filename)

    return charts

# Resize images for README.md
def resize_images(image_files, size=(512, 512)):
    resized_files = []
    for file in image_files:
        img = Image.open(file)
        img = img.resize(size)
        resized_file = file.replace(".png", "_resized.png")
        img.save(resized_file)
        resized_files.append(resized_file)
    return resized_files

def query_llm(prompt):
    url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {ai_proxy_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 2000,
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("choices", [{}])[0].get("message", {}).get("content", "")
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with AI Proxy: {e}")
        return ""


# Generate story
def generate_story(data_summary, insights, resized_charts):
    chart_refs = "\n".join([f"![Chart](./{chart})" for chart in resized_charts])
    prompt = f"""
Write a Markdown report:
- Data Summary: {data_summary}
- Insights: {insights}
Include these charts: {chart_refs}
"""
    return query_llm(prompt)

# Save README.md
def save_readme(content, output_dir):
    try:
        with open(f"{output_dir}/README.md", "w") as f:
            f.write(content)
        print(f"README.md created in {output_dir}.")
    except Exception as e:
        print(f"Error saving README.md: {e}")


# Main workflow
data_summary = perform_generic_analysis(data)
charts = create_visualizations(data, data_summary, output_dir)
resized_charts = resize_images(charts)
insights = query_llm(f"Analyze this dataset summary: {data_summary}")
# Generate story
story = generate_story(data_summary, insights, resized_charts)

# Check if the story (content) is empty
if not story.strip():  # Check if content is empty or whitespace
    print("Error: LLM returned empty content.")
    sys.exit(1)

# Print the story for debugging
print(story)  # Add this line to verify the generated story

# Save the story as README.md
save_readme(story, output_dir)

print(f"Analysis complete. Outputs saved in {output_dir}.")
