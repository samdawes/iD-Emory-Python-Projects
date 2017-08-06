print("Mad Libs is starting!")

adjective1 = input("Enter an adjective: ")

name = input("Enter a name:")

verb1 = input("Enter a verb: ")

place = input("Enter a place: ")

animal = input("Enter a plural animal: ")

thing = input("Enter a thing: ")

verb2 = input("Enter a second verb: ")

noun2 = input("Enter a noun: ")

superhero_name = input("Enter a superhero_name:")

adjective2 = input("Enter a second adjective: ")

#optional vars that could spice the story up
#food = input("Enter a food: ")
#fruit = input("Enter a fruit: ")
#number = input("Enter a number: ")
#country = input("Enter a country:")
#dessert = input("Enter a dessert:")
#year = input("Enter a year:")

#The template for the story
story = """This morning I woke up and felt '{0}' because '{1}'was going to finally '{2}' over the big '{3}'. On the other side of the '{3}' 
        were many '{4}'s protesting to keep '{5}' in stores. The crowd began to '{6}' to the rythym of the '{7}', which made '{8}'
        very '{10}'.""".format(adjective1, name, verb1, place, place, animal, thing, verb2, noun2, superhero_name, adjective2)

print(story)
