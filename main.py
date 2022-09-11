import pandas as pd
import praw
import settings 

#setting up authentication
reddit = praw.Reddit(
    client_id = settings.clientid,
    client_secret = settings.secret,
    user_agent = settings.useragent,
    password= settings.password,
    username = settings.username
)

# checking that authentication passed {"*"}
print("Scopes: ",reddit.auth.scopes())


# reddit instance
subreddit = reddit.subreddit('moneydiariesactive')

#retriving details from 1 result in subreddit search for test
for post in subreddit.search('subscriptions', limit=1):
    print(f"Title: {post.title}")   #prints post title
    print(f"Submission ID: {post.id}")  #prints post id
    print(f"Submission Date: {post.created_utc}")  #post date in unix time
    print(f"Number of Comments: {post.num_comments}")  #number of comments
    #print(f"Body: {post.selftext}")    #text inside post


# get count of results
amt_post = []
for post in subreddit.search('subscriptions', limit=1000):
    amt_post.append(post)

print("Amount of post: ",len(amt_post))


#Opening data in a pandas dataframe then saving it to a csv file
posts = []
for post in subreddit.search('subscriptions', limit=1000):
    posts.append(
        [
            post.id,
            post.title,
            post.created_utc,
            post.num_comments,
            post.selftext
        ]
    )

posts = pd.DataFrame(posts, columns = ["Submission ID", "Title", "Created", "Comments", "Body"])

posts.to_csv('md_datafetch.csv', index=False)

(print("Complete!"))
