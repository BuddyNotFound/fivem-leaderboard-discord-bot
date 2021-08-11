import MySQLdb
import discord
fruits = ["apple"]
db = MySQLdb.connect(
    host = 'localhost',
    user = 'data',
    passwd = 'pass',
    db = 'base'
)

cursor = db.cursor()
cursor.execute


def getAllRows():
        cursor.execute('SELECT nickname, kills FROM users ORDER BY kills DESC')
        result = cursor.fetchall()
        print("TOTAL:  ", len(result))
        print("INDIV")
        for row in result:
            user = row[0]
            kills = row[1]
            print("User", user)
            print("Kills", row[1])
            print("\n")

def getAllRows2():
        cursor.execute('SELECT kills FROM users ORDER BY kills DESC')
        result = cursor.fetchall()

        for row in result:
            kills = row[0]

            return kills

class MyClient(discord.Client):
    async def on_ready(self):
        getAllRows()

    async def on_message(self, message):
        # don't respond to ourselves


        if message.author == self.user:
            return

        if message.content.startswith('watzifak'):
                 cursor.execute('SELECT nickname, kills FROM users ORDER BY kills DESC')
        result = cursor.fetchall()
        print("TOTAL:  ", len(result))
        print("INDIV")
        x = 5
        index = 1
        embedVar = discord.Embed(title="TOP 5 PLAYERS",  color=0x00ff00)
        for row in result:
            user = row[0]
            kills = row[1]
            print("User", user)
            print("Kills", row[1])
            print("\n")

            embedVar.add_field(name=user, value=kills, inline=False)
            if index == x:
                break
            else:
                index += 1

        await message.channel.send(embed=embedVar)
         

            
client = MyClient()

client.run('')

