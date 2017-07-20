for MurderBackground in range(1):
    print("Welcome To The Estate of Lord James! He is throwing a party tonight and all of his closest friends have been invited.")
EnterEstate = input("Do you wish to enter the estate?")
if((EnterEstate == "yes") or (EnterEstate == "Yes")):
    print("You walk through the door and are greeted with a gruesome sight. Lord James has been murdered! But whose done it?")
else:
    print("If that's what you want!")
WantToInvestigate = input("Do you want to investigate?")
if((WantToInvestigate == "yes") or (WantToInvestigate == "Yes")):
    print("Great! Most of the guests have been interviewed and cleared by the police, but there are still three main suspects.")
else:
    print("Okay!You leave the estate with the other guests.")
for i in range(4):
    Suspects = input("The first suspect is Lady James, the materialistic wife of Lord James. The second is William, the untrustworthy butler of the James'. The third is Herald Quebec, Lord James' longtime business partner. Who do you wish to investigate?")
    if((Suspects == "lady james") or (Suspects=="Lady james") or (Suspects=="Lady James")):
        print("You walk over to Lady James. She appears unmoved by her husband's death.")
        ljq1 = input("Ask her where she was during the murder?")
        if((ljq1 == "yes") or (ljq1 == "Yes")):
    	       print("She says she was in the ballroom entertaining the other guests when she heard a scream. The other guests confirm, but they say she spent most of the night in the bedroom.")
        else:
               print("You are asked to leave the estate.")
        ljq2 = input("Do you wish to go to the bedroom?")
        if((ljq2 == "yes") or (ljq2 =="Yes")):
            print("You enter the bedroom. It is an extravagent room filled with fine drapery, paintings, and large bed.")
        ljq3 = input("Do you wish to look around?")
        if((ljq3 == "yes") or (ljq3 == "Yes")):
            print("You find clothes, books, pillows. But...what is that you see in the corner of the room? The balcony door is wide open and there is smoke coming from the closet.")
        else:
            print("The police enter the room and ask you to leave the estate. Better luck next time!")
        for i in range(2):
            ljq4 = input("Do you wish to go to the balcony or the closet?")
            if((ljq4 == "Balcony") or (ljq4 =="balcony") or (ljq4 == "the balcony") or (ljq4 == "The Balcony") or (ljq4 == "The balcony")):
                print("You enter the balcony. There is a locked suitcase lying on the ground.")
                ljb = input("Do you want to break it open or hand it over to the police? Type 'break' or 'police'")
                if((ljb == "break") or (ljb == "Break")):
                    print("You open the lock and find clothes, a gun, and a photo of Lord James.")
                if((ljb == "Police") or (ljb == "police")):
                    print("You are placed under arrest for interfering with evidence.")
            elif((ljq4 == "closet") or (ljq4 == "Closet") or (ljq4 == "The Closet") or (ljq4 == "The closet") or (ljq4 =="the closet")):
                print("You find a burnt photo of Lord and Lady James. It is still smoking.")
                ljq5 = input("Do you wish the take the photo or leave it?")
                if(ljq5 == "yes" or "Yes"):
                    print("You take the photo and place it in your jacket pocket and reenter the bedroom.")
                else:
                    print("Okay. You don't take the photo, but you do reenter the bedroom.")
    if((Suspects == "Herald Quebec") or (Suspects == "herald quebec") or (Suspects == "Herald quebec") or (Suspects =="herald Quebec")):
        print("You walk over to Herald Quebec. He is hysterically crying and being consolled by a few maids.")
        hqq1 = input("Do you want to ask him where he was at the time of the murder?")
        if((hqq1 == "yes") or ("Yes")):
            print("Between sobs he is able to get out that he is was in the study dealing with some paperwork. He then went to the kitchen to speak to the butler about dinner options.")
        else:
            print("The police realize that you are investigating and ask you to leave.")
            hqq2 = input("Do you want to go to the study or do you want to ask why he is taking Lord James' death so hard? Type 'study' or 'ask'")
            if((hqq2 == "study") or (hqq2 == "Study")):
                print(hotdog)
