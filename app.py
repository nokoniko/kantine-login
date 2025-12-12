from flask import Flask, render_template, request, redirect, session, url_for, flash

from utils.hjelp import Hjelp
from utils.data import *
from utils.liste import Liste
from utils.forms import Forms, RegisterForm, LoginForm
# ---- klasser ----
app = Flask(__name__)
app.secret_key = 'supersecretkey'
hjelp = Hjelp(__name__)
liste = Liste(__name__)
forms = Forms(__name__)

# --- route til nettsider ---

@app.route('/')
def index() -> str:
    return render_template('login/index.html')

@app.route('/hjem')
def hjem() -> str:
    return render_template('hjem/hjem.html')

@app.route('/meny')
def meny() -> str:
    return render_template('kantine/meny.html', menyen=liste.menyen)

@app.route('/kontakt')
def kontakt() -> str:
    return render_template('kantine/kontakt.html', kontakter=liste.kontanktpersoner)

@app.route('/varer')
def varer() -> str:
    return render_template('kantine/varer.html', varere=liste.varere)

@app.route('/register', methods=["GET", "POST"])
def register() -> str:
    forms = RegisterForm()
    if forms.validate_on_submit():
        brukernavn = forms.brukernavn.data
        passord = forms.passord.data
        navn = forms.navn.data

        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO brukere (brukernavn, passord, navn) VALUES (%s, %s, %s)",
            (brukernavn, passord, navn)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect("/login")

    return render_template("login/register.html", form=forms)

@app.route('/login', methods=["GET", "POST"])
def login():
    forms = LoginForm()
    if forms.validate_on_submit():
        brukernavn = forms.brukernavn.data
        passord = forms.passord.data

        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT navn FROM brukere WHERE brukernavn=%s AND passord=%s",
            (brukernavn, passord)
        )

        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            session['navn'] = user[0]
            return redirect('/hjem')
        else:
            # WTForms lagrer valideringsfeil i .errors-listen
            forms.brukernavn.errors.append("Feil brukernavn eller passord")
    return render_template("login/login.html", form=forms)

@app.route('/dagmeny')
def dagens() -> str:
    return hjelp.dagmeny()

@app.route('/rett/<slug>')
def rett(slug: str) -> str:
    # Viser enkel detaljside for rett basert på slug, koblet til templates/retter/<slug>.html
    return render_template(f'retter/{slug}.html')

@app.route('/tilbakemelding', methods=['GET', 'POST'])
def tilbakemelding():
    if request.method == 'POST':
        navn = request.form['navn']
        melding = request.form['melding']
        forms.save_message(navn, melding)
        flash("Takk for tilbakemeldingen! 😊")
        return redirect(url_for('tilbakemelding'))
    return forms.vis_tilbakemeldinger()
