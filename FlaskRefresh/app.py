from flask import Flask,render_template,request, url_for,redirect

app = Flask(__name__)

posts = {
    0:{
        'post_id':0,
        'title':'Hello, there',
        'content':'This is first blog post'
    },
    1: {
        'post_id':1,
        'title': 'Chasing Dreams',
        'content': 'Venturing into the unknown, chasing dreams with an unwavering spirit and a heart full of passion.'
    },
    2: {
        'post_id':2,
        'title': 'Capturing Moments',
        'content': 'Freezing fleeting moments in time, each photograph tells a unique story of life\'s beautiful journey.'
    },
    3: {
        'post_id':3,        
        'title': 'Musings of the Mind',
        'content': 'Delving into the labyrinth of thoughts, exploring the depths of the mind and discovering the power of introspection.'
    },
    4: {
        'post_id':4,
        'title': 'Wanderlust Chronicles',
        'content': 'Roaming the world, one adventure at a time, uncovering hidden gems and embracing the diversity of cultures.'
    },
    5: {
        'post_id':5,
        'title': 'Harmony in Chaos',
        'content': 'Finding balance and beauty in the chaos of everyday life, appreciating the symphony created by the juxtaposition of elements.'
    }
}

@app.route('/')
def home():
    return render_template('home.jinja2', posts =posts)


@app.route('/user_posts/<int:post_id>')
def user_posts(post_id):
    post = posts.get(post_id)
    if not post:
        return render_template('404.jinja2', message=f'A post with ID: {post_id} was not found')
    return render_template('post.jinja2',post=posts.get(post_id))

@app.route('/user_posts/create',methods = ['GET','POST'])
def create():
    if request.method=='POST':
        title = request.args.get('title')
        content = request.args.get('content')
        post_id = len(posts)
        posts[post_id]={"post_id":post_id,'title':title,'content':content}
        return redirect(url_for('user_posts',post_id=post_id))
    return render_template('create.jinja2')

if __name__ == '__main__':
    app.run(debug=True)

