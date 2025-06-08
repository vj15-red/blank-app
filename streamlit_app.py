import streamlit as st

st.title("🕰️ Journey Through Time Survey")

# Question 1
name = st.text_input("1. What's your name?")

# Question 2
perspective = st.text_input("2. What is your perspective on time travel? (e.g., fun, dangerous, fascinating)")

# Question 3
time_choice = st.radio("3. Would you rather travel to the PAST or the FUTURE?", ["Past", "Future"])

# Conditional questions
if time_choice == "Past":
    st.subheader("🔙 You chose the Past. Let's dive into history!")
    q4 = st.text_input("4. Which time period in history would you visit, and why?")
    q5 = st.text_input("5. Is there a historical figure you would like to meet? Who?")
    q6 = st.text_input("6. Would you change anything in the past if you could? Why or why not?")
elif time_choice == "Future":
    st.subheader("🚀 You chose the Future. Let’s look ahead!")
    q4 = st.text_input("4. How far into the future would you travel (10, 100, 1000 years)?")
    q5 = st.text_input("5. What is one thing you’re curious to see in the future?")
    q6 = st.text_input("6. Would you want to see your own future? Why or why not?")

# Submit button
if st.button("Submit"):
    st.success(f"✅ Thank you, {name}! Your responses have been recorded.")
    st.info("Time is yours to imagine... ✨")
