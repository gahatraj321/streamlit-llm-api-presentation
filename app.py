import streamlit as st


st.set_page_config(page_title="LLM API Presentation", layout="wide")

st.markdown("""
    <style>
    /* Main Background and Text Color */
    .stApp {
        background-color: #0f172a;
        color: white;
    }
    /* Increasing Global Font Sizes for Slide Look */
    html, body, [class*="st-"] {
        font-size: 20px; 
    }
    h1 { font-size: 55px !important; color: #38bdf8 !important; } /* Main Title */
    h2 { font-size: 45px !important; color: #f472b6 !important; } /* Section Headers */
    p, li { font-size: 26px !important; line-height: 1.6; } /* Body Text */
    
    /* Center aligning image captions */
    .stImage > div > div > p {
        text-align: center;
        font-size: 18px !important;
        color: #94a3b8;
    }
    </style>
""", unsafe_allow_html=True)

st.title("How to Use LLM API")

page = st.sidebar.selectbox(
    "Choose Section",
    ["Home", "What is LLM", "What is API", "How API Works", "Code Example", "Live Demo"]
)


if page == "Home":
    st.header("Welcome")
    st.write("This application will guide you through the fundamentals of LLM APIs step-by-step.")
    

    col1, col2, col3 = st.columns([1, 1.5, 1]) 
    with col2:
        st.image("HOME.jpg.png", use_container_width=True)


elif page == "What is LLM":
    st.header("What is LLM?")
    st.write("""
    * **LLM** stands for **Large Language Model**.
    * It is an AI system trained on massive datasets to understand and generate human-like text.
    * **Key Examples:** OpenAI's GPT-4, Google's Gemini, and Meta's Llama.
    """)
    
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.image("llm.jpg.png", use_container_width=True)


elif page == "What is API":
    st.header("What is API?")
    st.write("""
    * An **API** (Application Programming Interface) is a software intermediary.
    * It allows two applications to **talk to each other**.
    * Think of it as a messenger that delivers your request to the provider and then delivers the response back to you.
    """)
    
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.image("API.jpg.png", use_container_width=True)


elif page == "How API Works":
    st.header("How LLM API Works")
    st.write("""
    1. **Client Request:** Your app sends a prompt (text) via the API.
    2. **Authentication:** The API checks your API Key for permission.
    3. **Processing:** The LLM server generates a response based on your prompt.
    4. **Data Return:** The API sends the text back to your application interface.
    """)
    
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.image("API works.jpg.png", use_container_width=True)


elif page == "Code Example":
    st.header("Basic Python Implementation")
    st.write("Here is how simple it is to call an LLM API using the OpenAI library:")
    
    code = '''
from openai import OpenAI

# Initialize the client
client = OpenAI(api_key="your_api_key_here")

# Create a completion request
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Explain APIs to a 5th grader."}]
)

# Print the result
print(response.choices[0].message.content)
'''
    st.code(code, language="python")


elif page == "Live Demo":
    from openai import OpenAI
    import os
    from dotenv import load_dotenv

    load_dotenv() # Loads your key from the .env file
    
   
    api_key = os.getenv("OPENAI_API_KEY")
    
    st.header("Live Interactive Demo")
    
    if not api_key:
        st.error("API Key not found! Please check your .env file.")
    else:
        client = OpenAI(api_key=api_key)
        user_input = st.text_input("Enter a prompt to test the API:", placeholder="e.g., Write a poem about coding...")

        if st.button("Send Request"):
            if user_input:
                with st.spinner("AI is generating response..."):
                    try:
                        response = client.chat.completions.create(
                            model="gpt-4o-mini",
                            messages=[{"role": "user", "content": user_input}]
                        )
                        st.success(response.choices[0].message.content)
                    except Exception as e:
                        st.error(f"An error occurred: {e}")
            else:
                st.warning("Please enter a prompt first.")
