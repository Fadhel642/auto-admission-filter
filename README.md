# auto-admission-filter
**Objectif** : Script Python qui analyse les e-mails d’admission pour détecter automatiquement les refus (candidature) et les supprimer.

---
## 🙋 Motivation personnelle

En tant qu’étudiant en recherche d’alternance, je reçois beaucoup de mails de refus.
À force, ça finit par prendre de la place dans ma boîte mail, mais aussi dans ma tête.
Voir chaque jour des “nous ne donnons pas suite” ou “votre candidature n’a pas été retenue” peut devenir démoralisant.

> Alors j’ai décidé de créer un filtre automatique qui analyse mes mails, détecte les messages de refus, et les supprime et les marque dans un log.

---
## Fonctionnalités

- Connexion IMAP à une boîte mail (Gmail par exemple)
- Recherche des e-mails **non lus**
- Lecture du contenu (texte brut ou HTML)
- Détection des **mots-clés personnalisables** (dans `phrases_refus.txt`)
- Suppression simulée (mode test)
- Journalisation des actions dans `mail_log.txt`

---
## IMPORTANT

- Pense à utiliser un mot de passe d’application Gmail, et pas ton mot de passe principal ! MAIS il faut d'abord activer la validation en 2 étapes sur Gmail
- S’assurer d’avoir installé les modules nécessaires (`imaplib`, `dotenv`, `email`, `re`)
- **Pour activer la suppression réelle**
  Sur le programme, ces lignes sont désactivées pendant les tests :
  ```
  # imap.store(num, '+FLAGS', '\\Deleted')
  # imap.expunge()
  ```
  Supprime le (**#**) devant ces lignes seulement si tu es sûr de ta détection.
- **ATTENTION** : Ne jamais lancer sans tester (PS: j’ai failli supprimer tous mes mails)
