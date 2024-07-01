import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="mEALER : An Recipe generator App",
    page_icon=":food:",
    layout="centered"
)

# Get the Google API key from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Display the chatbot's title on the page
st.title("mEALER : An Recipe generator App")
st.subheader("Made by Dhiraj")
st.sidebar.header("Input Meal and Preferences")

# User input for ingredients
meal_name = st.sidebar.text_input("Enter the Meal")

# User input for cuisine type
cuisine = st.sidebar.selectbox(
        "Cuisine Type",
        ["Any", "Italian", "Chinese", "Mexican", "Indian", "American"]
    )

# User input for number of servings
servings = st.sidebar.slider("Number of Servings", 1, 10, 2)

# User input for dietary restrictions
dietary_restrictions = st.sidebar.multiselect(
        "Dietary Restrictions",
        ["None", "Vegetarian", "Vegan", "Gluten-Free", "Dairy-Free", "Nut-Free"]
    )
#prompt for recipe generation
prompt = f"Generate a recipe for {meal_name} with {servings} servings. "
prompt += f"Cuisine type: {cuisine}. "
if dietary_restrictions:
    prompt += "Dietary restrictions: " + ", ".join(dietary_restrictions) + ". "
prompt += "Include the list of ingredients and the steps for preparation."

# Button to generate recipe
generate_button = st.sidebar.button("Generate Recipe")

if generate_button:
    with st.spinner("Generating"):
            gemini_response = model.generate_content(prompt)
            #display the response
            st.write(gemini_response.parts[0].text)