import streamlit as st
import numpy as np

# Title of the Streamlit app
st.title("Showcase of My GitHub Open-Source Projects")

# Add a round picture
# image_path = "assets/images/86480339.jpeg"
# image = Image.open(image_path)
# st.image(image, caption="My GitHub Contributions",)


# Three-line subheading
st.subheader("Who Am I?")
st.write("I'm a passionate open-source contributor with a focus on impactful projects.")
st.write("I work on solving complex issues, merging pull requests, and contributing to the community.")
st.write("Explore my contributions and see how I've been making a difference in the open-source world.")

row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    tile = col.container(height=120)
    tile.title(":balloon:")
