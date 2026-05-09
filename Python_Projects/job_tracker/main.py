from utils import display_menu
from database import create_table
from datetime import datetime
from services import (add_application,view_applications,update_status,delete_application,search_applications,display_applications)
from analytics import (total_applicaions,status_summary,top_company,success_rate,export_to_csv)

create_table()

while True:

    display_menu()    
    
    choice=input("Enter your choice: ")


    if choice=="1":
        company=input("Enter company name: ")
        role=input("Enter role: ")
        status=input("Enter status: ")
        applied_date=input("Enter applied date: ")
        notes=input("Enter notes: ")

        if company== "" or role== "":
            print("Company and Role cannot be empty.")
        
        else:
            try:
                datetime.strptime(applied_date,"%d-%m-%Y")
                add_application(company,role,status,applied_date,notes)
            except ValueError:
                print("Invalid date format. Use DD-MM-YYYY")

    elif choice=="2":

        applications=view_applications()

        display_applications(applications)

    elif choice=="3":

        try:
            app_id=int(input("Enter application ID: "))
            new_status=input("Enter new status: ")

            update_status(app_id,new_status)
        except ValueError:
            print("Invalid ID. Please enter numbers only.")


    elif choice=="4":

        try:
            app_id=int(input("Enter application ID to delete: "))

            delete_application(app_id)
        except ValueError:
            print("Invalid ID. Please enter numbers only.")


    elif choice=="5":

        print("\n ====ANALYTICS=====")

        print("Total Applications: ",total_applicaions())

        print("\nStatus Summary: ")
        print(status_summary())

        print("\nTop Company: ")
        print(top_company())

        print("\nSuccess Rate: ")
        print(f"{success_rate():.2f}%")

    elif choice=="6":

        keyword=input("Enter keyword to search: ")

        results=search_applications(keyword)

        if len(results)==0:
            print("No matching application found.")
        else:
            display_applications(results)

    elif choice=="7":

        export_to_csv()

    elif choice=="8":

        print("Exited application")

        break


    else:

        print("Invalid choice. Please try again.")