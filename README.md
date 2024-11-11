Voici un fichier README pour la première version de votre projet Task Tracker CLI :

---

# Task Tracker CLI

Task Tracker CLI est une application de suivi de tâches en ligne de commande, permettant de gérer vos tâches facilement. L'application stocke les tâches dans un fichier JSON et vous permet d'ajouter, de mettre à jour, de supprimer, et de changer l'état des tâches.

## Fonctionnalités

L'application offre les fonctionnalités suivantes :

1. **Ajouter une tâche** : Ajoutez une nouvelle tâche avec une description.
2. **Mettre à jour une tâche** : Modifiez la description d'une tâche existante.
3. **Supprimer une tâche** : Supprimez une tâche en fonction de son identifiant.
4. **Marquer une tâche comme en cours ou terminée** : Changez le statut d'une tâche.
5. **Lister les tâches** : Affichez toutes les tâches, ou uniquement les tâches terminées, non terminées, ou en cours.

## Installation

1. Clonez le dépôt ou téléchargez les fichiers.
2. Assurez-vous que Python est installé sur votre système (Python 3.6 ou supérieur).
3. Naviguez vers le dossier du projet :

   ```bash
   cd task-tracker-cli
   ```

## Utilisation

Les commandes s'exécutent via la ligne de commande. Voici comment utiliser chaque fonctionnalité :

### 1. Ajouter une tâche

```bash
python task_tracker.py add "Acheter des courses"
```

### 2. Mettre à jour une tâche

```bash
python task_tracker.py update <id_de_la_tâche> "Acheter des courses et cuisiner"
```

### 3. Supprimer une tâche

```bash
python task_tracker.py delete <id_de_la_tâche>
```

### 4. Marquer une tâche comme en cours

```bash
python task_tracker.py mark-in-progress <id_de_la_tâche>
```

### 5. Marquer une tâche comme terminée

```bash
python task_tracker.py mark-done <id_de_la_tâche>
```

### 6. Lister les tâches

Pour afficher toutes les tâches :

```bash
python task_tracker.py list
```

Pour afficher uniquement les tâches terminées, non terminées ou en cours :

```bash
python task_tracker.py list done
python task_tracker.py list todo
python task_tracker.py list in-progress
```

## Format des Tâches

Chaque tâche est stockée dans le fichier `tasks.json` avec les propriétés suivantes :

- **id** : Identifiant unique de la tâche.
- **description** : Description de la tâche.
- **status** : Statut de la tâche (`todo`, `in-progress`, `done`).
- **createdAt** : Date et heure de création.
- **updatedAt** : Date et heure de la dernière mise à jour.

## Exemple d'utilisation

```bash
# Ajouter une tâche
python task_tracker.py add "Préparer la réunion de lundi"
# Mettre à jour la tâche
python task_tracker.py update 1 "Préparer la réunion de lundi avec le rapport trimestriel"
# Marquer la tâche comme en cours
python task_tracker.py mark-in-progress 1
# Marquer la tâche comme terminée
python task_tracker.py mark-done 1
# Lister toutes les tâches terminées
python task_tracker.py list done
```

## Structure du Projet

```
task-tracker-cli/
│
├── task_tracker.py         # Fichier principal de l'application
└── tasks.json              # Fichier JSON pour stocker les tâches (créé automatiquement)
```

## Gestion des Erreurs

Le programme gère les erreurs suivantes :
- **Fichier JSON vide ou inexistant** : Crée un fichier vide s'il n'existe pas.
- **ID de tâche non trouvé** : Affiche un message d'erreur si l'ID n'est pas valide.
- **Commandes incorrectes** : Vérifie et affiche un message d'erreur pour les commandes ou les arguments incorrects.

## Contributions

Les contributions sont les bienvenues ! N'hésitez pas à proposer des améliorations ou à ouvrir des issues pour discuter des problèmes ou des fonctionnalités potentielles.

## Licence

Ce projet est libre d'utilisation et modifiable selon vos besoins.

---

Cela devrait vous fournir un README clair et complet pour votre dépôt GitHub.