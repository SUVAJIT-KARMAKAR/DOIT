# IMPORT REQURIED MODULES IN THE WORK 
import streamlit as st
from pymongo import MongoClient

# MONGODB DATABASE CONNECTION
client = MongoClient('mongodb://localhost:27017/')
db = client['doit']
collection = db['tasks']

# APPLICATION
def main():
    st.title("DO IT : Make it happen")

    # Sidebar for CRUD operations
    st.sidebar.header("TASK OPERATION")
    operation = st.sidebar.radio("SELECT OPERATION", ["ADD YOUR TASK", "UPDATE YOUR TASK", "DELETE YOUR TASK"])

    if operation == "ADD YOUR TASK":
        add_task()
    elif operation == "UPDATE YOUR TASK":
        update_task()
    elif operation == "DELETE YOUR TASK":
        delete_task()

    # DISPLAYING TASKS
    display_tasks()

# FUNCTION :: ADD - TASK 
def add_task():
    task = st.sidebar.text_input("ENTER YOUR NEW TASK")
    if st.sidebar.button("ADD"):
        if task:
            collection.insert_one({"task": task, "completed": False})
            st.sidebar.success("TASK ADDED SUCCESSFULLY!")
        else:
            st.sidebar.error("PLEASE PROVIDE US YOUR TASK")

# FUNCTION :: UPDATE - TASK 
def update_task():
    tasks = list(collection.find())
    if tasks:
        task_names = [task['task'] for task in tasks]
        selected_task = st.sidebar.selectbox("SELECT YOUR TASK TO UPDATE", task_names)
        new_task = st.sidebar.text_input("ENTER YOUR UPDATED TASK", selected_task)
        completed = st.sidebar.checkbox("MARK IT AS COMPLETED")
        if st.sidebar.button("UPDATE"):
            collection.update_one(
                {"task": selected_task},
                {"$set": {"task": new_task, "completed": completed}}
            )
            st.sidebar.success("TASK UPDATED SUCCESSFULLY!")
    else:
        st.sidebar.info("NO TASKS PRESENT TO UPDATE")

# FUCNTION :: DELETE - TASK 
def delete_task():
    tasks = list(collection.find())
    if tasks:
        task_names = [task['task'] for task in tasks]
        selected_task = st.sidebar.selectbox("SELECT YOUR TASK TO DELETE", task_names)
        if st.sidebar.button("DELETE"):
            collection.delete_one({"task": selected_task})
            st.sidebar.success("TASK DELETED SUCCESSFULLY!")
    else:
        st.sidebar.info("NO TAKS PRESENT TO DELETE")

# FUCNTION :: DISPLAY - TASK 
def display_tasks():
    tasks = list(collection.find())
    if tasks:
        st.subheader("YOUR CURRENT DO IT LIST")
        for task in tasks:
            if task['completed']:
                st.markdown(f"- [x] {task['task']}")
            else:
                st.markdown(f"- [ ] {task['task']}")
    else:
        st.info("NO CURRENT DO IT LIST PRESENT. INITIATE YOUR TASK WITH A TASK")

# APPLICATION INITIATION
if __name__ == "__main__":
    main()