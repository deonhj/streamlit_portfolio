import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Deon Jordaan")
    content = """
    Embarking on an enriching programming odyssey, I am fervently absorbing the vast expanse of Python's 
    wisdom. My passion lies in harnessing Python's prowess for the realms of machine learning, 
    data visualization, and the art of streamlining everyday tasks.

    While my roots are firmly planted in the realm of Business Intelligence development, 
    I am dedicated to broadening my horizons through a focused immersion in the world of programming. 
    My journey thus far has led me through a myriad of online courses, with a keen emphasis on the 
    intricacies of machine learning, the finesse of feature engineering, and the visual storytelling 
    prowess of data visualization, all orchestrated through a symphony of Python libraries.

    Guided by an insatiable thirst for knowledge, my spotlight has been cast upon an ensemble of 
    libraries that have become my companions on this journey:

    Matplotlib * Pandas * Seaborn * Numpy * Scikit-Learn * PyTorch
    
    With this showcase, I invite you to explore the tangible fruits of my labor and the captivating 
    symphony of Pythonic creativity that I am delighted to present.
    """
    st.info(content)

st.info("Below you can find some of the apps I have built in Python. Feel free to contact me.")


df = pd.read_csv("data.csv", delimiter=";")


_, col3, _, col4, _ = st.columns([0.5, 1.5, 0.5, 1.5, 0.5])
with col3:
    for index, row in df[1::2].iterrows():
        st.title(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[::2].iterrows():
        st.title(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
