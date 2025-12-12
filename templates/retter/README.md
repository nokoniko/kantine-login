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
├── LICENSE
├── README.md
├── app.py
├── app.wsgi
├── config
├── messages
│   └── messages.json
├── static
│   ├── css
│   │   └── style.css
│   └── img
│       ├── bakgrund
│       │   ├── bilde.jpg
│       │   ├── kantine.JPG
│       │   └── kjøken.png
│       ├── logo
│       │   └── logo.png
│       ├── meny
│       │   ├── andeconfit.jpeg
│       │   ├── boeuf_bourguignon.jpg
│       │   ├── coq_au_vin.jpg
│       │   ├── hokkaido_suppe.jpeg
│       │   └── ratatouille.jpg
│       ├── personer
│       │   ├── Mio.jpeg
│       │   ├── audun.jpeg
│       │   ├── ebbe.JPG
│       │   ├── helene.jpeg
│       │   ├── jabok.jpeg
│       │   ├── ludvig.jpeg
│       │   ├── marcus.jpeg
│       │   ├── markus.jpeg
│       │   ├── markus2.JPG
│       │   ├── nikolai.jpeg
│       │   ├── sebastian.jpeg
│       │   ├── simen.jpeg
│       │   └── thea.JPG
│       └── varer
│           ├── Croissant.jpg
│           ├── bagguete.jpg
│           ├── brownie.webp
│           ├── epplejuice.jpg
│           ├── fruktBeger.jpg
│           ├── kaffe.jpg
│           ├── notter.jpg
│           ├── salat.Jpeg
│           ├── sjokolademelk.jpeg
│           ├── te.png
│           ├── vann.jpg
│           └── yoghurt.jpeg
├── templates
│   ├── base.html
│   ├── forms
│   │   └── tilbakemelding.html
│   ├── hjem
│   │   └── hjem.html
│   ├── kantine
│   │   ├── kontakt.html
│   │   ├── meny.html
│   │   └── varer.html
│   ├── login
│   │   ├── index.html
│   │   ├── login.html
│   │   └── register.html
│   └── retter
│       ├── README.md
│       ├── andeconfit.html
│       ├── boeuf-bourguignon.html
│       ├── coq_au_vin.html
│       ├── coqunvin.html
│       ├── hokkaido-suppe.html
│       └── ratatouille.html
└── utils
    ├── data.py
    ├── forms.py
    ├── hjelp.py
    └── liste.py
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