from openai import OpenAI
from langchain_community.utilities import GoogleSerperAPIWrapper # type: ignore
import json
def refine_searchresult_gpt(search_result, info_type):
    client = OpenAI()
    user_prompt = f'''
    당신은 검색 결과를 정제하는 인사담당자입니다. 
    회사에 대한 검색 결과를 정리해 주세요.
    - {info_type}에 관한 내용을 추출하세요.
    검색결과: {search_result}
    
    출력은 반드시 json형태로, 반드시 마크다운 없이 반환하세요.
    검색 결과에 원하는 정보가 없으면 "x"로 채우세요.
    {{
      "{info_type}": "정리 내용"
    }}'''

    try:
        for _ in range(5):
            response = client.chat.completions.create(model = "gpt-4o-mini",
                                            messages = [
                                                {'role': 'user', 'content': user_prompt},
                                                ],
                                            max_tokens=150,
                                            temperature=0)
            classified_category = json.loads(response.choices[0].message.content) # type: ignore
            break
    except:
        classified_category = '판별 실패'
        
    return classified_category


def search_w_retry(max_try_cnt,corp_name):
    for _ in range(max_try_cnt):
        search = GoogleSerperAPIWrapper()
           
        try:
            corp_intro_result = search.run(corp_name + ' 회사 소개서')
            corp_intro = refine_searchresult_gpt(corp_intro_result, 'corp_intro')
            break
        except:
            corp_intro = '생성 실패'

    for _ in range(max_try_cnt):    
        try:
            ideal_talent_result = search.run(corp_name + ' 인재상')
            ideal_talent = refine_searchresult_gpt(ideal_talent_result, 'ideal_talent')
            break
        except:
            ideal_talent = '생성 실패'

    for _ in range(max_try_cnt):    
        try:
            main_business_result = search.run(corp_name + ' 주요 사업')
            main_business = refine_searchresult_gpt(main_business_result, 'main_business')
            break
        except:
            main_business = '생성 실패'

    for _ in range(max_try_cnt):    
        try:
            esg_activity_result = search.run(corp_name + ' esg 활동')
            esg_activity = refine_searchresult_gpt(esg_activity_result, 'esg_activity')
            break
        except:
            esg_activity = '생성 실패'
    return corp_intro,ideal_talent,main_business,esg_activity