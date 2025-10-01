# agentic-doc PDF Table Extraction

This project demonstrates how to use the `agentic-doc` library to extract structured information and tables from PDF documents using Python.

## Features
- Extracts tables and structured data from PDFs
- Saves extracted content as markdown files
- Converts HTML tables in markdown to pandas DataFrames

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/avimittal30/DPT-document-parsing.git
   cd DPT-document-parsing
   ```

2. **Install dependencies:**
   ```powershell
   pip install agentic-doc pandas lxml --trusted-host pypi.org --trusted-host files.pythonhosted.org
   ```

3. **Set up your API key:**
   - Get your API key from [Landing AI](https://landing.ai/).
   - Add it to a `.env` file in your project root:
     ```env
     LANDING_API_KEY=your_api_key_here
     ```
## Notes
- The API key is required for document parsing and is obtained from [Landing AI](https://landing.ai/).
- Results are saved in the `results` directory as markdown files.
- Extracted tables are available as pandas DataFrames for further analysis.

