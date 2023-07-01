import streamlit as st

def add_task(task):
    tasks.append(task)

def delete_task(task):
    if task in tasks:
        tasks.remove(task)

def view_tasks():
    if len(tasks) == 0:
        st.write("Your to-do list is empty.")
    else:
        st.write("Your to-do list:")
        for i, task in enumerate(tasks, start=1):
            st.write(f"{i}. {task}")

def main():
    st.title("To-Do List Application")
    st.write("Enter a task and click 'Add' to add it to your to-do list.")
    task = st.text_input("Task:")
    add_button = st.button("Add")
    if add_button:
        add_task(task)
        task = ""

    view_tasks()

    delete_task_idx = st.number_input("Enter the task number to delete:", min_value=1, max_value=len(tasks), value=1, step=1)
    delete_button = st.button("Delete")
    if delete_button and delete_task_idx > 0:
        delete_task(tasks[delete_task_idx-1])

if __name__ == "__main__":
    tasks = []
    main()
