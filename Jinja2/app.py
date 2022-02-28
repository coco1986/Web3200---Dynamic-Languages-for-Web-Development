from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    my_fruit_list = ['oranges','limes','lemons','pumpkins']
    my_person_list = [
        {'name': 'Zoe', 'age': '36'},
        {'name': 'Mick', 'age': '40'},
        {'name': 'Lois', 'age': '10'},
        {'name': 'Allan', 'age': '44'},
        {'name':'Bob', 'age':'22'},
        {'name': 'Joe', 'age': '33'}
    ]
    print(my_person_list[1]['name'])
    column_sort_name = "age"
    return render_template('home.html', my_fruit_list=my_fruit_list, my_person_list=my_person_list, column_sort_name=column_sort_name)

@app.route("/grades/<column_name>")
def grades(column_name):
    my_person_list = [
        {'name': 'Zoe', 'grade': '36'},
        {'name': 'Mick', 'grade': '40'},
        {'name': 'Lois', 'grade': '10'},
        {'name': 'Allan', 'grade': '44'},
        {'name':'Bob', 'grade':'22'},
        {'name': 'Joe', 'grade': '33'}
    ]
    return render_template('grades.html', my_person_list=my_person_list, column_sort_name=column_name)


@app.route("/contact_me")
def contact_me():
    return render_template('contact_me.html')

if __name__ == '__main__':
    app.run(debug=True)
