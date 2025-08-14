from langchain_core.prompts import PromptTemplate


def select_prompt(classified_type):
    prompt_mtv = PromptTemplate.from_template(
        """당신은 자기소개서 작성에 특화된 작가입니다.
        다음의 정보를 참고하여 지원동기를 공백 포함 500자 이내로 작성하세요. 
        문장 작성 시 '저는'이라는 단어는 제외하세요.
        객관적이고 전문적인 태도를 유지하되, 자신감과 긍정적인 에너지를 드러내야 합니다. 
        지나치게 격식을 차린 딱딱한 어조보다는, 강점과 경험을 진솔하게 전달하며 회사와 직무에 대한 깊은 이해를 바탕으로 전문성을 표현하세요.
        내 정보: {my_info_context} 
        채용 정보: {recruit_info} 
        회사 정보: {corp_info}"""
    )

    # ability일때 프롬프트
    prompt_abl = PromptTemplate.from_template(
        """당신은 자기소개서 작성에 특화된 작가입니다.
        다음의 정보를 참고하여 역량을 공백 포함 500자 이내로 작성하세요. 
        문장 작성 시 '저는'이라는 단어는 제외하세요.
        객관적이고 전문적인 태도를 유지하되, 자신감과 긍정적인 에너지를 드러내야 합니다. 
        지나치게 격식을 차린 딱딱한 어조보다는, 강점과 경험을 진솔하게 전달하며 회사와 직무에 대한 깊은 이해를 바탕으로 전문성을 표현하세요.
        내 정보: {my_info_context} 
        채용 정보: {recruit_info} 
        회사 정보: {corp_info}"""
    )
    # ect일때 프롬프트
    prompt_ect = PromptTemplate.from_template(
        """당신은 자기소개서 작성에 특화된 작가입니다.
        다음의 정보를 참고하여 자기소개서를 공백 포함 500자 이내로 작성하세요. 
        문장 작성 시 '저는'이라는 단어는 제외하세요.
        객관적이고 전문적인 태도를 유지하되, 자신감과 긍정적인 에너지를 드러내야 합니다. 
        지나치게 격식을 차린 딱딱한 어조보다는, 강점과 경험을 진솔하게 전달하며 회사와 직무에 대한 깊은 이해를 바탕으로 전문성을 표현하세요.
        내 정보: {my_info_context} 
        채용 정보: {recruit_info} 
        회사 정보: {corp_info}"""
    )
    if classified_type == "motivation":
        generate_prompt = prompt_mtv
    elif classified_type =="ability":
        generate_prompt = prompt_abl
    elif classified_type == "etc":
        generate_prompt = prompt_ect
    return generate_prompt