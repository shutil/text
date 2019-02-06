from flask import Flask, render_template, request, url_for

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

        if removepunc == "on":
            word1=""
            punc = '''."'()<>!@#$%^&*~-_;:,'''
            for x in query:
                if x not in list(punc):
                    word1 += x
            pas = {"q":f"{word1}"}
            #return render_template('analize.html',pas=pas)
            query = word1

        if uppercase == "on":
            word1 =""
            word1 += query.upper()
            pas={"q":f"{word1}"}
            #return render_template('analize.html',pas=pas)
            query = word1

        return render_template('analize.html',pas=pas)

if __name__ == "__main__":
    app.run(debug=True)
