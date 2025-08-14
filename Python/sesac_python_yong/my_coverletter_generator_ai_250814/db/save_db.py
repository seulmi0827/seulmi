
import streamlit as st
from db.get_connection import get_connection

def save_session():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            sql = "INSERT INTO session () VALUES ()"
            cur.execute(sql)
            conn.commit()
            session_id = cur.lastrowid
            st.session_state['session_id'].append(session_id)
        return session_id
    finally:
        conn.close()

def save_corp(corp_name, corp_intro, ideal_talent, main_business, esg_activity):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            # 1) corp_name 저장 (중복 방지)
            cur.execute("SELECT corp_name_id FROM corp_name WHERE corp_name = %s", (corp_name,))
            result = cur.fetchone()
            if result:
                corp_name_id = result["corp_name_id"]
            else:
                cur.execute("INSERT INTO corp_name (corp_name) VALUES (%s)", (corp_name,))
                corp_name_id = cur.lastrowid

            # 2) corp_info 저장 (corp_name_id 기준 중복 방지)
            cur.execute("SELECT corp_info_id FROM corp_info WHERE corp_name_id = %s", (corp_name_id,))
            info_result = cur.fetchone()
            if not info_result:
                cur.execute("""
                    INSERT INTO corp_info (corp_name_id, corp_intro, ideal_talent, main_business, esg_activity)
                    VALUES (%s, %s, %s, %s, %s)
                """, (corp_name_id, corp_intro, ideal_talent, main_business, esg_activity))

            conn.commit()
        return corp_name_id
    finally:
        conn.close()

def save_chat(session_id, corp_name):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            # 1) corp_name_id 조회
            cur.execute("SELECT corp_name_id FROM corp_name WHERE corp_name = %s", (corp_name,))
            result = cur.fetchone()
            if not result:
                st.warning(f"저장 실패: '{corp_name}'에 해당하는 corp_name_id가 없습니다.")
                return
            corp_name_id = result['corp_name_id']

            # recruit_info 저장
            for i in range(len(st.session_state['recruit_info'])):
                cur.execute("INSERT INTO recruit_info (session_id, corp_name_id, recruit_info) VALUES (%s, %s, %s)", 
                            (session_id, corp_name_id, st.session_state['recruit_info'][i]))
                recruit_info_id = cur.lastrowid

                # user_request 저장
                cur.execute("INSERT INTO user_request (corp_name_id, recruit_info_id, my_request) VALUES (%s, %s, %s)", 
                            (corp_name_id, recruit_info_id, st.session_state['my_request'][i]))
                user_request_id = cur.lastrowid

                # classified_type 저장
                cur.execute("INSERT INTO classified_type (user_request_id, classified_type) VALUES (%s, %s)", 
                            (user_request_id, st.session_state['classified_type'][i]))

                # cover_letter 저장
                cur.execute("INSERT INTO cover_letter (user_request_id, my_cover_letter) VALUES (%s, %s) ", 
                            (user_request_id, st.session_state['my_cover_letter'][i]))

                # revise_user_request / revised_cover_letter 저장 (있는 경우만)
                if len(st.session_state['my_revise_request']) > i:
                    cur.execute(" INSERT INTO revise_user_request (my_cover_letter_id, revise_user_request) VALUES (LAST_INSERT_ID(), %s)", 
                                (st.session_state['my_revise_request'][i],))
                    revise_user_request_id = cur.lastrowid

                    if len(st.session_state['my_revised_cover_letter']) > i:
                        cur.execute("INSERT INTO revised_cover_letter (revise_user_request_id, revised_cover_letter) VALUES (%s, %s)", 
                                    (revise_user_request_id, st.session_state['my_revised_cover_letter'][i]['revised']))
            # chat_history 저장
            for chat in st.session_state['chat_history']:
                cur.execute("INSERT INTO chat_history (session_id, chat_history) VALUES (%s, %s) ", 
                            (session_id, chat['content'][:10]))  # VARCHAR(10) 제한 때문에 앞 10자만

            conn.commit()
    finally:
        conn.close()