# Kantine Webløsning

Dette er en enkel webapplikasjon for en kantine, bygget med Flask. Applikasjonen lar brukere registrere seg, logge inn og se en meny med ulike retter.

## Funksjoner

- Brukerregistrering og innlogging
- Visning av en meny med detaljerte beskrivelser av hver rett
- Enkel og ren sidestruktur

## Teknologistabel

- **Backend:** Python med Flask
- **Frontend:** HTML, CSS
- **Templating:** Jinja2

## Prosjektstruktur

```
kantine-login/
├── static/
│   └── img/
│       └── meny/
│           ├── andeconfit.jpeg
│           ├── boeuf_bourguignon.jpg
│           └── ... (bilder for rettene)
├── templates/
│   ├── login/
│   │   ├── index.html
│   │   ├── login.html
│   │   └── register.html
│   ├── retter/
│   │   ├── andeconfit.html
│   │   └── ... (maler for hver rett)
│   └── base.html
├── app.py          # Hovedapplikasjonen (antatt)
└── requirements.txt  # Prosjektavhengigheter (antatt)
```

## Oppsett og Kjøring

1.  **Klon repositoriet:**
    ```bash
    git clone <din-repo-url>
    cd kantine-login
    ```

2.  **Opprett og aktiver et virtuelt miljø (anbefalt):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # På Windows: venv\Scripts\activate
    ```

3.  **Installer avhengigheter:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Kjør applikasjonen:**
    ```bash
    flask run
    ```

5.  Åpne nettleseren din og gå til `http://127.0.0.1:5000`.