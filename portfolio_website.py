import streamlit as st
import google.generativeai as genai

# api_key = st.secrets["Google_Api_Key"]

genai.configure(api_key="AIzaSyCV9d0IPPHfo6TVfVPhQiv7JzNgIqT-JoY")
model = genai.GenerativeModel('gemini-1.5-flash')

col1 , col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Aniket Sidhu")

with col2:
    st.image("images/the-power-of-deadpool-6e-1920x1200.jpg")

st.title(" ")

persona = """
You are Aniket's AI Bot. You help people answer questions about yourself (i.e., Aniket). Answer as if you are Aniket. Don't answer in the second or third person. If you don't know the answer, simply say, "That is a secret." Here is more info about Aniket:
Aniket Sidhu has just completed his 12th grade this year from Kendriya Vidyalaya No. 2, Delhi Cantt. He possesses a diverse skill set that he continually improves to become more efficient and productive. His expertise includes 3D modeling, Blender, coding, and programming, with a strong passion for coding, programming, and artificial intelligence. Aniket is particularly interested in prompt engineering and aims to build a career in AI. He enjoys playing PC games like NFS and COD, as well as physical games such as cricket and football. Though he has not yet graduated, he is actively seeking colleges in Delhi, India, to pursue a BTech degree in AI and ML. Aniket showcases his 3D artwork on Instagram and sells his 3D assets online on various websites. The field of AI excites him immensely.
Aniket's Email: aniketsidhu425@gmail.com
Aniket's Instagram: https://www.instagram.com/aniket_sidhu_56?igsh=YjQwc2RjNTYxMXFy"""

st.title("Aniket's AI Bot")

user_question = st.text_input("Ask anything about me")

if st.button("ASK", use_container_width=400):
    prompt = persona + "Here is the question that the user asked:" + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title(" ")

col1 , col2 = st.columns(2)

with col1:
    st.subheader("Facts about Deadpool")
    st.write("- Anti-Hero")
    st.write("- Mercenary Background")
    st.write("- Healing Factor")
    st.write("- Fourth Wall Breaks")
    st.write("- Regenerative Degeneration")

with col2:
    st.video("https://www.youtube.com/watch?v=r3LisZEIK34")

st.title("")

st.title("My Favourite Transformer")

st.image("images/optimus-prime-in-transformers-4-1920x1200.jpg")

st.write("")

st.title("My Skills")

st.slider("3D Art",0,100,70)
st.slider("Programming",0,100,75)
st.slider("Typing",0,100,80)

# st.file_uploader("Please upload your files here")

st.write("")

st.title("Gallery")

col1 , col2 , col3 = st.columns(3)

with col1:
    st.image("images/2024-lamborghini-revuelto-car-ix-1920x1200.jpg")
    st.image("images/a-space-view-of-tomorrow-j4-1920x1200.jpg")
    st.image("images/adventures-in-pursuit-of-the-northern-lights-ei-1920x1200.jpg")

with col2:
    st.image("images/arcee-transformers-rise-of-the-beasts-5k-64-1920x1200.jpg")
    st.image("images/brian-o-conner-the-fast-saga-20th-anniversary-0k-1920x1200.jpg")
    st.image("images/bumblebee-transformers-rise-of-the-beasts-poster-5k-as-1920x1200.jpg")

with col3:
    st.image("images/bushido-samurai-wt-1920x1200.jpg")
    st.image("images/2017-the-fate-of-the-furious-do-1920x1200.jpg")
    st.image("images/4k-grey-nissan-gtr-2020-pk-1920x1200.jpg")

st.subheader(" ")

st.write("CONTACT")

st.title("For any inquiries:")

st.subheader("contact@aniketsidhu.com")












