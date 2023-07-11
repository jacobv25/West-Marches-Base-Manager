West Marches Base Manager Discord Bot
======================================

This bot is designed to facilitate community projects within a Discord server for the Mausritter RPG community, but can be used for any rpg.

Features
--------

*   Create new community projects
*   Update progress on existing projects
*   Mark projects as completed
*   List all projects and their statuses

Commands
--------

*   `!create [project name] [number of steps] [completion reward]`: Creates a new project with the specified name, number of steps, and reward for completion.
*   `!update [project name] [progress]`: Updates the progress of the specified project.
*   `!complete [project name]`: Marks the specified project as completed.
*   `!list_projects`: Lists all projects, their progress, rewards, and completion statuses.

Setup and Installation
----------------------

1.  Clone this repository or download the source code.
2.  Install the required Python packages: `discord.py`.
3.  Create a new bot in the Discord Developer Portal, enable permissions: read messages and send messages, and get your bot token.
4.  Replace "your\_token\_here" in the `bot.run("your_token_here")` line at the end of `bot.py` with your actual bot token.
5.  Run the bot using the command `python bot.py`.

Contributing
------------

Feel free to open issues or pull requests if you want to improve this bot!
