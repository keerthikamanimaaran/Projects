from database import connect

def add_application(company,role,status,applied_date,notes):
    conn=connect()

    cursor=conn.cursor()

    cursor.execute("""
    insert into applications (company,role,status,applied_date,notes)
    values(?,?,?,?,?)
""",(company,role,status,applied_date,notes))
    
    conn.commit()

    conn.close()

    print("Application added successfully!")



def view_applications():

    conn=connect()

    cursor=conn.cursor()

    cursor.execute("select * from applications")

    rows=cursor.fetchall()

    conn.close()

    return rows


def update_status(app_id,new_status):

    conn=connect()

    cursor=conn.cursor()

    cursor.execute("""
    update applications
    set status=?
    where id=?
    """,(new_status,app_id))

    conn.commit()

    conn.close()

    print("Status updated successfully!")



def delete_application(app_id):

    conn=connect()

    cursor=conn.cursor()

    cursor.execute("""
    delete from applications
    where id=?
    """,(app_id,))

    conn.commit()

    conn.close()

    print("Application deleted successfully!")


def search_applications(keyword):

    conn=connect()

    cursor=conn.cursor()

    cursor.execute("""
    select * from applications
    where company like ?
    or role like ?
    or status like ?
    """,(
        f"%{keyword}%",
        f"%{keyword}%",
        f"%{keyword}%"
    ))

    rows=cursor.fetchall()

    conn.close()

    return rows


def display_applications(applications):

    for app in applications:
        print("\n-----------------------------------")

        print(f"ID: {app[0]}")
        print(f"Company: {app[1]}")
        print(f"Role: {app[2]}")
        print(f"Status: {app[3]}")
        print(f"Applied Date: {app[4]}")
        print(f"Notes: {app[5]}")

        print("-------------------------------------")