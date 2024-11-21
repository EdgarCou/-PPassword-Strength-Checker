Le projet:

Password-Strangth-Checker est un outil en Python que j'ai conçu pour tenter d'analyser la robustesse d'un mot de passe donné.
Pour cela, il va se fier à plusieurs critères comme la taille et les différents type de caractères

Je l'ai conçu avec un objectif purement éducatif, il ne doit être utilisé que pour analyser vos propres mots de passe. L'utilisation de cet outil pour tester des mots de passe d'autres personnes sans leur consentement peut enfreindre des lois sur la confidentialité.

Les fonctionnalités:

- Vérifier la longueur du mot de passe.
- Vérification des caractères (Majuscule, minuscule, chiffre, caratères spéciaux).
- Score de sécurité, en fonction de ce score, une évaluation sera faite.
- Détails des point à revoir sur le mot de passe si besoin.


Techno utilisées:

- python 3
- getpass: permet de masquer la saisie du mot de passe pour assurer la                confidentialité.
- Colorama: Couleurs pour garder un visuel agréable

Utilisation: 

1. Lancer le script avec la commande "python3 Check.py"
2. Entrez votre mot de passe
3. Observez le résultat obtenu et améliorez le si besoin.


Résultat :

- Si le mot de passe contient tous les critères : 
    The password is strong enough!
- S'il en contient une partie:
    You must have at least one special character.
    The password is not good enough, try to make it stronger
- S'il n'en contient aucun: 
    Your password is too small. At least 12 characters
    You must have at least one capital letter.
    You must have at least one digit.
    You must have at least one special character.
    The password is too weak.

Limites / Améliorations possible:

- Rajouté des critères ou durcir ceux déjà présent.
- Optimiser le score en le rendant plus précis en focntion de l'importance de certain critère
- Rajouter une interface graphique 
- Comparer avec une liste de mots de passe communs