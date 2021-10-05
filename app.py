from flask import Flask,render_template
from path_generator import *
app = Flask(__name__)

Listfromfrontend= [
    {
        'name':'showerhead',
        'category':'bath'
    },
        {
        'name':'oil',
        'category':'automotive'
    },
    {'name':'phone',
    'category':'tech'},
    {
    'name':'easter egg',
    'category':'seasonal'}
    ,
    {
        'name':'showerhead',
        'category':'personal_care'
    },
      {
     'name':'barbie',
     'category':'toys'
    }
    ]
graph = CheckpointGenerator()
graph = graph.generate_checkpoints(Listfromfrontend)
@app.route('/')
def instore_nav():
    return render_template("myboard.html",graph=graph[1],path=graph[0].split(' ')[1:],steps=graph[2])

if __name__ == '__main__':
    app.run(debug=True)
