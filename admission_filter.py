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
with open("phrases_refus.txt", "r", encoding="utf-8") as f:                   # On ouvre le fichier contenant les phrases à rechercher (en mode lecture et encodage UTF-8)
    keywords = [line.strip().lower() for line in f if line.strip()]           # On stocke toutes les phrases non vides dans une liste appelée keywords, en minuscules pour la recherche


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


            # Sujet
            subject, encoding = decode_header(msg["Subject"])[0]              # Récupère l'en-tête « Subject » et la méthode d'encodage (ex. UTF-8, ISO-8859-1…)
            if isinstance(subject, bytes):                                    # Si le sujet est encore sous forme binaire, on le décode en texte
                subject = subject.decode(encoding or "utf-8",errors="ignore")         # Si l'encodage est inconnu, on force l'UTF-8 et on ignore les erreurs


            # Corps du mail
            body = ""                                                                                # Variable où l'on stockera le texte final
            if msg.is_multipart():                                                                   # Si le mail est en plusieurs parties (texte + HTML + pièce jointe…)
                for part in msg.walk():                                                              # On parcourt chaque partie du message
                    content_type = part.get_content_type()                                           # On récupère le type de contenu (ex : text/plain ou text/html)
                    content_disposition = str(part.get("Content-Disposition"))

                    if "attachment" in content_disposition:                  # On ignore les pièces jointes
                        continue
                        
                    try:
                        payload = part.get_payload(decode=True).decode(errors="ignore")   # On décode le contenu
                    except:
                        continue
                    if content_type == "text/plain":                         # Si on trouve du texte brut, on le prend
                        body = payload
                        break
                    elif content_type == "text/html" and not body:           # Si on ne trouve pas de texte brut, on prend le HTML
                        body = re.sub('<[^<]+?>', '', payload)               # On enlève toutes les balises HTML
            else:                                                            # Si le mail n'est pas multipart (un seul bloc)
                try:
                    payload = msg.get_payload(decode=True).decode(errors="ignore")  # On décode le corps
                    if msg.get_content_type() == "text/html":                # Si c’est du HTML, on nettoie les balises
                        body = re.sub('<[^<]+?>', '', payload)
                    else:
                        body = payload                                       # Sinon on prend le texte tel quel
                except:
                    pass

            full_content = f"{subject}\n{body}".lower()        # On assemble le sujet et le corps du mail en une seule chaîne, puis on met tout en minuscules pour faciliter la recherche


            # Détection de phrase
            match = any(keyword in full_content for keyword in keywords)                             # On vérifie si au moins un des mots/phrases clés est présent dans le mail

            with open("mail_log.txt", "a") as log:                                                   # On ouvre un fichier de log en mode ajout ("a") pour enregistrer ce qu'on a fait
                    if match:                                                                        # Si le mail contient une phrase clé (donc un refus) :
                        imap.store(num, '+FLAGS', '\\Deleted')                                       # On marque le mail pour qu'il soit supprimé (drapeau \Deleted)
                        log.write(f"[SUPPRIMÉ] {subject}\n")                                         # On écrit dans le journal que le mail a été supprimé

                    else:                                                                            # Si aucune phrase clé n'est détectée :
                        log.write(f"[OK] {subject}\n")                                               # On enregistre simplement dans le log que le mail a été conservé

imap.expunge()  # Supprime définitivement tous les mails marqués comme "\\Deleted"
imap.logout()  # Ferme proprement la connexion avec le serveur Gmail
