import discord
import random


TOKEN = 'токен бота(но я не буду его сюда вставлять'

# Список идей для поделок из пластика
ideas = [
    "Сделайте мобиль из пластиковых бутылок и подвесите его в вашем саду или на балконе",
    "Создайте оригинальную подставку для телефона из пластиковых стаканчиков",
    "Изготовьте красивый вазон для растений из пластиковых бутылок"
]

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} подключен к Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!поделка'):
        idea = random.choice(ideas)
        await message.channel.send(idea)

client.run(TOKEN)
