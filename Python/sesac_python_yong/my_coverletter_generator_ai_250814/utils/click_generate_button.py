import streamlit as st
from utils.streamlit_layout import create_st_session_state
from utils.load_my_info_db import load_my_info_db
from ai.classify_type_gpt import classify_type_gpt
from db.get_connection import get_connection
from ai.refine_searchresult_gpt import search_w_retry
from db.save_db import save_corp
import json
from ai.select_prompt import select_prompt
from ai.create_cover_letter_llm import create_cover_letter_llm

def click_generate_button(corp_name, recruit_info, my_request,status_placeholder):
    if 'chat_history' not in st.session_state or st.session_state['chat_history'] == []:
        create_st_session_state()
        
    st.session_state['corp_name'].append(corp_name)
    st.session_state['recruit_info'].append(recruit_info)
    st.session_state['my_request'].append(my_request)

    # 1단계: 내 정보 로드
    status_placeholder.info("📂 내 정보 Vector DB 불러오는 중...")
    persist_db = load_my_info_db()

    # 2단계: 질문 분류
    status_placeholder.info("🤖 질문 유형 분류 중...")
    classified_type = classify_type_gpt(my_request)
    st.session_state['classified_type'].append(classified_type)

    # 3단계: 기업 정보 수집
    status_placeholder.info(f"🔍 '{corp_name}' 기업 정보 수집 중...")
    max_try_cnt = 3

    # DB에서 corp_name이 이미 있는지 확인
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT corp_name_id FROM corp_name WHERE corp_name = %s", (corp_name,))
        existing_corp = cur.fetchone()
    conn.close()

    if existing_corp:  # sql로 불러온 목록에 존재하는 경우
        corp_name_id = existing_corp["corp_name_id"]
        # 기존 corp_info 불러오기
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("""
                SELECT corp_intro, ideal_talent, main_business, esg_activity
                FROM corp_info
                WHERE corp_name_id = %s """, 
                (corp_name_id,))
            corp_info_row = cur.fetchone()
        conn.close()

        corp_intro = corp_info_row["corp_intro"]# type: ignore
        ideal_talent = corp_info_row["ideal_talent"]# type: ignore
        main_business = corp_info_row["main_business"]# type: ignore
        esg_activity = corp_info_row["esg_activity"]# type: ignore

    else:  # sql로 불러온 목록에 존재하지 않는 경우 새로 검색
        corp_intro, ideal_talent, main_business, esg_activity = search_w_retry(max_try_cnt, corp_name)
        # DB에 insert
        corp_name_id = save_corp(
            corp_name,
            corp_intro.get("corp_intro", "") if isinstance(corp_intro, dict) else corp_intro,
            ideal_talent.get("ideal_talent", "") if isinstance(ideal_talent, dict) else ideal_talent,
            main_business.get("main_business", "") if isinstance(main_business, dict) else main_business,
            esg_activity.get("esg_activity", "") if isinstance(esg_activity, dict) else esg_activity
        )
    corp_info_ls = [corp_intro, ideal_talent, main_business, esg_activity]
    st.session_state['corp_intro'].append(corp_intro) #할당은 그대로 해야하니까 if문 밖에서 session_state에 할당
    st.session_state['ideal_talent'].append(ideal_talent)
    st.session_state['main_business'].append(main_business)
    st.session_state['esg_activity'].append(esg_activity)
    corp_info = json.dumps(corp_info_ls, ensure_ascii=False).replace('{','').replace('}','').replace('[','').replace(']','')
    st.session_state['corp_info'].append(corp_info)

    # 4단계: 프롬프트 선택
    status_placeholder.info(f"✏️ '{classified_type}' 유형에 맞는 프롬프트 선택 중...")
    generate_prompt = select_prompt(classified_type)

    # 5단계: 자소서 생성
    status_placeholder.info(f"📝 {classified_type} 자소서 초안 생성 중...")
    my_cover_letter = create_cover_letter_llm(generate_prompt,persist_db,classified_type,recruit_info,corp_info)
    st.session_state['my_cover_letter'].append(my_cover_letter)
    st.session_state['chat_history'].append({'role':'ai','content':my_cover_letter})
    status_placeholder.info("✅ 결과 출력 완료!")