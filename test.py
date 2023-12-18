import requests
from bs4 import BeautifulSoup
from collections import Counter
from urllib.parse import urlparse

# Etape 1
def word_occurrences(text):
    words = text.lower().split()
    occurrences = Counter(words)
    sorted_occurrences = sorted(occurrences.items(), key=lambda x: x[1], reverse=True)
    return sorted_occurrences

# Etape 2
def remove_stopwords(word_occurrences, stopwords):
    filtered_occurrences = [(word, count) for word, count in word_occurrences if word not in stopwords]
    return filtered_occurrences

# Etape 3
def load_stopwords_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = file.read().splitlines()
            stopwords = [word.lower() for word in reader]
        return stopwords
    except FileNotFoundError:
        print(f"Le fichier {file_path} n'a pas été trouvé.")
        return []
    except Exception as e:
        print(f"Une erreur s'est produite lors du chargement du fichier : {e}")
        return []

# Etape 5
def remove_html_tags(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    text_without_tags = soup.get_text(separator=' ')
    return text_without_tags

# Etape 6
def get_attribute_values(html_text, tag_name, attribute_name):
    soup = BeautifulSoup(html_text, 'html.parser')
    values = [tag.get(attribute_name) for tag in soup.find_all(tag_name) if tag.get(attribute_name)]
    return values

# Etape 8
def extract_domain_name(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

# Etape 10
def get_html_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite lors de la récupération du texte HTML : {e}")
        return None

# Etape 11
def page_audit(url):
    html_text = get_html_from_url(url)
    if html_text:
        # Etape 1
        words_occurrences = word_occurrences(html_text)
        print("Etape 1 - Mots clés avec occurrences:")
        print(words_occurrences[:3])
        print()

        # Etape 3
        stopwords_file_path = 'parasite.csv'  # Changez le chemin si nécessaire
        stopwords = load_stopwords_from_file(stopwords_file_path)

        # Etape 2
        filtered_occurrences = remove_stopwords(words_occurrences, stopwords)
        print("Etape 2 - Mots clés sans mots parasites:")
        print(filtered_occurrences[:3])
        print()

        # Nombre de liens entrants et sortants
        soup = BeautifulSoup(html_text, 'html.parser')
        inbound_links = len(soup.find_all('a', href=True))
        outbound_links = len(soup.find_all(['a', 'img'], href=True))

        print(f"Nombre de liens entrants : {inbound_links}")
        print(f"Nombre de liens sortants : {outbound_links}")
        print()

        # Présence de balises alt
        alt_values = get_attribute_values(html_text, 'img', 'alt')
        print("Balises alt des images:")
        print(alt_values)
        print()

# Menu principal
def main():
    print("Menu principal:")
    print("1. Effectuer l'étape 1")
    print("2. Effectuer l'étape 3")
    print("3. Effectuer l'étape 5")
    print("4. Effectuer l'étape 6 (Testez avec 'img' et 'a')")
    print("5. Effectuer l'étape 8")
    print("6. Effectuer l'étape 10")
    print("7. Effectuer l'étape 11")
    print("0. Quitter")

    choice = input("Veuillez choisir une option (0-7): ")

    if choice == '1':
        text = input("Entrez le texte à analyser : ")
        occurrences = word_occurrences(text)
        print("Liste des mots avec occurrences:")
        print(occurrences)
    elif choice == '2':
        text = input("Entrez le texte à analyser : ")
        occurrences = word_occurrences(text)
        stopwords_file_path = input("Entrez le chemin du fichier de mots parasites : ")
        stopwords = load_stopwords_from_file(stopwords_file_path)
        filtered_occurrences = remove_stopwords(occurrences, stopwords)
        print("Liste des mots sans mots parasites:")
        print(filtered_occurrences)
    elif choice == '3':
        stopwords_file_path = input("Entrez le chemin du fichier de mots parasites : ")
        stopwords = load_stopwords_from_file(stopwords_file_path)
        print("Liste des mots parasites:")
        print(stopwords)
    elif choice == '4':
        html_text = input("Entrez le texte HTML à analyser : ")
        tag_name = input(" Entrez le nom : ")


