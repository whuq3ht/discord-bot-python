from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! 🏓 {round(self.bot.latency * 1000)}ms")

async def setup(bot):
    await bot.add_cog(Example(bot))
# Bu dosya, botun cogs klasöründeki örnek bir cog'u temsil eder.
# Bu cog, botun pingini kontrol etmek için bir komut içerir.
# Cog'lar, botun işlevselliğini modüler hale getirmek için kullanılır.
# Bu sayede botun kodu daha düzenli ve okunabilir olur.
# Cog'lar, botun belirli bir işlevini veya özelliğini temsil eden sınıflardır.
# Her cog, botun bir parçası olarak çalışır ve genellikle belirli bir işlevi yerine getirir.
# Örneğin, bir cog, komutları işlemek, olayları dinlemek veya belirli bir API ile etkileşimde bulunmak için kullanılabilir.
# Cog'lar, botun ana sınıfından bağımsız olarak tanımlanabilir ve daha sonra botun ana sınıfına eklenebilir.
# Bu, botun kodunu daha modüler hale getirir ve her cog'un kendi işlevselliğini yönetmesine olanak tanır.
# Cog'lar, genellikle bir sınıf olarak tanımlanır ve bu sınıfın içinde komutlar ve olay dinleyicileri bulunur.
# Cog'lar, botun ana sınıfına eklenmeden önce yüklenmelidir. Bu, genellikle botun başlangıç dosyasında yapılır.
# Cog'lar, botun ana sınıfına eklenirken birkaç adım gerektirir.
# Made by whuq3ht Github Repo: https://github.com/whuq3ht/discord-bot-python