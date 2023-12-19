# Projet Python

import csv
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup 

# Etape 1

def List(t): # creation d'une fonction List
    mots = t.split()  # separation d'une phrase en une liste de mot
    occurence = [] # initialisation du nombre de repetition d'un mot
    for mot in mots:  # creation de la boucle for qui remplis les occurences
        occurence.append(mots.count(mot)) # comptabilite du nombre de repetition des mots
    couple = list(zip(mots, occurence)) # transformation d'un dictionnaire en liste avec 2
    couple.sort(key=lambda i:i[1]) # tri de mot par ordre croissant selon l'occurence
    print(mots) # impression du texte separer
    print(occurence) # impression du nombre de repetition des mots
    print(couple) # impression des mots trier par ordre croissant 
    return couple


def word_frequency(phrase, mot_parasite):
    mots = phrase.split()
    occurences = {}

    for mot in mots:
        mot = mot.lower()
        if mot not in mot_parasite:
            occurences[mot] = occurences.get(mot, 0) + 1

    couple = list(occurences.items())
    couple.sort(key=lambda x: x[1])

    print("Mots de la phrase:", mots)
    print("Occurences de chaque mot:", occurences)
    print("Mots tries par ordre croissant d'occurrence:", couple)

    return couple

# Etape 2

def cleaner(dual, parasites):
    cleared = [tup for tup in dual if not ((set(parasites) & set(tup)))]
    print(cleared)
    return (cleared)


# Etape 3

mot_parasite = ['le', 'la' , 'les', 'un', 'une']

def get_parasite(file_path):
    file_path = r"C:\Users\abdel\OneDrive\Desktop\Licence IG\Python\mot_parasite.csv"
    with open(file_path, 'r', ):
        reader = csv.reader(mot_parasite)
        words_list = [word.lower() for row in reader for word in row]
        print(words_list)
        
get_parasite(r"C:\Users\abdel\OneDrive\Desktop\Licence IG\Python\mot_parasite.csv")

# Etape 5

def no_balise(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')
    sans_balise = soup.get_text(separator=' ' , strip=True)
    return sans_balise

html_string = "<p>Bonjour je m'appelle Abdelkrim</p>"
resultat = no_balise(html_string)
print(resultat)



# Etape 6
def get_attribute_values(html_string, tag_name, attribute_name):
    values = []

    # Utilisation de BeautifulSoup pour analyser la page HTML
    soup = BeautifulSoup(html_string, 'html.parser')

    # Trouver toutes les balises avec le nom specifie
    tags = soup.find_all(tag_name)

    # Parcourir les balises et recuperer la valeur de l'attribut specifie
    for tag in tags:
        value = tag.get(attribute_name)
        if value:
            values.append(value)

    return values

# Exemple d'utilisation de la fonction


tag_name_to_search = "img"
attribute_name_to_search = "alt"
alt_href_content_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exemple HTML avec alt et href</title>
</head>
<body>
    <h1>Liens et Images</h1>

    <a href="https://www.example.com" alt="Site Web Example">Visitez notre site Web</a>

    <img src="example-image.jpg" alt="Image d'exemple">

    <a href="https://www.example2.com" alt="Site Web Example 2">
        <img src="example2-image.jpg" alt="Image d'exemple 2">
    </a>
</body>
</html>
"""
result_values = get_attribute_values(alt_href_content_html, tag_name_to_search, attribute_name_to_search)

print(f"Les valeurs associees aux balises '{tag_name_to_search}' avec l'attribut '{attribute_name_to_search}' sont : {result_values}")

# Etape 8
def extract_domain_from_url(url):
    try:
        # Utilise urlparse pour diviser l'URL en composants
        parsed_url = urlparse(url)
        
        # Retourne le composant netloc, qui correspond au nom de domaine
        return parsed_url.netloc
    except Exception as e:
        # En cas d'erreur, imprime un message d'erreur
        print(f"Erreur : {e}")
        
        # Retourne None en cas d'erreur
        return None

# Exemple d'utilisation
url = "https://www.esiee-it.fr/fr"

# Appelle la fonction extract_domain_from_url avec l'URL comme argument
domain = extract_domain_from_url(url)

# Affiche le résultat
print(f"Nom de domaine extrait : {domain}" if domain else "Impossible d'extraire le nom de domaine.")

# Etape 9
def classifier_par_domaine(domaine, urls):
    internes, externes = [], []
    for url in urls:
        extract = extract_domain_from_url(url)
        if extract == domaine:
            internes.append(url)
        else:
            externes.append(url)
    print(f"Les urls dans le domaine {internes}")
    print(f" Les urls qui ne font pas partie du domaine {externes}")
    return domaine, urls

domaine = "esiee-it.blackboard.com"
urls = "https://www.youtube.com/watch?v=cUrmG335e7o", "https://www.youtube.com/watch?v=8ZfdwUjzxkA&list=PLrSOXFDHBtfHKxuz6NySItyf4iSEcTw97&index=16" , "https://esiee-it.blackboard.com/ultra/stream/edit/document/_1173113_1?courseId=_101859_1"


classifier_par_domaine(domaine, urls)




#Etape 10

def get_html_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite lors de la récupération du texte HTML : {e}")
        return None


url = "https://esiee-it.blackboard.com/ultra/courses/_101859_1/outline/edit/document/_1173113_1?courseId=_101859_1&view=content"
html_content = get_html_from_url(url)

if html_content is not None:
    print(html_content)
else:
    print("La récupération du texte HTML a échoué.")

    get_html_from_url(url)


# Etape 11

def audit_page(url, mot_parasite_file_path):
    html = get_html_from_url(url)

    if html is not None:
        texte = no_balise(html)
        occurrences = List(texte)

        mots_parasites = get_parasite(mot_parasite_file_path)
        

    
        liens = get_attribute_values(html, 'a', 'href')
        liens_entrants = [lien for lien in liens if lien.startswith(url)]
        liens_sortants = [lien for lien in liens if not lien.startswith(url)]

        print(f"Nombre de liens entrants: {len(liens_entrants)}")
        print(f"Nombre de liens sortants: {len(liens_sortants)}")

        alts = get_attribute_values(html, 'img', 'alt')
        print(f"Présence de balises alt: {alts if alts else 'Non'}")

# Exemple d'utilisation
url_a_analyser = input("Veuillez entrer l'URL de la page à analyser : ")
mot_parasite_file_path = input("Veuillez entrer le chemin du fichier de mots parasites (mot_parasite.csv) : ")
audit_page(url_a_analyser, mot_parasite_file_path)



