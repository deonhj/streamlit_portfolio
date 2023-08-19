import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df = pd.read_csv("data2.csv")
df["Full Name"] = df["first name"].str.capitalize() + ' ' + df["last name"].str.capitalize()

st.header("The Best Company")
content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore 
magna aliqua. Cras tincidunt lobortis feugiat vivamus. Ac auctor augue mauris augue. A iaculis at erat pellentesque 
adipiscing commodo elit. Id ornare arcu odio ut sem nulla. Sit amet dictum sit amet justo donec enim. Viverra nam 
libero justo laoreet sit amet cursus. Ac turpis egestas maecenas pharetra convallis. Turpis egestas pretium aenean 
pharetra magna ac placerat vestibulum lectus. Laoreet id donec ultrices tincidunt arcu non sodales. Pellentesque 
elit eget gravida cum sociis natoque penatibus et. Felis bibendum ut tristique et egestas quis ipsum. Accumsan 
tortor posuere ac ut. Id aliquet lectus proin nibh nisl condimentum id venenatis. Consectetur adipiscing elit 
pellentesque habitant. Quis enim lobortis scelerisque fermentum dui faucibus in ornare. Amet purus gravida quis 
blandit turpis.
"""
st.write(content)
st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

with col1:
    for index, row in df.iloc[:4].iterrows():
        st.subheader(row["Full Name"])
        st.write(row["role"])
        st.image(f"images2/{row['image']}")

with col2:
    for index, row in df.iloc[4:8].iterrows():
        st.subheader(row["Full Name"])
        st.write(row["role"])
        st.image(f"images2/{row['image']}")

with col3:
    for index, row in df.iloc[8:12].iterrows():
        st.subheader(row["Full Name"])
        st.write(row["role"])
        st.image(f"images2/{row['image']}")