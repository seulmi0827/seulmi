from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser


def revise_cover_letter_llm(my_revise_request,my_cover_letter,recruit_info,corp_info):
    
    llm = ChatOpenAI(
        temperature=0.1,
        max_tokens=1024 ,
        model = "gpt-4o-mini",
    ) #.bind(logprobs=True)

    revise_prompt = PromptTemplate.from_template(
        """ 
        당신은 주어진 자기소개서를 채용공고, 회사 정보를 참고하여 평가 항목에 따라 평가하는 인사 담당자 입니다. 
        평가항목은 다음과 같습니다. 
        평가 항목 : 논리성, 구체성, 진정성, 지원 직무와의 연관성
        각 평가 항목을 10점 만점으로 점수를 매기고, 그 이유를 한줄로 서술하세요.
        
        자기소개서 : {my_cover_letter} 
        채용 정보: {recruit_info} 
        회사 정보: {corp_info}
        사용자의 요청 : {my_revise_request}
        
        해당 평가와 사용자의 요청을 바탕으로 자기소개서를 수정하세요.
        수정된 자기소개서는 기존 자기소개서와 어조,구성이 동일해야합니다.
        
        출력은 반드시 json형태로, 반드시 마크다운 없이 반환하세요.
        json 구성 요소 : reason, revised
            reason 구성요소
            - 논리성 : 논리성 점수와 그 이유,
            - 구체성 : 구체성 점수와 그 이유,
            - 진정성 : 진정성0 점수와 그 이유,
            = 지원 직무와의 연관성(점수) : 지원 직무와의 연관성 점수 이유
            revised 구성요소
            - 수정된 자기소개서 전체
        
        """)

    # 체인 구성
    chain = (revise_prompt | llm | JsonOutputParser()
    )

    my_revised_cover_letter = chain.invoke({
        "my_revise_request": my_revise_request,
        "my_cover_letter": my_cover_letter,
        "recruit_info": recruit_info,
        "corp_info": corp_info,
    })
    return my_revised_cover_letter