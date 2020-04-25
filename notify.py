import feedparser
import notify2
import time
def parser():
    f=feedparser.parse("https://www.indiatoday.in/rss/home")
    notify2.init("News Notification")
    for i in f['items']:
        n=notify2.Notification(i['title'],i['summary'],icon="/tmp/mozilla_abhinav0/abhi.ico")
        # n.update(i['title'],i['summary'],icon="/tmp/mozilla_abhinav0/abhi.ico")
    n.set_urgency(notify2.URGENCY_CRITICAL)
    n.show()
    n.set_timeout(15)
    time.sleep(1200)

parser()

