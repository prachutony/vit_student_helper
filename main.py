import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="VIT Student Saviour",
    initial_sidebar_state="expanded"
)


def gpa_inputs(n):
    grade = ["S","A","B","C","D","E","F","N","N1","N2","N3","N4"]
    grades = []
    credits = []
    for i in range(n):
        col1 , col2 = st.columns(2)
        with col1:
            credits.append(st.number_input(f"Enter the credit of subject {i + 1}:" , min_value=1.0 , step=0.5))
        with col2:
            grades.append(st.selectbox(f"Select the grade of subject {i + 1}:" , grade))

    return credits , grades





def cgpa_inputs(n):
    credits = [] #credits of each sem
    gpa = [] #gpa of each sem
    credits_to_reduce = 0
    for i in range(n+1):
        if i < n:
            with st.expander(f"Semester {i + 1}"):
                no_of_subjects = st.number_input(f"Enter the Total number of subjects in semester {i + 1}" , min_value=0 , key= f"number_{i}")
                st.warning("Do not include NON-GRADED COURSES")
                grade_1 = ["S","A","B","C","D","E","F","N","N1","N2","N3","N4"]
                sem_grades = []
                sem_credits = []
                for j in range(no_of_subjects):
                    col1 , col2 = st.columns(2)
                    with col1:
                        sem_credits.append(st.number_input(f"Enter the credit of subject {j + 1}:" , min_value=1.0 , step=0.5 , key=f"credits_{i}_{j}"))
                    with col2:
                        sem_grades.append(st.selectbox(f"Select the grade of subject {j + 1}:" , grade_1 , key=f"grades_{i}_{j}"))
                corrected_gpa = calculate_gpa(sem_credits , sem_grades)
                credits.append(sum(sem_credits))
                gpa.append(corrected_gpa)
        else:
            credits_to_reduce = final_step(n)
    
    

    return gpa , credits , credits_to_reduce


def calculate_cgpa(gpa , credits , credits_to_reduce):
    numerator = 0
    for i in range(len(gpa)):
        numerator += (gpa[i] * credits[i])
    final_credits = sum(credits) - credits_to_reduce
    cgpa = numerator/final_credits
    return round(cgpa,2)





def calculate_gpa(credits , grades):
    score = 0
    total_credits = 0
    for i in range(len(grades)):
        if grades[i] == "S":
            individual_score = 10 * credits[i]
            score += individual_score
            total_credits += credits[i]
        elif grades[i] == "A":
            individual_score = 9 * credits[i]
            score += individual_score
            total_credits += credits[i]
        elif grades[i] == "B":
            individual_score = 8 * credits[i]
            score += individual_score
            total_credits += credits[i]
        elif grades[i] == "C":
            individual_score = 7 * credits[i]
            score += individual_score
            total_credits += credits[i]
        elif grades[i] == "D":
            individual_score = 6 * credits[i]
            score += individual_score
            total_credits += credits[i]
        elif grades[i] == "E":
            individual_score = 5 * credits[i]
            score += individual_score
            total_credits += credits[i]
        elif grades[i] == "F":
            individual_score = 0 * credits[i]
            score += individual_score
            total_credits += credits[i]
        elif grades[i] == "N":
            individual_score = 0 * credits[i]
            score += individual_score
            total_credits += credits[i]
        elif grades[i] == "N1":
            individual_score = 0 * credits[i]
            score += individual_score
            total_credits += credits[i]
        elif grades[i] == "N2":
            individual_score = 0 * credits[i]
            score += individual_score
            total_credits += credits[i]
        elif grades[i] == "N3":
            individual_score = 0 * credits[i]
            score += individual_score
            total_credits += credits[i]
        elif grades[i] == "N4":
            individual_score = 0 * credits[i]
            score += individual_score
            total_credits += credits[i]
    if total_credits == 0:
        return 0
    else:
        score = score/total_credits
        return round(score,2)

def gpa_page():
    
    # Get the number of text inputs from the user.
    n = st.slider("Select the number of subjects:", 1,25)
    st.warning("Do not include NON-GRADED COURSES")

    # Create the text inputs.
    credits , grades = gpa_inputs(n)

    # Submit button.
    if st.button("Submit"):
        # Concatenate the text inputs.
        gpa = calculate_gpa(credits , grades)
        if gpa > 8.00:
                st.balloons()   
        # Display the concatenated text.
        st.title(f"Your GPA for this semester is {str(gpa)}")


def final_step(n):
    with st.expander("Final Step"):
        credits_to_reduce = 0
        if n == 1:
            no_of_arrear = st.number_input(f"Enter the total number of arrears you had in Semester 1" , min_value=0)
        else:
            no_of_arrear = st.number_input(f"Enter the total number of arrears you had from Semester 1 to semester {n}" , min_value=0)
        st.warning("Do not include NON-GRADED COURSES")
        for i in range(no_of_arrear):
            col1 , col2 = st.columns(2)
            with col1:
                credit = st.number_input(f"Enter the credit of arrear subject {i + 1}" , min_value=1.0 , step=0.5)
            with col2:
                option = st.selectbox(f"Did you clear the arrear subject {i + 1}?",["Not Cleared" , "Cleared"])
            if option == "Cleared":
                credits_to_reduce += credit
            else:
                credits_to_reduce = 0
    return credits_to_reduce


def cgpa_page():#For those who had arrears
    
    # Get the number of text inputs from the user.
    n = st.slider("Select the number of Semesters:", 1 , 10)

    # Create the text inputs.
    gpa , credits ,credits_to_reduce= cgpa_inputs(n)
    
    # Submit button.
    if st.button("Submit"):
        # Concatenate the text inputs.
        
        cgpa = calculate_cgpa(gpa , credits , credits_to_reduce)
        if cgpa > 8.00:
                st.balloons() 
        # Display the concatenated text.
        st.title(f"Your CGPA is {str(cgpa)}")


def quick_cgpa_calculator():
    st.warning("Please do not include the credits of NON-GRADED COURSES")
    cgpa_till_lastSem = st.number_input("Enter the CGPA till last semester:" , min_value=0.00)
    credits_till_lastSem = st.number_input("Enter total number of credits till last semester:" , min_value=0.00 , step=0.5)
    current_gpa = st.number_input("Enter the GPA of this semester:" , min_value=0.00)
    current_credits = st.number_input("Enter the credits in this semester:" , min_value=0.00 ,step=0.5)
    if (credits_till_lastSem + current_credits) == 0:
        return 0
    else:
        cgpa = ((cgpa_till_lastSem * credits_till_lastSem) + (current_gpa * current_credits))/(credits_till_lastSem + current_credits)
    
    return round(cgpa,2)



def semwise_cgpa_calculator():
    numerator = []
    sem_credits = []
    no_of_semester = st.number_input("For how many semesters you want to calculate CGPA?" , min_value=1 , max_value=10)
    st.warning("Please do not include the credits of NON-GRADED COURSES")
    for i in range(no_of_semester):
        col1 , col2 = st.columns(2)
        with col1:
            gpa = st.number_input(f"Enter the GPA of semester {i + 1} :" , min_value=0.00)
        with col2:
            credit = st.number_input(f"Enter the total credits in semester {i + 1} :" , min_value=0.00 , step=0.5)
        
        numerator.append(gpa * credit)
        sem_credits.append(credit)
    
    if sum(sem_credits) == 0:
        return 0
    else:
        cgpa = sum(numerator)/sum(sem_credits)
    
    return round(cgpa,2)





def cgpa_page_2():
    selected = st.radio("How do you want to calculate your CGPA?" , ["Quick CGPA Calculator" , "Semester wise CGPA Calculator"])
    if selected == "Quick CGPA Calculator":
        cgpa = quick_cgpa_calculator()
        if st.button("Submit"):
            if cgpa > 8.00:
                st.balloons()    
            st.title(f"Your CGPA is {str(cgpa)}")
    elif selected == "Semester wise CGPA Calculator":
        cgpa = semwise_cgpa_calculator()
        if st.button("Submit"):
            if cgpa > 8.00:
                st.balloons()   
            st.title(f"Your CGPA is {str(cgpa)}")



def main():
    with st.sidebar:
        navigated = st.selectbox("Choose your page:",["GPA Calculator" , "CGPA Calculator" , "CGPA Calculator for Students with backlog history"])
    if navigated == "GPA Calculator":
        st.header("GPA CALCULATOR")
        gpa_page()
    elif navigated == "CGPA Calculator for Students with backlog history":
        st.header("CGPA Calculator for backlog students" )
        st.success("Why this page? Because in here when it comes to calculating overall CGPA , it is calculated differently for students with backlog history. But dont worry , we have got you covered. Follow the instructions below to know your overall CGPA")
        cgpa_page()
    elif navigated == "CGPA Calculator":
        st.header("CGPA CALCULATOR")
        cgpa_page_2()


        
if __name__ == "__main__":
  main()
