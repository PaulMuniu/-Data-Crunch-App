import streamlit as st
import os

# Page setup
st.set_page_config(page_title="Data Crunch - Recipe Recommender")
st.sidebar.success("Enjoy Your Experience! 🌟 Don't forget to leave feedback.")

# Welcome page content
st.title("Data Crunch ~ Your Personalized Recipe Recommender 🍽️")


st.subheader("Welcome to a World of Culinary Delight!! 👨‍🍳🍝👩‍🍳")

st.write("""
Are you ready to transform your kitchen into a haven of creativity and taste? Whether you're a culinary novice or a seasoned chef, our app is here to guide you. With just a few ingredients from your pantry, you can explore a world of delicious recipes crafted specifically for you. Let's make every meal an adventure!
""")

# Base directory
base_dir = os.path.dirname(os.path.dirname(__file__))

# Define the paths to the images using relative paths
image_path1 = os.path.join(base_dir, 'Deployment/Image', 'pic1.jpg')
image_path2 = os.path.join(base_dir, 'Deployment/Image', 'pic2.jpg')

# Displaying images in columns
col1, col2 = st.columns(2)

col1.header("#Irresistibly Yummy")
col1.image(image_path1, caption="Tailored to your taste!", use_column_width=True)

col2.header("#Exquisitely Crafted")
col2.image(image_path2, caption="Personalized recipes!", use_column_width=True)

# Additional content
st.write("""
### Why Choose Data Crunch?
- **✔️Tailored Recipe Suggestions:** Get personalized recipe recommendations based on the ingredients you have.
- **✔️Wide Variety of Cuisines:** Discover recipes from various cuisines around the world.
- **✔️Reduce Food Waste♻️ :** Make the most of your ingredients and minimize waste.

### How It Works:
1. **Input Your Ingredients:** Simply enter the ingredients you have at home.
2. **Receive Customized Recipes:** Our smart algorithm will suggest recipes you can create immediately.
3. **Cook and Enjoy:** Follow the simple steps and enjoy a delicious meal tailored just for you!
""")

st.write("""
We believe cooking should be an enjoyable experience, not a chore. That's why we've designed this app to be your go-to kitchen companion, helping you create memorable meals with ease and joy. So, dive in, experiment with new dishes, and savor every bite!
""")

# Footer
st.write("---")
st.write("🔧 Develoved with love 💟")