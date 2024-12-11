# The Content Catalyst: AI-Powered Blog and Image Generator

**The Content Catalyst** is an innovative web application built with Streamlit, Google Gemini API, and OpenAI's DALL·E to help users generate high-quality blog posts and images in minutes. Simply input your blog title, keywords, and preferred word count, and the app will create a detailed blog post along with a relevant image, all powered by advanced language models and AI image generation.

## Features
- **AI-Powered Blog Generation**: Uses the Google Gemini API to generate blog content based on your title and keywords.
- **Image Generation with DALL·E**: Leverages OpenAI’s DALL·E API to create images based on the given keywords.
- **Streamlit Interface**: A clean and user-friendly web interface that makes it easy to input your blog details and generate content instantly.
- **Customizable Parameters**: Adjust the length of your blog posts (between 250 and 1000 words) to fit your needs.

## Requirements
Before running this app, make sure you have the following dependencies installed:

- `streamlit`
- `google-generativeai` (for Google Gemini API)
- `openai` (for DALL·E integration)
- `requests` (for HTTP requests)

Additionally, you'll need to configure the following API keys:

- **Google Gemini API Key**: [Get your Google API Key here](https://cloud.google.com/generative-ai)
- **OpenAI API Key**: [Get your OpenAI API Key here](https://platform.openai.com/signup)

## How to Run

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/content-catalyst.git
   cd content-catalyst
