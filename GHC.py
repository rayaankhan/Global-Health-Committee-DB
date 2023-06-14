import subprocess as sp
import pymysql
import pymysql.cursors
import maskpass
# 1
def Diseases_Data():
    query = "SELECT * FROM DISEASE NATURAL JOIN TYPE_NAME;"
    print(query)
    cur.execute(query)
    output = cur.fetchall()
    con.commit()
    for row in output:
        print(row)
    print("Data has been retrieved")
    return
# 2
def Health_Stats_Data():
    query = "SELECT * FROM HEALTH_STATISTICS NATURAL JOIN IDS_OF_COUNTRIES_AFFECTED;"
    print(query)
    cur.execute(query)
    output = cur.fetchall()
    con.commit()
    for row in output:
        print(row)
    print("Data has been retrieved")
    return
# 3 code changed
def Offices_Data():
    query = "SELECT * FROM (BRANCHES NATURAL JOIN LOCATION_OF_BRANCH) NATURAL JOIN COUNTRY_LOCATION;"
    print(query)
    cur.execute(query)
    output = cur.fetchall()
    con.commit()
    for row in output:
        print(row)
    print("Data has been retrieved")
    return
# 4
def Max_Duration():
    query = "SELECT PROGRAM_NAME, DURATION FROM PROGRAM_TIME WHERE DURATION IN(SELECT MAX(DURATION) FROM PROGRAM_TIME);"
    print(query)
    cur.execute(query)
    output = cur.fetchall()
    con.commit()
    for row in output:
        print(row)
    print("Data has been retrieved")
    return
# 5
def Sum_Deaths():
    query1 = "CREATE VIEW temp AS SELECT NO_OF_PEOPLE_AFFECTED - NO_OF_PEOPLE_RECOVERED AS Death FROM HEALTH_STATISTICS;"
    query2 = "SELECT SUM(Death) FROM temp;"
    query3 = "DROP VIEW temp;"
    cur.execute(query1)
    cur.execute(query2)
    output = cur.fetchall()
    cur.execute(query3)
    con.commit()
    for row in output:
        print(row)
    print("Data has been retrieved")
    return
# 6
def Sum_Local_Organisations():
    query = "SELECT SUM(NO_OF_LOCAL_ORGANIZATIONS) FROM BRANCHES;"
    print(query)
    cur.execute(query)
    output = cur.fetchall()
    con.commit()
    for row in output:
        print(row)
    print("Data has been retrieved")
    return
# 7
def Country_finder():
    to_find = input(
        "Type a string that comes at the beginning of the country's name: ")
    query = "SELECT DISTINCT COUNTRY_NAME FROM MEMBERS WHERE COUNTRY_NAME REGEXP '^%s';" % (
        to_find)
    print(query)
    cur.execute(query)
    output = cur.fetchall()
    con.commit()
    for row in output:
        print(row)
    print("Data has been retrieved")
    return
# 8
def Representative_finder():
    to_find = input(
        "Type a string that comes at the end of the representative's name: ")
    query = "SELECT DISTINCT NAME FROM MEMBERS WHERE NAME REGEXP '%s$';" % (to_find)
    print(query)
    cur.execute(query)
    output = cur.fetchall()
    con.commit()
    for row in output:
        print(row)
    print("Data has been retrieved")
    return
# 9
def Disease_finder_by_name():
    to_find = input("Type in part of the Disease name: ")
    query = "SELECT DISTINCT DISEASE_NAME AS 'Disease Name' FROM DISEASE WHERE DISEASE_NAME REGEXP '%s';" % (to_find)
    print(query)
    cur.execute(query)
    output = cur.fetchall()
    con.commit()
    for row in output:
        print(row)
    print("Data has been retrieved")
    return
# 10
def Researches_with_status():
    to_find = int(input("Enter the threashold for status of completion: "))
    query = "SELECT SERIAL_NO FROM BIOMEDICAL_RESEARCHES WHERE STATUS_OF_COMPLETION >= %d;" % (
        to_find)
    print(query)
    cur.execute(query)
    output = cur.fetchall()
    con.commit()
    for row in output:
        print(row)
    print("Data has been retrieved")
    return
# 11
def Branches_with_organisations():
    to_find = int(
        input("Enter the threashold of number of local organizations: "))
    query = "SELECT BRANCH_ID AS 'Branch IDs' FROM BRANCHES WHERE NO_OF_LOCAL_ORGANIZATIONS >= %d;" % (
        to_find)
    print(query)
    cur.execute(query)
    output = cur.fetchall()
    con.commit()
    for row in output:
        print(row)
    print("Data has been retrieved")
    return
# 12
def DiseaseID_mortality():
    to_find = int(input("Enter the threashold for mortality: "))
    query = "SELECT HEALTH_STATISTICS.DISEASE_ID, DISEASE_NAME FROM DISEASE NATURAL JOIN HEALTH_STATISTICS WHERE MORTALITY_RATE >= '%d';" % (to_find)
    print(query)
    cur.execute(query)
    output = cur.fetchall()
    con.commit()
    for row in output:
        print(row)
    print("Data has been retrieved")
    return
# 13
def Rnaught_recoveries():
    query = "SELECT RNAUGHT FROM DISEASE NATURAL JOIN HEALTH_STATISTICS WHERE NO_OF_PEOPLE_RECOVERED IN(SELECT MAX(NO_OF_PEOPLE_RECOVERED) FROM HEALTH_STATISTICS);"
    print(query)
    cur.execute(query)
    output = cur.fetchall()
    con.commit()
    for row in output:
        print(row)
    print("Data has been retrieved")
    return
# 14
def Mortality_minDoc():
    query = "SELECT COUNTRY_ID, MORTALITY_RATE FROM (MEDICAL_INFRASTRUCTURE NATURAL JOIN IDS_OF_COUNTRIES_AFFECTED) NATURAL JOIN HEALTH_STATISTICS WHERE NO_OF_DOCTORS IN(SELECT MIN(NO_OF_DOCTORS));;"
    print(query)
    cur.execute(query)
    output = cur.fetchall()
    con.commit()
    for row in output:
        print(row)
    print("Data has been retrieved")
    return
# 15
def AddingPolicies():
    try:
        row = {}
        print("Enter new Policy's details: ")
        row["PROGRAM_NO"] = int(input("Program Number: "))
        row["PROGRAM_NAME"] = input("Program Name: ")
        row["PROGRAM_TYPE"] = input("Program Type: ")
        row["DURATION"] = int(input("Duration: "))
        row["LOCATIONS"] = input("Location: ")
        row["DISEASE_ID"] = int(input("Disease ID: "))
        query1 = "SELECT LOCATION_ID FROM LOCATIONS WHERE NAME='%s';"%(row["LOCATIONS"])
        cur.execute(query1)
        output = cur.fetchall()
        output = (int)((output[0])[0])
        # print(output)
        query2 = "INSERT INTO PROGRAM_TIME(PROGRAM_NAME, DURATION, PROGRAM_TYPE)VALUES('%s','%d','%s');" % (row["PROGRAM_NAME"], row["DURATION"], row["PROGRAM_TYPE"])
        query3 = "INSERT INTO HEALTH_POLICIES(PROGRAM_NO, PROGRAM_NAME, LOCATION_ID, DISEASE_ID)VALUES('%d','%s','%d','%d');" % (row["PROGRAM_NO"], row["PROGRAM_NAME"],output, row["DISEASE_ID"])
   
        

        # print(query)
        cur.execute(query1)
        cur.execute(query2)
        cur.execute(query3)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
# 16
def AddMembers():
    try:
        row = {}
        print("Enter new Member's details: ")
        row["COUNTRY_ID"] = int(input("Country ID: "))
        row["COUNTRY_NAME"] = input("Country Name: ")
        row["NAME"] = input("Head's Name: ")
        row["YEAR_OF_TERM"] = int(input("Year Of Term: "))
        row["DESIGNATION"] = input("Designation: ")

        query1 = "INSERT INTO MEMBERS(COUNTRY_ID, COUNTRY_NAME, NAME,YEAR_OF_TERM, DESIGNATION, SSN_COUNTRY_ID )VALUES('%d','%s','%s','%d','%s','%d')" % (
            row["COUNTRY_ID"], row["COUNTRY_NAME"], row["NAME"], row["YEAR_OF_TERM"], row["DESIGNATION"], row["COUNTRY_ID"])

        # print(query)
        cur.execute(query1)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
# 17
def AddDisease():
    try:
        row = {}
        print("Enter new Disease's details: ")
        row["DISEASE_ID"] = int(input("Disease ID: "))
        row["DISEASE_NAME"] = input("Disease Name: ")
        row["RNAUGHT"] = int(input("RNaught: "))
        row["DISEASE_TYPE"] = input("Disease Type: ")

        query1 = "INSERT INTO DISEASE(DISEASE_ID, DISEASE_NAME, RNAUGHT )VALUES('%d','%s','%d');" % (
            row["DISEASE_ID"], row["DISEASE_NAME"], row["RNAUGHT"])
        query2 = "INSERT INTO TYPE_NAME(DISEASE_NAME, DISEASE_TYPE)VALUES('%s','%s');" % (
            row["DISEASE_NAME"], row["DISEASE_TYPE"])
        print(query2)
        print(query1)
        cur.execute(query2)
        cur.execute(query1)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
# 18
def AddingInfrastructure():
    try:
        row = {}
        print("Enter new Infrastructure's details: ")
        row["COUNTRY_ID"] = int(input("Country ID: "))
        row["NO_OF_HOSPITALS"] = int(input("No. Of Hospitals: "))
        row["NO_OF_DOCTORS"] = int(input("No. Of Doctors: "))
        row["NO_OF_EQUIPMENTS"] = int(input("No. Of Equipments: "))
        row["SERIAL_NO"] = int(input("Serial No.: "))
        row["EQUIPMENT_TYPE"] = input("Equipment Type: ")
        query1 = "INSERT INTO NO_OF_EQUIPMENT(NO_OF_EQUIPMENTS, EQUIPMENT_TYPE) VALUES('%d', '%s');" % (
            row["NO_OF_EQUIPMENTS"], row["EQUIPMENT_TYPE"])
        cur.execute(query1)
        cur.execute("SELECT NUMBER_ID FROM NO_OF_EQUIPMENT WHERE NO_OF_EQUIPMENTS='%d';"%(row["NO_OF_EQUIPMENTS"]))
        output = cur.fetchall()
        output = (int)((output[0])[0])
        # print(output)
        query2 = "INSERT INTO MEDICAL_INFRASTRUCTURE(COUNTRY_ID, NO_OF_HOSPITALS, NO_OF_DOCTORS, NUMBER_ID, SERIAL_NO)VALUES('%d','%d','%d','%d','%d')" % (
            row["COUNTRY_ID"], row["NO_OF_HOSPITALS"], row["NO_OF_DOCTORS"], output, row["SERIAL_NO"])

        # print(query)
        # cur.execute(query1)
        cur.execute(query2)
        # cur.execute(query4)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
# 19
def RepresentativeChange():
    try:
        print("Enter new Representative: ")
        Representative = input("Write the name of New Representative: ")
        country = input("Enter the country's name: ")
        query = "UPDATE MEMBERS SET NAME='%s' WHERE COUNTRY_NAME='%s'" % (
            Representative, country)
        cur.execute(query)
        con.commit()
        print("Updated")
    except Exception as e:
        con.rollback()
        print("Failed to update into database")
        print(">>>>>>>>>>>>>", e)
# 20
def LocationChange():
    try:
        print("Enter new Location: ")
        Location = input("Write the name of New Location ID: ")
        ID = int(input("Enter the Branch ID: "))
        query = "UPDATE BRANCHES SET LOCATION_ID='%s' WHERE BRANCH_ID='%d'" % (
            Location, ID)
        cur.execute(query)
        con.commit()
        print("Updated")
    except Exception as e:
        con.rollback()
        print("Failed to update into database")
        print(">>>>>>>>>>>>>", e)
# 21
def CompletionChange():
    try:
        print("Updating the status of completion: ")
        Status = int(input("Write the new status of completion: "))
        ID = int(input("Enter the Serial Number: "))
        query = "UPDATE BIOMEDICAL_RESEARCHES SET STATUS_OF_COMPLETION='%d' WHERE SERIAL_NO='%d'" % (
            Status, ID)
        cur.execute(query)
        con.commit()
        print("Updated")
    except Exception as e:
        con.rollback()
        print("Failed to update into database")
        print(">>>>>>>>>>>>>", e)
# 22
def VaccineChange():
    try:
        print("Updating the Vaccination Status: ")
        Status = int(input("Write the new Vaccine's Status: "))
        Type = input("Enter the Disease Type: ")
        query = "UPDATE HEALTH_STATISTICS SET VACCINATION_STATUS='%d' WHERE DISEASE_TYPE='%s'" % (
            Status, Type)
        cur.execute(query)
        con.commit()
        print("Updated")
    except Exception as e:
        con.rollback()
        print("Failed to update into database")
        print(">>>>>>>>>>>>>", e)
# 23
def PolicyDeletion():
    try:
        print("Deleting an expired policy: ")
        progname = input("Program name that is to be deleted: ")
        query2 = "DELETE FROM PROGRAM_TIME WHERE PROGRAM_NAME='%s';"%(progname)
        cur.execute("SELECT PROGRAM_NO FROM HEALTH_POLICIES WHERE PROGRAM_NAME='%s';"%(progname))
        progno = cur.fetchall()
        progno = (int)((progno[0])[0])
        query3 = "DELETE FROM IMPLEMENT WHERE PROGRAM_NO='%d';"%(progno)
        query4 = "DELETE FROM AFFECTS WHERE PROGRAM_NO='%d';"%(progno)
        cur.execute(query3)
        cur.execute(query4)
        query1 = "DELETE FROM HEALTH_POLICIES WHERE PROGRAM_NO='%d';"%(progno)
        cur.execute(query1)
        cur.execute(query2)        
        con.commit()
        print("All expired policies deleted")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
# 24
def CountryRemoval():
    try:
        print("Removing a country from country_location: ")
        ID = int(input("Write the Country's ID: "))
        query2 = "DELETE FROM COUNTRY_LOCATION WHERE COUNTRY_ID='%d';" % (ID)
        cur.execute(query2)
        con.commit()
        print("Deletion successfull")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        Diseases_Data()
    elif(ch == 2):
        Health_Stats_Data()
    elif(ch == 3):
        Offices_Data()
    elif(ch == 4):
        Max_Duration()
    elif(ch == 5):
        Sum_Deaths()
    elif(ch == 6):
        Sum_Local_Organisations()
    elif(ch == 7):
        Country_finder()
    elif(ch == 8):
        Representative_finder()
    elif(ch == 9):
        Disease_finder_by_name()
    elif(ch == 10):
        Researches_with_status()
    elif(ch == 11):
        Branches_with_organisations()
    elif(ch == 12):
        DiseaseID_mortality()
    elif(ch == 13):
        Rnaught_recoveries()
    elif(ch == 14):
        Mortality_minDoc()
    elif(ch == 15):
        AddingPolicies()
    elif(ch == 16):
        AddMembers()
    elif(ch == 17):
        AddDisease()
    elif(ch == 18):
        AddingInfrastructure()
    elif(ch == 19):
        RepresentativeChange()
    elif(ch == 20):
        LocationChange()
    elif(ch == 21):
        CompletionChange()
    elif(ch == 22):
        VaccineChange()
    elif(ch == 23):
        PolicyDeletion()
    elif(ch == 24):
        CountryRemoval()
    else:
        print("Error: Invalid Option")

# Global
tmp = sp.call('clear', shell=True)
while(1):

    # Can be skipped if you want to hardcode username and password
    # username = input("Username: ")
    # password = input("Password: ")

    # Set db name accordingly which have been create by you
    # Set host to the server's address if you don't want to use local SQL server
    username = input("Username: ")
    password = maskpass.askpass(mask="*") 
    if (((username.lower() == "root") and (password == "12345678"))or True):
        con = pymysql.connect(
            host='localhost',
            user=username,
            password=password,
            db='GHC',
        )
        tmp = sp.call('clear', shell=True)

        if con.open:
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)

                # 1. Queries
                # 1.1 Selection
                print("1. Retrieving data of all the diseases")
                print("2. Retrieving entire data about world health's stats")
                print("3. Retrieving data of all the offices with their data")
                # 1.2 Aggregate
                print("4. Finding maximum duration among all the health policies with the name of the policy")
                print("5. Finding sum of all the deaths caused by all the diseases")
                print("6. Finding sum of all local organisations of all brannches")
                # 1.3 Search
                print("7. List of all the countries whose name starts with 'Ans'")
                print("8. Number of all representatives with name ending with 'an'")
                print("9. List of all diseases having 'ler' between their name")
                # 1.4 Projection
                print("10. List of all Bio-Medical researches with status of completion >= 90%")
                print("11. List of all the branches in a particular country with more than 30 local organizations")
                print("12. List of all Disease IDs with more than 60(integer) mortality rate")

                # 2. Analysis
                print("13. R0 value of the disease with maximum number of recoveries")
                print("14. Mortality rate of the country with minimum number of doctors/nurses")

                # 3. Modification
                # 3.1 Insertion
                print("15. Adding any new policy being deployed by some country")
                print("16. Adding any new members who wants to join GHC")
                print("17. Inserting any new disease being found")
                print("18. Adding new branches and infrastructures formed.")
                # 3.2 Update
                print("19. Change in representative of any country")
                print("20. Change in location of any branch")
                print("21. Change in status of completion of any Bio-Medical research")
                print("22. Updating the percentage of vaccination status of a disease")
                # 3.3 Deletion
                print("23. Deleting any policy after its expiry")
                print("24. Removing any country who wants to leave GHC group")

                print("25. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 25:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    else:
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
