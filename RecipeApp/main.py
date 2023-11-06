import streamlit as st
import requests
import os
import random
from requests.exceptions import HTTPError
from send_email import sendEmail
from getImage import getImageURL
from pathlib import Path


# API
# https://api.api-ninjas.com/v1/recipe?query=

TOPIC = ""
BLOB = ""

st.set_page_config(page_title="FOOD LOVERS", initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

path = os.path.dirname(__file__)
image_path = Path(__file__).with_name("banner.png").relative_to(Path.cwd())
css = path + '/style.css'


with open(css) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


# Make website using streamlit

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image(str(image_path))

with col3:
    st.write(' ')

st.text_input(label="Search", placeholder="Enter Dish",
              key="-DISH-", label_visibility="hidden")

if st.session_state['-DISH-']:
    query = st.session_state['-DISH-']
    query = query.title()
    TOPIC = query

    try:

        with st.status("Finding the Perfect Dish...", expanded=True) as status:
            st.write("Searching the Recipe Api...")
            api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(
                query)
            response = requests.get(
                api_url, headers={'X-Api-Key': '3F0UXHsxd+xEzMYD9I1/Ow==yoFuk0DEiPYombQG'})
            if response.status_code == requests.codes.ok:
                # access JSOn content
                jsonResponse = response.json()
                recipe = random.choice(jsonResponse)

                if recipe['title'] is not None and recipe['instructions'] is not None:
                    BLOB = BLOB + recipe['title'] + '\n' + \
                        recipe['instructions'] + '\n' + 2*'\n'

            st.write("Recipe Found: " + recipe['title'])
            st.write("Getting Image...")
            img = getImageURL(recipe['title'])
            st.write("Preparing Ingredients List...")
            ingredients = recipe['ingredients'].split('|')
            status.update(label="Recipe Loaded...Enjoy!",
                          state="complete", expanded=False)

        st.subheader(recipe['title'])
        st.image(img)
        st.write('Ingredients:')
        for i in ingredients:
            st.markdown("- " + i)
        st.write(recipe['servings'])
        st.write('Instructions:')
        st.markdown(recipe['instructions'])
        st.markdown("<hr />", unsafe_allow_html=True)

    except HTTPError as http_err:
        st.error(f'HTTP error occurred: {http_err}')
    except Exception as err:
        st.error(f'Other error occurred: {err}')
