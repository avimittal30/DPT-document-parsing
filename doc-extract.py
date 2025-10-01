from agentic_doc.parse import parse

import os
from dotenv import load_dotenv
load_dotenv()
# Parse a local file

import re
os.environ['VISION_AGENT_API_KEY']=os.getenv("LANDING_API_KEY")

file_path="C:\\tutorials\\agentic-doc-extraction\\IBM_Annual_report.pdf"


results = parse(file_path)
for idx, result in enumerate(results):
    with open(f"results/result_{idx+1}.md", "w", encoding="utf-8") as f:
        f.write(result.markdown)



with open("results/result_1.md", "r", encoding="utf-8") as f:
    markdown_content = f.read()

# Find all <table>...</table> blocks
tables = re.findall(r"<table.*?>.*?</table>", markdown_content, re.DOTALL)

# Convert each table to a pandas DataFrame
all_dataframes = []
for table_html in tables:
    dfs = pd.read_html(table_html)
    all_dataframes.extend(dfs)
