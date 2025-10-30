
### It was difficult, but I really enjoyed making it!

#HISTORY

unknown_answer = "It seems you are using ancient magical words!, but unfortunately, in this kingdom we only speak english Sir!, please try again!"

history = "You are a knight from the 1400s. Your armor is bright and magnificent. You stand in a row on your horse with hundreds of your brothers on a large green field. Behind you is your beloved city. You are all about to fight another kingdom. You always liked growing plans in your free time, and today you have a great battle to fight! Your king blows his trumpet — everybody charges! What do we choose?: "

#Charge Path 
charge = "You charge — and immediately you are knocked unconscious. You should've practiced more instead of thinking you were hungry during drills. When you wake up, you are in the garrison's medical center. What should you do?"
sleep = "You fell asleep while counting sheep in your head.\nYou counted so many sheep that eventually you discovered a new way of adding. You kept using your newfound great intellect to become a great merchant — eventually buying the kingdom.\n\nWith your fortune, should you put it into real state, or into Bitcoin?"
real_state = "You invest in real estate. Your family prospers because of you — the Lamborgini name will be remembered forever. THE END."
bitcoin = "You invested everything in Bitcoin... We won't deny it, Baki — it was like throwing money into the river; at least it was fun!"
outside = "You go outside and feel like you're already better. You head back to your little house to rest, sleep in your own bed, and rethink your career — then you move far away and become a farmer. \nOne day they come for you to serve your nation again. Should you go or stay? "
back = "You returned and all your relatives missed you. You resume your knightly duties and serve as a knight for the rest of your days. THE END."
stay = "You remained and spent your days as a gardener. One day, while digging in the earth, you find a gold rock — rock is an understatement; it's a mountain. With it you buy 10,000 farms and the entire kingdom. You become king overnight. Congratulations!"

#Run Path

run_story = "You fled the battle! A bit of a chicken on your part, but still, you remembered you left the stove on. You can return to the kingdom or escape to the woods. Which do you choose?"
one_forest_story = "You escape to the woods, and while you listen to your horse, you hear a voice. It's soft and small. When you look out of the corner of your eye, it sounds like a mosquito, but it's not a mosquito. It seems to be a fairy like in a fairy tale. (What a redundancy.) she becomes your friend and you both are happy for ever, THE END."
two_speak_story = "You talk to him but he doesn't speak English, he speaks ''Adinglish'' but luckily you had studied Adinglish in your free time, just in case, you become good friends and live happily ever after, you want to give him something, you gave her a little wand, you become friends, THE END."
three_diamond_story = "You give her a diamond, it's so tiny you can barely see it, not everyone would accept it, but for your friend it's perfect, congratulations! THE END."
three_wand_story = "You give her a wand... if you can even call it a wand, it's more like a splinter, surprisingly she can do magic too, she casts a spell on you and turns you into a fairy too, congratulations, you went from knight to Ada! THE END."
two_squash_story = "You squash the mosquito, it seems to be tougher than it looks, it looks a little annoyed, looks at you and walks away, you couldn't take on an army, nor a little fairy, you start to reconsider your career, the fairy turns you into a toad, in a few hours while you were worried and jumping around, a beautiful villager approaches, she kisses you, and you become a human again, they both are happy for ever, THE END."
three_frog_story = "You run away from the beautiful villager, a strange decision indeed, you accidentally fall into a mud pit, it's not deep, as there's no way out you jump through a tunnel, find a society of frogs, and eventually become the king of the frogs! LONG LIVE THE FROG KING! THE END.!!"
one_kingdom_story = "You throw your armor into the river, you come back with only the clothes you were wearing inside, the guards watch you enter through the door, they are not stupid, they recognize the marks of the kingdom in your clothes, they put you in the dungeon for running away, 2 days pass, they have fed you well after all, then by accident, you press a hidden button in the middle of the bricks, it reveals a chest, there is a scroll with the image of a dragon on it and the other a toy rubber chicken, something tells you that if you touch one of them, you will gain great power, which one do you take? "
two_chicken_story = "You take the dragon's scythe, and suddenly your body begins to change. It becomes smaller, and your cackling can be heard in the dungeons. You've turned into a chicken! Some guards passing by are surprised to see you talking! The most careless of them grabs you and carries you off. Yo became good friend and after a few time, you become a human again, you are still friends!"
two_dragon_story = "You take the chicken, and suddenly your body begins to change, it grows and you break the dungeons, turning into a dragon, you return to the enemy camp, the war continues, you set it on fire, the enemy surrenders, you learn to transform into a human and you are crowned Major General of the armies (Although with you armies are no longer needed, only you) THE END."

print(history)
decision_one = input("CHARGE or RUN? ").lower()

### Charge path
if decision_one == "charge":
    print(charge)
    charge_one = input("SLEEP or GO" ).lower()

    if charge_one == "sleep":
        print(sleep)
        
        charge_one_two = input("REAL STATE or BITCOIN ").lower()

        if charge_one_two == "real state":
             print(real_state)
             
        if charge_one_two == "bitcoin":
            print(bitcoin)

        if charge_one_two == "real state" or charge_one_two == "bitcoin":
            exit(0) 
        

    if charge_one =="go":
        print(outside)
        
        charge_two_two = input("GO or STAY ").lower()

        if charge_two_two == "go":
             print(stay)
             
        if charge_two_two == "stay":
            print(back)
        
        if charge_two_two == "stay" or charge_two_two == "go":
            exit(0) 
###



### Run Path
if decision_one == "run":
    print(run_story)
    charge_one = input("FOREST or KINGDOM ").lower()

    if charge_one == "forest":
        print(one_forest_story)
        charge_one_two = input("SPEAK or SQUASH ").lower()

        if charge_one_two == "speak":
             print(two_speak_story)
             
        if charge_one_two == "squash":
            print(two_squash_story)

        if charge_one_two == "speak" or charge_one_two == "squash":
            exit(0) 
        

    if charge_one =="kingdom":
        print(one_kingdom_story)
        
        charge_two_two = input("DRAGON  or CHICKEN? ").lower()

        if charge_two_two == "dragon":
             print(two_dragon_story)
             
        if charge_two_two == "chicken":
            print(two_chicken_story)
        
        if charge_two_two == "dragon" or charge_two_two == "chicken":
            exit(0) 




       

        else: print(unknown_answer)
    else: print(unknown_answer)
else: print(unknown_answer)

exit(0)