from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for tasks. Each task is a dict with 'id' and 'description'.
tasks = []
next_id = 1  # To assign unique IDs to tasks

@app.route('/')
def index():
    """Homepage: List all tasks."""
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    """Route to add a new task via a form."""
    global next_id
    if request.method == 'POST':
        description = request.form.get('description')
        if description:
            tasks.append({'id': next_id, 'description': description})
            next_id += 1
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """Route to delete a task by its ID."""
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))

@app.route('/about')
def about():
    """Route to display the About page."""
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 