from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analize',methods=['POST','GET'])
def analize():
    if request.method == 'POST':
        query = request.form.get('query')
        removepunc = request.form.get('removepunc')
        uppercase = request.form.get('uppercase')
        word1=""
        if removepunc == "on":
            punc = '''."'()<>!@#$%^&*~-_;:,'''
            for x in query:
                if x not in list(punc):
                    word1 += x
            pas = {"q":f"{word1}"}
            return render_template('analize.html',pas=pas)

        elif uppercase == "on":
            word1 += query.upper()
            pas={"q":f"{word1}"}
            return render_template('analize.html',pas=pas)

        else:
            return "<h1>Error</h1>"

if __name__ == "__main__":
    app.run(debug=True)
