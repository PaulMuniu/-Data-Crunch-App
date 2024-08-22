import streamlit as st

# Contact Us page content
st.title("Get in Touch with Us 📞")

st.subheader("We’d Love to Hear From You!")

st.write("""
Whether you have a question, feedback, or just want to connect, we’re here for you. Your input helps us improve and grow!
""")

# Contact information
st.write("**📧 Email:** [support@datacrunchapp.com](mailto:support@recipeapp.com)")
st.write("**📞 Phone:** +254-123-456-789")
st.write("**🏢 Address:** Moringa School, Westlands, Nairobi")

# Contact form
st.write("Or simply fill out the form below, and we’ll get back to you as soon as possible:")

# Form inputs
name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

# Submit button
if st.button("Submit"):
    st.success(f"Thank you, {name}! We've received your message and will reach out to you at {email} soon.")

# Tabs for additional information
tab1, tab2 = st.tabs(["FAQs", "Upcoming Events 🎭"])

with tab1:
    st.write("""
1. **Is the app free to use?**
   - Yes, our app is completely free to use, with all features available at no cost. Enjoy exploring new recipes without any charges!
2. **How accurate are the ingredient matches?**
   - Our algorithm uses advanced techniques to match your ingredients with the best possible recipes, but feel free to tweak the suggestions to suit your taste.
3. **Can I suggest new features or recipes to be added?**
   - Absolutely! We welcome user suggestions. You can reach out to us via the contact form or email us directly with your ideas.
    """)

with tab2:
    st.write("""
    **Stay Updated:** No food event currently. We’ll keep you posted on what’s cooking! ✅
    """)

# Footer
st.write("---")
st.write("🔧 Developed with love 💟")
