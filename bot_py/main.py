import uuid
import requests
import shutil
import disnake
from disnake.ext import commands
intents = disnake.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None, test_guilds=[])# айди вашего сервера в квадратные скобки
@bot.command()
async def help(ctx):
    embed = disnake.Embed(color=0xe51c1c,
    title='`Вот мои команды: \n!help - список команд\n!save + image - сохраняет картинку`' )  # создаёт embed
    await ctx.send(embed=embed)  # отправляет embed

@bot.command()
async def save(ctx):
    try:
        url = ctx.message.attachments[0].url            # Проврека есть ли картнка
    except IndexError:
        print("Error")
        await ctx.send("Вы не прикрепили изображение!")
    else:

        r = requests.get(url, stream=True)

        imageName = str(uuid.uuid4()) + ".jpg" # Даёт имя картинке

        with open(imageName, 'wb') as out_file:
            print('Saving image: ' + imageName)
            shutil.copyfileobj(r.raw, out_file)     # Сохраняет картинку

bot.run('TOKEN')

