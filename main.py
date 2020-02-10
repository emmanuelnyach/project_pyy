from flask import Flask, render_template
import pygal
import psycopg2


app = Flask(__name__)


@app.route('/line')
def graph():


    data_line=[('january',20),
               ('february',40),
               ('march',60),
               ('april',82),
               ('may',60),
               ('june',13),
               ('july',17),
               ('august',45),
               ('september',55),
               ('october',82),
               ('november',79),
               ('december',40)]
    x=[]
    y=[]
    for i in data_line:
        x.append(i[0])
    for i in data_line:
        y.append(i[1])

    line_chart=pygal.Line()
    line_chart.title='sales for the year 2019'
    line_chart.x_labels=map(str,x)
    line_chart.add('Sales',y)

    line_data=line_chart.render_data_uri()


    # browser=pygal.Line()
    # browser.title='change of programming over the years'
    # browser.x_labels=['2011','2012','2013','2014','2015','2016']
    # browser.add('python',[15,31,89,200,350,960])
    # browser.add('java',[15,45,76,80,91,95])
    # browser.add('c++',[5,51,54,102,150,201])
    # browser.add('all other',[5,15,21,55,92,105])
    # line_graph=browser.render_data_uri()

    return render_template('about.html',line_data=line_data)

@app.route('/person/<name>/<int:age>')
def person(name,age):
    return '{} is {} years'.format(name,age)

@app.route('/addition/<int:a>/<int:b>')
def addition(a,b):
    total = a+b
    return str(total)

@app.route('/templating')
def templating():
    conn=psycopg2.connect("dbname='sales_demo' user='postgres' host='localhost' password='1995Derrick'")
    cur=conn.cursor()
    cur.execute("SELECT to_char(created_at,'MM') as Months, SUM(sales_data.quantity) as Total_Sales FROM public.sales_data GROUP BY months Order By (months)")
    records=cur.fetchall()

    data=[('internet explorer', 19.5),
          ('firefox',36.6),
          ('chrome',36.3),
          ('safari',4.5),
          ('opera', 2.3)]

    pie_chart=pygal.Pie()
    pie_chart.title='browser usage feb 2012'
    pie_chart.add(data[0][0],data[0][1])
    pie_chart.add(data[1][0],data[1][1])
    pie_chart.add(data[2][0],data[2][1])
    pie_chart.add(data[3][0],data[3][1])
    pie_chart.add(data[4][0],data[4][1])

    pie_data=pie_chart.render_data_uri()

    data_line = [('january', 20),
                 ('february', 40),
                 ('march', 60),
                 ('april', 82),
                 ('may', 60),
                 ('june', 13),
                 ('july', 17),
                 ('august', 45),
                 ('september', 55),
                 ('october', 82),
                 ('november', 79),
                 ('december', 40)]

    x=[]
    sales=[]
    for i in records:
        x.append(i[0])
        sales.append(i[1])

    line_chart = pygal.Line()
    line_chart.title = 'sales for the year 2019'
    line_chart.x_labels = map(str, x)
    line_chart.add('Sales', sales)

    line_data = line_chart.render_data_uri()

    return render_template('index.html', pie_data=pie_data, line_data=line_data)



@app.route('/')
def home():

    return 'hello world!!!!!!'

@app.route('/about')
def about():
    return render_template('about.html',title='About Page')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('service.html')



if __name__ == '__main__':
    app.debug=True
    app.run()
