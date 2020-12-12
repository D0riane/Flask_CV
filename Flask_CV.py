from flask import Flask, render_template

app = Flask("Curriculum Vitae")

diplomes = {
    0: {
        "titre": "Baccalauréat",
        "spec": "Economique et sociale",
        "institution1": "Lycée François Couperin, Fontainebleau",
        "date": [2012],
        "description": "Mention AB : 13/20"
    },
    1: {
        "titre": "Licence",
        "spec": "Histoire",
        "institution1": "Université Paris Est Marne la Vallée",
        "date": [2012, 2015],
        "description": "L3 effectuée en ERASMUS à l'Université de Bologne "
                       " | Histoire antique, médiévale, moderne contemporaine, gégraphie, sociologie "
                       " | Mention TB : 17/20"
    },
    2: {
        "titre": "Master",
        "spec": "Recherche histoire moderne et contemporaine",
        "institution1": "Université Aix Marseille",
        "institution2": "La Sapienza Università di Roma",
        "date": [2015, 2018],
        "description": "Double diplôme franco italien " " | Rédaction de deux mémoires de recherche "
                       " | 'L'implantation de la Compagnie de Jésus en France "
                       "pendant les guerres de religions du XVIe siècle.' "
                       " | Sous la direction de Jérémie Foa et Stefania Nanni " " | Mention TB 17/20"
    }
}

experiences = {
    0: {
        "titre": "Animatrice",
        "spec": "",
        "institution": "Centre aérés",
        "ville": "",
        "date": [2011, 2014],
        "description": "Préparation et encadrement des activités et du quotidien " " | Groupe d'enfant de 6 à 14 ans"
    },
    1: {
        "titre": "Employée commerciale",
        "spec": "Boulangerie",
        "institution": "Monoprix",
        "ville": "Paris",
        "date": [2018, 2019],
        "description": "Axe vente : caisse et mise en valeur du rayon "
                       " | Axe labo : cuisson des pains et viennoiseries, gestion des stocks et des commandes, "
                       "traçabilité "
    },
    2: {
        "titre": "Ingénieure d'étude",
        "spec": "Stagiaire puis vacataire",
        "institution": "Observatoire de Paris - PSL ",
        "ville": "Paris",
        "date": [2020],
        "description": "Stage puis vacation dans l'équipe DH au projet ALFA "
                       " | Travail sur la base de donnée " " | Astronomie médiévale"
    }
}

@app.route("/")
def accueil_cv():
    return render_template("pages/Flask_CV_accueil.html", nom="Curriculum Doriane",
                           diplomes=diplomes, experiences=experiences)


@app.route("/graduation/<int:graduation_id>")
def diplome(graduation_id):
    return render_template("pages/Flask_CV_graduation.html", nom="Curriculum Doriane",
                           graduation=diplomes[graduation_id])


@app.route("/experience/<int:experience_id>")
def experience(experience_id):
    return render_template("pages/Flask_CV_exp_pro.html", nom="Curriculum Doriane",
                           experience=experiences[experience_id])


if __name__ == "__main__":
    app.run(debug=True)
