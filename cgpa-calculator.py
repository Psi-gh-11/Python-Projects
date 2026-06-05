#This project aims to make a simple cgpa and sgpa calculator for students.
def sgpa():
    print("Choose the following as per your convinience to calculate your SGPA:")
    print("-->>Enter '1' to calculate using given Marks\n-->>Enter '2' to calculate using given Grade")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        calculate_using_marks()
    elif ch == 2:
        calculate_using_grade()
    else: 
        print("Invalid choice, please enter a valid option.")

def cgpa():
    sgpa_list = []  
    credit_list = []
    cgpa_result = 0
    val = 0
    print("Enter the following to calculate your CGPA from the SGPA: ")
    n = int(input("Enter the number of semesters u want to calculate the CGPA for: "))
    for i in range(0,n):
        sgpa_res = float(input("Enter the SGPA result: "))
        credit_reg = int(input("Enter the total number of credits 'REGISTERED' for this semester (total credits out of which its calculated): "))
        credit_comp = int(input("Enter the total number of credits 'COMPLETED' for this semester (total credits you have completed): "))
        sgpa_list.append(sgpa_res)
        if credit_reg == credit_comp:
            credit_list.append(credit_reg)
        else:
            credit_list.append(credit_comp)
    for j in range(n):
        val += sgpa_list[j] * credit_list[j]
    cgpa_result = val / sum(credit_list)    #has to be sum(credit_) not sgpa_
    print(f"\nYour total calculated CGPA for {n} semesters is: {cgpa_result:.2f}\n")

def calculate_using_marks():

    dict_details = {}
    s_name = []
    dict_marks_grade = {}
    dict_overall_details = {}
    marks = []
    grade = ""
    g_list = []
    val = 0
    sgpa_val = 0
    

    n = int(input("Enter the number of subjects which have a 'non-zero' credits only: "))
    for i in range(0,n):
        sub_name = input("Enter the name of the subject: ")
        sub_credit = int(input(f"Enter the number of credits assigned to {sub_name}: "))
        sub_marks = float(input(f"Enter the marks for {sub_name}: "))   #should be an f string
        s_name.append(sub_name)
        marks.append(sub_marks)
        dict_details[sub_name] = sub_credit

        if (100 >= sub_marks >= 90):
            grade = "O"
            grade_point = 10
        elif (90 > sub_marks >= 85):
            grade = "A+"
            grade_point = 9
        elif (85 > sub_marks >= 80):
            grade = "A"
            grade_point = 8
        elif (80 > sub_marks >= 75):
            grade = "B+"
            grade_point = 7
        elif (75 > sub_marks >= 70):
            grade = "B"
            grade_point = 6
        elif (70 > sub_marks >= 60):
            grade = "C"
            grade_point = 5
        elif (60 > sub_marks >= 50):
            grade = "D"
            grade_point = 4
        else :
            grade = "F"
            grade_point = 0
        dict_marks_grade[sub_name] = grade_point  #two subjects can have same marks, so changed [k] to [sub_name]
        g_list.append(grade)

    cr = list(dict_details.values())
    gp = list(dict_marks_grade.values())
    for l in range(0,n):
        val += cr[l]*gp[l]
    sgpa_val = val/sum(cr)
    print(f"\nYour total SGPA for this semester is: {sgpa_val:.2f}\n")

    for j in range(0,n):
        dict_overall_details[s_name[j]] = g_list[j]
    ans = input("Fun fact: You can now find out how grade points are assigned to your respective marks in a range. Do you want to know the corresponding grades assigned to your subject? Type 'yes' otherwise type 'no':\n ")
    if ans.lower() == "yes":
        print(dict(dict_overall_details))
    else:
        print("Alright, no problem!")

def calculate_using_grade():
    dict_details = {}
    dict_marks_range = {} #this is the range for the given grade
    dict_grade_point = {} #for the assigned grade this is the corresponding grade point
    grade = []
    s_name = []
    sgpa_val = 0
    val = 0

    n = int(input("Enter number of subjects which have a 'non-zero' credits only: "))
    for i in range(0,n):
        sub_name = input("Enter the name of the subject: ")
        sub_credit = int(input(f"Enter the number of credits assigned to {sub_name}: "))
        sub_grade = input("Enter the grade recieved for the subject: ")
        dict_details[sub_name] = sub_credit
        grade.append(sub_grade)
        s_name.append(sub_name)

        if sub_grade.upper() == "O":
            grade_point = 10
        elif sub_grade.upper() == "A+":
            grade_point = 9
        elif sub_grade.upper() == "A":
            grade_point = 8
        elif sub_grade.upper() == "B+":
            grade_point = 7
        elif sub_grade.upper() == "B":
            grade_point = 6
        elif sub_grade.upper() == "C":
            grade_point = 5
        elif sub_grade.upper() == "D":
            grade_point = 4
        else: 
            grade_point = 0
        dict_grade_point[sub_name] = grade_point
    
    cr = list(dict_details.values()) 
    gp = list(dict_grade_point.values())
    for l in range(0,n): 
        val += cr[l]*gp[l]
    sgpa_val = val/sum(cr)
    print(f"\nYour total SGPA for this semester is: {sgpa_val:.2f}\n")

    for j in range(0,n):
        gp_val = dict_grade_point[s_name[j]]
        if gp_val == 10:
            range_var = "O grade: [100,90] between 90 and 100 - OUTSTANDING"
        elif gp_val == 9:
            range_var = "A+ grade: (90,85] less than 90 but >=85 - EXCELLENT"
        elif gp_val == 8:
            range_var = "A grade: (85,80] less than 85 but >=80 - VERY GOOD"
        elif gp_val== 7:
            range_var = "B+ grade: (80,75] less than 80 but >=75 - GOOD"
        elif gp_val == 6:
            range_var = "B grade: (75,70] less than 75 but >=70 - ABOVE AVERAGE"
        elif gp_val == 5:
            range_var = "C grade: (70,60] less than 70 but >=60 - AVERAGE"
        elif gp_val == 4:
            range_var = "D grade: (60,50] less than 60 but >=50 - PASS"
        else: 
            range_var = "F grade: <50 - FAIL"
        dict_marks_range[s_name[j]] = range_var

    ans = input("Fun fact: Our calculator provides details for your grade points. Do you want to know the marks range for particular grade points? if yes, type 'yes' otherwise type 'no':\n ")
    if ans.lower() == "yes":
        print(dict_marks_range)
    else: 
        print("Alright, no problem!")

def main():
    print("\n~~~ WELCOME TO THE SGPA AND CGPA CALCULATOR ~~~\n")
    print("What do you want to calculate?")
    print("Choose from the following:")
    print("-->>Enter '1' for SGPA\n-->>Enter '2' for CGPA")
    ch = int(input("Enter your desired choice: "))
    if ch == 1:
        sgpa()
    elif ch == 2:
        cgpa()
    else:
        print("Invalid choice please try again.")

if __name__ == '__main__':
    main()