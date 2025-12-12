from flask import render_template
import datetime

class Hjelp:
    def __init__(self, name: str) -> None:
        self.name = name
    def dagmeny(self) -> str:
        """
        Finner dagens rett basert på ukedagen og returnerer den tilhørende templaten.
        Datoen hentes hver gang funksjonen kalles for å sikre at den alltid er korrekt.
        """
        # Henter navnet på gjeldende dag (f.eks. "Monday") hver gang funksjonen kjøres.
        dag: str = datetime.datetime.now().strftime("%A")
        match dag:
            case "Monday":
                return render_template('retter/andeconfit.html')
            case "Tuesday":
                return render_template('retter/coq_au_vin.html')
            case "Wednesday":
                return render_template('retter/hokkaido-suppe.html')
            case "Thursday":
                return render_template('retter/boeuf-bourguignon.html')
            case "Friday":
                return render_template('retter/ratatouille.html')
            case _:
                return "Ingen rett i dag desverre"
