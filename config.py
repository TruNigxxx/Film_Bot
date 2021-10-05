@bot.command()
async def SendPepe(ctx):
    emb = discord.Embed(title = "Pepe", colour=discord.Colour.dark_green())
    emb.set_image(url = "https://i.imgur.com/Hab3RJO.jpg")
    await ctx.send(embed = emb)


