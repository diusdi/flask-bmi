from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = ''
    if request.method == 'POST' and 'berat' in request.form:
        berat = float(request.form.get('berat'))
        tinggi = float(request.form.get('tinggi'))
        bmi = hitung_bmi(berat, tinggi)
        if bmi>=40: info=['Obesitas Kelas III', 1]
        elif bmi>=35: info=['Obesitas Kelas II',2]
        elif bmi>=30:info=['Obesitas Kelas I', 3]
        elif bmi>=25:info=['Kegemukan', 4]
        elif bmi>=18:info=['Normal', 5]
        else: info=['Kurus',6]
    return render_template("index.html",bmi=bmi, info=info)

def hitung_bmi(berat, tinggi):
    return round((berat / ((tinggi / 100) ** 2)), 2)
