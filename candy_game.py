import random
candy = 221
limit = 28
user1_name = input("введите имя первого игрока: ")
user2_bot= "Bot"
while candy>0:
   valid_user_1 = False
   while not valid_user_1:
      user1_candy = int(input(f"{user1_name}_введите количесто вонфет которое возбмете: "))
      if user1_candy<=candy and 1<=user1_candy<=limit:
         candy=candy-user1_candy
         valid_user_1=True
      else:
         print("повторите")
      if candy == 0:
         print(user1_name + " WiN")
   print("осталось конфет "+str(candy))
   valid_user_2 = False
   while not valid_user_2:
      user2_candy = random.randint(1,29)
      if user2_candy<=candy and 1<=user2_candy<=limit:
         print(f"bot берет {user2_candy} конфет")
         candy=candy-user2_candy
         valid_user_2=True
      if candy == 0:
         print(user2_bot + " WiN")
         break
   print("осталось конфет "+str(candy))