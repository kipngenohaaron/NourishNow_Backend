from flask import Flask,request,jsonify
from flask_migrate import Migrate
from models import User,db,Donation,Article

app = Flask(__name__)






# Add a donation for the user



# Add an article for the user


# Access user's donations
# user_donations = user.donations

# # Access user's articles
# user_articles = user.articles

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)
# with app.app_context():
#     user = User.query.filter(User.id == 1).first()
#     article = Article(user=user, author=user.name, title='My Article', body='This is the article body.')
#     db.session.add(article)
#     db.session.commit()


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/signUp',methods=['POST'])
def create_user():
    new_user = User(name = request.json['name'], email = request.json['email'],password = request.json['password'])
    db.session.add(new_user)
    db.session.commit()

    new_user_data = {
        'id': new_user.id,
        'name': new_user.name,
        'email': new_user.email
    }

    return jsonify(new_user_data)


if __name__ == '__main__':
    app.run(debug=True)