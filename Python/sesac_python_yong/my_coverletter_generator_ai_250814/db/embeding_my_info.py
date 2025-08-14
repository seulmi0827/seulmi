from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

DB_PATH = r"C:\Users\seul\Desktop\yong\only-pull-me\5_생성형AI\실습\db250811"

text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=0)
recruit_loader = TextLoader(r"C:\Users\seul\Desktop\yong\only-pull-me\5_생성형AI\실습\db250811\my_info_sample.txt")
recruit_doc = recruit_loader.load_and_split(text_splitter)
texts = [doc.page_content for doc in recruit_doc]
metadatas = [doc.metadata for doc in recruit_doc]

chroma_db = Chroma.from_texts(
    texts=texts,
    metadatas=metadatas,
    embedding=OpenAIEmbeddings(),
    collection_name="my_info_db",
    persist_directory=DB_PATH
)