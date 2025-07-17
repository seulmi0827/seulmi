import streamlit as st

cols_1 = st.columns(4)
with cols_1[0]:
    inter_cols = st.columns(2)
    with inter_cols[0] :
        st.write('')
        st.markdown('![장바구니](https://placehold.co/40x40)')
    with inter_cols[1] :
        st.caption('All Spendings')
        st.write('**$574.34**')

with cols_1[1]:
    inter_cols = st.columns(2)
    with inter_cols[0] :
        st.caption('Spent this month')
        st.write('**$574.34**')
    with inter_cols[1] :
        st.write('')
        st.markdown('![그래프1](https://placehold.co/40x40)')

with cols_1[2]:
    inter_cols = st.columns(2)
    with inter_cols[0] :
        st.write('')
        st.markdown('![그래프2](https://placehold.co/40x40)')
    with inter_cols[1] :
        st.caption('Earnings')
        st.write('**$350.40**')

with cols_1[3]:
    inter_cols = st.columns(3)
    with inter_cols[0]:
        st.write('')
        st.markdown('![장바구니](https://placehold.co/40x40)')
    with inter_cols[1]:
        st.caption('New clients')
        st.write('**321**')
    with inter_cols[2]:
        st.write('')
        st.markdown('![장바구니](https://placehold.co/40x40)')


cols_2 = st.columns(3)
with cols_2[0]:
    st.metric('This month earnings', '$682.5', 2.45)
    st.write('')
    st.markdown('![장바구니](https://placehold.co/200x80)')

with cols_2[1]:
    st.metric('This month earnings', '$682.5')
    st.write('')
    st.write('')
    st.markdown('![그래프1](https://placehold.co/200x80)')

with cols_2[2]:
    st.write('**Your Transfers**')
    inner_cols1 = st.columns(3)
    with inner_cols1[0]:
        st.markdown('![프로필사진](https://placehold.co/40x40)')
    with inner_cols1[1]:
        st.write('**from Alex Manda**')
        st.caption('Today')
    with inner_cols1[2]:
        st.markdown('+$50')
        
    inner_cols2 = st.columns(3)
    with inner_cols2[0]:
        st.markdown('![프로필사진](https://placehold.co/40x40)')
    with inner_cols2[1]:
        st.write('**To Laura Santos**')
        st.caption('Today')
    with inner_cols2[2]:
        st.markdown('-$30')
        
    inner_cols3 = st.columns(3)
    with inner_cols3[0]:
        st.markdown('![프로필사진](https://placehold.co/40x40)')
    with inner_cols3[1]:
        st.write('**from Jadon S.**')
        st.caption('Today')
    with inner_cols3[2]:
        st.markdown('+$20')

cols_3 = st.columns(2)

with cols_3[0]:
    st.caption('Total Spent')
    st.write('**$682.5**')
    st.markdown('![프로필사진](https://placehold.co/400x200)')
    
with cols_3[1]:
    st.write('**Your transactions**')
    inner_cols11 = st.columns(2)
    with inner_cols11[0]:
        st.markdown('![프로필사진](https://placehold.co/40x40)')
    with inner_cols11[1]:
        st.write('**Public Transport**')
        st.caption('22 September 2020')
        
    inner_cols22 = st.columns(2)
    with inner_cols22[0]:
        st.markdown('![프로필사진](https://placehold.co/40x40)')
    with inner_cols22[1]:
        st.write('**Grocery Store**')
        st.caption('22 September 2020')
        
    inner_cols33 = st.columns(2)
    with inner_cols33[0]:
        st.markdown('![프로필사진](https://placehold.co/40x40)')
    with inner_cols33[1]:
        st.write('**Public Transport**')
        st.caption('22 September 2020')
        
