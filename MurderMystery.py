for MurderBackground in range(1):
    print("Welcome To The Estate of Lord James! He is throwing a party tonight and all of his closest friends have been invited.")
EnterEstate = input("Do you wish to enter the estate?\n")
if((EnterEstate == "yes") or (EnterEstate == "Yes")):
    print("You walk through the door and are greeted with a gruesome sight. Lord James has been murdered! But whose done it?")
else:
    print("Okay! You leave!")
    exit(0)
WantToInvestigate = input("Do you want to investigate?\n")
if((WantToInvestigate == "yes") or (WantToInvestigate == "Yes")):
    print("Great! Most of the guests have been interviewed and cleared by the police, but there are still three main suspects.")
else:
    print("Okay!You leave the estate with the other guests.")
    exit(0)
for i in range(3):
    Suspects = input("The first suspect is Lady James, the materialistic wife of Lord James. The second is William, the untrustworthy butler of the James'. The third is Herald Quebec, Lord James' longtime business partner. Who do you wish to investigate?\n")
    if((Suspects == "lady james") or (Suspects=="Lady james") or (Suspects=="Lady James")):
        print("You walk over to Lady James. She appears unmoved by her husband's death.")
        ljq1 = input("Ask her where she was during the murder?\n")
        if((ljq1 == "yes") or (ljq1 == "Yes")):
    	       print("She says she was in the ballroom entertaining the other guests when she heard a scream. The other guests confirm, but they say she spent most of the night in the bedroom.")
        else:
               print("You are asked to leave the estate.")
               exit(0)
        ljq2 = input("Do you wish to go to the bedroom?\n")
        if((ljq2 == "yes") or (ljq2 =="Yes")):
            print("You enter the bedroom. It is an extravagent room filled with fine drapery, paintings, and large bed.")
        ljq3 = input("Do you wish to look around?\n")
        if((ljq3 == "yes") or (ljq3 == "Yes")):
            print("You find clothes, books, pillows. But...what is that you see in the corner of the room? The balcony door is wide open and there is smoke coming from the closet.")
        else:
            exit(0)
            print("The police enter the room and ask you to leave the estate. Better luck next time!")
        ljq4 = input("Do you wish to go to the balcony or the closet?\n")
        if((ljq4 == "Balcony") or (ljq4 =="balcony") or (ljq4 == "the balcony") or (ljq4 == "The Balcony") or (ljq4 == "The balcony")):
            print("You enter the balcony. There is a locked suitcase lying on the ground.")
            ljb = input("Do you want to break it open or hand it over to the police? Type 'break' or 'police'.\n")
            if((ljb == "break") or (ljb == "Break")):
                print("You open the lock and find clothes and a gun.")
            if((ljb == "Police") or (ljb == "police")):
                print("You are placed under arrest for interfering with evidence.")
        elif((ljq4 == "closet") or (ljq4 == "Closet") or (ljq4 == "The Closet") or (ljq4 == "The closet") or (ljq4 =="the closet")or (ljq5 == "no") or (ljq5 == "No") or ljq5 == "yes" or "Yes"):
            print("You find a burnt photo of Lord and Lady James. It is still smoking.")
        ljq5 = input("Do you wish the take the photo or leave it? Type 'yes' or 'no'\n")
        if(ljq5 == "yes" or "Yes"):
            print("You take the photo and place it in your jacket pocket and reenter the bedroom.")
        elif((ljq5 == "no") or (ljq5 == "No")):
            print("Okay. You don't take the photo, but you do reenter the bedroom and head for the closet.")
    if((Suspects == "Herald Quebec") or (Suspects == "herald quebec") or (Suspects == "Herald quebec") or (Suspects =="herald Quebec")):
        print("You walk over to Herald Quebec. He is hysterically crying and being consolled by a few maids.")
        hqq1 = input("Do you want to ask him where he was at the time of the murder?\n")
        if((hqq1 == "yes") or ("Yes")):
            print("Between sobs he is able to get out that he is was in the study dealing with some paperwork. He then went to the kitchen to speak to the butler about dinner options.")
        else:
            print("The police realize that you are investigating and ask you to leave.")
        hqq2 = input("Do you want to go to the study or do you want to ask why he is taking Lord James' death so hard? Type 'study' or 'ask'\n")
        if((hqq2 == "ask") or (hqq2 == "Ask")):
            print("He explains that he and Lord James were more than just business partners. They were lifelong best friends. They shared a special type of bond that can never be replaced.")
            hqq6 = input("You apologize for his loss. Do you wish to enter the study? Type 'study'.\n")
        if((hqq2 == "study") or (hqq2 == "Study") or (hqq6 == "study") or (hqq6 == "Study")):
            print("You enter the study. It is smaller than the other rooms in the estate, but still much larger than anything in your own home. The walls are covered with carved oak and green curtains drape the windows. On the right is a gorgeous mahogany table covered in papers.")
            hqq3 = input("Do you wish to inspect the desk or do you want to look under the rug? Type 'rug' or 'desk'.\n")
            if((hqq3 == "desk") or (hqq3 == "Desk"):
                print("You go over to the desk. You see that it is littered with papers as though someone had been searching for something. Lying on the desk is Lord James' bank statements declaring that he had withdrawn $100,000,000,000 from his account. While this is only a small dent in his fortune, it was enough to scare the bank. It appears his account is currently closed.")
                hqq4 = input("Do you wish to look under the rug? Type 'rug'.\n")
            elif((hqq3 == "rug") or (hqq3 == "Rug") or (hqq4 == "Rug") or (hqq4 == "rug")):
                print("You pull the embellished carpeting from the floor and find a small trapdoor.")
                hqq5 = input("Do you wish to go through the trapdoor?\n")
                if((hqq5 == "yes") or (hqq5 == "Yes")):
                    print("You pull the handle and it leads outside. You see the police.")
                    hqq8 = input("Do you want to run back inside or tell them what you find? Type 'police' or 'run'\n")
                    if((hqq8 == "police") or (hqq8 == "Police")):
                        print("You are arrested for interfering with police evidence.")
                        exit(0)
                    elif((hqq8 == "run") or (hqq8 == "Run")):
                        print("Okay, you return to the study.")
                        hqq9 = input("Do you want to go to the desk?")
                        if((hqq8 == "no") or (hqq8 == "No")):
                            print("Okay. You exit the study.")
                        elif((hqq8 = "yes") or (hqq8 = "Yes")):
                            if((hqq3 == "desk") or (hqq3 == "Desk"):
                                print("You go over to the desk. You see that it is littered with papers as though someone had been searching for something. Lying on the desk is Lord James' bank statements declaring that he had withdrawn $100,000,000,000 from his account. While this is only a small dent in his fortune, it was enough to scare the bank. It appears his account is currently closed.")
                                print("You exit the study.")
                elif((hqq5 == "No") or (hqq5 == "no")):
                    print("Okay. You exit the study.")
    if((Suspects == "William") or (Suspects == "william")):
        print("You walk over to William. He appears incredibly angry.")
print("Now that you have heard everyone's story")
GuessMurderer = input("Who do you think killed Lord James? Type 'lady james', 'herald quebec', 'william' depending on who you think killed Lord James.\n")
if((GuessMurderer == "Lady James") or (GuessMurderer == "lady james"):
    print("Sorry! Lady James was not the killer. After finding out about her husband's affair with his business partner, Herald Quebec, Lady James decided to use it against him. She asked William to help her blackmail Lord James, denying him his pay to get him to cooperate. She asked Lord James for a large sum of money. Half of it would be used to pay William and the other half would be used to run away and start a new life. After his account was frozen, Lady James was unable to run away and unable to pay William. William retaliated against Lord James, killing him to recieve the money left for him in Lord James' will.")
    exit(0)
if((GuessMurderer == "Herald Quebec") or (GuessMurderer == "herald quebec")):
    print("Sorry! Herald Quebec was not the killer. Herald Quebec and Lord James had a scandalous secret affiar. After Lady James found out about her husband's affair with Herald, she decided to use it against him. She asked William to help blackmail Lord James, denying him his pay to get him to cooperate. She asked Lord James for a large sum of money. Half of it would be used to pay William and the other half would be used to run away and start a new life. After his account was frozen, Lady James was unable to run away and unable to pay William. William retaliated against Lord James, killing him to recieve the money left for him in Lord James' will.")
    exit(0)
if((GuessMurderer == "William") or (GuessMurderer == "william")):
    print("Yes! William was the killer. Herald Quebec and Lord James had a scandalous secret affiar. After Lady James found out about her husband's affair with Herald, she decided to use it against him. She asked William to help blackmail Lord James, denying him his pay to get him to cooperate. She asked Lord James for a large sum of money. Half of it would be used to pay William and the other half would be used to run away and start a new life. After his account was frozen, Lady James was unable to run away and unable to pay William. William retaliated against Lord James, killing him to recieve the money left for him in Lord James' will.")
    exit(0)
