# Commandes pour Uploader le Projet sur GitHub

## ⚠️ IMPORTANT : Créer le Repository sur GitHub d'abord !

1. Allez sur https://github.com/new
2. Nom du repository : `YouTube-Sentiment-Analysis`
3. **NE COCHEZ PAS** "Add a README file"
4. **NE COCHEZ PAS** "Add .gitignore"
5. Cliquez sur **"Create repository"**

## 📋 Commandes à Exécuter dans PowerShell

Copiez et exécutez ces commandes **UNE PAR UNE** dans PowerShell :

```powershell
# 1. Vérifier que vous êtes dans le bon dossier
cd D:\YouTube-Sentiment-Analysis-main

# 2. Initialiser Git
git init

# 3. Configurer Git (remplacez l'email par le vôtre)
git config --global user.name "TALEB7"
git config --global user.email "votre-email@example.com"

# 4. Ajouter tous les fichiers
git add .

# 5. Vérifier les fichiers ajoutés
git status

# 6. Créer le premier commit
git commit -m "Initial commit: YouTube Sentiment Analysis MLOps Project"

# 7. Ajouter le repository GitHub comme origine
git remote add origin https://github.com/TALEB7/YouTube-Sentiment-Analysis.git

# 8. Vérifier la connexion
git remote -v

# 9. Renommer la branche en 'main'
git branch -M main

# 10. Uploader le code sur GitHub
git push -u origin main
```

## 🔐 Authentification GitHub

Lors de l'étape 10 (`git push`), GitHub vous demandera :
- **Username** : `TALEB7`
- **Password** : Utilisez un **Personal Access Token** (PAS votre mot de passe)

### Créer un Personal Access Token :

1. Allez sur : https://github.com/settings/tokens
2. Cliquez sur **"Generate new token (classic)"**
3. Donnez un nom : `YouTube-Sentiment-Analysis`
4. Sélectionnez les permissions : **repo** (toutes les cases)
5. Cliquez sur **"Generate token"**
6. **COPIEZ LE TOKEN** (vous ne pourrez plus le voir après !)
7. Utilisez ce token comme mot de passe lors du `git push`

## ✅ Vérification

Après le push, allez sur :
https://github.com/TALEB7/YouTube-Sentiment-Analysis

Vous devriez voir tous vos fichiers !

## 🔄 Commandes pour Mettre à Jour Plus Tard

Quand vous modifiez des fichiers :

```powershell
# Voir les modifications
git status

# Ajouter les modifications
git add .

# Créer un commit
git commit -m "Description de vos modifications"

# Uploader les modifications
git push
```

## 🐛 Résolution de Problèmes

### Erreur : "remote origin already exists"
```powershell
git remote remove origin
git remote add origin https://github.com/TALEB7/YouTube-Sentiment-Analysis.git
```

### Erreur : "failed to push some refs"
```powershell
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### Erreur d'authentification
- Vérifiez que vous utilisez un **Personal Access Token** et non votre mot de passe
- Le token doit avoir les permissions **repo**

