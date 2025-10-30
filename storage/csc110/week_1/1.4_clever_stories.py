print ("Please enter the following:")

abjective = input("abjective: ")
animal = input("animal: ")
verb_1 = input("verb: ")
exclamation = input("exclamation: ")
verb_2 = input("verb: ")
verb_3 = input ("verb: ")

abjective = abjective.lower()
animal = animal.lower()
verb_1 = verb_1.lower()
exclamation = exclamation.capitalize()
verb_2 = verb_2.lower()
verb_3 = verb_3.lower()

story = (f'Your story is:\n\nThe other day, I was really in trouble. It all started when I saw a very\n{abjective} {animal} {verb_1} down the hallway. "{exclamation}!" I yelled. But all\nI could think to do was to {verb_2} over and over. Miraculously,\nthat caused it to stop, but not before it tried to {verb_3}\nright in front of my family. ')

print(story) 