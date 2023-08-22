import random
from discord.ext import commands

class Texts(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def compliment(self, ctx):
        truths = ['You\'re like sunshine on a rainy day.',
        'Colors seem brighter when you\'re around.',
        'How do you keep being so funny and making everyone laugh?',
        'When you say, "I meant to do that," I totally believe you.',
        'You\'re always learning new things and trying to better yourself. That\'s awesome.',
        'Everyone gets knocked down sometimes; only people like you get back up again and keep going.',
        'I am so proud of you, and I hope you are too!',
        'You\'re a great example to others.',
        'Actions speak louder than words, and yours tell an incredible story.',
        'The way you treasure your loved ones is incredible.',
        'You\'re a gift to those around you.',
        'The people you love are lucky to have you in their lives.',
        'Any team would be lucky to have you on it.',
        'There\'s ordinary, and then there\'s you.',
        'Everything would be better if more people were like you.',
        'You are enough.',
        'You are perfect just the way you are.',
        'You inspire me to be a better person.',
        'Being around you makes everything better.',
        'You have such a great heart.',
        'You\'ve accomplished so many incredible things.',
        ' I\'m lucky just to know you.',
        'You spark so much joy in my life.',
        'Your potential is limitless.',
        'You make the small things count.',
        'You are the epitome of a good person.',
        'I always learn so much when I\'m around you.',
        'You\'re better than a triple-scoop ice cream cone. With sprinkles.',
        'You should be thanked more often. So thank you!!',
        'You continue to impress me.',
        'How did you learn to be so great?',
        'On a scale of one to ten, you’re an eleven.',
        'You know just how to make my day!'
        ]
        message = random.choice(truths)
        await ctx.send(message)

    @commands.command()
    async def insult(self, ctx):
        if ctx.author.name == 'Askeladd':
            await ctx.send("No insults for you !!!")
            return
        else:
            insults = ['You\'re so fat, the photo I took of you last christmas is still printing.',
            'You\'re so fat that your favourite necklace is the food chain.',
            'You\'re so ugly that when you tried to enter an ugly contest the judges said, "sorry, no professionals".',
            'You\'re so ugly, when your mom dropped you off at school she got a fine for littering.',
            'You\'re so ugly that I\'m going to have to stop drinking just in case I start seeing two of you.',
            'You are so ugly that your portraits hang themselves.',
            'You\'re so dumb that when you heard it was chilly outside you ran and got a bowl and spoon.',
            'You\'re so dumb that you thought a quarterback was a refund.',
            'The IQ chart doesn\'t go below 75. You can stop trying to go lower.',
            'You\'re so stupid that you climbed a glass wall to see what was on the other side.',
            'I am not saying that you are stupid, just that you are constantly unlucky when you try thinking.',
            'You have an extremely kind face, the kind you throw bricks at.',
            'It\'s better to let someone think you are an Idiot than to open your mouth and prove it.',
            '​If I had a face like yours, I\'d sue my parents.',
            'Roses are red violets are blue, God made me pretty, what happened to you?',
            'Some babies were dropped on their heads but you were clearly thrown at a wall.',
            'I\'d slap you, but that would be animal abuse.',
            'They say opposites attract. I hope you meet someone who is good-looking, intelligent, and cultured.',
            'I\'m busy now. Can I ignore you some other time?',
            'Keep rolling your eyes, perhaps you will find a brain back there.',
            'Why don\'t you slip into something more comfortable, like a coma.',
            'You should really carry a plant around with you to replace the oxygen that you waste when you speak.',
            'I\'m trying to see things from your point of view, but I can\'t get my head that far up my ass.',
            'Your mind is on vacation but your mouth is working overtime.',
            'When I see your face there is not one thing that I would change, apart from the direction that I was walking in.'
            ]
            message = random.choice(insults)
            await ctx.send(message)

    @commands.command()
    async def joke(self, ctx):
        jokes = ['I tripped over a bra in the store the other day \n It was a booby trap.',
        'Why are bakers so rich? \n They make so much dough.',
        'This guy just insulted my boat launch and now I can\'t find him \n I\'ve never seen someone diss a pier like that before.',
        'Someone stole all my lamps. You\'d think I\'d be upset... \n ... But I\'m actually delighted.',
        'Why do teenage girls walk in groups on 3, 5 and 7? \n Because they literally can\'t even...',
        'What is brown and rhymes with snoop? \n Dr. Dre.',
        'How did the pirate get his ship so cheap? \n It was on sail.',
        'How do trees access the internet? \n They log in.',
        'To the person who stole my place in the queue \n I\'m after you now.',
        'I have a fetish for intellectual realization. \n I struggled for a while, but then I came to a conclusion.',
        'My wife asked me to go get 6 cans of Sprite from the grocery store. \n I realized when I got home that I had picked 7 up.',
        'My brother is dating a girl called Rosemary... \n I don\'t know what he season her...',
        'Do you know what the F in “orphan” stands for? \n Family.',
        'I bought a book titled “How To Scam People Online” about three months ago... \n It still hasn’t arrived.',
        'My landlord texted saying we need to meet up and talk about how high my heating bill is. \n I replied back: “Sure, my door is always open.”',
        'I think the girl at the Airlines check-in just threatened me. \n She looked me dead in the eye and said, “Window or aisle?” I laughed in her face and replied, “Window or you\'ll what?”',
        'Did you know that 10+10 and 11+11 are the same? \n 10+10 is 20 and 11+11 is 22.',
        'My wife said, “You really have no sense of direction, do you?” \n I said, “Where did that come from?”',
        'The guy who stole my diary died yesterday. \n My thoughts are with his family.',
        'How did the computer hackers get away from the scene of crime? \n They just ransomware.',
        'Why has Alabama man had sex with clock? \n Because time is relative',
        'Do you know what the opposite of ladyfingers is? \n Mentos.'
        ]
        message = random.choice(jokes)
        await ctx.send(message)

    @commands.command()
    async def guess(ctx, number: int):
        """Guess a random number from 1 to 6."""
        # explained in a previous example, this gives you
        # a random number from 1-6
        value = random.randint(1, 6)
        # with your new helper function, you can add a
        # green check mark if the guess was correct,
        # or a red cross mark if it wasn't
        print(value)
        await ctx.tick(number == value)