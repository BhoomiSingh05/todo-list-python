from flask import Flask, render_template, request, redirect, url_for

# Configure Flask to use the current directory for templates and static files
app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')

tasks = []
history = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks, history=history)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
        history.append(f"Added: {task}")
    return redirect(url_for('index'))

@app.route('/delete/<int:index>', methods=['POST'])
def delete_task(index):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        history.append(f"Deleted: {removed_task}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
