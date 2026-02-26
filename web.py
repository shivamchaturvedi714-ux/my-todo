import streamlit as st
import function

def add_todo():
    todo=st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function.write_fun(todos)


todos= function.get_todos()

st.title("My Todo App")
st.subheader("My Todos")
st.write("mera naam shivam hai")
for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_fun(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label=" ",placeholder="add new todo...",
              on_change=add_todo,key="new_todo")

st.session_state