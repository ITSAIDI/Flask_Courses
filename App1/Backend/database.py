from colorama import Fore, Back, Style, init

init()

#conn = sqlite3.connect('Mydatabase.db')

def CreateDatabse(conn):
    cursor = conn.cursor()
    try:
        
        cursor.execute('''
            CREATE TABLE Friends (
                Userid TEXT PRIMARY KEY NOT NULL,
                Fullname TEXT NOT NULL,
                Role TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE Cards (
                Cardid INTEGER PRIMARY KEY AUTOINCREMENT,
                fk_Userid TEXT NOT NULL,
                Description TEXT NOT NULL,
                FOREIGN KEY(fk_Userid) REFERENCES Friends(Userid)
            )
        ''')
        CommitAndClose(conn)
        print(Style.BRIGHT + Fore.GREEN + "Tables created successfully")
        
    except Exception as e:
        print(Style.BRIGHT + Fore.RED + "Error creating tables")
        print(Style.BRIGHT+ Fore.RESET +str(e))


def InsertUser(conn,userid,fullname,role):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Friends
                (Userid, Fullname, Role)
            VALUES (?,?,?)""",
            (userid,fullname,role))
        print(Style.BRIGHT + Fore.GREEN + "User inserted successfully")
    except Exception as e:
        print(Style.BRIGHT + Fore.RED + "Error inserting data")
        print(Style.BRIGHT+ Fore.RESET +str(e))
    CommitAndClose(conn)

def InsertCard(conn,userid,description):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO cards
                (fk_Userid, Description)
            VALUES (?,?)""",
            (userid,description))
        print(Style.BRIGHT + Fore.GREEN + "Card inserted successfully")
    except Exception as e:
        print(Style.BRIGHT + Fore.RED + "Error inserting data")
        print(Style.BRIGHT+ Fore.RESET +str(e))
    CommitAndClose(conn)
   
def FetchAllUsers(conn):
    cursor = conn.cursor()
    rows = cursor.execute('SELECT * FROM Friends').fetchall()
    print(Style.BRIGHT + Fore.GREEN + "Users fetched successfully")   
    FormatedRows = [{"Userid":row[0],"Fullname":row[1],"Role":row[2]} for row in rows]
    CommitAndClose(conn)
    return  FormatedRows

def FetchAllCards(conn):
    cursor = conn.cursor()
    rows = cursor.execute('SELECT * FROM Cards').fetchall()
    print(Style.BRIGHT + Fore.GREEN + "Cards fetched successfully")  
    FormatedRows = [{"Cardid":row[0],"Userid":row[1],"Description":row[2]} for row in rows]
    
    for row in FormatedRows:
        #print(row)
        userid = row['Userid']
        userinfo =  cursor.execute('SELECT * FROM Friends Where Userid = ?', (userid,)).fetchone()
        #print(userinfo)
        row["Userinfo"] = {"FullName":userinfo[1],"Role":userinfo[2]}
    CommitAndClose(conn)
    return  FormatedRows

def FetchUser(conn,userid):
    cursor = conn.cursor()
    row = cursor.execute('SELECT * FROM Friends Where Userid = ?', (userid,)).fetchone()
    print(Style.BRIGHT + Fore.GREEN + f"{userid} fetched successfully")   
    CommitAndClose(conn)
    return  row

def FetchCard(conn,cardid):
    cursor = conn.cursor()
    row = cursor.execute('SELECT * FROM Cards Where Cardid = ?', (cardid,)).fetchone()
    print(Style.BRIGHT + Fore.GREEN + f"{cardid} fetched successfully")   
    CommitAndClose(conn)
    return  row
        
def UpdateCard(conn,cardid,description):    
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE cards
            SET Description = ?
            WHERE Cardid = ?""",
            (description,cardid))
        print(Style.BRIGHT + Fore.GREEN + "Card updated successfully")
    except Exception as e:
        print(Style.BRIGHT + Fore.RED + "Error updating data")
        print(Style.BRIGHT+ Fore.RESET +str(e))
    CommitAndClose(conn)
        
         
def CommitAndClose(conn):
    conn.commit() 
    conn.close()
    print(Style.BRIGHT + Fore.GREEN + "Database closed successfully")
    
#CreateDatabse()
"""InsertUser(conn,"user01","John Doe","Frontend Developer")
InsertUser(conn,"user02","Jane Doe","Backend Developer")
InsertUser(conn,"user03","Jack Doe","Fullstack Developer")
InsertUser(conn,"user04","Jill Doe","Devops Developer")
InsertCard(conn,"user01","Noureddine is a Fullstack Developer")
InsertCard(conn,"user02","Best one")
InsertCard(conn,"user03","Awesome")
InsertCard(conn,"user04","Good and rich profile")
InsertCard(conn,"user04","Good and Strong background")"""

#print(Style.RESET_ALL+str(FetchCard(conn,1)))
#print(Style.RESET_ALL+str(FetchUser(conn,"user01")))
#CommitAndClose(conn)


        




















