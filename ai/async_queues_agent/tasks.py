from openai import OpenAI;
from langchain_openai import OpenAIEmbeddings;
from langchain_qdrant import QdrantVectorStore;

client = OpenAI();

ebedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)


vectore_store = QdrantVectorStore.from_existing_collection(
    embedding=ebedding_model,
    url="http://localhost:6333",
    collection_name="js_doc"
)

def process_query(query:str):
    search_result = vectore_store.similarity_search(query=query)

    context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number:  {result.metadata["page_label"]}\nFile Location: {result.metadata["source"]}" for result in search_result ])

    SYSTEM_PROMPT= f"""
    You are an helpfull AI assistent who answeres user query based on the available context 
    retrieved from a PDF file along with page_contents and page number.

    You should only ans the user based on the following context and navigate tthe 
    user to open the rihgt page number to know more.

    Context: {context}
    """


    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role":"user", "content": query}
        ]
    )

    print(response.choices[0].message.content)
    return response.choices[0].message.content;