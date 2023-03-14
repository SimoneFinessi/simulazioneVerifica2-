from flask import Flask,render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def tour():
    return render_template("tour4.html")

@app.route('/singolo', methods=['GET'])
def singol():
    return render_template("costo.html",pagamento=10)

@app.route('/gruppo', methods=['GET'])
def grup():
    return render_template("costo.html",pagamento=8)

@app.route('/guidata', methods=['GET'])
def guida():
    return render_template("costo.html",pagamento=12)





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
  