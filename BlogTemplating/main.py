from flask import Flask, render_template
import requests
import datetime
KEY = "YOU_KEY_VALUE"
content = ''
app = Flask(__name__)

@app.route('/')
def home_page():
    today = str(datetime.date.today())
    week_ago = str(datetime.date.today()-datetime.timedelta(days=7))
    print(today)
    print(week_ago)
    r = requests.get(f"https://newsapi.org/v2/everything?q=technology"
                     f"&from={today}&to={week_ago}&sortBy=popularity"
                     f"&pageSize=20&language=zh"
                     f"&apiKey={KEY}")
    global content
    content = r.json()["articles"]
    return render_template("index.html", content=content)

@app.route('/blog/<int:num>')
def get_blog(num):
    return render_template("post.html", content=content[num], num=num)


if __name__ == "__main__":
    app.run(debug=True)
