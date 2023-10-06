# DiscordBotPython


Use the command **py -3 main.py** to run the bot.

Every bot command should start with the *!* character.

Use the command *!commandslist* to view every available command.

## Prerequisites:

1. Install python (and add it to the PATH in env variables on Windows)
2. Make sure you have pip to manage libraries through python
3. Use pip to install the following:
    - discord
    - pytube
    - fix any other error by adding the mentioned package if it's missing
4. Make sure, that when you deploy the bot, the error messages displayed to the users need to be adjusted to not explicitly show the error due to security reasons (so change *await ctx.send(exception)* to *await ctx.send(errorMessage)*)

## Known bugs:

1. The *!skip* command does not work as intended:
    - the files are not deleted
    - setting the client voice to "stop" does not send the *A song is playing* message, but setting it to "pause" works, but this is definitely not a correct solution
2. Autoplaying songs does not send the *A song is playing* message
3. Sending the *No more songs in the queue* message does not work as intended
4. Weird characters don't work

## Known issues:

1. Data is persisted locally (when it comes to jokes etc.) instead of DB.
2. Refactoring is always possible for improving.
