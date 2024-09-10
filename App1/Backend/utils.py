def Fetch_All_Contacts(conn):
    cursor = conn.cursor()
    rows = cursor.execute('SELECT * FROM Contacts').fetchall()   
    CommitAndClose(conn)
    return rows

def Fetch_Contact(conn, id):
    cursor = conn.cursor()
    row = cursor.execute('SELECT * FROM Contacts WHERE id = ?', (id,)).fetchone()   
    CommitAndClose(conn)
    return row

def Insert_Contact(conn, fistName, lastName,IsStudent, email):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Contacts (Firstname, Lastname,Student, Email) VALUES(?,?,?,?)', (fistName, lastName,IsStudent, email))
    CommitAndClose(conn)
    
def Update_contact(conn, id,FistName, LastName,IsStudent, Email):
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Contacts
        SET FistName = ?, LastName = ?,Student = ?, Email = ?
        WHERE id = ?
    ''', (FistName, LastName,IsStudent, Email, id))
    CommitAndClose(conn)
    
    
def Delete_Contact(conn, id):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Contacts WHERE id = ?', (id,))
    CommitAndClose(conn)
    
def CommitAndClose(conn):
    conn.commit() 
    conn.close()      
    





























