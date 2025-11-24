# Guide : Uploader le Projet sur GitHub

Ce guide vous explique étape par étape comment uploader ce projet sur votre repository GitHub **TALEB7/YouTube-Sentiment-Analysis**.

## Prérequis

- Un compte GitHub (https://github.com)
- Git installé sur votre ordinateur
- Accès en ligne de commande (Terminal, PowerShell, ou CMD)

## Étape 1 : Créer le Repository sur GitHub

1. Connectez-vous à [GitHub](https://github.com)
2. Cliquez sur le bouton **"+"** en haut à droite, puis sélectionnez **"New repository"**
3. Remplissez les informations :
   - **Repository name** : `YouTube-Sentiment-Analysis`
   - **Description** : `MLOps project for analyzing YouTube comments sentiment`
   - **Visibility** : Public ou Private (selon votre choix)
   - ⚠️ **NE COCHEZ PAS** "Add a README file" (vous en avez déjà un)
   - ⚠️ **NE COCHEZ PAS** "Add .gitignore" (vous en avez déjà un)
4. Cliquez sur **"Create repository"**

## Étape 2 : Vérifier l'Installation de Git

Ouvrez votre terminal/PowerShell dans le dossier du projet et vérifiez que Git est installé :

```bash
git --version
```

Si Git n'est pas installé, téléchargez-le depuis : https://git-scm.com/downloads

## Étape 3 : Initialiser Git dans le Projet

Dans le dossier racine du projet (`D:\YouTube-Sentiment-Analysis-main`), exécutez :

```bash
# Initialiser le repository Git
git init

# Vérifier le statut
git status
```

## Étape 4 : Configurer Git (si pas déjà fait)

Si c'est la première fois que vous utilisez Git sur cet ordinateur :

```bash
git config --global user.name "TALEB7"
git config --global user.email "votre-email@example.com"
```

## Étape 5 : Ajouter les Fichiers

```bash
# Ajouter tous les fichiers (le .gitignore exclura automatiquement venv/, __pycache__, etc.)
git add .

# Vérifier les fichiers qui seront ajoutés
git status
```

## Étape 6 : Faire le Premier Commit

```bash
git commit -m "Initial commit: YouTube Sentiment Analysis MLOps Project"
```

## Étape 7 : Connecter au Repository GitHub

```bash
# Ajouter le repository distant (remplacez TALEB7 par votre nom d'utilisateur si différent)
git remote add origin https://github.com/TALEB7/YouTube-Sentiment-Analysis.git

# Vérifier la connexion
git remote -v
```

## Étape 8 : Uploader le Code (Push)

```bash
# Renommer la branche principale en 'main' (si nécessaire)
git branch -M main

# Uploader le code sur GitHub
git push -u origin main
```

Si GitHub vous demande vos identifiants :
- **Username** : TALEB7
- **Password** : Utilisez un **Personal Access Token** (pas votre mot de passe GitHub)

### Créer un Personal Access Token

1. Allez sur GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Cliquez sur **"Generate new token (classic)"**
3. Donnez un nom (ex: "YouTube-Sentiment-Analysis")
4. Sélectionnez les permissions : **repo** (toutes les cases sous "repo")
5. Cliquez sur **"Generate token"**
6. **COPIEZ LE TOKEN** (vous ne pourrez plus le voir après)
7. Utilisez ce token comme mot de passe lors du `git push`

## Vérification

1. Allez sur https://github.com/TALEB7/YouTube-Sentiment-Analysis
2. Vous devriez voir tous vos fichiers uploadés !

## Commandes Utiles pour Plus Tard

### Mettre à jour le Repository après des Modifications

```bash
# Voir les fichiers modifiés
git status

# Ajouter les modifications
git add .

# Créer un commit
git commit -m "Description de vos modifications"

# Uploader les modifications
git push
```

### Voir l'Historique des Commits

```bash
git log
```

### Annuler des Modifications Locales

```bash
# Annuler les modifications d'un fichier spécifique
git checkout -- nom-du-fichier

# Annuler toutes les modifications non commitées
git reset --hard HEAD
```

## Fichiers Ignorés par Git

Grâce au fichier `.gitignore`, les fichiers suivants ne seront **PAS** uploadés :
- `venv/` (environnement virtuel Python)
- `__pycache__/` (fichiers Python compilés)
- `*.pyc` (fichiers compilés)
- `data/` (données brutes)
- `models/*.joblib` (modèles entraînés)
- `.env` (variables d'environnement)

## Problèmes Courants

### Erreur : "remote origin already exists"

```bash
# Supprimer l'ancienne connexion
git remote remove origin

# Réessayer l'étape 7
git remote add origin https://github.com/TALEB7/YouTube-Sentiment-Analysis.git
```

### Erreur : "failed to push some refs"

```bash
# Récupérer les changements distants d'abord
git pull origin main --allow-unrelated-histories

# Puis push
git push -u origin main
```

### Erreur d'authentification

- Vérifiez que vous utilisez un **Personal Access Token** et non votre mot de passe
- Le token doit avoir les permissions **repo**

## Support

Si vous rencontrez des problèmes, consultez :
- [Documentation Git](https://git-scm.com/doc)
- [GitHub Help](https://docs.github.com)

---

**Bon upload ! 🚀**

