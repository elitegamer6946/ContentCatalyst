import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key , openai_api_key
import requests
from openai import OpenAI

client = OpenAI(api_key=openai_api_key)

genai.configure(api_key=google_gemini_api_key)


#Creating Model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
#Setting up the model
model = genai.GenerativeModel(
  model_name="learnlm-1.5-pro-experimental",
  generation_config=generation_config,
)

# Set app to wide mode
st.set_page_config(layout='wide')

#title of our app
st.title('The Content Catalyst: Ignite your blog with the power of AI')

#create a subheader
st.subheader("The Content Catalyst is your AI-powered writing partner, here to help you overcome writer's block and generate high-quality blog posts in minutes. Simply provide a topic or a few keywords, and our advanced language model will craft compelling content, tailored to your needs.")

#sidebar for user input

with st.sidebar:
    st.title("Input Your Blog Details")
    st.subheader("Enter Details of the Blog You want to generate")

    #Blog title
    blog_title=st.text_input("Blog Title")

    # Keywords input
    keywords = st.text_area("Keywords (comma-separated)")

    # Number of words
    num_words = st.slider("Number of words",min_value=250, max_value=1000, step=250)

    # Number of Images
    #num_images = st.number_input("Number of Images",min_value=1,max_value=5,step=1)

    prompt_parts = [
            f"Generate a comprehensive ,engaging blog post relevant to to the given title\"{blog_title}\" and keywords\"{keywords}\" The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintain a consistent tone throughout."
    ]
     
    
    # Submit button
    submit_button = st.button("Generate Blog")

if submit_button:
     
    response = model.generate_content(prompt_parts)

    img_response = client.images.generate(
    model="dall-e-3",
    prompt=keywords,
    size="1024x1024",
    quality="standard",
    n=1,
    )
    image_url = img_response.data[0].url

    st.image(image_url)
    st.write(response.text)