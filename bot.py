import praw
import pymongo

# Change me
MY_CLIENT_SECRET = ""
MY_CLIENT_ID = ""
MY_CLIENT_USERNAME = ""
MY_CLIENT_PASSWORD = ""
MY_USER_AGENT = "<Platform>:<version>(by u/Your name)"

trigger_words = ["potato"] # You can add as many trigger_words you would like here
message_replies = ["I see that you said potato somewhere in your comment. I am making sure you are aware of that. Thank you!"]  # Each index of this list ^ corresponds to the indeces of the trigger_words list. So you can have different messages for different words
# ^ These two lists must be of same length to work
total_replies = 0
bot_signiture = "\n\nI am a bot that replies to people who have said potato." # Your signature ending after every reply

# Mongo DB connection *Optional*
useDb = True # U can make this false to turn of database usage and run this without a database
mongoDb = pymongo.MongoClient("Mongo Db Link Here")

# Initial Setup
def set_up_bot():
    global reddit # Make it global so the rest can see
    reddit = praw.Reddit(
    client_id = MY_CLIENT_ID,
    client_secret = MY_CLIENT_SECRET,
    user_agent = MY_USER_AGENT,
    username = MY_CLIENT_USERNAME,
    password = MY_CLIENT_PASSWORD)

    load_post_count()

# Scrapes the specific subreddit
# Never ending version that keeps finding new submissions
def scrape_subreddit(name):
    subreddit = reddit.subreddit(name)
    
    for submission in subreddit.stream.submissions():
        submission.comments.replace_more(0) # Get rid of more comments instance
        all_comments = submission.comments.list()

        for comment in all_comments:
            process_comment(comment)

        print(submission.url)

# Scrapes the specific subreddit
# This terminates after getting an "x" amount of posts from this subreddit
# You can also grab the hottest posts in this subreddit
def scrape_subreddit_limit(name, post_limit, hot = False):
    if (hot):
        subreddit = reddit.subreddit(name)
        all_submissions = subreddit.hot(limit = post_limit)
    else:
        subreddit = reddit.subreddit(name)
        all_submissions = subreddit.new(limit = post_limit)

    
    for submission in all_submissions:
        submission.comments.replace_more(0) # Get rid of more comments instance
        all_comments = submission.comments.list()

        for comment in all_comments:
            process_comment(comment)

        print(submission.url)

# Processes the comment and checks to see it they contain any "trigger words". Then replies if necessary
def process_comment(comment):
    for i in range(len(trigger_words)):
        if (comment is None):
            continue

        if (trigger_words[i].lower() in str(comment.body.lower())):
            print("Found a trigger word!")
            global total_replies
            total_replies = total_replies + 1

            reply = "Hello there " + str(comment.author) + "! " + message_replies[i] + bot_signiture + " I have replied to " + str(total_replies) + " comment(s)!"
            comment.reply(reply)

            save_comment(comment, reply, trigger_words[i], total_replies)
            save_post_count()

def save_post_count():
    if (useDb == False):
        return
    myDb = mongoDb["Posted_Comments"]
    mycol = myDb["Post_Count"]
    
    saved_data = mycol.find_one()

    if (saved_data is None) :
        data = {"Total Posted Replies": total_replies}
        x = mycol.update_one(data)
    else:
        saved_data["Total Posted Replies"]
        x = mycol.replace_one(saved_data, {"Total Posted Replies": total_replies})


def load_post_count():
    if (useDb == False):
        return
        
    myDb = mongoDb["Posted_Comments"]
    mycol = myDb["Post_Count"]

    data = mycol.find_one()
    num = data["Total Posted Replies"]
    global total_replies

    if (num is None):
        total_replies = 0
        save_post_count()
        return

    total_replies = int(num)

def save_comment(comment, reply, trigger_word, reply_num):
    if (useDb == False):
        return
    
    myDb = mongoDb["Posted_Comments"]
    mycol = myDb["Saved_Comments"]
    data = { "Author": str(comment.author), "Body": str(comment.body), "Comment ID:": str(comment.id), "Score": int(comment.score), "Subreddit": str(comment.subreddit_id), "Link ID:": str(comment.link_id), "Permalink": str(comment.permalink), "Trigger Word": trigger_word, "Bot Reply": reply, "Reply Number": reply_num}

    x = mycol.insert_one(data)


set_up_bot()
scrape_subreddit_limit("test", 10)