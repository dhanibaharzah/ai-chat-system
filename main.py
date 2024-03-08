import fitz  # PyMuPDF
import openai

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to ask a question based on the knowledge base (PDF content)
def ask_question(question, knowledge_base_text):
    openai.api_key = 'open-ai-api-key'
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "assistant", "content": knowledge_base_text},
        {"role": "user", "content": question},
    ]
    
    response = openai.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=messages,
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    # Path to your PDF file
    pdf_path = '/Users/ramadhani/Downloads/2022-Starbucks-Global-Environmental-Social-Impact-Report.pdf'
    
    # Extract text from the PDF
    knowledge_base_text = extract_text_from_pdf(pdf_path)
    
    # Preprocess or summarize your text here if necessary
    
    # Prompt for a question
    question = input("What's your question? \n")
    
    # Fetch and print the answer
    answer = ask_question(question, knowledge_base_text)
    print("Answer:", answer)
