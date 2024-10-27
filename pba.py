import mysql.connector as p
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
mydb=p.connect(host='localhost', user='root', passwd='5100')
myc=mydb.cursor()

myc.execute("CREATE DATABASE IF NOT EXISTS PBA")
myc.execute("USE PBA")

def sign_in():
    import mysql.connector as p
    mydb=p.connect(host='localhost', user='root', passwd='5100', database='PBA')
    myc=mydb.cursor()
    oo=input("do you already have an account? (y/n) ")
    while oo=='n': #for sign up
        print("\nSIGN UP")
        myc.execute("CREATE TABLE IF NOT EXISTS account(nuser varchar(50), psswd varchar(20), contact varchar(40), salary float)")
        use=input("create username: ")
        cntct=input("enter email id: ")
        psswd0=input("enter password: ")
        if len(psswd0)>6:
            psswd1=input("confirm password: ")
            if psswd0==psswd1:
                sal=int(input("enter monthly salary (this is for comparison purposes): "))
                myc.execute("SELECT * FROM account")
                rec=myc.fetchall()
                if len(rec)>1:
                    myc.execute("DROP TABLE account")
                    myc.execute("CREATE TABLE account(nuser varchar(50), psswd varchar(25), contact varchar(40), salary int)")
                q="INSERT INTO account VALUES('{}', '{}', '{}', {})".format(use, psswd0, cntct, sal)
                myc.execute(q)
                mydb.commit()
                print("\nSIGN UP SUCCESS!!!")
                return psswd1
                oo=''
            else:
                print("password confirmation was not correct...")
        else:
            print("password must be longer than 6 characters!")


    


def compchart(l1, l2, l3):
    x = np.array(l1)
    y1 = np.array(l2)
    z2 = np.array(l3)
    x_axis = np.arange(len(x))
    plt.bar(x_axis - 0.2, y1, 0.4, label = 'expense')
    plt.bar(x_axis + 0.2, z2, 0.4, label = 'budget')
    plt.xticks(x_axis, x)
    plt.xlabel("Areas")
    plt.ylabel("Rupees")
    plt.title("Expenditure & Budget")
    plt.legend()
    plt.show()

    

print("\nwelcome to your own Personal Budget Analyzer!!!")

psswd1=sign_in()

myc.execute("SHOW TABLES") #log in
rec=myc.fetchall()
for i in rec:
    if 'account' in i:
        print("\nLOG IN")
        myc.execute("SELECT nuser FROM account")
        a=myc.fetchone()
        use=a[0]
        print("\nwelcome back", use, "!!!")
        myc.execute("SELECT psswd FROM account")
        a=myc.fetchall()
        psswd=a[0][0]
        ss=True
        while ss:
            psswd1=input("\nplease enter your password: ")
            if psswd1!=psswd:
                print("\ninvalid password")
                q=input("do you wish to quit? (y/n)")
                if q in 'yY':
                    print("exiting")
                    mydb.close()
                    break
            else:
                print("\nLOG IN SUCCESSFUL")
                ss=False
        break
    if 'account' not in i:
        print("you haven't signed up")
        psswd1=sign_in()

ch=0
#main menu, executes only if psswd inputed is right
while psswd1==psswd:
    print("\nMAIN MENU")
    print("1. Account & Budget Plan")
    print("2. Monthly Analysis")
    print("3. Previous Reports")
    print("4. Exit Program")
    c=int(input("\nPlease enter your choice: "))

    if c==1: #first module, first sub-menu
        while ch!=5:
            print("\nAccount & Budget Plan")
            print("1. See Budget Plan")
            print("2. Create New Budget Plan")
            print("3. Modify Existing Budget Plan")
            print("4. Account Settings")
            print("5. Exit Menu")
            ch=int(input("Enter choice: "))
            if ch==1:
                print("\narea\t\t budget")
                myc.execute("SELECT area, budget FROM budget WHERE budget IS NOT NULL")
                c=myc.rowcount
                rec=myc.fetchall()
                for i in rec:
                    print(i[0], "\t", i[1])
            elif ch==2:
                myc.execute("DROP TABLE budget")
                myc.execute("CREATE TABLE budget(ano int, area varchar(25), budget int)")
                myc.execute("INSERT INTO budget(ano, area, budget) VALUES (1, 'groceries', NULL), (2, 'utilities', NULL), (3, 'medical', NULL), (4, 'electricity', NULL), (5, 'water', NULL), (6, 'education', NULL), (7, 'insurance', NULL), (8, 'transportation', NULL), (9, 'outings', NULL), (10, 'entertainment', NULL)")
                mydb.commit()
                ss=True
                while ss:
                    print("\nBUDGET OPTIONS")
                    print("1. groceries")
                    print("2. utilities")
                    print("3. medical")
                    print("4. electricity")
                    print("5. water")
                    print("6. education")
                    print("7. insurances")
                    print("8. transportation")
                    print("9. outings")
                    print("10. entertainment")
                    print("11. exit menu")
                    n=int(input("enter required area: "))
                    if n in range(1,11): #option number is same as that of ano in sql table
                        bud=int(input("enter budget amount: "))
                        q="UPDATE budget SET budget={} WHERE ano={}".format(bud, n)
                        myc.execute(q)
                        mydb.commit()
                    elif n==11:
                        ss=False
            elif ch==3:
                o='y'
                myc.execute("SELECT * FROM budget WHERE budget IS NOT NULL")
                print("BUDGET PLAN")
                print("\nano\t area\t\t budget amount")
                for i in myc:
                    print(i[0], "\t", i[1], "\t", i[2])
                for o in 'y':
                    n=int(input("enter the ano of the area that needs to be modified: "))
                    bud=int(input("enter new budget amount: "))
                    q="UPDATE budget SET budget={} WHERE ano={}".format(bud, n)
                    myc.execute(q)
                    mydb.commit()
                    o=input("do you wish to continue? (y/n)")
                    if o not in 'yn':
                        print('invalid option! try again')
                        o=input("\ndo you wish to continue? (y/n)")
            elif ch==4:
                psswd0=input("please enter password: ")
                if psswd0==psswd:
                    o=0
                    while o!=6:#secondary sub-menu
                        print("\nACCOUNT SETTINGS")
                        print("1. See Account Details")
                        print("2. Change Password")
                        print("3. Change Username")
                        print("4. Change Email")
                        print("5. Update Salary")
                        print("6. Previous Page")
                        o=int(input("enter option: "))
                        if o==1:
                            myc.execute("SELECT * FROM account")
                            rec=myc.fetchone()
                            print("\nACCOUNT DETAILS")
                            print("Username: ", rec[0])
                            print("Password: ", rec[1])
                            print("Your Email: ", rec[2])
                            print("Your Salary: ", rec[3])
                        elif o==2:
                            npsswd=input("enter new password: ")
                            if len(npsswd)>6:
                                npsswd0=input("confirm new password: ")
                                if npsswd0==npsswd:
                                    q="UPDATE account SET psswd='{}' WHERE psswd='{}'".format('npsswd', 'psswd')
                                    myc.execute(q)
                                    mydb.commit()
                                    print("please log in again!")
                                    mydb.close()
                                else:
                                    print("the confirmation went wrong")
                            else:
                                print("password should be longer than 6 characters!")
                        elif o==3:
                            usen=input("enter new username: ")
                            q="UPDATE account SET nuser='{}' WHERE psswd='{}'".format(usen, psswd0)
                            myc.execute(q)
                            mydb.commit()
                            print("successfully changed to", usen)
                        elif o==4:
                            email=input("enter new email: ")
                            q="UPDATE account SET contact='{}' WHERE psswd='{}'".format(email, psswd0)
                            myc.execute(q)
                            mydb.commit()
                        elif o==5:
                            sal=input("enter updated salary: ")
                            q="UPDATE account SET salary={} WHERE psswd='{}'".format(sal, psswd0)
                            myc.execute(q)
                            mydb.commit()
                        elif o not in (1, 2, 3, 4, 5, 6):
                            print("please select a valid option")
                else:
                    print("Incorrect password")
            else:
                print("invlaid option, try again")

    elif c==2:
        ss=True
        print("\nMonthly Analysis")
        dt=input("\nenter today's month and year: ")
        for i in dt:
            if i.isspace():
                d=dt.split()
                dt=d[0]+'_'+d[1]
        myc.execute("DROP TABLE IF EXISTS {}".format(dt))
        q="CREATE TABLE {}(ano int PRIMARY KEY, area varchar(25), expense int, budget int)".format(dt)
        myc.execute(q)
        print("\nPlease insert the values for each budgeted area below for the analysis!")
        myc.execute("SELECT * FROM budget WHERE budget IS NOT NULL")
        rec=myc.fetchall()
        for i in rec:
            e=int(input("\nEnter the expenses spent on "+i[1]+" this month: "))
            q="INSERT INTO {} VALUES({}, '{}', {}, {})".format(dt, i[0], i[1], e, i[2])
            myc.execute(q)
            mydb.commit()
        print("\narea\t\t expenditure\t budget")
        q="SELECT area, expense, budget FROM {}".format(dt)
        myc.execute(q)
        rec=myc.fetchall()
        for i in rec:
            print(i[0], '\t', i[1], '\t\t', i[2])
        while ss:#second sub-menu
            print("\nANALYSIS")
            print("1. Area-wise")
            print("2. Salary comparison")
            print("3. Graphs")
            print("4. Exit")
            ch=int(input("enter choice: "))
            if ch==1:#deviations
                q="SELECT SUM(expense) FROM {}".format(dt)
                myc.execute(q)
                d=myc.fetchone()
                a=d[0]
                print("\n1.1 total money spent: ", a)
                print("\n1.2 areas that need improvement")
                print("area\t\t increased spending")
                q="SELECT area, expense, budget FROM {}".format(dt)
                myc.execute(q)
                rec=myc.fetchall()
                r=myc.rowcount
                i=0
                while i<r:
                    a=rec[i][1]-rec[i][2]
                    if a>0:
                        print(rec[i][0], '\t', a)
                    i+=1
                print("\n1.3 areas that have improved")
                print("area\t\t improvement by")
                q="SELECT area, expense, budget FROM {}".format(dt)
                myc.execute(q)
                rec=myc.fetchall()
                r=myc.rowcount
                i=0
                while i<r:
                    a=rec[i][2]-rec[i][1]
                    if a>0:
                        print(rec[i][0], '\t', a)
                    i+=1
            elif ch==2:#comparisons
                q="SELECT SUM(expense), SUM(budget) FROM {}".format(dt)
                myc.execute(q)
                d=myc.fetchone()
                a=d[1]-d[0]
                if a>0:
                    print("\n2.1. money saved: ", a, 'rupees')
                elif a==0:
                    print("\n2.1. you didn't save any money")
                else:
                    print("\n2.1. you've lost: ", a, 'rupees')
                myc.execute("SELECT salary FROM account")
                sal0=myc.fetchone()
                a=float(sal0[0])-float(d[0])
                print("2.2. money remaining from monthly salary: ", a)
            elif ch==3:#graph
                q="SELECT area, expense, budget FROM {}".format(dt)
                myc.execute(q)
                rec=myc.fetchall()
                l1=[]
                l2=[]
                l3=[]
                for j in rec:
                    l1.append(j[0])
                    l2.append(j[1])
                    l3.append(j[2])
                compchart(l1, l2, l3)
            elif ch==4: #exiting sub-menu
                o=input("are you sure? (y/n) ")
                if o in 'yY':
                    print("\nexiting analysis")
                    ss=False
            else:
                print("invalid option")

    elif c==3:#third sub-menu
        ch=''
        while ch!='3':
            print("\nBUDGET HISTORY")
            print("1. Previous Reports")
            print("2. Average Expenditure Per Month")
            print("3. Exit")
            ch=input("please enter your choice: ")
            myc.execute("SHOW TABLES")
            rec=myc.fetchall()
            T={}
            o=1
            for i in rec:
                if i[0] not in ('account', 'budget'):
                    T[o]=i[0]
                    o+=1

            if ch=='1':
                print("\nBUDGET HISTORY")
                print("\nno. \tmonth")
                for i in T:
                    print(i, '\t', T[i])
                o=int(input("\nenter the mno of the month who's report is required: "))
                dt=T[o]
                print("\nREPORT")
                #table representation of selected month's expenditure
                print("\narea\t\t expenditure\t budget")
                q="SELECT area, expense, budget FROM {}".format(dt)
                myc.execute(q)
                rec=myc.fetchall()
                for i in rec:
                    print(i[0], '\t', i[1], '\t\t', i[2])
                cc=0
                while cc!=4:#secondary sub-menu
                    print("\nANALYSIS")
                    print("1. Area-wise")
                    print("2. Salary comparison")
                    print("3. Graphs")
                    print("4. Exit")
                    cc=int(input("enter choice: "))
                    if cc==1:#deviations
                        q="SELECT SUM(expense) FROM {}".format(dt)
                        myc.execute(q)
                        d=myc.fetchone()
                        a=d[0]
                        print("\n1.1 total money spent: ", a)
                        print("\n1.2 areas that need improvement")
                        print("area\t\t increased spending")
                        q="SELECT area, expense, budget FROM {}".format(dt)
                        myc.execute(q)
                        rec=myc.fetchall()
                        r=myc.rowcount
                        i=0
                        while i<r:
                            a=rec[i][1]-rec[i][2]
                            if a>0:
                                print(rec[i][0], '\t', a)
                            i+=1
                        print("\n1.3 areas that have improved")
                        print("area\t\t improvement by")
                        q="SELECT area, expense, budget FROM {}".format(dt)
                        myc.execute(q)
                        rec=myc.fetchall()
                        r=myc.rowcount
                        i=0
                        while i<r:
                            a=rec[i][2]-rec[i][1]
                            if a>0:
                                print(rec[i][0], '\t', a)
                            i+=1
                    elif cc==2:#comparisons
                        q="SELECT SUM(expense), SUM(budget) FROM {}".format(dt)
                        myc.execute(q)
                        d=myc.fetchone()
                        a=d[1]-d[0]
                        if a>0:
                            print("\n2.1. money saved: ", a, 'rupees')
                        elif a==0:
                            print("\n2.1. you didn't save any money")
                        else:
                            print("\n2.1. you've lost: ", a, 'rupees')
                        myc.execute("SELECT salary FROM account")
                        sal0=myc.fetchone()
                        a=float(sal0[0])-float(d[0])
                        print("2.2. money remaining from monthly salary: ", a)
                    elif cc==3:#graph
                        q="SELECT area, expense, budget FROM {}".format(dt)
                        myc.execute(q)
                        rec=myc.fetchall()
                        l1=[]
                        l2=[]
                        l3=[]
                        for j in rec:
                            l1.append(j[0])
                            l2.append(j[1])
                            l3.append(j[2])
                        compchart(l1, l2, l3)
                    else:
                        print("\ninvalid option")

            elif ch=='2':
                l=len(T)
                print("\nyou have used Personal Budget Analyzer for", l, 'months')
                L=[]
                print("\nmonth\t total monthly expenditure")
                for i in T:
                    dt=T[i]
                    q="SELECT SUM(expense) FROM {}".format(dt)
                    myc.execute(q)
                    v=myc.fetchone()
                    L.append(v[0])
                    print(dt, '\t', v[0])
                print("\nmoney spent so far: ", sum(L))
                print("averge spent per month: ", st.mean(L))
            
            else:
                print("invalid option")
         
    elif c==4: #exiting program
        o='0'
        while o not in 'ynNY':
            o=input("are you sure you want to exit? (y/n) ")
            if o in 'yY':
                print("exiting application")
                mydb.close()
                print("application exited")
                psswd1=''
            elif o not in 'nN':
                print('please input valid option')

    else:
        print("Please enter a valid choice")
