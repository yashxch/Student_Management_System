from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks

students = []

@app.route('/')
def home():
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        roll_number = int(request.form['roll_number'])
        name = request.form['name']
        marks = float(request.form['marks'])
        student = Student(roll_number, name, marks)
        students.append(student)
        return redirect('/')
    return render_template('add.html')

@app.route('/delete/<int:roll_number>')
def delete(roll_number):
    for i, student in enumerate(students):
        if student.roll_number == roll_number:
            del students[i]
            break
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
