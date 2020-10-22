import sys
from bs4 import BeautifulSoup
import requests
import json
import discord
import datetime
import jpholiday


TOKEN = 'NzY4NDE0NzM3NTc4MDY1OTUw.X5AH_Q.ymUUXC0PIbgtBSk4MMQ6o-WWJ98'

CHANNNEL = "768414931905019904" 

client = discord.Client()


@client.event
async def on_ready():
    channel = client.get_channel(int(CHANNNEL))
    print('complete set up.')

    indeta = requests.get("http://newsapi.org/v2/top-headlines?country=jp&apiKey=f291901a86e44b7a8742012b541a3d97")


    w_deta = indeta.json()

    jsontxt = json.dumps(w_deta,indent=4)

    j_data = json.loads(indeta.text)



    cnt = 0
    check = 0
    while(cnt < 20 ):
        source = j_data["articles"][cnt]["source"]["name"]
        title = j_data["articles"][cnt]["title"]
        t_url = j_data["articles"][cnt]["url"]
        img = j_data["articles"][cnt]["urlToImage"]
        time = j_data["articles"][cnt]["publishedAt"]
        print(cnt)
        if img is None:
            print("image has not found(404)")
            img = "https://i.pinimg.com/originals/a4/2d/d8/a42dd8bab11d67086e6a82338bbfa290.jpg"
        cnt = cnt + 1 

        if(source == "Nikkei.com"):
            check = check + 1
            out_news = discord.Embed(title = title,url = t_url,color = discord.Colour.green())
            out_news.add_field(name=source,value=time)
            out_news.set_image(url = img)
            await channel.send(embed = out_news)

    if(check == 0):
        await channel.send("今日の日経記事は出てないみたいだ・・・")

    await client.close()
    try:
        sys.exit(0)
    except SystemExit:
        None



# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)