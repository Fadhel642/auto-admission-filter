import os                                 # Permet d'accéder aux variables d'environnement (comme EMAIL et PASSWORD)
from dotenv import load_dotenv            # Charge automatiquement les variables contenues dans le fichier .env
import imaplib                            # permet de se connecter à une boîte mail via le protocole IMAP.
import email                              # sert à lire et analyser les e-mails récupérés depuis la boîte mail.
from email.header import decode_header    # Sert à décoder l'en-tête d'un e-mail
import re                                 # Permet d'utiliser les expressions régulières (recherche avancée de mots ou phrases)

load_dotenv()                             # Charge les variables (EMAIL et PASSWORD) du fichier .env dans le script Python

EMAIL = os.getenv("EMAIL")                # Récupère la valeur de la variable EMAIL depuis le fichier .env
PASSWORD = os.getenv("PASSWORD")          #    =      =   =     =  =   =   PASSWORD depuis le fichier .env
IMAP_SERVER = "imap.gmail.com"            # Adresse du serveur IMAP de Gmail, pour accéder à la boîte de réception


#CHARGER LES PHRASES CLÉS 
with open("phrases_refus.txt", "r") as f:                                     # ("r") Permet d'ouvrer le fichier "phrases_refus.txt" en mode lecture 
    keywords = [line.strip().lower() for line in f if line.strip()]           # on stocke toutes les phrases dans une liste appelée keywords


# CONNEXION À LA BOITE MAIL
imap = imaplib.IMAP4_SSL(IMAP_SERVER)     # Permet de se connecter au serveur IMAP de Gmail en mode sécurisé (SSL)
imap.login(EMAIL, PASSWORD)               # On se connecte à la boîte mail avec les identifiants
imap.select("inbox")                      # On sélectionne le dossier 'inbox' (la boîte de réception) pour y lire les mails


# RECHERCHER LES MAILS NON LUS
status, messages = imap.search(None, '(UNSEEN)')                              # On recherche tous les e-mails non lus dans la boîte de réception

for num in messages[0].split():                                               # On parcourt tous les IDs de mails non lus
    status, msg_data = imap.fetch(num, "(RFC822)")                            # Permet de récupèrer le contenu complet du mail (format brut)
    for response_part in msg_data:
        if isinstance(response_part, tuple):                                  # Permet de vérifier qu'on a bien une partie avec les données du mail
            msg = email.message_from_bytes(response_part[1])                  # On convertit le contenu brut en objet email lisible

 
