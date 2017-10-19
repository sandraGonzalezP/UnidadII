from flask import Flask, render_template, request, redirect
from gravitation import gravitational_force

app = Flask(__name__)


@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='gravitation Force')


@app.route('/force', methods=['GET', 'POST'])
def execute() -> 'html':
    G = float(request.form['G'])
    M = float(request.form['M'])
    m = float(request.form['m'])
    r = float(request.form['r'])
    tittle = 'The result of gravitational force is : '
    result = gravitational_force(G, M, m, r)
    return render_template('result.html',
                           this_tittle=tittle,
                           the_G=G,
                           the_M=M,
                           the_m=m,
                           the_r=r,
                           the_result=result)


app.run(debug=True)
