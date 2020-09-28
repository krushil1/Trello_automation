import os
from trello import create_board, create_list, create_card

board_id = create_board("Work") #This is where you name your new trello board that gets created, you can replace it with what I have

for filename in os.listdir():
    if filename.endswith(".txt"):
        filename = os.path.splitext(filename)[0]
        list_name = create_list(board_id, filename.title())
        with open(f"{filename}.txt", "r") as txt_file:
            for card_name in txt_file.readlines():
                create_card(list_name, card_name)
