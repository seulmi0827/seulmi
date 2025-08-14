from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_openai import ChatOpenAI


def create_cover_letter_llm(generate_prompt,persist_db,classified_type,recruit_info,corp_info):
    llm = ChatOpenAI(
        temperature=0.1,
        max_tokens=1024,
        model="gpt-4o-mini",
    ) #.bind(logprobs=True)

    retriever = persist_db.as_retriever(search_kwargs={'k': 2})

    # retriever 별도 호출 후 chain에 단순 전달
    docs = retriever.get_relevant_documents(classified_type)
    retrieved_text = "\n".join(doc.page_content for doc in docs[:2])

    # 체인 구성
    chain = generate_prompt | llm | StrOutputParser()

    my_cover_letter = chain.invoke({
        "my_info_context": retrieved_text,
        "recruit_info": recruit_info,
        "corp_info": corp_info,
    })
    return my_cover_letter
