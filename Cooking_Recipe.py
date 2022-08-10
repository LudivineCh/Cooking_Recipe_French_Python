
import requests
import webbrowser

app_id = 'f6d692a7'
app_key = 'e3aa6c44e7b86fcd4b8b8327646b0506'

def cherche_recette(ingredient, ingr):
    resultat = requests.get(
        "https://api.edamam.com/search?q={}&ingr={}&app_id={}&app_key={}".format(
            ingredient, ingr, app_id, app_key
        )
    )
    data = resultat.json()
    return data["hits"]


def cherche_recette_meal(ingredient, ingr, mealType):
    resultat = requests.get(
        "https://api.edamam.com/search?q={}&ingr={}&mealType={}&app_id={}&app_key={}".format(
            ingredient, ingr, mealType, app_id, app_key
        )
    )
    data = resultat.json()
    return data["hits"]

def cherche_recette_healthy1(ingredient, ingr, choix1):
# Créez un compte pour obtenir des identifiants
    resultat = requests.get('https://api.edamam.com/search?q={}&ingr={}&health={}&app_id={}&app_key={}'.format(ingredient, ingr, choix1, app_id, app_key))
    data = resultat.json()
    return data['hits']

def cherche_recette_healthy2(ingredient, ingr, choix1, choix2):
# Créez un compte pour obtenir des identifiants
    resultat = requests.get('https://api.edamam.com/search?q={}&ingr={}&health={}&health={}&app_id={}&app_key={}'.format(ingredient, ingr, choix1, choix2, app_id, app_key))
    data = resultat.json()
    return data['hits']

def cherche_recette_healthy3(ingredient, ingr, choix1, choix2, choix3):
# Créez un compte pour obtenir des identifiants
    resultat = requests.get('https://api.edamam.com/search?q={}&ingr={}&health={}&health={}&health={}&app_id={}&app_key={}'.format(ingredient, ingr, choix1, choix2, choix3, app_id, app_key))
    data = resultat.json()
    return data['hits']

def cherche_recette_healthy4(ingredient, ingr, mealType, choix1):
# Créez un compte pour obtenir des identifiants
    resultat = requests.get('https://api.edamam.com/search?q={}&ingr={}&mealType={}&health={}&app_id={}&app_key={}'.format(ingredient, ingr, mealType, choix1, app_id, app_key))
    data = resultat.json()
    return data['hits']

def cherche_recette_healthy5(ingredient, ingr, mealType, choix1, choix2):
# Créez un compte pour obtenir des identifiants
    resultat = requests.get('https://api.edamam.com/search?q={}&ingr={}&mealType={}&health={}&health={}&app_id={}&app_key={}'.format(ingredient, ingr, mealType, choix1, choix2, app_id, app_key))
    data = resultat.json()
    return data['hits']

def cherche_recette_healthy6(ingredient, ingr, mealType, choix1, choix2, choix3):
# Créez un compte pour obtenir des identifiants
    resultat = requests.get('https://api.edamam.com/search?q={}&ingr={}&mealType={}&health={}&health={}&health={}&app_id={}&app_key={}'.format(ingredient, ingr, mealType, choix1, choix2, choix3, app_id, app_key))
    data = resultat.json()
    return data['hits']


def run():
    print(
        "Bienvenue dans l'application qui permet de trouver une recette parfaite pour vous."
    )
    chosen_nb = []
    stock = int(input("Combien d'ingredients minimum souhaitez-vous utiliser ?"))
    for i in range(stock):
        question = input("Entrez un ingrédient (en anglais): ")
        chosen_nb.append(question)

        ingredient = ",".join(str(e) for e in chosen_nb)

    ingr = int(input("Combien des ingredients maximum voulez vous? : "))
    mealType_question = input(
        "Voulez-vous choisir un type de repas ex. dinner? oui/non "
    )
    health_question = input("Voulez vous une recette healthy? oui/non ")

    with open("mycookbook.txt", "w") as fichier:
        if mealType_question == "non" and health_question == "non":
            resultats = cherche_recette(ingredient, ingr)[:3]

            for resultat in resultats:
                recette = resultat["recipe"]
                name = recette["label"]
                nb_ingrs = str(len(recette["ingredients"]))
                nb_servings = str(int(recette["yield"]))
                url = recette["url"]
                text = f"La recette {name} est prevue pour {nb_servings} personnes, elle contient en total {nb_ingrs} ingredients dont: {ingredient}. Vous la trouver sur cette page: {url} \n\n"
                fichier.write(text)
                webbrowser.open_new(url)

        elif mealType_question == "oui" and health_question == "non":
            mealType = input(
                "Vous voulez une recette pour breakfast,lunch, dinner, or snack?"
            )
            resultats = cherche_recette_meal(ingredient, ingr, mealType)[:3]

            for resultat in resultats:
                recette = resultat["recipe"]
                name = recette["label"]
                nb_ingrs = str(len(recette["ingredients"]))
                nb_servings = str(int(recette["yield"]))
                url = recette["url"]
                text = f"La recette {name} est prevue pour {nb_servings} personnes, elle contient en total {nb_ingrs} ingredients dont: {ingredient} est elle est prevue pour  {mealType}. Vous la trouver sur cette page: {url} \n\n"
                fichier.write(text)
                webbrowser.open_new(url)

        elif mealType_question == "non" and health_question == "oui":
            nombre_choix = int(input("Combien de critères santé souhaitez-vous choisir? (entre 1 et 3) \n Liste: alcohol-free, immuno-supportive, celery-free, crustacean-free, dairy-free, egg-free, fish-free, fodmap-free, gluten-free, keto-friendly, kidney-friendly, kosher, low-potassium, lupine-free, mustard-free, \n low-fat-abs, No-oil-added, low-sugar, paleo, peanut-free, pecatarian, pecatarian, pork-free, red-meat-free, sesame-free, shellfish-free, soy-free, sugar-conscious, tree-nut-free, vegan, vegetarian, wheat-free. \n  Nombre de critères à prendre en compte: "))
            nombre_choix2 = nombre_choix
            choix_sante = []
            while nombre_choix2 > 0:
                choix = str(input("Ecrivez un critère santé? "))
                choix_sante.append(choix)
                nombre_choix2 -= 1
            print(choix_sante)

            if nombre_choix == 1:
                choix1 = choix_sante[0]
                resultats = cherche_recette_healthy1(ingredient, ingr, choix1)[:3]
                i = 0
                for resultat in resultats:
                    i += 1
                    recette = resultat["recipe"]
                    name = recette["label"]
                    nb_ingrs = str(len(recette["ingredients"]))
                    nb_servings = str(int(recette["yield"]))
                    url = recette["url"]
                    text = (
                            "La recette "
                            + name
                            + " est prevue pour "
                            + nb_servings
                            + " personnes  et elle contient "
                            + nb_ingrs
                            + " ingredients. Elle peut etre trouvee sur cette page "
                            + url
                            + "\n"
                    )
                    text_to_print = str(i) + ". " + text
                    fichier.write(text_to_print)
                    webbrowser.open_new(url)

            if nombre_choix == 2:
                choix1 = choix_sante[0]
                choix2 = choix_sante[1]
                resultats = cherche_recette_healthy2(ingredient, ingr, choix1, choix2)[:3]
                i = 0
                for resultat in resultats:
                    i += 1
                    recette = resultat["recipe"]
                    name = recette["label"]
                    nb_ingrs = str(len(recette["ingredients"]))
                    nb_servings = str(int(recette["yield"]))
                    url = recette["url"]
                    text = (
                            "La recette "
                            + name
                            + " est prevue pour "
                            + nb_servings
                            + " personnes  et elle contient "
                            + nb_ingrs
                            + " ingredients. Elle peut etre trouvee sur cette page "
                            + url
                            + "\n"
                    )
                    text_to_print = str(i) + ". " + text
                    fichier.write(text_to_print)
                    webbrowser.open_new(url)

            if nombre_choix == 3:
                choix1 = choix_sante[0]
                choix2 = choix_sante[1]
                choix3 = choix_sante[2]
                resultats = cherche_recette_healthy3(ingredient, ingr, choix1, choix2, choix3)[:3]
                i = 0
                for resultat in resultats:
                    i += 1
                    recette = resultat["recipe"]
                    name = recette["label"]
                    nb_ingrs = str(len(recette["ingredients"]))
                    nb_servings = str(int(recette["yield"]))
                    url = recette["url"]
                    text = (
                            "La recette "
                            + name
                            + " est prevue pour "
                            + nb_servings
                            + " personnes  et elle contient "
                            + nb_ingrs
                            + " ingredients. Elle peut etre trouvee sur cette page "
                            + url
                            + "\n"
                    )
                    text_to_print = str(i) + ". " + text
                    fichier.write(text_to_print)
                    webbrowser.open_new(url)


        elif mealType_question == "oui" and health_question == "oui":
            mealType = input(
                "Vous voulez une recette pour breakfast,lunch, dinner, or snack?"
            )

            nombre_choix = int(input(
                "Combien de critères santé souhaitez-vous choisir? (entre 1 et 3) \n Liste: alcohol-free, immuno-supportive, celery-free, crustacean-free, dairy-free, egg-free, fish-free, fodmap-free, gluten-free, keto-friendly, kidney-friendly, kosher, low-potassium, lupine-free, mustard-free, \n low-fat-abs, No-oil-added, low-sugar, paleo, peanut-free, pecatarian, pecatarian, pork-free, red-meat-free, sesame-free, shellfish-free, soy-free, sugar-conscious, tree-nut-free, vegan, vegetarian, wheat-free. \n  Nombre de critères à prendre en compte: "))
            nombre_choix2 = nombre_choix

            choix_sante = []
            while nombre_choix2 > 0:
                choix = str(input("Ecrivez un critère santé? "))
                choix_sante.append(choix)
                nombre_choix2 -= 1
            print(choix_sante)

            if nombre_choix == 1:
                choix1 = choix_sante[0]
                resultats = cherche_recette_healthy4(ingredient, ingr, mealType, choix1)[:3]
                i = 0
                for resultat in resultats:
                    i += 1
                    recette = resultat["recipe"]
                    name = recette["label"]
                    nb_ingrs = str(len(recette["ingredients"]))
                    nb_servings = str(int(recette["yield"]))
                    url = recette["url"]
                    text = (
                            "La recette "
                            + name
                            + " est prevue pour "
                            + nb_servings
                            + " personnes  et elle contient "
                            + nb_ingrs
                            + " ingredients. Elle peut etre trouvee sur cette page "
                            + url
                            + "\n"
                    )
                    text_to_print = str(i) + ". " + text
                    fichier.write(text_to_print)
                    webbrowser.open_new(url)

            if nombre_choix == 2:
                choix1 = choix_sante[0]
                choix2 = choix_sante[1]
                resultats = cherche_recette_healthy5(ingredient, ingr, mealType, choix1, choix2)[:3]
                i = 0
                for resultat in resultats:
                    i += 1
                    recette = resultat["recipe"]
                    name = recette["label"]
                    nb_ingrs = str(len(recette["ingredients"]))
                    nb_servings = str(int(recette["yield"]))
                    url = recette["url"]
                    text = (
                            "La recette "
                            + name
                            + " est prevue pour "
                            + nb_servings
                            + " personnes  et elle contient "
                            + nb_ingrs
                            + " ingredients. Elle peut etre trouvee sur cette page "
                            + url
                            + "\n"
                    )
                    text_to_print = str(i) + ". " + text
                    fichier.write(text_to_print)
                    webbrowser.open_new(url)

            if nombre_choix == 3:
                choix1 = choix_sante[0]
                choix2 = choix_sante[1]
                choix3 = choix_sante[2]
                resultats = cherche_recette_healthy6(ingredient, ingr, mealType, choix1, choix2, choix3)[:3]
                i = 0
                for resultat in resultats:
                    i += 1
                    recette = resultat["recipe"]
                    name = recette["label"]
                    nb_ingrs = str(len(recette["ingredients"]))
                    nb_servings = str(int(recette["yield"]))
                    url = recette["url"]
                    text = (
                            "La recette "
                            + name
                            + " est prevue pour "
                            + nb_servings
                            + " personnes  et elle contient "
                            + nb_ingrs
                            + " ingredients. Elle peut etre trouvee sur cette page "
                            + url
                            + "\n"
                    )
                    text_to_print = str(i) + ". " + text
                    fichier.write(text_to_print)
                    webbrowser.open_new(url)


run()