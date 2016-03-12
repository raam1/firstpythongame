print('Welcome!\n')
print('This is my first game where you play a character and have to chose between bad and worse choices')
print("Basically you are a black nerd in the american ghetto that love 90's hip-hop, today you were at school\n"
      "and now you're biking your way home but there is a problem your usual route is blocked by a gang shooting a music video\n"
      "If you go through there they will beat you up and take your bike and whatever of value you have there is another way\n"
      "but thats where the dope dealers are that always try to steal your bike....")

first = int(input("\n please enter '1 = bike through the gang OR 2 = 2nd route.': "))
if first == 1:
    print("You start biking to the gang and when you are sure you will make it you feel a very intense pain in your back.\n"
          "GAME OVER")
elif first == 2:
    print("You bike to the 2nd route and mentally getting prepared for men running after you trying to grab your bike when you see\n"
          "the most popular dope dealer 'Domenic' in the city standing there calling you")

second = int(input("\n please enter '1 = don't bat an eye and keep going OR 2 = bike to him and talk.': "))
if second == 1:
    print("You keep biking and pick up speed when you hear 2 men behind you running shouting telling you they will catch you\n"
          "and after maybe 20 seconds you get beaten down and the two men get on your BMX")
    secondOne = int(input("\n please enter '1 = Walk home OR 2 = walk back to Domenic.': "))
if secondOne == 1:
    print("You walk home and the rest of your life is boring you did get beat at home for losing your bike")
elif secondOne == 2:
    second = 2

if second == 2:
    print("You get to Domenic and he looks at you and tells you that he needs some help")
    print("DOMENIC: Now will you help me or nah N!##4?")
    secondTwo = int(input("\n please enter '1 = Help Domenic OR 2 = Tell him you can't and don't help Domenic.': "))