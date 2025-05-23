from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
notes = []

@app.route('/')
def index():
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    note = request.form.get('note')
    if note:
        notes.append(note)
    return redirect(url_for('index'))

@app.route('/delete/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    if 0 <= note_id < len(notes):
        del notes[note_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
