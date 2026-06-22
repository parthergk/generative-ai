from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

load_dotenv()
pdf_path = Path(__file__).parent / "JavaScript.pdf";

loader = PyPDFLoader(pdf_path);

docs = loader.load();

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap=300
);

chunks = splitter.split_documents(docs);

embedding_model = OpenAIEmbeddings(
    model= "text-embedding-3-large"
)

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding= embedding_model,
    url= 'http://localhost:6333',
    collection_name="rag_learn"
) 

print("indexing done-----")