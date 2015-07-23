import sqlite3
from bottle import route, run, debug, template, request, error

class Task:
    def __init__(self):
        print("init task")

    def todo_list(self):
        conn = sqlite3.connect('todo_data.db')
        c = conn.cursor()
        c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
        result = c.fetchall()
        #return str(result)
        c.close()
        output = template('make_table', rows=result)
        return output

    def new_item(self):
        if request.GET.get('save','').strip():
            new = request.GET.get('task', '').strip()
            conn = sqlite3.connect('todo_data.db')
            c = conn.cursor()
            c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
            new_id = c.lastrowid
            conn.commit()
            c.close()
            return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
        else:
            return template('new_task.tpl')

    def edit_item(self, no):
        if request.GET.get('save','').strip():
            edit = request.GET.get('task','').strip()
            status = request.GET.get('status','').strip()
            if status == 'open':
                status = 1
            else:
                status = 0
            conn = sqlite3.connect('todo_data.db')
            c = conn.cursor()
            c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
            conn.commit()
            return '<p>The item number %s was successfully updated</p>' % no
        else:
            conn = sqlite3.connect('todo_data.db')
            c = conn.cursor()
            c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no)))
            cur_data = c.fetchone()
            return template('edit_task', old=cur_data, no=no)

    def delete_item(self, no):
        conn = sqlite3.connect('todo_data.db')
        c = conn.cursor()
        print('\n '+str(no)+"\n")
        c.execute("DELETE FROM todo WHERE id LIKE %s" % (str(no)))
        conn.commit()
        # redirect('/')
        return 'success deleting todo No%s' % str(no)