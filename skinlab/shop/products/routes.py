from flask import redirect, render_template, url_for, flash, request, session, current_app
from shop import db, app, photos
from .models import Brand, Category, Addskin
from .forms import AddSkin
import secrets, os

@app.route('/')
def home():
    page = request.args.get('page',1,type=int)
    skins = Addskin.query.filter(Addskin.stock > 0).paginate(page=page, per_page=4)
    barnds = Brand.query.join(Addskin, (Brand.id == Addskin.brand_id)).all()
    categories = Category.query.join(Addskin, (Category.id == Addskin.category_id)).all()
    return render_template('products/index.html', skins = skins, collections=barnds, categories=categories)

@app.route('/collection/<int:id>')
def get_collection(id):
    page = request.args.get('page',1,type=int)
    get_brand = Brand.query.filter_by(id=id).first_or_404()
    brand = Addskin.query.filter_by(brand=get_brand).paginate(page=page, per_page=4)
    categories = Category.query.join(Addskin, (Category.id == Addskin.category_id)).all()
    barnds = Brand.query.join(Addskin, (Brand.id == Addskin.brand_id)).all()
    return render_template('products/index.html', brands = brand, collections=barnds, categories=categories ,get_brand=get_brand)

@app.route('/category/<int:id>')
def get_category(id):
    page = request.args.get('page',1,type=int)
    get_cat = Category.query.filter_by(id=id).first_or_404()
    category = Addskin.query.filter_by(category=get_cat).paginate(page=page, per_page=4)
    categories = Category.query.join(Addskin, (Category.id == Addskin.category_id)).all()
    barnds = Brand.query.join(Addskin, (Brand.id == Addskin.brand_id)).all()
    return render_template('products/index.html', category = category, categories = categories, collections=barnds,get_cat=get_cat)

@app.route('/product/<int:id>')
def single_page(id):
    skin = Addskin.query.get_or_404(id)
    categories = Category.query.join(Addskin, (Category.id == Addskin.category_id)).all()
    barnds = Brand.query.join(Addskin, (Brand.id == Addskin.brand_id)).all()
    return render_template('products/single_page.html', skin=skin, collections=barnds, categories=categories)

@app.route('/addcollection', methods=['GET','POST'])
def addcollection():
    if 'email' not in session:
        print("esta el email")
        flash(f'Iniciar Sesion antes', 'danger')
        return redirect(url_for('login'))
    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name= getbrand)
        db.session.add(brand)
        flash(f'The brand {getbrand} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addcollection'))
    return render_template('products/addcollection.html', brands='brands')

@app.route('/updatecollection/<int:id>', methods=['GET','POST'])
def updatecollection(id):
    if 'email' not in session:
        print("esta el email")
        flash(f'Iniciar Sesion antes', 'danger')
        return redirect(url_for('login'))
    updatecollection = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method == 'POST':
        updatecollection.name = brand
        flash(f'La coleccion fue actualizada', 'success')
        db.session.commit()
        return redirect(url_for('collections'))
    return render_template('products/updatecollection.html', title='Update collection', updatecollection=updatecollection)

@app.route('/deletecollection/<int:id>', methods = ['POST'])
def deletecollection(id):
    estado = True
    brand = Brand.query.get_or_404(id)
    skins = Addskin.query.all()
    for skin in skins :
        if brand.id == skin.brand_id :
            estado = False
    if request.method == 'POST' and estado:
        print("hola1")
        db.session.delete(brand)
        db.session.commit()
        flash(f'La coleción {brand.name} se elimino de la base de datos','success')
        return redirect(url_for('admin'))
    else:
        flash(f'La coleción {brand.name} no se elimino de la base de datos','warning')
        return redirect(url_for('admin'))

@app.route('/updatecategory/<int:id>', methods=['GET','POST'])
def updatecategory(id):
    if 'email' not in session:
        print("esta el email")
        flash(f'Iniciar Sesion antes', 'danger')
        return redirect(url_for('login'))
    updatecategory = Category.query.get_or_404(id)
    category = request.form.get('category')
    if request.method == 'POST':
        updatecategory.name = category
        flash(f'La categoria de armas fue actualizada', 'success')
        db.session.commit()
        return redirect(url_for('categories'))
    return render_template('products/updatecollection.html', title='Update category', updatecategory=updatecategory)


@app.route('/addcat', methods=['GET','POST'])
def addcat():
    if 'email' not in session:
        print("esta el email")
        flash(f'Iniciar Sesion antes', 'danger')
        return redirect(url_for('login'))
    if request.method == "POST":
        getcat = request.form.get('category')
        cat = Category (name = getcat)
        db.session.add(cat)
        flash(f'The category {getcat} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('products/addcollection.html')

@app.route('/deletecat/<int:id>', methods = ['POST'])
def deletecat(id):
    estado = True
    category = Category.query.get_or_404(id)
    skins = Addskin.query.all()
    for skin in skins :
        if category.id == skin.brand_id :
            estado = False
    if request.method == 'POST' and estado:
        db.session.delete(category)
        db.session.commit()
        flash(f'La categoria {category.name} se elimino de la base de datos','success')
        return redirect(url_for('admin'))
    else:
        flash(f'La categoria {category.name} no se elimino de la base de datos','warning')
        return redirect(url_for('admin'))


@app.route('/addskin', methods=['POST', 'GET'])
def addskin():
    if 'email' not in session:
        print("esta el email")
        flash(f'Iniciar Sesion antes', 'danger')
        return redirect(url_for('login'))
    brands = Brand.query.all()
    categories = Category.query.all()
    form = AddSkin(request.form)
    if request.method == "POST":
        name = form.name.data
        price = form.price.data
        float = form.float.data
        stock = form.stock.data
        brand = request.form.get('brand')
        category = request.form.get('category')
        image = photos.save(request.files.get('image'), name=secrets.token_hex(10) + ".")
        addskin = Addskin(name=name, price=price, float=float, stock=stock, brand_id=brand, category_id=category, image=image)
        db.session.add(addskin)
        flash(f'La skin fue cargada con exito')
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('products/addskin.html', title='Agregar Skin a la venta', form=form, brands=brands, categories=categories)

@app.route('/updateskin/<int:id>', methods=["GET","POST"])
def updateskin(id):
    collec = Brand.query.all()
    categories = Category.query.all()
    skin = Addskin.query.get_or_404(id)
    collection = request.form.get('collection')
    category = request.form.get('category')
    form = AddSkin(request.form)
    if request.method == 'POST':     
        skin.name = form.name.data
        skin.price = form.price.data
        skin.float = form.float.data
        skin.stock = form.stock.data
        
        if request.files.get('image'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + skin.image))
                skin.image =photos.save(request.files.get('image'), name=secrets.token_hex(10) + ".")
            except:
                skin.image =photos.save(request.files.get('image'), name=secrets.token_hex(10) + ".")
        db.session.commit()
        flash(f'Skin actualizada')
        return redirect(url_for('admin'))

    form.name.data = skin.name
    form.price.data = skin.price
    form.float.data = skin.float
    form.stock.data = skin.stock

    return render_template('products/updateskin.html', form=form, collections=collec, categories=categories, skin=skin)

@app.route('/deleteskin/<int:id>', methods = ['POST'])
def deleteskin(id):
    skin = Addskin.query.get_or_404(id)
    if request.method == 'POST':
        try:
            os.unlink(os.path.join(current_app.root_path, "static/images/" + skin.image))
        except Exception as e:
            print(e)
        db.session.delete(skin)
        db.session.commit()
        flash(f'La skin {skin.name} se elimino de la base de datos','success')
        return redirect(url_for('admin'))
    flash(f'La skin {skin.name} no se elimino de la base de datos','warning')
    return redirect(url_for('admin'))