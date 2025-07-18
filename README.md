# auto-admission-filter
**Objectif** : Script Python qui analyse les e-mails d’admission (candidature) pour détecter automatiquement les refus et les supprimer ou archiver.

---

## Fonctionnalités

- Connexion IMAP à une boîte mail (Gmail par exemple)
- Lecture des e-mails non lus
- Détection de phrases comme :
  - "malheureusement"
  - "votre candidature n’a pas été retenue"
  - "nous ne donnerons pas suite"
- Suppression ou archivage des mails détectés
- Journalisation des actions dans `mail_log.txt`

---
