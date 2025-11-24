# Guide Utilisateur - YouTube Sentiment Analysis

## Vue d'ensemble

L'extension YouTube Sentiment Analysis permet d'analyser automatiquement le sentiment des commentaires sur n'importe quelle vidéo YouTube. Elle utilise l'intelligence artificielle pour classifier chaque commentaire comme Positif, Neutre ou Négatif.

## Utilisation

### Étape 1 : Accéder à une vidéo YouTube

1. Ouvrez Google Chrome
2. Allez sur [YouTube](https://www.youtube.com)
3. Ouvrez n'importe quelle vidéo avec des commentaires

### Étape 2 : Charger les commentaires

**Important** : Les commentaires doivent être visibles à l'écran pour être analysés.

1. Faites défiler la page vers le bas jusqu'à la section des commentaires
2. Continuez à défiler pour charger plus de commentaires (optionnel)
3. L'extension analysera jusqu'à 50 commentaires visibles

### Étape 3 : Lancer l'analyse

1. Cliquez sur l'icône de l'extension dans la barre d'outils Chrome
   - Si vous ne la voyez pas, cliquez sur l'icône de puzzle et épinglez l'extension
2. Une fenêtre popup s'ouvre avec le titre "YouTube Sentiment"
3. Cliquez sur le bouton rouge **"Analyze Comments"**

### Étape 4 : Consulter les résultats

#### Statistiques Globales

En haut de la fenêtre, vous verrez trois cartes colorées :

- **Carte Verte (Positive)** : Pourcentage de commentaires positifs
- **Carte Grise (Neutral)** : Pourcentage de commentaires neutres
- **Carte Rouge (Negative)** : Pourcentage de commentaires négatifs

Exemple :

```
Positive: 45%    Neutral: 30%    Negative: 25%
```

#### Nombre Total

Sous les statistiques : `Analyzed 20 comments`

#### Liste Détaillée

Chaque commentaire analysé est affiché avec :

- **Numéro** : Identifiant du commentaire (Comment 0, Comment 1, etc.)
- **Sentiment** : Positive, Neutral ou Negative
- **Confiance** : Pourcentage de certitude du modèle (ex: 98.2%)

Les commentaires sont colorés selon leur sentiment :

- Bordure verte = Positif
- Bordure grise = Neutre
- Bordure rouge = Négatif

## Cas d'Usage

### Pour les Créateurs de Contenu

- **Évaluer la réception** : Comprendre rapidement si une vidéo est bien reçue
- **Identifier les problèmes** : Repérer les vidéos avec beaucoup de commentaires négatifs
- **Suivre l'évolution** : Comparer le sentiment entre différentes vidéos

### Pour les Spectateurs

- **Évaluer avant de regarder** : Voir si une vidéo vaut le coup selon les commentaires
- **Éviter les contenus toxiques** : Identifier les vidéos avec beaucoup de négativité
- **Trouver les pépites** : Repérer les vidéos très appréciées

## Limitations

### Nombre de Commentaires

- Maximum 50 commentaires par analyse
- Seuls les commentaires visibles sont analysés (pas les réponses aux commentaires)

### Langues

- Le modèle est entraîné principalement sur des textes en anglais
- Les performances peuvent être réduites sur d'autres langues

### Précision

- Précision moyenne : 90%
- Les commentaires sarcastiques ou ironiques peuvent être mal classifiés
- Les emojis seuls ne sont pas bien interprétés

## Confidentialité

- **Aucune donnée stockée** : Les commentaires ne sont pas sauvegardés
- **Traitement temporaire** : Les données sont analysées puis supprimées
- **Pas de tracking** : L'extension ne collecte aucune information personnelle

## Support

En cas de problème :

1. Vérifiez que l'API est en ligne : [https://has1elb-youtube-sentiment-analysis.hf.space/health](https://has1elb-youtube-sentiment-analysis.hf.space/health)
2. Actualisez la page YouTube
3. Rechargez l'extension dans `chrome://extensions/`

## Exemples de Résultats

### Vidéo Éducative

```
Positive: 70%    Neutral: 25%    Negative: 5%
Analyzed 35 comments
```

→ Contenu bien reçu, audience satisfaite

### Vidéo Controversée

```
Positive: 20%    Neutral: 30%    Negative: 50%
Analyzed 42 comments
```

→ Réception mitigée, beaucoup de critiques

### Vidéo Neutre/Informative

```
Positive: 15%    Neutral: 80%    Negative: 5%
Analyzed 28 comments
```

→ Contenu factuel, peu d'émotions

## Astuces

1. **Charger plus de commentaires** : Faites défiler avant d'analyser pour avoir un échantillon plus large
2. **Analyser plusieurs fois** : Les commentaires changent avec le temps, réanalysez régulièrement
3. **Comparer des vidéos** : Utilisez l'extension sur plusieurs vidéos d'un même créateur pour voir les tendances

## Mise à Jour

Pour mettre à jour l'extension :

1. Téléchargez la nouvelle version
2. Allez sur `chrome://extensions/`
3. Supprimez l'ancienne version
4. Installez la nouvelle version selon les instructions d'installation
