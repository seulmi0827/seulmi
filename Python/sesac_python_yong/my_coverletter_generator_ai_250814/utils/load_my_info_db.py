from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

def load_my_info_db():
    DB_PATH = r"C:\Users\seul\Desktop\yong\only-pull-me\5_생성형AI\실습\db250811"
    persist_db = Chroma(
        persist_directory=DB_PATH,
        embedding_function=OpenAIEmbeddings(),
        collection_name="my_info_db",
    )
    return persist_db