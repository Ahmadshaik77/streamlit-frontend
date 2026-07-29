import streamlit as st
import requests

st.set_page_config(page_title="Student Management", page_icon="😊")

st.title("Student Management Web Application")

API_URL = "https://fast-api-krtl.onrender.com/"

with st.sidebar:
    st.header("Student Management")
    option = st.selectbox(
        "Choose your option",
        [
            "view_all_students",
            "view_single_student",
            "add_a_student",
            "update_a_student",
            "delete_a_student",
        ],
    )

#View Single Student

if option == "view_single_student":

    st.subheader("View Single Student")

    student_id = st.number_input(
        "Enter Student ID",
        min_value=1,
        max_value=100,
        value=1,
        step=1,
        key="view_id",
    )

    if st.button("Submit", key="view_btn"):
        response = requests.get(f"{API_URL}get_single_student_by_id/{student_id}")

        if response.status_code == 200:
            st.success(response.json())
        else:
            st.error(response.text)

#View All Students

elif option == "view_all_students":

    st.subheader("View All Students")

    if st.button("Submit", key="all_btn"):
        response = requests.get(f"{API_URL}get_all_students")

        if response.status_code == 200:
            st.write(response.json())
        else:
            st.error(response.text)

#Add Student

elif option == "add_a_student":

    st.subheader("Add Student")

    student_id = st.number_input(
        "Student ID",
        min_value=1,
        max_value=100,
        value=1,
        key="add_id",
    )

    name = st.text_input("Name")
    course = st.text_input("Course")

    if st.button("Submit", key="add_btn"):
        response = requests.post(
            f"{API_URL}add_student",
            json={
                "studentid": student_id,
                "name": name,
                "course": course,
            },
        )

        if response.status_code == 200:
            st.success(response.json())
        else:
            st.error(response.text)

#Update Student

elif option == "update_a_student":

    st.subheader("Update Student")

    student_id = st.number_input(
        "Student ID",
        min_value=1,
        max_value=100,
        value=1,
        key="update_id",
    )

    name = st.text_input("Name", key="update_name")
    course = st.text_input("Course", key="update_course")

    if st.button("Submit", key="update_btn"):
        response = requests.put(
            f"{API_URL}update_student_Details_by_id/{student_id}",
            params={
                "studentid": student_id,
                "name": name,
                "course": course,
            },
        )

        if response.status_code == 200:
            st.success(response.json())
        else:
            st.error(response.text)

# Delete Student

elif option == "delete_a_student":

    st.subheader("Delete Student")

    student_id = st.number_input(
        "Student ID",
        min_value=1,
        max_value=100,
        value=1,
        key="delete_id",
    )

    if st.button("Submit", key="delete_btn"):
        response = requests.delete(
            f"{API_URL}delete_student_Details_by_id/{student_id}"
        )

        if response.status_code == 200:
            st.success(response.json())
        else:
            st.error(response.text)