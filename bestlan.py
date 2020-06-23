import time
def bestlanguage (mylang):
    langlist = (
        ("Python","You Rock! Big guy!"),
        ("microPython","You also rock, little guy!"),
        ("Java","So that's how you want to spend your life huh?"),
        ("C","Did you miss the memo? Also, is it you that keeps leaving all this garbage around?"),
        ("C++","It's ok to be a masochist, as long as you are efficient. Now take out your garbage!"),
        ("Go","You're alright man *chuck*"),
        ("Cobol","Take a seat, you are looking a little pale old guy."),
        ("Pascal","Dear god, WHY?"))
    for lang in langlist:
        if mylang.lower() == lang[0].lower():
            print ("You like %s %s" % lang)

while True:
    print ("What language do you like progarmming in? ")
    bestlanguage(input())
    time.sleep(2)
    
