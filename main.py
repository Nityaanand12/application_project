from operations import login,insert_user,delete_user,update_user,report_on_customers,register
while True:
    print("Home Screen:\n\t1.Login\n\t2.Register\n\t3.quit")
    option = input("Enter option from above list :")
    if option =="1":
        flag = login()
        if flag:
            while True:
                print("Customer menu:\n\t1.Create\n\t2.Delete\n\t3.update\n\t4.report\n\t5.quit")
                opt = input("Enter one operation you want to perform :")
                if opt =="1":
                    insert_user()
                elif opt == "2":
                    delete_user()
                elif opt == "3":
                    update_user()
                elif opt == "4":
                    report_on_customers()
                elif opt == "5":
                    print("Thank you")
                    break
                else:
                    print("Wrong option")
                    

    elif option =="2":
        flag2 = register()
        if flag2:
            while True:
                print("Customer menu:\n\t1.Create\n\t2.Delete\n\t3.update\n\t4.report\n\t5.quit")
                opt = input("Enter one operation you want to perform :")
                if opt =="1":
                    insert_user()
                elif opt == "2":
                    delete_user()
                elif opt == "3":
                    update_user()
                elif opt == "4":
                    report_on_customers()
                elif opt == "5":
                    print("Thank you")
                    break
                else:
                    print("Wrong option")
                    
    elif option =="3":
        print("Thank you")
        break
    else:
        print("Wrong option")