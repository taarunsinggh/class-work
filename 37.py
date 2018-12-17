
dinner_list=['NaniJi', 'NanaJi','Mamma','Daddy']
print("Dear "+ dinner_list[0] +" The honour of your presence is requested at The Yacht Club 117 Seaside Drive Miami, Florida on Saturday, June 11th  for Cocktails and Hors d'oeuvres at six o'clock in the evening, Dinner immediately following")
print("Dear "+ dinner_list[1] +" The honour of your presence is requested at The Yacht Club 117 Seaside Drive Miami, Florida on Saturday, June 11th  for Cocktails and Hors d'oeuvres at six o'clock in the evening, Dinner immediately following")
print("Dear "+ dinner_list[2] +" The honour of your presence is requested at The Yacht Club 117 Seaside Drive Miami, Florida on Saturday, June 11th  for Cocktails and Hors d'oeuvres at six o'clock in the evening, Dinner immediately following")
print("Dear "+ dinner_list[3] +" The honour of your presence is requested at The Yacht Club 117 Seaside Drive Miami, Florida on Saturday, June 11th  for Cocktails and Hors d'oeuvres at six o'clock in the evening, Dinner immediately following")

print(dinner_list[1])


dinner_list.pop(1)

dinner_list.insert(1,'MamaJi')
print("Dear "+ dinner_list[0] +" The honour of your presence is requested at The Yacht Club 117 Seaside Drive Miami, Florida on Saturday, June 11th  for Cocktails and Hors d'oeuvres at six o'clock in the evening, Dinner immediately following")
print("Dear "+ dinner_list[1] +" The honour of your presence is requested at The Yacht Club 117 Seaside Drive Miami, Florida on Saturday, June 11th  for Cocktails and Hors d'oeuvres at six o'clock in the evening, Dinner immediately following")
print("Dear "+ dinner_list[2] +" The honour of your presence is requested at The Yacht Club 117 Seaside Drive Miami, Florida on Saturday, June 11th  for Cocktails and Hors d'oeuvres at six o'clock in the evening, Dinner immediately following")
print("Dear "+ dinner_list[3] +" The honour of your presence is requested at The Yacht Club 117 Seaside Drive Miami, Florida on Saturday, June 11th  for Cocktails and Hors d'oeuvres at six o'clock in the evening, Dinner immediately following")

print ("Dear Guests, I have a good news that I have managed to get a bigger table for the dinner night which was earlier unavailable. That means we can have 3 additional guests")
dinner_list.insert(0,'Kaale')
dinner_list.insert(2,'Savita Didi')
dinner_list.append('Jiji')
print(dinner_list)


print("Dear "+ dinner_list[0] +" The honour of your presence is requested at The Yacht Club 117 Seaside Drive Miami, Florida on Saturday, June 11th  for Cocktails and Hors d'oeuvres at six o'clock in the evening, Dinner immediately following")
print("Dear "+ dinner_list[1] +" The honour of your presence is requested at The Yacht Club 117 Seaside Drive Miami, Florida on Saturday, June 11th  for Cocktails and Hors d'oeuvres at six o'clock in the evening, Dinner immediately following")
print("Dear "+ dinner_list[2] +" The honour of your presence is requested at The Yacht Club 117 Seaside Drive Miami, Florida on Saturday, June 11th  for Cocktails and Hors d'oeuvres at six o'clock in the evening, Dinner immediately following")
print("Dear "+ dinner_list[3] +" The honour of your presence is requested at The Yacht Club 117 Seaside Drive Miami, Florida on Saturday, June 11th  for Cocktails and Hors d'oeuvres at six o'clock in the evening, Dinner immediately following")
print("Dear "+ dinner_list[4] +" The honour of your presence is requested at The Yacht Club 117 Seaside Drive Miami, Florida on Saturday, June 11th  for Cocktails and Hors d'oeuvres at six o'clock in the evening, Dinner immediately following")
print("Dear "+ dinner_list[5] +" The honour of your presence is requested at The Yacht Club 117 Seaside Drive Miami, Florida on Saturday, June 11th  for Cocktails and Hors d'oeuvres at six o'clock in the evening, Dinner immediately following")
print("Dear "+ dinner_list[6] +" The honour of your presence is requested at The Yacht Club 117 Seaside Drive Miami, Florida on Saturday, June 11th  for Cocktails and Hors d'oeuvres at six o'clock in the evening, Dinner immediately following")

#3-7. Shrinking Guest List: You just found out that your new dinner table won’t
#arrive in time for the dinner, and you have space for only two guests.
#• Start with your program from Exercise 3-6. Add a new line that prints a
#message saying that you can invite only two people for dinner.
#• Use pop() to remove guests from your list one at a time until only two
#names remain in your list. Each time you pop a name from your list, print
#a message to that person letting them know you’re sorry you can’t invite
#them to dinner.
#• Print a message to each of the two people still on your list, letting them
#know they’re still invited.
#• Use del to remove the last two names from your list, so you have an empty
#list. Print your list to make sure you actually have an empty list at the end
#of your program.
print(dinner_list[6])

print('Dear friends I want to apologize that the bigger table that was booked has not yet reached and I will be able to invite only 2 people for dinner')


remove_zero=dinner_list.pop(0)
print("Dear "+ remove_zero+" , I am sorry to inform that due to unavoidable circumstances I can't invite you for dinner.")

remove_two=dinner_list.pop(2)
print("Dear "+ remove_two+" , I am sorry to inform that due to unavoidable circumstances I can't invite you for dinner.")

remove_four=dinner_list.pop(4)
print("Dear "+ remove_four+" , I am sorry to inform that due to unavoidable circumstances I can't invite you for dinner.")

remove_five=dinner_list.pop(3)
print("Dear "+ remove_five+" , I am sorry to inform that due to unavoidable circumstances I can't invite you for dinner.")

remove_six=dinner_list.pop(2)
print("Dear "+ remove_six+" , I am sorry to inform that due to unavoidable circumstances I can't invite you for dinner.")

print("Dear " + dinner_list[0]+" , you're still invited for dinner")
print("Dear " + dinner_list[1]+" , you're still invited for dinner")

del(dinner_list[0])
del(dinner_list[0])

print(dinner_list)





