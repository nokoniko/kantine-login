# Importerer nødvendige moduler for filhåndtering, JSON og dato/tid
import os, json
from datetime import datetime
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import InputRequired

class Forms:
    """
    En klasse for å håndtere tilbakemeldinger og meldinger i kantina-applikasjonen.
    Denne klassen kan lagre, laste og vise meldinger fra brukere.
    """
    
    def __init__(self, name: str):
        """
        Initialiserer Forms-klassen ved å sette opp filbane for meldingslagring.
        Oppretter også messages-mappen hvis den ikke eksisterer.
        """
        # Definerer hvor meldingsfilen skal lagres
        self.DATA_FILE = os.path.join("messages", "messages.json")
        # Oppretter messages-mappen hvis den ikke finnes (exist_ok=True betyr at det er OK hvis mappen allerede eksisterer)
        os.makedirs(os.path.dirname(self.DATA_FILE), exist_ok=True)
        self.name = name


    def save_message(self, name: str, message: str):
        """
        Lagrer en ny melding til JSON-filen.
        
        Args:
            name (str): Navnet på personen som sender meldingen
            message (str): Meldingsteksten som skal lagres
        """
        # Oppretter et data-objekt med meldingsinformasjon
        data = {
            "navn": name,  # Navnet på avsenderen
            "melding": message,  # Meldingsteksten
            "tidspunkt": datetime.now().strftime("%d.%m.%Y kl. %H:%M")  # Nåværende tidspunkt formatert som "dd.mm.yyyy kl. hh:mm"
        }

        # Starter med en tom liste for eksisterende meldinger
        messages = []
        
        # Sjekker om meldingsfilen allerede eksisterer
        if os.path.exists(self.DATA_FILE):
            # Åpner filen for lesing med UTF-8 encoding (støtter norske tegn)
            with open(self.DATA_FILE, "r", encoding="utf-8") as f:
                try:
                    # Prøver å laste eksisterende meldinger fra JSON-filen
                    messages = json.load(f)
                except json.JSONDecodeError:
                    # Hvis filen er korrupt eller ikke gyldig JSON, starter vi med tom liste
                    messages = []

        # Legger til den nye meldingen i listen
        messages.append(data)

        # Lagrer den oppdaterte listen tilbake til filen
        with open(self.DATA_FILE, "w", encoding="utf-8") as f:
            # ensure_ascii=False lar oss bruke norske tegn, indent=2 gjør filen mer lesbar
            json.dump(messages, f, ensure_ascii=False, indent=2)

    def load_messages(self):
        """
        Laster alle lagrede meldinger fra JSON-filen.
        
        Returns:
            list: En liste med alle meldinger, eller tom liste hvis filen ikke eksisterer eller er korrupt
        """
        # Sjekker om meldingsfilen eksisterer
        if not os.path.exists(self.DATA_FILE):
            return []  # Returnerer tom liste hvis filen ikke finnes
        
        # Åpner filen for lesing
        with open(self.DATA_FILE, "r", encoding="utf-8") as f:
            try:
                # Laster og returnerer alle meldinger fra JSON-filen
                return json.load(f)
            except json.JSONDecodeError:
                # Hvis filen er korrupt, returnerer tom liste
                return []

    def vis_tilbakemeldinger(self):
        """
        Laster alle meldinger og sender dem til en HTML-template for visning.
        
        Returns:
            str: HTML-innhold generert fra tilbakemelding.html template
        """
        # Laster alle lagrede meldinger
        messages = self.load_messages()
        # Sender meldingene til HTML-template for visning
        return render_template("forms/tilbakemelding.html", messages=messages)

class RegisterForm(FlaskForm):
    brukernavn = StringField("brukernavn", validators=[InputRequired()])
    passord = PasswordField("Passord", validators=[InputRequired()])
    navn = StringField("Navn", validators=[InputRequired()])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    brukernavn = StringField("brukernavn", validators=[InputRequired()])
    passord = PasswordField("Passord", validators=[InputRequired()])
    submit = SubmitField("Submit")