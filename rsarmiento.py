from tkinter import *
import sqlite3

root = Tk()
root.title("My Project")
root.geometry("500x500")

# Consistent database path
db_path = 'C:/Users/STUDENTS/Documents/my_project.db'
conn = sqlite3.connect(db_path)
c = conn.cursor()

def submit():
    c.execute("INSERT INTO student_info VALUES (:f_name, :l_name, :age, :address, :email)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'age': age.get(),
                  'address': address.get(),
                  'email': email.get(),
              })
    conn.commit()
    clear_entries()

def clear_entries():
    f_name.delete(0, END)
    l_name.delete(0, END)
    age.delete(0, END)
    address.delete(0, END)
    email.delete(0, END)

def query():
    c.execute("SELECT *, oid FROM student_info")
    records = c.fetchall()
    
    print_records = ""
    for record in records:
        print_records += f"{record[0]} {record[1]} {record[2]} {record[3]} {record[4]} \t{record[5]}\n"
    
    query_label.config(text=print_records)

def delete():
    c.execute("DELETE FROM student_info WHERE oid=?", (delete_box.get(),))
    conn.commit()
    delete_box.delete(0, END)

def edit():

    editor=Tk()
    editor.title('Update Record from database')
    editor.geometry("500x500")

    #database
    conn=sqlite3.connect('C:/Users/CICT/data.db')

    #create cursor
    c=conn.cursor()

    #query to the database
    record_id=delete_box.get()
    c.execute("SELECT* FROM studentinfoWHERE oid="+record_id)
    records=c.fetchall()
    #print(records)

    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        age_editor.insert(0,record[2])
        address_editor.insert(0,record[3])
        email_editor.insert(0,record[4])


    #print_records="
    #for record in records:
    #print_records+=str(record[0])+ ""+str(record[1])+""+str(record[2])+""+str(record[3])+""+str(record[[4])+""+"\t"+str(record[5])+"\n"

        #create text boxes
        f_name_editor=Entry(editor,width=30)
        f_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))
        l_name_editor=Entry(editor,width=30)
        l_name_editor.grid(row=1,column=1,padx=20)
        age_name_editor=Entry(editor,width=30)
        age_name_editor.grid(row=2,column=1,padx=20)
        address_name_editor=Entry(editor,width=30)
        address_name_editor.grid(row=3,column=1,padx=20)
        email_name_editor=Entry(editor,width=30)
        email_name_editor.grid(row=4,column=1,padx=20)
        
            

# UI Elements
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
age = Entry(root, width=30)
age.grid(row=2, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=3, column=1, padx=20)
email = Entry(root, width=30)
email.grid(row=4, column=1, padx=20)

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
age_label = Label(root, text="Age")
age_label.grid(row=2, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=3, column=0)
email_label = Label(root, text="Email")
email_label.grid(row=4, column=0)

submit_btn = Button(root, text="Add Record to Database", command=submit, width=20)  # Set a fixed width
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

query_btn = Button(root, text="Show Records", command=query, width=20)  # Set the same fixed width
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

delete_box = Entry(root,width=30)
delete_box.grid(row=10,column=1,padx=30)

delete_box_label = Label(root,text="Select ID No.")
delete_box_label.grid(row=10,column=0)

delete_btn = Button(root,text="Delete Record",command=delete)
delete_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10)

query_label = Label(root,text="", justify='left')
query_label.grid(row=30,column=0,columnspan=2)


# Close connection on exit
def on_closing():
    conn.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

        
root.mainloop()
