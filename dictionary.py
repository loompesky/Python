#Student Data
#In the telephone book example, the key-value were always name - telephone number.
#In the following example, the data for a student consisting of name, first-name,ID,e-mail,city etc.
#is represented using a dictionary.
#This is again a dictionary with keys and values. However, the keys and values are quite different in nature.
#all keys describe different attributes of the same student. The advantage of this representation is, that you
#do not have to remember at which index what kind of attribute is stored. Another advantage(in comparison to tuples) is
#that additional attributes can be added and not required attributes can be deleted.

student = {
    "name": "McJordan",
    "firstname": "Prince",
    "subject": "Music",
    "musician": True,
    "instruments": ["bass","guitar","piano"],
    "bands": ["Beatles","Wings"],
}
print(student)
print(student["name"])


#Exx1: Translation
#create a dictionary which consist of the colors red,green,blue,yellow as keys and the 
#german translation rot,grun,blau,gelb as values. Using input() ask for another English
#color and its German translation and add this pair to the dictionary


trans = {
    "red":"rot",
    "green":"grun",
    "blue":"blau",
    "yello":"gelb",
}
print(trans)
english = input("Enter English color:")
german = input("Enter German color:")
#the new colours should be added to the existing dictionary
trans[english] = german
print(trans)




#list are in square brackets[], its mutable meaning you can make changes
#tuples are in round brackets () , they are not mutable
#dictionary are in {} and its a key-value pairs, its mutable meaning you can make changes
