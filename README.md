# RiskRem

A Python-based automation pipeline that leverages a 100% local, air-gapped LLM and Retrieval-Augmented Generation (RAG) to instantly answer enterprise security questionnaires.

This tool eliminates the manual overhead of filling out massive vendor assessment spreadsheets while guaranteiting zero data leakage. By utilizing local models, sensitive network diagrams, access control policies, and compliance postures are never exposed to public APIs or cloud providers.

## Key Features

- **100% Local LLM**: Runs entirely on-premises, ensuring that sensitive data never leaves your environment.
- **Retrieval-Augmented Generation (RAG)**: Combines the power of LLMs with a local knowledge base to provide accurate and context-aware responses.
- **Automated Questionnaire Filling**: Instantly populates security assessment forms, saving time and reducing human error.
- **Customizable Knowledge Base**: Easily integrate your own documents, policies, and diagrams to enhance the model's understanding of your specific security posture.

## prerequisites

- Python 3.x
- Ollama (for local LLM hosting)
  -AnythingLLM: Configured locally with an active workspace and embedded security documentation.

## Installation

1. Clone the repository:

   ```bash
   git clone
   ```

2. Navigate to the project directory:

   ```bash
   cd RiskRem
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Environment Variables:
   - `OLLAMA_HOST`: The URL of your local Ollama instance (e.g., `http://localhost:11434`).
   - `ANYTHINGLLM_WORKSPACE`: The name of your AnythingLLM workspace containing the embedded security documentation.
   - `anythingllm_api_key`: Your API key for accessing the AnythingLLM workspace.

## Usage

Export the enterprise security questionnaire into a single-column file named client_questions.csv (with the header Original Question).

Place the file in the project directory.

Run the processing script:

```bash
python process.py
```

The script will read the questions from `client_questions.csv`, use the local LLM and RAG to generate answers, and output the results.

## Security and Privacy

- RiskRem is designed with security and privacy in mind. By running entirely on-premises, it ensures that sensitive information never leaves your environment. All processing is done locally, and no data is sent to external servers or cloud providers.

- This repo uses a .gitignore file to exclude sensitive files and directories from being tracked by Git. Make sure to review the .gitignore file and add any additional sensitive files or directories that should not be included in version control.
