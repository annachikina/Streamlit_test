import streamlit as st
import analysis
import pandas as pd


def load_page():
    st.title('Архив статей')

    news = pd.read_csv("news_v2.csv")

    st.header('Поиск')

    names = ['Владимир', 'ГИБДД по Владимирской области', 'Пожар', 'ДТП', 'Владимир Жириновский', 'Администрация '
                                                                                                  'Владимирской '
                                                                                                  'области',
             'Ковровский район', 'МЧС по Владимирской области', 'Убийство', 'Владмимир Путин']
    st.multiselect('Введите имя, место и/или название организации', names)

    st.text_input('Введите ключевое слово', 'QR-код')

    st.header('Фильтрация')

    news = pd.read_csv("news_v2.csv")
    genres = news["rubric"].unique()

    st.multiselect("Выберите одну или несколько тем", genres)

    st.date_input("Введите период",
                  value=[])

    sources = ["Коммерсант", "РБК", "Известия"]
    st.multiselect('Выберите источник', sources)

    arch_article1 = "Система обязательных QR-кодов выполнила свою задачу и будет отменена"
    arch_article2 = "Собянин разрешил посещать веранды ресторанов без QR-кода до 1 августа"
    arch_article3 = "Собянин объяснил введение QR-кодов большим количеством жулья"

    selected_article = st.selectbox("Выберите статью",
                                    (arch_article1, arch_article2, arch_article3)
                                    )

    if selected_article == arch_article1:
        st.header('Назавание статьи')
        st.subheader("Система обязательных QR-кодов выполнила свою задачу и будет отменена — Сергей Собянин")

        st.header('Дата:')
        st.subheader('17.07.2021')

        st.header('Автор')
        st.subheader('Иван Иванов')

        st.header('Рубрика')
        st.subheader('Политика')

        st.header('Текст статьи:')
        st.write(
            'Система обязательных QR-кодов выполнила свою задачу и будет отменена — Сергей Собянин \n Сделать такой '
            'шаг позволяет улучшение эпидемиологической ситуации в городе. С 19 июля в столице отменяют обязательные '
            'QR-коды для посещения ресторанов и кафе. Об этом сообщил Сергей Собянин во время заседания '
            'Координационного совета при Правительстве России по борьбе с распространением коронавирусной инфекции, '
            'которое провел Председатель Правительства России Михаил Мишустин. «Ко мне было много обращений от '
            'бизнеса, общественных организаций, партийных организаций, в частности от Федерации рестораторов и '
            'отельеров, от “Единой России”. Хотел поблагодарить московский бизнес за '
            'ответственное отношение к тем мерам, которые мы принимали, к совместной работе, которая позволила '
            'сделать дальнейшие шаги по нормализации обстановки и работы экономики», — сказал Мэр Москвы.\n Пойти на '
            'такое решение позволило улучшение эпидемиологической обстановки. Так, почти в два раза снизилось '
            'количество ежедневно выявляемых заболевших COVID-19 и на треть сократилось количество госпитализаций. '
            'Это также дало возможность более шести тысяч коек вновь направить на плановую работу.\n На снижение '
            'показателей влияет не только строгое соблюдение санитарных требований, но и массовая вакцинация. Только '
            'за последний месяц в столице привили более двух миллионов человек. В целом первый компонент вакцины '
            'получили 3,8 миллиона, а два компонента — более двух миллионов человек.\n «Тем не менее мы должны '
            'понимать, что мы находимся еще в зоне риска, в зоне эпидемии, которая продолжается. И конечно, '
            'должны выполнять те санитарные требования и обеспечить дальнейшую массовую вакцинацию населения. И всем '
            'нам соблюдать эти требования и беречь себя и своих родных. Хотел поблагодарить москвичей за такое '
            'активное участие в мероприятиях, направленных на снижение заболеваемости, их ответственность и '
            'выполнение требований, которые предписаны врачами и Роспотребнадзором», — добавил Сергей Собянин.\n '
            'Граждане по-прежнему смогут оформить QR-код, а заведения общепита будут принимать решения '
            'самостоятельно, проверять их у всех посетителей или нет.\n Также с 19 июля с сохранением необходимых '
            'санитарных требований возобновляют работу фуд-корты, а рестораны и кафе смогут обслуживать посетителей в '
            'ночное время (с 23:00 до 06:00). Кроме того, смогут открыться детские игровые комнаты, ночные клубы и '
            'бары.\n Для организаций, работающих без QR-кодов, будут сохранены некоторые ограничения. Так, '
            'при проведении концертных, спортивных и прочих развлекательных мероприятий должны быть созданы '
            'посадочные места. Организаторы должны выполнить это требование вне зависимости от количества '
            'одновременно присутствующих посетителей. Кроме того, если при входе на мероприятие не проверяют QR-коды, '
            'по-прежнему запрещено одновременное присутствие более 500 человек.\n QR-коды доступны переболевшим не '
            'более шести месяцев назад и вакцинированным гражданам, а также тем, кто сделал ПЦР-тест и получил '
            'отрицательный результат, который действителен 72 часа с момента его регистрации в лаборатории.')

    elif selected_article == arch_article2:
        st.header('Назавание статьи')
        st.subheader("Собянин разрешил посещать веранды ресторанов без QR-кода до 1 августа")

        st.header('Дата:')
        st.subheader('20.07.2021')

        st.header('Автор')
        st.subheader('Иван Иванов')

        st.header('Рубрика')
        st.subheader('Политика')

        st.header('Текст статьи:')
        st.write(
            "Собянин разрешил посещать веранды ресторанов без QR-кода до 1 августа \n Веранды кафе и ресторанов в "
            "Москве можно будет посещать без QR-кода до 1 августа, заявил Сергей Собянин. По словам мэра, "
            "«стабилизация ситуации» с коронавирусом в столице «внушает осторожный оптимизм» Жители Москвы до 1 "
            "августа 2021 года смогут посещать веранды кафе и ресторанов, не предъявляя QR-код о вакцинации, "
            "перенесенной болезни или отрицательном ПЦР-тесте. Об этом у себя на сайте написал мэр города Сергей "
            "Собянин. «По просьбе представителей общепита, обслуживание на летних верандах посетителей без "
            "предъявления QR-кодов будет разрешено до 1 августа (включительно)», — отметил мэр. По его словам, "
            "это решение должно поддержать «рестораны, и туристическую отрасль в целом, и просто москвичей, "
            "которые пока не успели завершить вакцинацию».\n Изначально запрет на посещение летних веранд без "
            "QR-кодов должен был начать действовать 12 июля. В сами кафе и рестораны посетителей без QR-кодов "
            "перестали пускать с 28 июня. Исключение делается для детей и подростков младше 18 лет, "
            "которых сопровождают родители, у которых есть код.\n Собянин заявил, что ситуация с распространением "
            "коронавируса в городе начала стабилизироваться. «Количество выявляемых случаев заболевания и "
            "госпитализаций все еще очень высокое, но по крайней мере оно немного снизилось по сравнению с пиковыми "
            "значениями недельной давности», — отметил он. Кроме того, москвичи, по мнению мэра, стали ответственнее "
            "подходить к санитарным требованиям и вакцинации: «Ежедневно мы прививаем около 100 000 человек».\n Это "
            "позволяет городским властям не вводить новые антиковидные ограничения и даже возобновить работу "
            "городских объектов на открытом воздухе, где риск заражения «гораздо меньше, чем в помещениях», "
            "отметил Собянин. \n «Стабилизация ситуации с распространением инфекции внушает осторожный оптимизм», "
            "— заключил мэр, добавив, что риск заражения при этом остается высоким, а «бороться с ковидом возможно "
            "только массовой вакцинацией».\n По данным оперативного штаба, за последние сутки COVID-19 в Москве "
            "заразились 6040 человек. Это максимальный суточный прирост инфицированных за три дня. К аппаратам "
            "искусственной вентиляции легких в столичных больницах подключен 691 человек. Скончались от инфекции в "
            "столице за день 109 человек. Суточная смертность не опускается ниже 100 случаев с 27 июня.")

    elif selected_article == arch_article3:
        st.header('Назавание статьи')
        st.subheader("Собянин объяснил введение QR-кодов большим количеством жулья")

        st.header('Дата:')
        st.subheader('28.07.2021')

        st.header('Автор')
        st.subheader('Иван Иванов')

        st.header('Рубрика')
        st.subheader('Политика')

        st.header('Текст статьи:')
        st.write(
            "Собянин объяснил введение QR-кодов большим количеством жулья \n Решение о QR-кодах, а не бумажных "
            "сертификатах было принято из-за большого количества «жулья», от которых цифровой код дает защиту. Об этом "
            "сообщил мэр Москвы Сергей Собянин в эфире «Вестей в субботу». «Зайдите в интернет, посмотрите, "
            "сколько там жулья всякого, которое обещает вам в течение нескольких часов доставить вам бумажный "
            "сертификат», — отметил он. Бумажный сертификат можно получить в поликлинике и при необходимости "
            "показывать, однако его сверка будет проходить через электронную базу, добавил Собянин. По словам мэра, "
            "QR-код является самой надежной и оптимальной историей.\n Новые ограничения столичные власти ввели на "
            "фоне роста числа заболевших. Система QR-кодов в Москве заработает 28 июня. Без них нельзя будет попасть "
            "в заведения общепита и на массовые мероприятия численностью более 500 человек. Более того, "
            "с 12 июля QR-код понадобится для доступа на летние веранды кафе.\n Москвичи могут получить QR-код в трех "
            "случаях: если прошли вакцинацию от COVID-19; если у них есть отрицательный ПЦР-тест, сделанный не ранее, "
            "чем три дня назад; если они перенесли коронавирус за последние полгода.")

    if st.button('Посмотреть статистику'):
        analysis.load_page()

    else:
        st.write('Нажмите, чтобы увидеть аналитику по статьям')
