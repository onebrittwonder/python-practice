import random
from random import randint

inventory = []
hallway_completed = False

def add_to_inventory(item):
    if item not in inventory:
        inventory.append(item)
        print(f"{item.title()} has been added to your inventory.\n")
    else:
        print(f"You already have {item.title()} in your inventory.\n")

def check_inventory():
    if inventory:
        print("\nYour inventory contains:")
        for item in inventory:
            print(f"- {item}")
    else:
        print("\nYour inventory is empty.\n")

def hallway_puzzle():
    global hallway_completed
    
    steps = randint(3, 5)
    successful_steps = 0

    print("You hear faint shuffling sounds in the dark hallway...")
    print("To navigate safely, move opposite to the sound.")

    while successful_steps < steps:
        shuffling_direction = random.choice(["left", "right"])
        print(f"\nYou hear shuffling to your {shuffling_direction}")

        player_direction = input("What to do? (Left / Right)")

        if player_direction not in ["left", "right"]:
            print("Invalid choice! Please choose 'Left' or 'Right'")
            continue
        
        if (shuffling_direction == "left" and player_direction == "right") or (shuffling_direction == "right" and player_direction == "left"):
            successful_steps += 1
        else:
            print("Something attacks you! You must start over...")
            successful_steps = 0
        
    print("""
          You've made it to the end of the hallway, you can see the faint glow of a small chest. 
          It contains a ceremonial dagger. It could break seals or be used as a weapon.
          """)
    add_to_inventory("dagger")
    hallway_completed = True
    print("\nYou return to the main floor. Whatever was in the hallway must have been guarding the dagger.")

def trapdoor():
    print("""
          Down the trap door leads to another iron door, tinged with rust. 
          There is traces of dried blood everywhere. You hear Muffins hiss from through the door. 
          It's now or never.
          """)
    while True:
        print("There is no choice here.")
        action = input("What to do?\n (Proceed / Inventory) ").lower()
        
        if action == "proceed":
            print("""
                  You push the door open...
                  """)
            boss_encounter()
            
        elif action == "inventory":
            check_inventory()

        else:
            print("Invalid choice. Please select an available option.")

def ending_one():
    print("""
        A week later you get a letter in the mail, it was short, 'Thank you for breaking the seal
        that kept us chained to that dreadful place! We can resume our cat meetings in peace.'
                      
        Thanks for playing!
        """)
    exit()

def ending_two():
    print("""
        A week later, you see a news story about the government siezing control of an "ultimate"
        weapon in the form of a creature of unknown origin. It was found in the basement of an
        abandoned warehouse run by a cat cult...
        
        You pet Muffins who is sitting securely on your lap.
                      
        Thanks for playing!
        """)
    exit()

def boss_encounter():
    print("""
          A bulbous, convulsing creature stands guard over walls lined with cats in cages. 
          You spot Muffins' calico fur and purple collar.
          The creature turns to you. It looks like some failed science experiment. 
          It snarls in your direction.
          """)
    
    while True:
        action = input("What to do?\n (Attack / Bait / Run) ").lower()

        if action == "attack": 
            if "dagger" in inventory:
                print("""
                    The dagger grows hot in your hand as you lunge at the creature, pointy end first. 
                    As the blade pierces the beast, it shrieks in pain and hunches over. Now's your chance!
                    You sprint to the cages and grab Muffins. You unlock the rest of the cats 
                    and return to the entrance.
                    """)
                ending_one()
            else:
                print("""
                    You ball up your fists. The creature sulks towards you, in no hurry. You step and punch.
                    The creature's skin is solid and your fist aches with pain. The creature envelops you 
                    and nothing exists but darkness.
                      
                    You have failed to rescue Muffins.
                      
                    Thanks for playing!
                    """)
                exit()

        elif action == "bait": 
            if "meat" in inventory:
                print("""
                    The slab of meat is heavy. You throw it to the far end of the room and the creature runs
                    for it. While it's distracted, you grab Muffins and unlock the rest of the cats. The cats scatter
                    as you return to the entrance.
                    """)
                ending_two()
            else:
                print("""
                    You have nothing to satisfy the beast. It charges you and everything after is black.
                      
                    You have failed to rescue Muffins.
                      
                    Thanks for playing!
                    """)
                exit()

        elif action == "run":
            print("""
                You try to sprint passed the creature but you're not fast enough, it grabs you by the ankles
                and drags you towards it. The last thing you feel is a stabbing pain in your chest.
                      
                You have failed to rescue Muffins.
                      
                Thanks for playing!
                """)
            exit()

        elif action == "inventory":
            check_inventory()

        else:
            print("Invalid choice. Please select an available option.")

def main_floor():
    door_examined = False
    door_unlocked = False

    if "flashlight" not in inventory:
        print("""
            The room was enormous. The lifelessness made you feel watched. You can't see far.
            You better come back with some light.""")
    else:
        print("""
            You turn on the flashlight. 'Muffins!' your hushed, frantic whispers echoed around you.
            An agitated growl could be heard from somewhere in the room, but it sounded muffled, as if underground...
            """)
        print("""
            The flashlight reveals another room: The storeroom. A small hallway extends to your right,
            just kiddy corner of the door.
            
            The flashlight flickers as you scan the warehouse floor. Old beams stretch above you, 
            covered in cobwebs, the air thick with dust. Broken crates and shelves lie scattered around.
            An iron door stands at the far end of the room, its hinges creaking as the air shifts.
              
            The growl comes again, this time closer, reverberating from beneath. 
            A faint glow emanates from the corner, where an old, cracked mirror rests on the wall.
        
            Suddenly, a noise from above — something moving in the rafters. You catch a glimpse of something small 
            and fast darting between the beams... a pair of glowing eyes watching you.
            """)

        while True:
            if door_unlocked:
                action = input("What to do?\n (Storeroom / Hallway / Open Door / Mirror / Rafters)\n (Inventory / Back) ").lower()
            else:
                action = input("What to do?\n (Storeroom / Hallway / Door / Mirror / Rafters)\n (Inventory / Back) ").lower()

            if action == "storeroom":
                if "meat" in inventory:
                    print("The fridge is open and empty.")
                elif "code 6490" in inventory:
                    print("""
                        The storeroom contains one mini fridge with a digital padlock. There is a 4 digit code to open...
                        
                        Inside is a slab of marbeled meat. It's wrapped in parchment, the blood drippings
                        dried on the paper. A sticky note sits on top, 'Please feed to Brutus ASAP!!!'
                        """)
                    add_to_inventory("meat")
                else:
                    print("""
                        The storeroom contains one mini fridge with a digital padlock. There is a 4 digit code to open...
                        There must be a code around here somewhere.
                        """)
                    
            elif action == "hallway":
                if not hallway_completed:
                    print("""
                        The hallway is even darker than the main floor. The flashlight has no effect. 
                        In fact, the longer you stand at the mouth of the abyss, it begins to flicker. You reach out and put your 
                        hand through the threshold. You feel a drop in temperature as you see the blackness cover you compeletely. 
                        
                        You take a brave step into the hallway and it's completely silent and black. All you can hear is your breath 
                        and footsteps until a shuffling noise stops you in your tracks. You are not alone. 
                        """)
                    hallway_puzzle()
                else:
                    print("\nThere's nothing for you hear but certain death.")

            elif action == "door":
                if not door_unlocked:
                    print("""
                        There’s a message scrawled nearby: 'The door cannot be opened unless the reflection shows your soul.'
                        """)
                    door_examined = True
                else:
                    print("\nThe door is slightly ajar. You can now choose to open it when ready.")     

            elif action == "mirror":
                if not door_examined:
                    print("""
                        You see a tired reflection. Nothing out of the ordinary.
                        """)
                else:
                    print("""
                        You feel a radiating heat around your head as you look in the mirror. Two slitted, glowing red eyes
                        cover your own. Elongated, pointed ears grow out of your head, the heat of pain feeling
                        very real. 

                        Suddenly it stops, and you hear a click from the large rusted door.
                        """)
                    door_unlocked = True

            elif action == "rafters":
                print("""
                    You look up into the rafters, but whatever was there seems to have disappeared.
                    """)
                
            elif action == "inventory":
                check_inventory()

            elif action == "back":
                print("\nGoing back to warehouse entrance...\n")
                return "back"
            
            elif action == "open door" and door_unlocked:
                print("\nThe door creaks open, revealing an open trapdoor leading down...")
                trapdoor()

            else:
                print("Invalid choice. Please select an available option.") 

def breakroom_scene():
    print("""
        The break room is dusty and filled with chairs. Tables now strewn about the room. 
        Graffiti plastered the walls. The average layperson couldn't decipher their meaning. 
        Though some symbols look very strange...

        Shelves lined the walls, filled with books, documents, and trinkets.
        """)

    graffiti_examined = False

    while True:
        if graffiti_examined:
            action = input("What to do?\n (Decode graffiti / Tables / Shelves)\n (Inventory / Back) ").lower()
        else:
            action = input("What to do?\n (Graffiti / Tables / Shelves)\n (Inventory / Back) ").lower()

        if action == "graffiti" and not graffiti_examined:
            print("""
                  The symbols on this wall seem strange and the longer you look at them you feel nauseous. 
                  You take note of a particular set of symbols. It looks like a code you can decipher. 
                  You should come back when you know more.
                  """)
            graffiti_examined = True

        elif action == "tables":
            print("\nThere's nothing of note besides some notched eldritch drawings underneath the tables.\n")

        elif action == "shelves":
            print("""
                  Hanging from an obsidian statue of a cat, shines a golden key. 
                  The head in the shape of a feline. 
                  'Fitting', you think. Could come in handy.
                  """)
            add_to_inventory("strange key")

        elif action == "decode graffiti" and "tattered journal" not in inventory:
            print("\nI can't understand this without some kind of cipher. I need to look around more.\n")

        elif action == "decode graffiti" and "tattered journal" in inventory:
            print("""
                  The symbols correspond to numbers. Looks like a code within a code. 
                  You take out the journal and find that the 4 symbols on the wall is the code 6940.
                  There must be some place to use this code.
                  """)
            add_to_inventory("code 6940")

        elif action == "inventory":
            check_inventory()

        elif action == "back":
            print("\nGoing back to warehouse entrance...\n")
            return "back"
        
        else:
            print("Invalid choice. Please select an available option.")

def conference_scene():
    print("""
        What remained of a large table lay in the center of the room. Chairs are emptied
        but are adorned with strange ceremonial objects. Twigs tied with red string in the
        shape of cat ears. At the head of the table, the chair had an extended headpiece
        holding a crown. This must be where the cult holds their meetings. 
          
        Well, at least they're reusing the space semi-appropriately!
        
        Amulets and talismans of various shapes and sizes hung from the ceiling, again 
        with vibrant red string.
        
        You notice a safe tucked in the corner of the room by some filing cabinets.
          
        Incoherent scribblings layered the whiteboard behind the crowned chair. Intricate
        symbols and in the center of it all, a tall, black figure loomed over all.
        It appeared to be of the feline variety.
          
        Time to put some pep in your step! Get the hell outta here!  
        """)
    
    while True:
        action = input("What to do?\n (Crown / Safe / Amulets / Whiteboard)\n (Inventory / Back) ").lower()

        if action == "crown":
            print("""
                The room turns into nothing. The floor disappearing beneath your feet.
                Though you remain, hand unable to be pried from the crown, the only other
                thing existing in this universe besides you.
                
                'You have entered the domain of the Temple of Bastet. It seems your stray has found
                her true calling. The mortals say to love something is to...set it free. Don't you agree?'
                
                Suddenly, the room is back and everything is as it was before. You yank your hand free
                from the tendrils of the crown. A bead of sweat falls down your temple. You gulp and 
                come to your senses. 
                """)

        elif action == "safe":
            if "strange key" in inventory:
                print("""
                There's no chance in opening this without a key. There's a golden keyhole.
                The golden cat key from earlier could work...
                
                The key slides into the safe. You turn and hear a click as the safe door pops.
                  
                Inside lies a tattered journal, the edges of the leather seem to be singed. 
                Did someone try to burn this?
                
                You flip through the pages until your eyes land on a table of symbols and their
                corresponding numbers.
                """)
                add_to_inventory("tattered journal")
            else:
                print("\nThere's no chance in opening this without a key. There's a golden keyhole.\n")
 
        elif action == "amulets":
            print("""
                You twist a hanging amulet around with your fingers. Feeling a warmth radiating from 
                the branch figurine, you take your palm off. In the center of its feline shaped
                head lie a red jewel. You could swear it was emitting a slight glow.
                """)
            
        elif action == "whiteboard":
            print("""
                None of this makes sense. The scribbled, thick black figure makes you nervous.
                The symbols around it seem to pulse in an eerie way.
                  
                As you step away from the board, your shoes kick something under the table. 
                There's a flashlight.
                """)
            add_to_inventory("flashlight")

        elif action == "inventory":
            check_inventory()

        elif action == "back":
            print("\nGoing back to warehouse entrance...\n")
            return "back"
        
        else:
            print("Invalid choice. Please select an available option.") 

def intro_scene():
    while True:
        choice = input("What to do?\n (Break Room / Conference Room / Main Floor)\n (Inventory / Exit) ").lower()
        if choice == "break room":
            print("Entering the breakroom...")
            breakroom_scene()

        elif choice == "conference room":
            print("Entering the conference room...")
            conference_scene()

        elif choice == "main floor":
            print("Entering main floor...")
            main_floor()

        elif choice == "inventory":
            check_inventory()

        elif choice == "exit":
            print("""
            Exiting warehouse. You have let Muffins get captured by the cult
                  
            Jerk...
            """)
            break
        
        else:
            print("Invalid choice. Please select an available option.")

def start_game():
    print("""
    The entrance to the warehouse was unsealed. You managed to pry open a side door.
    The dankness of the large, concrete room hits your nose. It must be inactive for quite some time.
    'Muffins, are you here?' you call out, the echoing of your voice is unsettling. 
    Nothing can be heard but the building creaking and moist droplets hitting various surfaces.
          
    There's three doors with signs: Break Room, Conference Room, Main Floor
    """)

    intro_scene()

def main():
    print("""
    Welcome to a short adventure

    Short Summary:

    Your cat Muffins has absconded to the streets and ran into an abandoned warehouse.
    There's rumors of cult activity within its walls. But you would face anything to save
    your best friend.
    """)
    print("Please type in one of the displayed options to play\n")
    start_or_exit_input = input("What would you like to do?\n (Start / Exit:) ").lower()

    if start_or_exit_input == "start":
        start_game()
    else:
        print("Exited the game")

if __name__ == "__main__":
    main()