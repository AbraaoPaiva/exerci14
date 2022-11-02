from flask import Flask, request
app = Flask(__name__)

products = [
    {
       "id": 1,
       "product": "Sapato",
       "price": "R$: 99,99"
    },
    {
       "id": 2,
       "product": "Bolsa",
       "price": "R$: 103,89"
    },
    {
       "id": 3,
       "product": "Camisa",
       "price": "R$: 49,98"
    },
    {
       "id": 4,
       "product": "Calça",
       "price": "R$: 89,72"
    },
    {
       "id": 5,
       "product": "Blusa",
       "price": "R$: 97,35"
    }]
# http://127.0.0.1:5000/product
@app.route('/product', methods=['POST'])
def product_json():
    id = -1
    objeto_json = request.get_json()
    if objeto_json is not None:
        if 'id' in objeto_json:
            id = objeto_json['id']
    resp = {'product': '', 'price': None} 
    for product in products: 
        if product['id'] == id:
            resp = product

    return '''
            id: {}
            product: {}
            price: {}
            '''.format(resp['id'],resp['product'],resp['price'])

if __name__ == '__main__':
    app.run(debug = True, port = 5000)