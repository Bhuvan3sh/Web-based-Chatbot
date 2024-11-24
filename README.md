# Web-based-Chatbot
This open-source framework is designed to help you build your own intelligent chatbot quickly and easily. With a robust backend powered by Google Generative AI and a user-friendly frontend interface, this framework allows you to customize and deploy a chatbot tailored to your specific needs. Whether you're building a customer support bot, a virtual assistant, or an educational companion, this framework provides the tools and flexibility you need to bring your chatbot to life. Dive into the world of conversational AI and create engaging, responsive chat experiences effortlessly. There two files in the package, one is app.py which supports the backend and the other one is index.html which is responsible for the fronend display of the chats. The backend framework uses flask for communication with the frontend web app via the JSON script in the index.html.

## Customizations 

-> If you tried running directly the app.py and opening index.html, then you would have noticed some weired things such as 'YOU_BOT_NAME - Line 189' and  '<INITIAL_TEXT - Line 192>'.<br>
-> So here there are certin things you need to replace before starting to use it, follow the bellow steps to make it a ready to use bot.<br>

**Step 1:** Go to line 12 in app.py replace 'YOUR_BOT_NAME' with your bot.s name.<br>
**Step 2:** Go to line 28 in app.py and replace '<INSER_HERE>' with the context based on with you want your conversation should start.<br>
**Step 3:** Go to line 189 in index.html and replace 'YOUR_BOT_NAME' with with your bot's name.<br>
**Step 4:** Go to Line 192 in index.html and replace '<INITIAL_TEXT>' with the introductory text with you want the bot to show at the initiation of the web app chat.<br>
**Step 5:** Most important part if you skip your bot would'nt work, adding the API key, so as you have understood This chatbot is built.<br><br>
                GO to <a href='https://aistudio.google.com/app/apikey'> aistudio.google.com</a> and then generate a key ![image](https://github.com/user-attachments/assets/dc7ec17b-1c9c-4e1a-b52e-92306e1cea95)<br>
                You might have to create a project for getting an API key, you can create a project by going to cloud.google.com<br>
                Once you have the API key, go-a-head grab it.<br>
**Step 6:** After copying the API key, run 'python3 API_KEY.py' just paste the API Key when it asks you. Now, you are ready to rock.

<u>After doing the above you can go a head to install the dependencies and perform the usage of the web based chatbot you just created.</u>


## Installation and usage
1. **Install requirments.txt**
  ```bash
     pip install -r requirments.txt
   ```
2. **Copy the API key and run this**
```bash
   python3 API_KEY.py
```
2. **Run the app.py file**
```bash
     python app.py
```
3. **Open index.html in a browser**

4. **Start communication**


# GOOD LUCK!!!
