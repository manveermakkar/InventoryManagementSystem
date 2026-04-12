# Setting up Database connection
import mysql.connector as ms
m=ms.connect(host="localhost",user="root",password="Manveer123^",database="INVENTORY__ITEMS1")
mc=m.cursor()

#Set up function to display all tables in the Database
def AllTables():        
 queryTables="SELECT * FROM CATEGORY"
 i=0
 mc.execute(queryTables)
 rows=mc.fetchall()
 while i<len(rows):
         print(rows[i])
         i=i+1
 print("\n")


#Set up function to see the items in a particular Table
def DisplayData(ChID):
            queryTables="SELECT TABLE_NAME FROM CATEGORY WHERE ID = '%s'" %ChID           
            mc.execute(queryTables)
            rows=mc.fetchone()
            print("\n")
            print("Table Name: ",rows[0])
            print("\n")
            global Tablename
            Tablename=rows[0]
            query1="SELECT * from %s" %rows[0]
            mc.execute(query1)
            rows1=mc.fetchall()
            j=0
            while j<len(rows1):
                   print(rows1[j])
                   j=j+1
            print("\n")
            
#Set up function to view all tables and all items in particular table
            #by taking input from users and calling above functions.                  
def ViewItems():
        
        AllTables()    
        ChID=input("Select Which table you want to view by writing their ID: ")
        try:
            DisplayData(ChID)
        except:
          print("!!!!!----------Enter Valid ID to proceed----------!!!!!\n")
          ViewItems()
       
        
#function to Insert items
          
def InsertItems():        
    AllTables()
    ChID=input("Select which table you want to Insert by writing their ID: ")
    try:
     DisplayData(ChID)
    except:
     print("!!!!!----------Enter Valid ID to proceed----------!!!!! \n")
     InsertItems()
     
    SID=input("Provide ID in format ID as number and unique: ")
    product_name=input("Provide Product Name: ")
    quantity=input("Provide Quantity as number: ")            
    price=input("Provide price as float number till 2 decimal places: ")
    try:
        Insertsql1="INSERT INTO {} (SID,product_name,quantity,price) VALUES (%s, %s, %s, %s)".format(Tablename)
        Insertdata1=(SID,product_name,quantity,price)
        mc.execute(Insertsql1,Insertdata1)    
        m.commit()
        print("\n")  
        print("successfully inserted")
    except:
        print("\n")   
        print("!!!!!----------Enter all values of insert properly----------!!!!! \n")
        print("*****SID should be as per table***** \n")
        print("*****Product name is alphanumeric***** \n")
        print("*****Quantity should be whole number***** \n")
        print("*****Price should be Float and decimal to 2 places***** \n")       
        InsertItems()



        

#function to Update items
              
def UpdateItems():
        
    AllTables()
    ChID=input("Select which table you want to Update by writing their ID: ")
    try:
        DisplayData(ChID)
    except:
         print("!!!!!----------Enter Valid ID to proceed----------!!!!!  \n")
         UpdateItems()
     
    SID=input("Select which row of table to update by writing their ID: ")
    product_name=input("Provide Product Name: ")
    quantity=input("Provide Quantity as number: ")            
    price=input("Provide price as float number till 2 decimal places: ")
    try:
            updatesql1="UPDATE {} SET product_name=%s,quantity=%s,price=%s WHERE SID=%s".format(Tablename)
            updatedata1=(product_name,quantity,price,SID)
            mc.execute(updatesql1,updatedata1)               
            m.commit()
            print("\n")  
            print("successfully updated")
    except:
            print("\n")   
            print("!!!!!---------Enter all values of Update properly----------!!!!!\n")
            print("*****SID should be as per table***** \n")
            print("*****Product name is alphanumeric***** \n")
            print("*****Quantity should be whole number***** \n")
            print("*****Price should be Float and decimal to 2 places***** \n")       
            UpdateItems()

#function to Delete items
          
def DeleteItems():
        
    AllTables()
    ChID=input("select the table from which you want to delete the record by choosing its ID: ")
    try:
     DisplayData(ChID)
    except:
     print("!!!!!---------Enter Valid ID to proceed----------!!!!! \n")
     DeleteItems()
     
    SID=input("Select which row of table to delete by writing their ID: ")
    try:
        deletesql1="DELETE from {} WHERE SID=%s".format(Tablename)
        deletedata1=[SID]
        mc.execute(deletesql1,deletedata1)    
        m.commit()
        print("\n")  
        print("successfully deleted")
    except:
        print("\n")   
        print("*****SID should be as per table***** \n")
        DeleteItems()


#Switch mehthod to see the choice of user , what was selected
def switch(choice):
    if choice == 1:
        return ViewItems() 
    elif choice == 2:
        return InsertItems()
    elif choice == 3:
        return UpdateItems()
    elif choice == 4:
        return DeleteItems()    
    else:
        print("!!!!!---------please do it again----------!!!!! \n")
        choice =int(input("SELECT THE RESPECTIVE NUMBER FOR PERFORMING THE TASK: "))
        switch(choice)

#Static information to be taken by user to display his/her information
print(" Welcome to INVENTORY MANAGEMENT SYSTEM by Manveer Makkar (12th A, FAS)!!!\n")
print("ENTER USER DETAILS BELOW:-\n")
##Static information to be taken by user to display his/her information and ask choices
def UserEntry():
    Name=input("ENTER YOUR NAME: ")
    EmployeeNumber =input("ENTER EMPLOYEE ID: ")
    print("\n")      
    print("NAME-", Name)
    print("\n")  
    print("EmployeeID-" ,EmployeeNumber)
    print("\n")
    global Confirm1
    Confirm1=input("please confirm your details(Y/N): ")
    if Confirm1 != "Y":
       print("!!!!!---------please renter information----------!!!!! \n") 
       UserEntry()    
    else:  
        print("\n")
        print("\n")
        print("1-VIEW ITEMS OF AN INVENTORY")
        print("2-INSERT ITEMS OF AN INVENTORY")
        print("3-UPDATE ITEMS OF AN INVENTORY")
        print("4-DELETE ITEMS OF AN INVENTORY")
        print("\n")
        choice =int(input("SELECT THE RESPECTIVE NUMBER FOR PERFORMING THE TASK: "))
        #Based on user choice perform action
        switch(choice)
        
#to start the project this function is called
UserEntry()
exit()
