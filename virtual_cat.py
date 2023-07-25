#Copyright David Zeidenfeld/St34lth1nt0r (C) 2023
# Using capital letters to name your cat will crash the program
#Use both the Shell and Turtle on screen for best results
import turtle
import time

print('Hello! I am your virtual cat! Thank you SO much for adopting me.')
my_stuff = input('What name would you like to give me, now that Im yours? ')
print('Okay then! My name is... uh... ',my_stuff,', was it? Yeah, that was it!')
print('Anyways, now that I have a name, Ill tell you a few things about me')
print('You can make my happy by giving me some cat treats or some leftovers')
print('(press "M" for "meal") or by rubbing me (press "R" for "rub").')
print('If you have something to do, put me to sleep so I')
print('wont get sad while you are gone (press "S" for "sleep").')
print('If you feed me, or rub me, or put me to bed too much, then')
print('I will go away. If you miss me, you can always help me find my')
print('way back by calling my name (press "P" for "pspsps").')

food = 0
sleep = 0
scritches = 0

def feed_meal():
    global food
    print('Feeding time, ',my_stuff,'!')
    t.screen.addshape('Cat_default.gif')
    t.shape('Cat_default.gif')
    food = food + 1
    print('Got food!')
    print('* ',my_stuff,' has been fed',food,'times *')
    if food > 9:
        t.screen.addshape('cat_sad1.gif')
        t.shape('cat_sad1.gif')
        print('* ',my_stuff,' is looking sad *')
        print('* Maybe they ate too much? *')
    if food > 19:
        t.screen.addshape('cat_sad2.gif')
        t.shape('cat_sad2.gif')
        print('* ',my_stuff,' is crying now *')
        print('* You might have fed them')
        print('one too many times... *')
    if food > 29:
        t.screen.addshape('cat_missing.gif')
        t.shape('cat_missing.gif')
        print('* ',my_stuff,' has left you...')
        print('Hopefully they come back... *')
        print('* Yeah, you definitely')
        print('fed them too much... *')
def go_asleep():
    global sleep
    print('sleeping time!')
    t.screen.addshape('Cat_defaut.gif')
    t.shape('Cat_default.gif')
    sleep = sleep + 1
    print('Meow meow! ZZZZ')
    print('* ',my_stuff,' has gone to sleep', sleep, 'times *')
    if sleep > 9:
        t.screen.addshape('cat_sad1.gif')
        t.shape('cat_sad1.gif')
        print('* ',my_stuff, 'is looking sad *')
        print('* Maybe they slept too much? *')
    if sleep > 19:
        t.screen.addshape('cat_sad2.gif')
        t.shape('cat_sad2.gif')
        print('* ',my_stuff,' is crying now *')
        print('* You might have put them to bed')
        print('one too many times... *')
    if sleep > 29:
        t.screen.addshape('cat_missing.gif')
        t.shape('cat_missing.gif')
        print('* ',my_stuff, 'has left you...')
        print('Hopefully they come back... *')
        print('* Yeah, you definitely')
        print('let them sleep too much... *')
def give_pet_rub():
    global scritches
    print('Who wants scritches?')
    t.screen.addshape('Cat_default.gif')
    t.shape('Cat_default.gif')
    scritches = scritches + 1
    print('Im a good cat! Yes I am, Yes I am!')
    print('* You have rubbed ',my_stuff,'', scritches,' times *')
    if scritches > 9:
        t.screen.addshape('cat_sad1.gif')
        t.shape('cat_sad1.gif')
        print('* ',my_stuff,' is looking sad *')
        print('* Maybe you rubbed them too much? *')
    if scritches > 19:
        t.screen.addshape('cat_sad2.gif')
        t.shape('cat_sad2.gif')
        print('* ',my_stuff,' is crying now... *')
        print('* You might have rubbed them')
        print('one too many times... *')
    if scritches > 29:
        t.screen.addshape('cat_missing.gif')
        t.shape('cat_missing.gif')
        print('* ',my_stuff,' has left you...')
        print('Hopefully they come back... *')
        print('* Yeah, you definitely')
        print('rubbed them too much... *')
def call_name():
    global scritches
    global sleep
    global food
    print('pspsps, here kitty cat!')
    t.screen.addshape('Cat_default.gif')
    t.shape('Cat_default.gif')
    print('Im here!')
    if t.shape == ('cat_missing.gif'):
        scritches = 0
        food = 0
        sleep = 0
        

t = turtle.Pen()
turtle.onkey(feed_meal, 'm')
turtle.onkey(go_asleep, 's')
turtle.onkey(give_pet_rub, 'r')
turtle.onkey(call_name, 'p')
t.screen. addshape('Cat_default.gif')
t.shape('Cat_default.gif')
turtle.listen()

##Feedback appreciated!

    




