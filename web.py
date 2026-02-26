import streamlit as st
import function

todos= function.get_todos()

st.title("My Todo App")
st.subheader("My Todos")
st.write("mera naam shivam hai")
for todo in todos:
    st.checkbox(todo)

st.text_input(label=" ",placeholder=" ")
st.time_input("")