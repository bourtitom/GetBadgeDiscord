# Bot Discord Badge Reminder

Ce bot vous aide à maintenir votre badge de développeur Discord en vous rappelant de l'utiliser régulièrement.

## Configuration

1. Installez les dépendances :
```bash
pip install -r requirements.txt
```

2. Créez un bot Discord sur le [portail développeur Discord](https://discord.com/developers/applications)
   - Créez une nouvelle application
   - Allez dans la section "Bot"
   - Copiez le token du bot
   - Activez les "Message Content Intent" dans les paramètres du bot

3. Modifiez le fichier `.env` et remplacez `votre_token_ici` par le token de votre bot

4. Invitez le bot sur votre serveur en utilisant le lien d'invitation généré dans le portail développeur

## Utilisation

- `!wakeup` : Lance ou réinitialise le compteur de 30 jours
- Le bot vous enverra un message privé 7 jours avant l'expiration du badge
- Utilisez à nouveau `!wakeup` pour réinitialiser le compteur à tout moment

## Fonctionnalités

- Compteur de 30 jours
- Alerte 7 jours avant expiration
- Sauvegarde automatique de l'état du compteur
- Messages privés pour les rappels
