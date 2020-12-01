from flask import redirect, render_template, url_for, flash, request, session, current_app
from shop import db, app
from shop.products.models import Addskin
from shop.products.models import Brand, Category, Addskin

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
            DictItems = {skin_id:{'name':skin.name, 'price':skin.price, 'float':skin.float, 'quantity':quantity, 'image':skin.image}}

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


@app.route('/carts')
def getCart():
    barnds = Brand.query.join(Addskin, (Brand.id == Addskin.brand_id)).all()
    categories = Category.query.join(Addskin, (Category.id == Addskin.category_id)).all()
    if 'Shoppingcart' not in session or len(session['Shoppingcart']) <= 0:
        return redirect(url_for('home'))
    grantotal = 0
    for key, skin in session['Shoppingcart'].items():
        grantotal += float(skin['price']*int(skin['quantity']))
    return render_template('products/carts.html' , grantotal = grantotal,collections=barnds, categories=categories )

@app.route('/updatecart/<int:code>', methods = ['POST'])
def updatecart(code):
    if 'Shoppingcart' not in session and len(session['Shoppingcart']) <= 0:
        return redirect(url_for('home'))
    if request.method == "POST":
        quantity = request.form.get('quantity')
        try:
            session.modified = True
            for key, item in session['Shoppingcart'].items():
                if int(key) ==  code:
                    item['quantity'] = quantity
                    flash('Item actualizado','success')
                    return redirect(url_for('getCart'))
        except Exception as e:
            print(e)
            return redirect(url_for('getCart'))

@app.route('/removecart/<int:id>')
def deleteitem(id):
    if 'Shoppingcart' not in session and len(session['Shoppingcart']) <= 0:
        return redirect(url_for('home'))
    try:
        session.modified = True
        for key , item in session['Shoppingcart'].items():
            if int(key) == id:
                flash('Item removido','danger')
                session['Shoppingcart'].pop(key, None)
                return redirect(url_for('getCart'))
    except Exception as e:
        print(e)
        return redirect(url_for('getCart'))