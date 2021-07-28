import streamlit as st
import pandas as pd
import numpy as np


def load_page():
    st.title("Статистика архива")

    st.header("Эта страница техническая. Здесь можно увидеть обзор всех материалов архива")

    col1, col2 = st.beta_columns(2)

    with col1:
        news = pd.read_csv("news_v2.csv")
        date = news["date"].unique()
        dx = news["index"].unique()
        df = pd.read_csv('news_keywords.csv')

        bch = df["topic"].value_counts()
        st.bar_chart(bch, height=800)

        top = [('Владимир', 7546),
               ('ГИБДД по Владимирской области', 7412),
               ('Пожар', 6124),
               ('ДТП', 6042),
               ('Владимир Жириновский', 5234),
               ('Администрация Владимирской области', 5211),
               ('Ковровский район', 5126),
               ('МЧС по Владимирской области', 5032),
               ('Убийство', 4831),
               ('Путин', 4752),
               ]

        top_data = pd.DataFrame(top, columns=['Имя, место, организация', 'Количество упоминаний'],
                                index=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        st.subheader('Топ-10 самых частоупоминаемых явлений в материалах архива')
        st.dataframe(top_data)

        a = news.set_index('rubric')
        count1 = a.loc['Новости 33; Общество']
        count2 = a.loc['Новости 33; Происшествия 33']
        count3 = a.loc['Новости 33; Культура']
        count4 = a.loc['Новости 33; Власть']
        count5 = a.loc['Новости 33']
        count6 = a.loc['Новости 33; Спорт']
        count7 = a.loc['Новости 33; Помоги!']
        count8 = a.loc['Новости 33; Здоровье 33']
        count9 = a.loc['Новости 33; ДТП во Владимирской области']
        count10 = a.loc['Новости 33; Цифра дня']
        count11 = a.loc['Новости 33; Выходные во Владимире']

        d1 = {'Количество материалов': [len(count1), len(count2), len(count3), len(count4), len(count5), len(count6),
                                        len(count7), len(count8), len(count9), len(count10), len(count11)]}
        i1 = {'Новости 33; Общество',
              'Новости 33; Происшествия 33',
              'Новости 33; Культура',
              'Новости 33; Власть',
              'Новости 33',
              'Новости 33; Спорт',
              'Новости 33; Помоги!',
              'Новости 33; Здоровье 33',
              'Новости 33; ДТП во Владимирской области',
              'Новости 33; Цифра дня',
              'Новости 33; Выходные во Владимире'}

        bc = pd.DataFrame(data=d1, index=i1)

        st.subheader('Количество материалов по рубрикам')
        st.bar_chart(bc, height=800)
        st.markdown('График показывает общее количество материалов в зависимости от доступных рубрик')

    with col2:
        artnum = {'Количество статей': [4256, 4562, 4823, 4561, 4816, 4823, 4789, 5713, 4876, 4568, 4862, 5681, 4568,
                                        4568, 5698, 5486, 5238, 4852, 4962, 4123, 4762, 4213, 5687, 4798, 4465, 5687,
                                        4568, 4821, 5668, 4587, 5748]}
        linechart_data = pd.DataFrame(data=artnum,
                                      columns=['Количество статей'],
                                      index=['01.07', '02.07', '03.07', '04.07', '05.07', '06.07', '07.07', '08.07',
                                             '09.07', '10.07', '11.07', '12.07', '13.07', '14.07', '15.07', '16.07',
                                             '17.07', '18.07', '19.07', '20.07', '21.07', '22.07', '23.07', '24.07',
                                             '25.07', '26.07', '27.07', '28.07', '29.07', '30.07', '31.07'])

        st.subheader('Количество статей за последний месяц')
        st.line_chart(linechart_data)
        st.markdown('На графике отображено общее количество статей в архиве, опубликованных за последний месяц')

        d2 = {'Политика': [1404, 4545, 3656], "Экономика": [4482, 1244, 3975], "Происшествия": [1244, 904, 2566]}
        i2 = {"РБК", "Коммерсант", "Известия"}

        barchart_data2 = pd.DataFrame(data=d2, index=i2)

        st.subheader('Количество материалов по тематике')
        st.bar_chart(barchart_data2, width=100)
        st.markdown('На графике показано, в какой тематике публиковались материалы')

        linechart_data2 = pd.DataFrame(
            np.random.randn(31, 3),
            columns=['РБК', 'Коммерсант', 'Известия'])

        st.subheader('Количество статей в СМИ за месяц')
        st.line_chart(linechart_data2)
        st.markdown('График показывает, сколько материалов выходило каждый день в течение '
                    'заданного периода в различных СМИ')
