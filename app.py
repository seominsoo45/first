import math
import streamlit as st
import sqlite3
import pandas as pd
import os.path

con = sqlite3.connect('db.db')
cur = con.cursor()

def login_user(id, pw):
    cur.execute(f"SELECT * "
                f"FROM users "
                f"WHERE id='{id}' and pwd = '{pw}'")
    return cur.fetchone()

menu = st.sidebar.selectbox('MENU', options=['로그인','회원가입','회원목록','인원별 석차등급 범위'])

if menu == '로그인':
    st.subheader('로그인')
    login_id = st.text_input('아이디', placeholder='아이디를 입력하세요')
    login_pw = st.text_input('비밀번호',
                             placeholder='비밀번호를 입력하세요',
                             type='password')
    login_btn = st.button('로그인')
    st.sidebar.subheader('로그인')
    if login_btn:
        user_info = login_user(login_id, login_pw)
        file_name = './img/'+user_info[0]+'.jpeg'

        if os.path.exists(file_name):
            st.sidebar.image(file_name)
            st.sidebar.write(user_info[4], '님 환영합니다.')
        else:
            st.sidebar.write(user_info[4], '님 환영합니다.')

if menu == '회원가입':
    st.subheader('회원가입')
    st.info('다음 양식을 모두 입력후 회원가입 버튼을 클릭하세요.')
    uid = st.text_input('아이디', max_chars=10, placeholder='새로운 아이디를 입력하세요')
    uname = st.text_input('이름', max_chars=10, placeholder='이름을 입력하세요')
    upw = st.text_input('비밀번호', type='password', placeholder='새로운 비밀번호를 입력하세요')
    upw_chk = st.text_input('비밀번호 확인', type='password', placeholder='비밀번호를 다시 입력하세요')
    uage = st.number_input('나이', step = 1)
    ugender = st.radio('성별', options=['여','남'], horizontal=True)
    ubtn = st.button('회원가입')

    if ubtn:
        if upw != upw_chk:
            st.error('비밀번호가 일치하지않습니다.')
            st.stop()

        cur.execute(f"INSERT INTO users(id, pwd, gender, age, name) "
                    f"VALUES('{uid}','{upw}','{ugender}',{uage},'{uname}')")
        st.success('회원가입에 성공했습니다.')
        con.commit()

if menu == '회원목록':
    st.subheader('회원목록')
    df = pd.read_sql('SELECT name,age,gender FROM users', con)
    st.dataframe(df)
    st.sidebar.write('회원목록')

if menu == '인원별 석차등급 범위':
    st.warning('*주의: 학교의 산출 기준과 차이가 있을 수 있습니다.')
    st.subheader('인원별 석차 등급 범위')
    rank = st.number_input('자신의 수강과목의 학생수를 입력하세요', step=1)
    rank_btn = st.button('확인')
    if rank_btn:
        b = math.ceil((rank*4)//100)
        st.write('1등급 = ', 1,'~',b,'등 까지','/','인원:',math.ceil((rank*4)//100),'명','/','반영 비율: 4%')
        c = math.ceil((rank*11)//100)
        st.write('2등급 = ', 1 + b,'~',c,'등 까지','/','인원:',math.ceil((rank*7)//100),'명','/','반영 비율: 7%')
        d = math.ceil((rank*23)//100)
        st.write('3등급 = ', 1 + c,'~',d,'등 까지','/','인원:',math.ceil((rank*12)//100),'명','/','반영 비율: 12%')
        e = math.ceil((rank*40)//100)
        st.write('4등급 = ', 1 + d,'~',e,'등 까지','/','인원:',math.ceil((rank*17)//100),'명','/','반영 비율: 17%')
        f = math.ceil((rank*60)//100)
        st.write('5등급 = ', 1 + e,'~',f,'등 까지','/','인원:',math.ceil((rank*20)//100),'명','/','반영 비율: 20%')
        g = math.ceil((rank*77)//100)
        st.write('6등급 = ', 1 + f,'~',g,'등 까지','/','인원:',math.ceil((rank*17)//100),'명','/','반영 비율: 17%')
        h = math.ceil((rank*89)//100)
        st.write('7등급 = ', 1 + g,'~',h,'등 까지','/','인원:',math.ceil((rank*12)//100),'명','/','반영 비율: 12%')
        i = math.ceil((rank*96)//100)
        st.write('8등급 = ', 1 + h,'~',i,'등 까지','/','인원:',math.ceil((rank*7)//100),'명','/','반영 비율: 7%')
        j = math.ceil((rank*100)//100)
        st.write('9등급 = ', 1 + i,'~',j,'등 까지','/','인원:',math.ceil((rank*4)//100),'명','/','반영 비율: 4%')
