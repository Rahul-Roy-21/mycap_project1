import csv

# Function to Append a Row Of Info into .csv file
def write_to_file(student_info):
    f = open('students_details.csv',mode='a',newline='')
    writer_obj = csv.writer(f)

    if f.tell() == 0:
        writer_obj.writerow(["NAME","ROLL","AGE","CONTACT","EMAIL"])
    
    writer_obj.writerow(student_info)

# Display Student Info from a info_list
def display_details(info_list):
    print('_'*15)
    print("NAME : {}".format(info_list[0]))
    print("ROLL No. : {}".format(info_list[1]))
    print("AGE : {} Years".format(info_list[2]))
    print("CONTACT NO. : {}".format(info_list[3]))
    print("EMAIL ID : {}".format(info_list[4]))
    print('_'*20)

if __name__ == '__main__':
    more_info, student_entry = True, 1
    
    while(more_info):
        inf = input("Enter Student {} Details as (Name Roll Age Contact_No Email_ID): ".format(student_entry))

        student_info_list = inf.split(" ")
        display_details(student_info_list)

        user_satisfied = input("Everything's OK, Insert this Entry? Answer in (yes/no): ")
        
        if user_satisfied.lower() == 'yes':
            write_to_file(student_info_list)
            student_entry += 1
            print("\n1 ROW INSERTED SUCCESSFULLY !!!" + "~"*30 + "\n")

        elif user_satisfied.lower() == 'no':
            print("Re-Enter the Student Details __")
            continue
        
        continue_input = input("Do You Want to Enter More Students? Answer in (yes/no): ")

        if continue_input.lower() == 'no':
            more_info = False
        elif continue_input.lower() == 'yes':
            print("_"*20 + "\n")
            continue

    
