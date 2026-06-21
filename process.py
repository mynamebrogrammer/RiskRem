import csv
import requests
import time
import os
from dotenv import load_dotenv


load_dotenv()  
API_KEY = os.getenv("ANYTHINGLLM_API_KEY")
WORKSPACE_SLUG = "my-workspace"
BASE_URL = "http://localhost:3001/api/v1" # Default AnythingLLM port

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

INPUT_FILE = "Documents/client_questions.csv"
OUTPUT_FILE = "completed_questionnaire.csv"

def ask_anythingllm(question):
    """Sends a question to the specific AnythingLLM workspace."""
    url = f"{BASE_URL}/workspace/{WORKSPACE_SLUG}/chat"
    
    payload = {
        "message": question,
        "mode": "query" 
    }
    
    try:
        response = requests.post(url, headers=HEADERS, json=payload)
        
        # If the server rejects the request, print the exact reason!
        if response.status_code == 400:
            return f"Server Rejected: {response.text}"
        # --------------------------
            
        response.raise_for_status()
        data = response.json()
        return data.get("textResponse", "Error: No response text found.")
    except Exception as e:
        return f"Connection Error: {e}"

def process_spreadsheet():
    """Reads questions, gets answers, and writes to a new CSV."""
    print("Starting processing pipeline...")
    
    with open(INPUT_FILE, mode='r', encoding='utf-8') as infile, \
         open(OUTPUT_FILE, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Write headers for the output file
        writer.writerow(["Original Question", "AI Answer", "Requires CySA+ Review"])
        
        # Skip the header row of the input file if it has one
        next(reader, None) 
        
        for row in reader:
            if not row: continue # Skip empty rows
            question = row[0] 
            
            print(f"Processing: {question[:50]}...")
            answer = ask_anythingllm(question)
            
            # Auto-flag for manual review based on your system prompt
            flagged = "YES" if "FLAG FOR CYSA+ REVIEW" in answer else "NO"
            
            writer.writerow([question, answer, flagged])

            # Small delay to keep the local machine from freezing
            time.sleep(1)

    print(f"Pipeline complete! Results saved to {OUTPUT_FILE}")

    print("Opening the completed questionnaire...")
    try: 
        os.startfile(OUTPUT_FILE)
    except Exception as e:
        print(f"Could not open the file automatically: {e}")

if __name__ == "__main__":
    process_spreadsheet()