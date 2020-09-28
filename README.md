# Trello_automation
This a program which creates a Trello board for you and puts in as many cards as you wish

To get this running:
1. Download both the task_to_trello.py and trello.py files
2. Create a new folder and store both of the downloaded files into that folder.
3. Open both of the files in your prefered IDE.
4. Create a account for Trello if you don't have one or if you do then just open up trello and sign in to it.
5. Once Trello is opened, open this link: https://trello.com/app-key in a new tab. 
6. Once the link is opened on a new tab, copy your API key, it should be around 32 characters.
7. Once the API key is copied, paste it in the trello.py file where it says key.
8. Then, head back to https://trello.com/app-key and right underneath your API key, there should this thing called token, click on the blue link which reads Token.
9. After clicking on Token, you should be redirected a new trello page which reads "Would you like to give the following application access to your account?", verify the information and then head all the way down to where it says "Allow".
10. Click on the Allow button and it should give you your token, the token number should be around 65 characters.
11. Copy that token number and paste it in trello.py file where it says key.
12. Then go to your folder where you saved both the trello.py and task_to_trello.py files
13. Once in that folder, create a new .txt file and name it whatever you want. Remember that whatever you name that .txt file will be the name of your list on Trello.
14. In the .txt file, write as much things as want, each of them will be added as cards to your Trello board. 
15. Once done, make sure you save that .txt file
16. Head back to task_to_trello.py in the IDE. 
17. Once in task_to_trello.py, you will find a variable called board_id = create_board("Work"), whatever is you type inside quotation will be your board's name on Trello.
18. Finally, run the trello.py program first and then run the task_to_trello.py program.
19. You are all set!!
20. Also, you can create as many .txt files as you want!
