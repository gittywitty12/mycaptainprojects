import csv

def write_into_csv(info_list):
    with open ('student_info.csv', 'a',newline='') as csv_file:
        writer=csv.writer(csv_file)        
        if csv_file.tell() == 0:
            writer.writerow(["Name","age","contact_info","mail_ID"])
        writer.writerow(info_list)
    
if __name__ == '__main__':
    condition =True
    student_num =1
    while (condition):

        info_student=input("Please enter information for the #{} student in the following format: [Name Age Contact_number mail_ID]:- ".format(student_num))
        
        # split 
        info_student_list =info_student.split(' ')
        
        print("\n The entered information is - \nName: {} \nAge: {} \nContact_number: {} \nMail_id: {}".format(info_student_list[0], info_student_list[1], info_student_list[2], info_student_list[3]) )
        
        choice_check=input("Is the entered info correct? (yes/no)")
        if choice_check=="yes":
            write_into_csv(info_student_list)
            condition_check=input("do you want to provide another students info? (YES/NO)")
            if condition_check== "yes":
                condition = True
                student_num=student_num+1
            elif condition_check =="no":
                condition = False
        elif choice_check=="no":
            print("\nPlease enter the correct values!")
