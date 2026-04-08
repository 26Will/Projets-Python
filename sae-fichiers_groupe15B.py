code_groupe = "15B"
nom_entree = "groupe15B_data.txt"
dossier_destination = "../data_res/"

# --- Lecture du fichier source ---
f = open(nom_entree, mode="r", encoding="utf-8")
contenu = f.read() 
f.close()       

# On remplace les retours à la ligne par des espaces pour tout traiter d'un coup
contenu = contenu.replace("\n", " ") 

# On prépare la première ligne du futur fichier Excel (CSV)
lignes_csv = ["Référence;Titre;Durée (min);Année;Restriction;Nombre de votes;Score;Description"] 

# Initialisation des compteurs et de la liste pour les calculs
liste_scores = [] 
compteur_drama = 0
compteur_action = 0
compteur_films = 0

# On coupe le texte à chaque fois qu'on voit "title=" pour isoler chaque film
films_bruts = contenu.split("title=") 

for bloc in films_bruts:
    # On vérifie que le bloc contient bien des informations (10 est une valeur arbitraire)
    if len(bloc) > 10:
        
        # On découpe le bloc étape par étape pour extraire les infos
        parties = bloc.split(",type=")
        
        # On vérifie qu'il y a bien au moins deux morceaux pour éviter les erreurs
        if len(parties) >= 2:
            titre_brut = parties[0]
            reste = parties[1]
            
            parties = reste.split(",restriction=")
            genre_brut = parties[0]
            reste = parties[1]
            
            parties = reste.split(",nbvotes=")
            restriction_brut = parties[0]
            reste = parties[1]
            
            parties = reste.split(",score=")
            votes_brut = parties[0]
            reste = parties[1]
            
            parties = reste.split(",duration=")
            score_brut = parties[0]
            reste = parties[1]
            
            parties = reste.split(",year=")
            duree_brut = parties[0]
            reste = parties[1]
            
            parties = reste.split(",desc=")
            annee_brut = parties[0]
            desc_brut = parties[1]
            
            # On nettoie la description pour enlever ce qui dépasse après le #
            desc_brut = desc_brut.split("#")[0]
        
            # On compte un film de plus
            compteur_films = compteur_films + 1
            
            # Nettoyage des textes (enlever les espaces inutiles au début/fin)
            titre = titre_brut.strip().title()
            restriction = restriction_brut.strip().title()
            description = desc_brut.strip()
            
            # Conversion des chiffres (on enlève les virgules ou points inutiles)
            annee = str(int(float(annee_brut))) if annee_brut.strip() else ""
            duree = str(int(float(duree_brut))) if duree_brut.strip() else ""
            votes = votes_brut.strip()
            score = score_brut.strip()
        
            # Si le score existe, on l'ajoute à notre liste pour faire la moyenne plus tard
            if score != "":
                liste_scores.append(float(score))
                
            # On vérifie si le genre contient "drama" ou "action"
            genre_mini = genre_brut.lower()
            if "drama" in genre_mini:
                compteur_drama = compteur_drama + 1
            if "action" in genre_mini:
                compteur_action = compteur_action + 1
        
            # Création de la ligne finale pour ce film
            ref = "F-" + code_groupe + str(compteur_films) + "-" + annee
            ligne = ref + ";" + titre + ";" + duree + ";" + annee + ";" + restriction + ";" + votes + ";" + score + ";" + description
            lignes_csv.append(ligne)

# --- Création du fichier CSV final ---
nom_csv = nom_entree.replace(".txt", ".csv")
chemin_csv = dossier_destination + nom_csv

f = open(chemin_csv, mode="w", encoding="cp1252")
f.write("\n".join(lignes_csv)) # On rassemble toutes les lignes avec un saut de ligne
f.close()

# --- Calculs des statistiques ---
mini = min(liste_scores) if liste_scores else 0
maxi = max(liste_scores) if liste_scores else 0
moyenne = sum(liste_scores) / len(liste_scores) if liste_scores else 0

t_drama = (compteur_drama / compteur_films * 100) if compteur_films > 0 else 0
t_action = (compteur_action / compteur_films * 100) if compteur_films > 0 else 0

# Préparation du texte de résumé
texte_infos = "Nom du fichier : " + nom_entree + "\n"
texte_infos += "Nombre de films : " + str(compteur_films) + "\n"
texte_infos += "Score minimum : " + str(mini) + "\n"
texte_infos += "Score maximum : " + str(maxi) + "\n"
texte_infos += "Score moyen : " + "%.2f" % moyenne + "\n"
texte_infos += "Taux de drames : " + "%.2f" % t_drama + "%\n"
texte_infos += "Taux de films d’action : " + "%.2f" % t_action + "%"

# --- Enregistrement du fichier info ---
nom_infos = "groupe" + code_groupe + "_infos.txt"
chemin_infos = dossier_destination + nom_infos

f = open(chemin_infos, mode="w", encoding="utf-8")
f.write(texte_infos)
f.close()

print("Traitement terminé. Les fichiers sont dans " + dossier_destination)