# A Reddit Bot!

# Description
- A bot that is made to scrape either endlessly or with a limit subreddit submission comments. It will parse through most of the comments (Not including the ones that are not loaded in initially) then reply to those comments who have a certain "trigger" word. I mainly created this to practice Python more.

# Features
- MongoDB saving comments & post counts
- Two ways to scrape submissions
- Can use multiple trigger words and corresponding messages when parsing comments. 
- Easy to set up for your self

# Technologies used
- PRAW library, MongoDB, I also used an AWS EC2 instance to host this for personal use.

# Requirements
- Python
- PRAW
- registered bot for Reddit
- *Optional MongoDB*

# How to setup
- ![image](https://user-images.githubusercontent.com/60799172/121957131-d87d5880-cd16-11eb-9432-f88d790a0598.png)
- ^ You need to change those fields for your own bot info ^
- *Optional* If you have MongoDB and want to save data, you can set the varaible "useDb" to True and insert the mongodb connection link on line 19 ![image](https://user-images.githubusercontent.com/60799172/121957279-0bbfe780-cd17-11eb-811e-16abf87c18d3.png)
- The default trigger word that this bot replies to is if the comment contains "potato". You can obviously change this here: ![image](https://user-images.githubusercontent.com/60799172/121958193-4413f580-cd18-11eb-9ebf-fce49ce18e4c.png)
- You can also change the corresponding message for that word (By Index) in the message_replies list

-  Then you can choose between two functions, scrape_subreddit("subreddit") & scrape_subreddit_limit("subreddit", limit = x, hot = True/False). scrape_subreddit will endlessly get new submissions from that certain subreddit you choose (there is an api limit though). And scrape_subreddit_limit will choose the first "x" amount of posts to process and you can choose to get the "hot" posts only.


# A couple of pictures
- Working Reply: ![image](https://user-images.githubusercontent.com/60799172/121957912-e7b0d600-cd17-11eb-90fc-604d6f68c62a.png)
- MongoDB database: ![image](https://user-images.githubusercontent.com/60799172/121957984-f9927900-cd17-11eb-8a56-84e68bb1cd8a.png)
- ![image](https://user-images.githubusercontent.com/60799172/121958004-0020f080-cd18-11eb-93da-f4e4f49bbff8.png)


