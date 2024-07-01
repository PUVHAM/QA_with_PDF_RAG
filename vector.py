from file import process_file
from file import embedding
from chainlit.types import AskFileResponse
from langchain_chroma import Chroma
import chainlit as cl

def get_vector_db(file: AskFileResponse):
    docs = process_file(file)
    cl.user_session.set("docs", docs)
    vector_db = Chroma.from_documents(documents=docs,
                                      embedding=embedding)
    return vector_db

    
    
    