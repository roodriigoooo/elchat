import PyPDF2
import pytesseract
from PIL import Image
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT
from whoosh.qparser import QueryParser
import os

# Define schema for the search index
schema = Schema(title=TEXT(stored=True), content=TEXT)

# Create index directory
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
    ix = create_in("indexdir", schema)
else:
    ix = open_dir("indexdir")

# Extract text from PDFs
def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text() or ''
            return text
    except Exception as e:
        print(f"Error processing PDF {pdf_path}: {e}")
        return ""

# Extract text from text files
def extract_text_from_txt(txt_path):
    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error processing text file {txt_path}: {e}")
        return ""

# Extract text from images using OCR
def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return ""

# Add content to the index
def add_to_knowledge_base(file_path):
    if file_path.endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith('.txt'):
        text = extract_text_from_txt(file_path)
    elif file_path.endswith(('.jpg', '.png')):
        text = extract_text_from_image(file_path)
    else:
        text = ""

    if text:
        writer = ix.writer()
        writer.add_document(title=os.path.basename(file_path), content=text)
        writer.commit()
        print(f"Added {file_path} to knowledge base.")

# Search the knowledge base
def search_knowledge_base(query):
    with ix.searcher() as searcher:
        query_parser = QueryParser("content", ix.schema)
        parsed_query = query_parser.parse(query)
        results = searcher.search(parsed_query, limit=1)  # Get top result
        if results:
            return results[0]['content']
        return None

# Example usage
if __name__ == "__main__":
    add_to_knowledge_base("sample.pdf")
    add_to_knowledge_base("sample.txt")
    add_to_knowledge_base("sample.jpg")