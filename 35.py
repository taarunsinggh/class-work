#3-5. Changing Guest List: You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.
#• Start with your program from Exercise 3-4. Add a print statement at the
#end of your program stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with
#the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still
#in your list.

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
