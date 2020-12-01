from flask import redirect, render_template, url_for, flash, request, session, current_app
from shop import db, app
from shop.products.models import Addskin

def MargerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance (dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance (dict2, dict):
        return dict(list(dict1.items()) + list (dict2.items()))
    return False

@app.route('/addcart', methods = ['POST'])
def AddCart():
    try:
        skin_id = request.form.get('skin_id')
        quantity = request.form.get('quantity')
        skin = Addskin.query.filter_by(id=skin_id).first()
        if skin_id and quantity and request.method == 'POST':
            DictItems = {skin_id:{'name':skin.name, 'price':skin.price, 'float':skin.float, 'quantify':quantity, 'image':skin.image}}

            if 'Shoppingcart' in session:
                print(session['Shoppingcart'])
                if skin_id in session['Shoppingcart']:
                    print("Esta skin ya esta en el carro")
                else:
                    session['Shoppingcart'] = MargerDicts(session['Shoppingcart'], DictItems)
                    return redirect(request.referrer)
            else:
                session['Shoppingcart'] = DictItems
                return redirect(request.referrer)
    except Exception as e :
        print(e)
    finally:
        return redirect(request.referrer)