import discord
from discord.ext import commands
import json
import os

# Ayarları yükle
with open('config.json') as f:
    config = json.load(f)

intents = discord.Intents.default()
intents.message_content = True  # Komutları okuyabilmek için gerekli

bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

@bot.event
async def on_ready():
    print(f"✅ {bot.user} olarak giriş yapıldı.")

# Otomatik tüm cogs klasörünü yükle
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(config['token'])

# Bu dosya, botun ana dosyasıdır.
# Botun başlangıç ayarlarını yapar ve cogs klasöründeki tüm cog'ları yükler.
# Bot, Discord API ile etkileşimde bulunmak için discord.py kütüphanesini kullanır.
# Botun prefix'i ve token'ı config.json dosyasından alınır.
# Bot, cogs klasöründeki tüm cog'ları otomatik olarak yükler.
# Bu, botun modüler ve düzenli bir şekilde çalışmasını sağlar.
# Bot, cogs klasöründeki her bir cog'u yüklerken, cog'un adını kullanarak yükler.
# Bu, cog'ların adlarının benzersiz olmasını gerektirir.
# Bot, cogs klasöründeki her bir cog'u yüklerken, cog'un adını kullanarak yükler.
# Bu, cog'ların adlarının benzersiz olmasını gerektirir.