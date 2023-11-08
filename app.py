from flask import Flask, request, render_template


app = Flask(__name__)


@app.get('/')
def form():
    return render_template('form.html')  # jinja templates


@app.post('/')
def table():
    try:
        kwargs = {
            'dimension': int(request.form['dimension']),
            'even_color': request.form['even_color'],
            'odd_color': request.form['odd_color'],
            'with_border': bool(request.form.get('with_border', False)),
        }                
    except ValueError:
        return 'Wymiar tablicy musi być liczbą.'
    
    return render_template('table.html', **kwargs)


if __name__ == '__main__':
    app.run()
