from dotenv import load_dotenv;
load_dotenv();
from pathlib import Path;
from langchain_community.document_loaders import PyPDFLoader;
from langchain_text_splitters import RecursiveCharacterTextSplitter;
from langchain_openai import OpenAIEmbeddings;
from langchain_qdrant import QdrantVectorStore;

file_path = Path(__file__).parent / "JavaScript.pdf";

loader = PyPDFLoader(file_path=file_path);
docs = loader.load();

doc_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)

chunks = doc_splitter.split_documents(docs);

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url= "http://localhost:6333",
    collection_name="js_doc"
)

print("indexing done.....")
