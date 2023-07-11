import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

class Project:
    def __init__(self, name, steps, reward):
        self.name = name
        self.steps = steps
        self.reward = reward
        self.progress = 0
        self.status = "In Progress 🚧"

projects = {}

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def create(ctx, name, steps: int, reward):
    projects[name] = Project(name, steps, reward)
    await ctx.send(f"Project {name} has been created!")

@bot.command()
async def update(ctx, name, progress: int):
    if name in projects:
        projects[name].progress = progress
        await ctx.send(f"Project {name} has been updated!")
    else:
        await ctx.send(f"Project {name} doesn't exist!")

@bot.command()
async def complete(ctx, name):
    if name in projects:
        projects[name].status = "Completed ✅"
        await ctx.send(f"Project {name} has been marked as complete!")
    else:
        await ctx.send(f"Project {name} doesn't exist!")

@bot.command()
async def list_projects(ctx):
    for name, project in projects.items():
        progress_bar = "["
        for i in range(project.steps):
            if i < project.progress:
                progress_bar += "▓"
            else:
                progress_bar += "▒"
        progress_bar += "]"
        await ctx.send(f"{name}\nProgress: {progress_bar} {project.progress}/{project.steps}\nCompletion Reward: {project.reward}\nStatus: {project.status}")

bot.run("your-token-here")
