from flask import render_template, url_for, flash, redirect,  request
from ultimoTeste import app, db
from ultimoTeste.forms import RegistrationForm
from werkzeug.security import generate_password_hash
from ultimoTeste.models import Cliente
from werkzeug.security import check_password_hash


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('senha')
        user = Cliente.query.filter_by(email=email).first()
        
        if user:
            if check_password_hash(user.senha, password):
                flash('Login realizado com sucesso!', 'success')
                return redirect(url_for('usuarios'))
            else:
                flash('Senha incorreta. Tente novamente.', 'danger')
        else:
            print('Conta não encontrada. Verifique o email ou cadastre-se.')
            flash('Conta não encontrada. Verifique o email ou cadastre-se.', 'warning')
    return render_template('login.html', title='Login')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_client = Cliente(
            nome_e_sobrenome=form.nomeSobrenome.data,
            email=form.email.data,
            senha=hashed_password,
            celular=form.celular.data,
            sexo=form.sexo.data
        )
        db.session.add(new_client)
        db.session.commit()
        flash('Sua conta foi criada! Você pode agora fazer login.', 'success')
        return redirect(url_for('login'))

    return render_template('cadastro.html', title='Cadastrar', form=form)

@app.route('/usuarios')
def usuarios():
    clientes = Cliente.query.all()  # Busca todos os clientes cadastrados no banco de dados
    return render_template('usuarios.html', clientes=clientes)
