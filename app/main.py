import streamlit as st
from PIL import Image
import base64
from io import BytesIO  # Import BytesIO from the io module
import os  # Import os for file path checking

# Initial page config
st.set_page_config(
     page_title='Streamlit Cheat Sheet',
     layout="wide",
     initial_sidebar_state="expanded",
)

# Load the image for the circular display
image_path = "assets/images/86480339.jpeg"  # Adjust this path as needed
image = Image.open(image_path)

# Load the LinkedIn and GitHub icons
linkedin_icon_path = "assets/icons/linkedin.png"  # Adjust this path as needed
github_icon_path = "assets/icons/github.png"
Resume_icon_path = "assets/icons/approved.png"  # Adjust this path as needed

# Function to load images with error handling
def load_image(image_path):
    if os.path.exists(image_path):
        return Image.open(image_path)
    else:
        st.error(f"Image not found: {image_path}")
        return None

linkedin_icon = load_image(linkedin_icon_path)
github_icon = load_image(github_icon_path)
Resume_icon = load_image(Resume_icon_path)

# Convert images to base64 for inline display
def image_to_base64(image):
    if image:
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()
    return None

linkedin_icon_base64 = image_to_base64(linkedin_icon)
github_icon_base64 = image_to_base64(github_icon)
Resume_icon_base64 = image_to_base64(Resume_icon)

# Display the image in a circular shape using CSS
st.markdown("""
    <style>
    .circle-image {
        width: 150px;  /* Adjust the size as needed */
        height: 150px; /* Adjust the size as needed */
        border-radius: 50%; /* This makes the image circular */
        overflow: hidden; /* Ensures the image fits within the circle */
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.3); /* Optional shadow */
        margin: 20px auto; /* Center the image and add space after it */
    }
    .circle-image img {
        width: 100%;
        height: auto; /* Maintain aspect ratio */
        object-fit: cover; /* Cover the div without stretching */
    }
    .sidebar-text {
        text-align: center; /* Center the text */
        margin-bottom: 10px; /* Add space between the lines */
    }
    .sidebar-link {
        text-align: center; /* Center the links */
        margin-bottom: 10px; /* Add space between the links */
    }
    .sidebar-section-title {
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .social-icons img {
        width: 24px; /* Adjust the size as needed */
        height: 24px; /* Adjust the size as needed */
        margin: 0 10px; /* Add space between the icons */
    }
    </style>
""", unsafe_allow_html=True)

# Create a div for the circular image
# Convert the image to base64 for inline display
buffered = BytesIO()
image.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue()).decode()

# Display the circular image in the sidebar
with st.sidebar:
    st.markdown(f'<div class="circle-image"><img src="data:image/jpeg;base64,{img_str}"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Harshal Honde</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Data Science Intern @Nroad</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Pune, IN</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section-title">Contact Information: </div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">HarshalHonde50@gmail.com</div>', unsafe_allow_html=True)
    if linkedin_icon_base64 and github_icon_base64:
        st.markdown(f"""
            <div class="social-icons" style="text-align: center;">
                <a href="https://www.linkedin.com/in/harshal-honde268/">
                    <img src="data:image/png;base64,{linkedin_icon_base64}" alt="LinkedIn">
                </a>
                <a href="https://github.com/Harry262000">
                    <img src="data:image/png;base64,{github_icon_base64}" alt="GitHub">
                </a>
                 <a href="/assets/Resume/Harshal_Honde_Intern.pdf">
                    <img src="data:image/png;base64,{Resume_icon_base64}" alt="Resume">
                </a>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section-title">Skills</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Python</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Machine Learning</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Data Analysis</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section-title">Hobbies and Interests</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Reading</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Traveling</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Gaming</div>', unsafe_allow_html=True)

# Title of the Streamlit app
st.title("**Showcase of My GitHub Open-Source Projects**")


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

# Create tabs
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

# Content for Tab 1
with tab1:
    st.header("This is Tab 1")
    st.write("Content for the first tab goes here.")


st.button('Hit me')
st.data_editor('Edit data', data)
st.checkbox('Check me out')
st.radio('Pick one:', ['nose','ear'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.download_button('On the dl', data)
st.camera_input("一二三,茄子!")
st.color_picker('Pick a color')