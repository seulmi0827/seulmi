import json
from openai import OpenAI
def classify_type_gpt(user_query):
    user_prompt = f'''
    당신은 사용자의 질문을 분류하는 판별가 입니다. 
    분류는 다음과 같습니다.
    type : motivation, ability, etc
    1개의 질문은 1개의 종류로만 분류됩니다.

    사용자의 질문 : {user_query}
    
    출력은 반드시 json형태로 마크다운 없이 반환하세요.
    'type' : 분류
    '''
    client = OpenAI()

    for _ in range(5): 
        try:
            response = client.chat.completions.create(model = "gpt-4o",
                                                messages = [
                                                    {'role': 'user', 'content': user_prompt},
                                                    ],
                                                max_tokens=150,
                                                temperature=0
                                                )
            classified_type = json.loads(response.choices[0].message.content)['type'] #type:ignore
            break
        except:
            print("판별 실패")
    return classified_type
