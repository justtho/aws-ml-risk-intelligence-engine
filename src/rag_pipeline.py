import os
import pandas as pd
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI

load_dotenv()

def build_vector_store():
    df = pd.read_csv("data/sample_cases.csv")

    documents = [
        Document(
            page_content=row["text"],
            metadata={"category": row["category"]}
        )
        for _, row in df.iterrows()
    ]

    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(documents, embeddings)

    return vector_store

def semantic_search(query, top_k=3):
    vector_store = build_vector_store()
    results = vector_store.similarity_search(query, k=top_k)

    return [
        {
            "text": doc.page_content,
            "category": doc.metadata["category"]
        }
        for doc in results
    ]

def generate_case_summary(text, prediction, similar_cases):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    context = "\n".join(
        [f"- {case['text']} | Category: {case['category']}" for case in similar_cases]
    )

    prompt = f"""
You are an AI risk analyst.

Analyze the case below and provide:
1. Short summary
2. Risk category
3. Key indicators
4. Recommended next action

Case:
{text}

Predicted category:
{prediction}

Similar historical cases:
{context}
"""

    response = llm.invoke(prompt)
    return response.content