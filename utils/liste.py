class Liste(object):
    def __init__(self, name: str) -> None:
        self.name = name

    # lagger 2 lister den enne til mat menyen og den adnre til de faste varerene
    menyen: list[dict[str, str | list[str]]] = [
        {"navn": "Andeconfit", "kategori": "Varmrett", "allergier": ["gluten", "melk"], "bilde": "andeconfit.jpeg", "dag": "Mandag", "slug": "andeconfit"},
        {"navn": "Coq au vin", "kategori": "Varmrett", "allergier": [], "bilde": "coq_au_vin.jpg", "dag": "Tirsdag", "slug": "coq_au_vin"},
        {"navn": "Hokkaido-suppe", "kategori": "Suppe", "allergier": ["melk"], "bilde": "hokkaido_suppe.jpeg", "dag": "Onsdag", "slug": "hokkaido-suppe"},
        {"navn": "Bœuf bourguignon", "kategori": "Varmrett", "allergier": [], "bilde": "boeuf_bourguignon.jpg", "dag": "Torsdag", "slug": "boeuf-bourguignon"},
        {"navn": "Ratatouille", "kategori": "Vegetarrett", "allergier": [], "bilde": "ratatouille.jpg", "dag": "Fredag", "slug": "ratatouille"}
    ]

    varere: list[dict[str, str | list[str] | int | float]] = [
        {"navn": "Sjokolademelk", "kategori": "Drikke", "allergier": ["melk"], "bilde": "sjokolademelk.jpeg", "pris": 68},
        {"navn": "Eplejuice", "kategori": "Drikke", "allergier": [], "bilde": "epplejuice.jpg", "pris": 62},
        {"navn": "Mineralvann", "kategori": "Drikke", "allergier": [], "bilde": "vann.jpg", "pris": 52},
        {"navn": "Nøtteblanding", "kategori": "Snack", "allergier": ["nøtter"], "bilde": "notter.jpg", "pris": 42},
        {"navn": "Yoghurt med granola", "kategori": "Snack", "allergier": ["melk", "gluten", "nøtter"], "bilde": "yoghurt.jpeg", "pris": 58},
        {"navn": "Croissant", "kategori": "Bakverk", "allergier": ["gluten", "melk"], "bilde": "croissant.jpg", "pris": 50},
        {"navn": "Baguette med ost og skinke", "kategori": "Mat", "allergier": ["gluten", "melk"], "bilde": "baguette.jpg", "pris": 100},
        {"navn": "Salatboks", "kategori": "Mat", "allergier": ["egg"], "bilde": "salat.jpeg", "pris": 120},
        {"navn": "Fruktbeger", "kategori": "Snack", "allergier": [], "bilde": "fruktbeger.jpg", "pris": 90},
        {"navn": "Kaffe", "kategori": "Drikke", "allergier": [], "bilde": "kaffe.jpg", "pris": 33},
        {"navn": "Te", "kategori": "Drikke", "allergier": [], "bilde": "te.png", "pris": 33},
        {"navn": "Brownie", "kategori": "Bakverk", "allergier": ["gluten", "melk", "egg"], "bilde": "brownie.webp", "pris": 67},
    ]

    kontanktpersoner: list[dict[str, str | list[str]]]  = [
        {"navn": "Nikolai pai", "stilling": "Kaffesjef", "bilde": "nikolai.jpeg", "epost": "nikolai.kantine@yessirski.li", "tlf": "400 12 345"},
        {"navn": "Audun bao bum", "stilling": "Assisterene Vaske hjelp", "bilde": "audun.jpeg", "epost": "audun.kantine@yessirski.com", "tlf": "401 23 456"},
        {"navn": "Ebbe Lebbe", "stilling": "Brownie-ansvarlig", "bilde": "ebbe.jpg", "epost": "ebbe.kantine@yessirski.com", "tlf": "402 34 567"},
        {"navn": "Helene grene", "stilling": "Logistikk-magiker", "bilde": "helene.jpeg", "epost": "helene.kantine@yessirski.com", "tlf": "403 45 678"},
        {"navn": "Ludvig sudvig", "stilling": "Saus-sommelier", "bilde": "ludvig.jpeg", "epost": "ludvig.kantine@yessirski.com", "tlf": "404 56 789"},
        {"navn": "Sebastian nastian", "stilling": "Vaffel-ingeniør", "bilde": "sebastian.jpeg", "epost": "sebastian.kantine@yessirski.com", "tlf": "405 67 890"},
        {"navn": "markus", "stilling": "Fruktkurator", "bilde": "markus2.jpg", "epost": "markus.kantine@yessirski.com", "tlf": "406 41 911"},
        {"navn": "thea", "stilling": "Kryddermester", "bilde": "thea.jpg", "epost": "thea.kantine@yessirski.com", "tlf": "407 44 671"},
        {"navn": "Mio", "stilling": "Kantine katt", "bilde": "mio.jpeg", "epost": "mio.kantine@yessirski.com", "tlf": "407 67 271"},
        {"navn": "Jabok", "stilling": "Lokal narkoman", "bilde": "jabok.jpeg", "epost": "jabok.kantine@yessirski.com", "tlf": "67676767"},
        {"navn": "Marcus", "stilling": "vakt", "bilde": "marcus.jpeg", "epost": "marcus.kantine@yessirski.com", "tlf": "413 56 789"},
        {"navn": "Simen", "stilling": "Vaskehjelp vikar", "bilde": "simen.jpeg", "epost": "simen.kantine@yessirski.com", "tlf": "414 67 890"}
    ]