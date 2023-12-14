import os
import random
import streamlit as st
import math

st.set_page_config(page_title="LUCKY STUDENT")

path = os.path.dirname(__file__)
banner = path + '/banner.png'
css = path + '/style.css'

with open(css) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

images = [path + "/images/Lucky.png", path + "/images/one.png", path +
          "/images/two.png", path + "/images/three.png", path + "/images/four.png", path + "/images/five.png", path + "/images/six.png"]


st.text(str(images[0]))
st.image(str(images[0]))
st.header("LUCKY STUDENT")

students = st.text_input(
    "Students:", placeholder="Enter the names of the students seperated by comma: ", key="-SEARCH-").title()

if st.session_state['-SEARCH-']:
    student_list = [word.strip() for word in students.split(',')]

    if len(student_list) > 1:
        with st.sidebar:
            for index, student in enumerate(student_list):
                st.subheader(f"{index + 1} : {student}")

        total = len(student_list)
        total_dice = math.ceil(total / 6)

        for x in range(total_dice):
            st.image(images[x])

    if st.button('GET LUCKY', type="primary"):
        st.write(random.choice(student_list))
