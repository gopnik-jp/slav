import discord
from numpy.random import *

# Botのアクセストークン
TOKEN = 'NjI4ODYzNjcxNzk1NDQ5ODc3.XZ2Paw.awtCCrkrHae3imPJTH0qGNTvZEk'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    print('chacha')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):

    # 対応表
    num_to_obj = {1:"cheeki breeki", 2:"blin", 3:"vodka", 4:"potatoes", 5:"sunflower seed", 6:"mayonnaise", 7:"3 stripes", 8:"chacha", 9:"kalashinikov", 10:"dragunov", 11:"hardbass", 12:"squat", 13:"Tsar Bomba", 14:"communism", 15:"matryoshka doll", 16:"FBI corpse", 17:"SAIGA 12", 18:"tobacco", 19:"gopnitsa", 20:"Believe in yourself"}


    if message.author.bot:
        return

    if message.content == '.help':
        await message.channel.send('.help : これ\n.cyka : blyat\n.USA : 資本主義の犬め\n.Joseph-Stalin : 総書記\n.今日のラッキーアイテムは何ですか? : ゴプニク流のものを教えてくれるぞ(?は半角)')
    elif message.content == '.cyka':
        await message.channel.send('blyat')
    elif message.content == '.USA':
        await message.channel.send('cyka blyat')
    elif message.content == '.Joseph-Stalin':
        await message.channel.send('Get up, comrade!')
    #elif message.content == '.cyka_in_csgo':

    elif message.content == '.今日のラッキーアイテムは何ですか?':
        num = randint(1,len(num_to_obj))
        if num in num_to_obj:
            word = num_to_obj[num]
            await message.channel.send(word)
        

@client.event
async def on_member_join(member):
    await message.channel.send('WELCOME BLYAT')


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
