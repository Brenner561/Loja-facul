from flask import render_template, redirect, request
from models.Produ import produtos

class ProduController():
  def index():
    return render_template('index.html', produtos=produtos)

  def create():
    title = request.form.get('title')
    price = request.form.get('price')
    produtos.append({'title': title, 'price':  price })
    return redirect('/')

  def delete(index):
    produtos.pop(index)
    return redirect('/')

  def update(index):
    title = request.form.get('title')
    price = request.form.get('price')
    produtos[index]['title'] = title
    produtos[index]['price'] = price
    return redirect('/')