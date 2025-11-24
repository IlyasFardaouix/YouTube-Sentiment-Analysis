# Guide d'Installation - Extension Chrome YouTube Sentiment Analysis

## Prérequis

- Google Chrome (version 88 ou supérieure)
- Connexion Internet

## Installation

### Méthode 1 : Chargement en Mode Développeur (Recommandé)

1. **Ouvrir la page des extensions**

   - Ouvrez Google Chrome
   - Tapez `chrome://extensions/` dans la barre d'adresse
   - Appuyez sur Entrée

2. **Activer le Mode Développeur**

   - En haut à droite de la page, activez le bouton **"Mode développeur"**
   - Le bouton devient bleu quand il est activé

3. **Charger l'extension**

   - Cliquez sur le bouton **"Charger l'extension non empaquetée"**
   - Naviguez vers le dossier `chrome-extension` de ce projet
   - Sélectionnez le dossier et cliquez sur **"Sélectionner le dossier"**

4. **Vérification**
   - L'extension "YouTube Sentiment Analysis" apparaît dans la liste
   - Une icône de puzzle apparaît dans la barre d'outils Chrome

### Méthode 2 : Installation depuis le fichier ZIP

1. **Extraire le fichier**

   - Décompressez `chrome-extension.zip` dans un dossier de votre choix

2. **Suivre les étapes 1-4 de la Méthode 1**

## Configuration

### URL de l'API

L'extension est préconfigurée pour utiliser l'API déployée sur Hugging Face :

```
https://has1elb-youtube-sentiment-analysis.hf.space
```

Si vous souhaitez utiliser une API locale :

1. Ouvrez le fichier `chrome-extension/popup.js`
2. Modifiez la ligne 47 :
   ```javascript
   const apiUrl = "http://127.0.0.1:8000/predict_batch";
   ```
3. Rechargez l'extension dans `chrome://extensions/`

## Dépannage

### L'extension ne s'affiche pas

- Vérifiez que le Mode Développeur est activé
- Actualisez la page `chrome://extensions/`

### Erreur "Could not establish connection"

- Actualisez la page YouTube (F5)
- Vérifiez que l'API est en ligne

### Aucun commentaire trouvé

- Faites défiler la page YouTube vers le bas pour charger les commentaires
- Attendez quelques secondes que les commentaires s'affichent

## Désinstallation

1. Allez sur `chrome://extensions/`
2. Trouvez "YouTube Sentiment Analysis"
3. Cliquez sur **"Supprimer"**
4. Confirmez la suppression
