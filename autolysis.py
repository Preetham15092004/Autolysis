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

# Import necessary libraries
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from PIL import Image

# --- VALIDATE INPUT AND SETUP ENVIRONMENT ---
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

# Check for AI Proxy Token
try:
    ai_proxy_token = os.environ["AIPROXY_TOKEN"]
    print(f"AIPROXY_TOKEN detected: {ai_proxy_token[:10]}...")  # Only print part of the token for security
except KeyError:
    print("Error: AIPROXY_TOKEN environment variable is not set.")
    sys.exit(1)

# --- LOAD DATASET ---
try:
    data = pd.read_csv(dataset_file)
    print(f"Dataset {dataset_file} loaded successfully.")
except Exception as e:
    print(f"Error loading dataset: {e}")
    sys.exit(1)

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# --- PERFORM GENERIC ANALYSIS ---
def perform_generic_analysis(data):
    """Perform generic analysis on the dataset."""
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

# --- VISUALIZATION FUNCTIONS ---
def visualize_correlation_matrix(corr_matrix, filename):
    """Visualize the correlation matrix as a heatmap with tight layout."""
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True, square=True)
    plt.title("Correlation Matrix Heatmap")
    plt.tight_layout()  # Adjust layout to avoid clipping
    plt.savefig(filename)
    plt.close()

def visualize_numeric_distributions(data, column, filename):
    """Visualize and save numeric column distribution with tight layout."""
    plt.figure(figsize=(8, 6))
    sns.histplot(data[column].dropna(), kde=True, bins=30, color="blue")
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.tight_layout()  # Adjust layout to avoid clipping
    plt.savefig(filename)
    plt.close()

def visualize_categorical_counts(data, column, filename):
    """Visualize and save top 10 categories in a column with tight layout."""
    sanitized_filename = filename.replace(" ", "_")
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=data[column].value_counts().index[:10],
        y=data[column].value_counts().values[:10],
        palette="viridis",
    )
    plt.xticks(rotation=45, ha="right")
    plt.title(f"Top 10 Categories in {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.tight_layout()  # Adjust layout to avoid clipping
    plt.savefig(sanitized_filename)
    plt.close()


def create_visualizations(data, data_summary, output_dir):
    """Generate visualizations and save them in the output directory."""
    charts = []
    numeric_cols = data.select_dtypes(include=["number"]).columns
    categorical_cols = data.select_dtypes(include=["object", "category"]).columns

    # Correlation matrix
    if "correlations" in data_summary:
        corr_matrix = pd.DataFrame(data_summary["correlations"])
        if not corr_matrix.empty:
            filename = os.path.join(output_dir, "correlation_matrix.png")
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            visualize_correlation_matrix(corr_matrix, filename)
            charts.append(filename)

    # Numeric distributions
    for col in numeric_cols[:3]:
        filename = os.path.join(output_dir, f"{col}_distribution.png")
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        visualize_numeric_distributions(data, col, filename)
        charts.append(filename)

    # Categorical distributions
    for col in categorical_cols[:3]:
        filename = os.path.join(output_dir, f"{col}_bar_chart.png")
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        visualize_categorical_counts(data, col, filename)
        charts.append(filename)

    return charts

# --- RESIZE IMAGES ---
def resize_images(image_files, size=(512, 512)):
    """Resize images to the given size and sanitize filenames."""
    resized_files = []
    for file in image_files:
        try:
            # Sanitize filename
            sanitized_file = file.replace(" ", "_").replace("(", "").replace(")", "")
            if sanitized_file != file and not os.path.exists(sanitized_file):
                os.rename(file, sanitized_file)

            # Open, resize, and save the image
            img = Image.open(sanitized_file)
            img = img.resize(size)
            resized_file = sanitized_file.replace(".png", "_resized.png")
            img.save(resized_file)
            resized_files.append(resized_file)
        except Exception as e:
            print(f"Error resizing image {file}: {e}")
    return resized_files


# --- QUERY LLM FOR INSIGHTS ---
def query_llm(prompt):
    """Query the LLM for insights."""
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

# --- GENERATE STORY ---
def generate_story(data_summary, insights, resized_charts, output_dir):
    """Generate a Markdown story using data summary and insights."""
    chart_refs = "\n".join([
        f"![Chart]({os.path.relpath(chart, start=output_dir)})".replace("\\", "/") for chart in resized_charts
    ])
    prompt = f"""
Write a Markdown report:
- Data Summary: {data_summary}
- Insights: {insights}
Include these charts: {chart_refs}
"""
    return query_llm(prompt)

# --- SAVE README.md ---
def save_readme(content, output_dir):
    """Save the story as README.md in the output directory."""
    try:
        with open(os.path.join(output_dir, "README.md"), "w") as f:
            f.write(content)
        print(f"README.md created in {output_dir}.")
    except Exception as e:
        print(f"Error saving README.md: {e}")

# --- MAIN WORKFLOW ---
data_summary = perform_generic_analysis(data)
charts = create_visualizations(data, data_summary, output_dir)
resized_charts = resize_images(charts)
insights = query_llm(f"Analyze this dataset summary: {data_summary}")
story = generate_story(data_summary, insights, resized_charts, output_dir)

# Save README.md
save_readme(story, output_dir)

print(f"Analysis complete. Outputs saved in {output_dir}.")
