import streamlit as st

# Page setup
st.set_page_config(page_title="Hello")
st.sidebar.success("Have Fun & Don't forget to rate us.")

# Welcome page content
st.title("Welcome to Your Personalized Recipe Recommender! 🍳")

st.subheader("Discover Delightful Meals with What You Have!")

st.write("""
Welcome to our Recipe Recommender System, where we turn your kitchen into a culinary adventure. Whether you’re a seasoned chef or just looking to whip up something quick and easy, our app is here to help you discover delicious recipes tailored to the ingredients you already have.
""")

# Additional content
st.write("""
**Why Choose Us?**
- **✔️ Personalized Recommendations**
- **✔️ Catering to Your Needs**
- **✔️ Reduce Food Waste**
""")

st.write("""
**How It Works:**
1. **Enter Your Ingredients**: Input the ingredients you have, and our smart system will do the rest.
2. **Get Cooking**: Receive a list of recipes you can make right now and start cooking!
""")

st.write("""
We believe that cooking should be easy, fun, and stress-free. So go ahead, explore new recipes, try out new ingredients, and enjoy the process of creating delicious meals with what’s already in your kitchen.
""")

# Footer
st.write("---")
st.write("🔧 Developed with love 💟")
