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
