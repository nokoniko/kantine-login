# Kantina-prosjekt

Dette er en Flask-basert webapplikasjon for en kantine, designet for å presentere dagens meny, et fullstendig utvalg av varer, kontaktinformasjon for ansatte, og detaljerte beskrivelser av individuelle retter. Prosjektet legger vekt på **bærekraft og kvalitet**.

## Funksjoner

-   **Dynamisk Dagsmeny**: Viser dagens rett basert på ukedagen.
-   **Omfattende Meny**: En dedikert side som viser alle hovedretter.
-   **Vareoversikt**: En side som lister opp ulike varer som drikke, snacks og andre matprodukter.
-   **Detaljerte Rettsider**: Hver hovedrett har sin egen side med beskrivelse og bilde.
-   **Kontaktinformasjon for Ansatte**: En kontaktside med detaljer (navn, stilling, e-post, telefon, bilde) for kantinepersonalet.
-   **Bærekraftsfokus**: Fremhever kantinens forpliktelse til bærekraftige praksiser, som bruk av kortreiste råvarer og reduksjon av matsvinn.
-   **Responsivt Design**: Tilpasser seg ulike skjermstørrelser for en god brukeropplevelse.

## Teknologier Brukt

-   **Python 3.x**
-   **Flask**: Et lettvekts webrammeverk for Python.
-   **Jinja2**: Templating-motor brukt av Flask for å generere HTML.
-   **HTML5**
-   **CSS3**

## Oppsett og Installasjon

Følg disse trinnene for å få prosjektet til å kjøre lokalt:

1.  **Klon repositoryet**:
    ```bash
    git clone https://github.com/nokoniko/kantina-prosjekt.git # Erstatt med den faktiske URL-en til ditt repository
    cd kantina-prosjekt
    ```

2.  **Opprett et virtuelt miljø**:
    Det er god praksis å bruke et virtuelt miljø for å håndtere prosjektavhengigheter.
    ```bash
    python3 -m venv venv
    source venv/bin/activate # På Windows bruk `venv\Scripts\activate`
    ```

3.  **Installer avhengigheter**:
    ```bash
    pip install Flask
    ```

4.  **Kjør applikasjonen**:
    ```bash
    python app.py # windowa
    python3 app.py # macOS/linux
    ```
    Applikasjonen vil vanligvis kjøre på `http://127.0.0.1:5000/`.

## Prosjektstruktur

```diff
kantina-prosjekt/
 # Hovedmappe
+ ├── app.py                  # Hoved Flask-applikasjonsfil
 ├── static/                 # Statiske filer (CSS, bilder)
 │   ├── css/
 │   │   └── style.css       # Hovedstilark
 │   └── img/                # Bilder for logoer, menyer, personer, etc.
 ├── templates/              # HTML-maler
 │   ├── base.html           # Grunnmal for konsistent layout
 │   ├── hjem/
 │   │   └── index.html
 │   ├── kantine/
 │   │   ├── kontakt.html
 │   │   ├── meny.html
 │   │   └── varer.html
 │   └── retter/
 │       ├── andeconfit.html
 │       ├── boeuf-bourguignon.html
 │       ├── coq_au_vin.html
 │       ├── hokkaido-suppe.html
 │       └── ratatouille.html
 └── utils/                  # Hjelpeskript
+    ├── hjelp.py            # Hjelpefunksjoner
+    └── liste.py            # Datalagring
```

## Bidrag

Du er velkommen til å forke repositoryet, gjøre forbedringer og sende inn pull requests.

## Lisens

Dette prosjektet er åpent kildekode og tilgjengelig under MIT-lisensen.

## Kilder

Chatgpt til å generere tekst til hjemmesiden og beskrivelsen til de forskjellige rettene, lage json logiken, gemini til å lage README.md fil og fikse noen css problemer.