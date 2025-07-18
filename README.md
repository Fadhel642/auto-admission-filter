# auto-admission-filter
**Objectif** : Script Python qui analyse les e-mails d’admission (candidature) pour détecter automatiquement les refus et les supprimer ou archiver.

---
## 🙋 Motivation personnelle

En tant qu’étudiant en recherche d’alternance, je reçois beaucoup de mails de refus.
À force, ça finit par prendre de la place dans ma boîte mail… mais aussi dans ma tête.
Voir chaque jour des “nous ne donnons pas suite” ou “votre candidature n’a pas été retenue” peut devenir démoralisant.

> Alors j’ai décidé de créer un filtre automatique qui analyse mes mails, détecte les messages de refus, et les supprime ou les archive directement.

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
