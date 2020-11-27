from flask import Blueprint
from controllers.ProduController import ProduController

web = Blueprint('web', __name__)

@web.route('/')
def index():
  return ProduController.index()

@web.route('/create', methods=['POST'])
def create():
  return ProduController.create()

@web.route('/delete/<int:index>')
def delete(index):
  return ProduController.delete(index)

@web.route('/update/<int:index>', methods=['POST'])
def update(index):
  return ProduController.update(index)
