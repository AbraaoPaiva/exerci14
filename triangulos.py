from flask import Flask, request
app = Flask (__name__)


#Exercício 1
@app.route('/exercicio/1', methods=["POST"])
def Triangulo():
    objeto_json = request.get_json()
    if objeto_json is not None:
        triangulo = ''
        if 'A' in objeto_json:
            A = objeto_json['A']
        if 'B' in objeto_json:
            B = objeto_json['B']
        if 'C' in objeto_json:
            C = objeto_json['C']
        
        x = float(A)
        y = float(B)
        z = float(C)
            
        if x+y>z and x+z>y and y+z>x:
            triangulo = 'É triangulo.'
        else:
            triangulo = 'Não é triangulo.'

        return '''
            A: {}
            B: {}
            C: {}
            Situação: {}
            '''.format(A, B,C,triangulo)
    

if __name__ == "__main__":
    app.run (debug = True, port = 5000)