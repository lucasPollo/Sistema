from flask import Flask, url_for, render_template, request, redirect
from db import db
from models import Cliente





#inicio
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dados.db"
db.init_app(app)

@app.route('/')
def indexPage():

    
    
    
    
    
    
    
    
  return render_template('index.html')



@app.route("/clientes")
def clientesPage():
  clientes = db.session.query(Cliente).all()
  qtdClientes = db.session.query(Cliente.id).count()
  return render_template('clientes.html', clientes=clientes, qtdClientes=qtdClientes)



@app.route('/cadastro', methods=['GET', 'POST'])
def cadastroPage():
  if request.method == 'GET':
     return render_template('cadastro.html')
  elif request.method == 'POST':
    nome = request.form.get('nomeForm')
    email = request.form.get('emailForm')
    cpf = request.form.get('cpfForm')
    endereco = request.form.get('enderecoForm')
    estado = request.form.get('estadoForm')
    
    novoCliente = Cliente(nome=nome, email=email, cpf=cpf, endereco=endereco, estado=estado)
   
    
    db.session.add(novoCliente)
    db.session.commit()
    
    
    
    
    
    
    
    
    
    return redirect(url_for('indexPage'))
  
 
  
  
  
  
  
  
  
#python main.py para rodar


@app.route('/estoque', methods=['GET', 'POST'])
def estoquePage():
  from teste import estoque

  
  
  teste = 421
    






  return render_template('estoque.html',teste=teste, estoque=estoque)

#execucao


@app.route('/deletar/<int:id>')
def deletar(id):
  cliente = db.session.query(Cliente).filter_by(id=id).first()
  db.session.delete(cliente)
  db.session.commit()
  
  return redirect(url_for("indexPage"))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
  cliente = db.session.query(Cliente).filter_by(id=id).first()
  if request.method == "GET":
   return render_template('editarCliente.html', cliente=cliente)
  elif request.method == "POST":
    nome = request.form.get('nomeForm')
    email = request.form.get('emailForm')
    cpf = request.form.get('cpfForm')
    endereco = request.form.get('enderecoForm')
    estado = request.form.get('estadoForm')
    
    cliente.nome = nome
    cliente.email = email
    cliente.cpf = cpf
    cliente.endereco = endereco
    cliente.estado = estado
    db.session.commit()
    return redirect(url_for('indexPage'))
    


if __name__== "__main__":
  
  with app.app_context():
    db.create_all()
  app.run(debug=True)

