import discord
from discord.ext import commands, tasks
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
import json

# Charger les variables d'environnement
load_dotenv()

# Configuration du bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Fichier pour stocker les données du compteur
COUNTER_FILE = 'counter.json'

def load_counter():
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_counter(data):
    with open(COUNTER_FILE, 'w') as f:
        json.dump(data, f)

@bot.event
async def on_ready():
    print(f'{bot.user} est connecté et prêt!')
    check_expiration.start()

@bot.command(name='wakeup')
async def wakeup(ctx):
    user_id = str(ctx.author.id)
    current_time = datetime.now()
    expiration_date = current_time + timedelta(days=30)  # 30 jours avant expiration
    
    counter_data = load_counter()
    counter_data[user_id] = expiration_date.isoformat()
    save_counter(counter_data)
    
    await ctx.send(f"✅ Compteur réinitialisé! Je vous préviendrai une semaine avant l'expiration du badge.")

@tasks.loop(hours=24)  # Vérifie une fois par jour
async def check_expiration():
    counter_data = load_counter()
    current_time = datetime.now()
    
    for user_id, expiration_str in counter_data.items():
        expiration_date = datetime.fromisoformat(expiration_str)
        warning_date = expiration_date - timedelta(days=7)  # Alerte 7 jours avant
        
        if current_time >= warning_date and current_time < expiration_date:
            user = await bot.fetch_user(int(user_id))
            days_left = (expiration_date - current_time).days
            await user.send(f"⚠️ Attention! Votre badge Discord expirera dans {days_left} jours. Utilisez la commande `!wakeup` pour réinitialiser le compteur!")

# Lancer le bot
bot.run(os.getenv('DISCORD_TOKEN'))
