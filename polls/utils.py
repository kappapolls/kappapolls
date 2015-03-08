import praw, json
from polls_bot_settings import username, password, user_agent

class KappaPollsBot:
    def __init__(self):
        self.user_agent = user_agent
        self.r = praw.Reddit(user_agent=self.user_agent)
        self.r.login(username, password)
        # sometimes cloudflare throws out HTTPError 521 and 522
        # before reddit can respond
        self.r.RETRY_CODES += [521, 522]

    def count_kappapolls_words_in_first_thread(self):
        words = {}
        thread = self.r.get_subreddit('kappapolls').get_hot(limit=1).next()
        flat_comments = praw.helpers.flatten_tree(thread.comments)
        for comment in flat_comments:
            for word in comment.body.split(' '):
                words[word] = words.get(word, 0) + 1

        return words

    def top_kappapolls_commenters(self):
        users = {}
        comments = self.r.get_comments('kappapolls', limit=None)
        for comment in comments:
            user = comment.author.name
            users[user] = users.get(user, 0) + 1

        top_users = sorted(users, key=lambda x: users[x], reverse=True)[:10]
        user_list = []
        for user in top_users:
            user_list.append({'user': user, 'comments': users[user]})

        return user_list

