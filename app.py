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




# Add an article for the user
@app.route('/articles', methods=['POST'])
def create_article():
    data = request.get_json()
    user_id = data.get('user_id')
    user = User.query.get(user_id)

    if user:
        new_article = Article(
            user=user,
            author=user.name,
            title=data['title'],
            body=data['body']
        )
        db.session.add(new_article)
        db.session.commit()
        return jsonify({'message': 'Article created successfully'}), 201
    else:
        return jsonify({'message': 'User not found'}), 404

# Access user's articles
@app.route('/articles/user/<int:user_id>', methods=['GET'])
def get_user_articles(user_id):
    user = User.query.get(user_id)

    if user:
        articles = Article.query.filter_by(user_id=user_id).all()
        article_list = []

        for article in articles:
            article_data = {
                'id': article.id,
                'author': article.author,
                'title': article.title,
                'body': article.body,
            }
            article_list.append(article_data)

        return jsonify({'articles': article_list})
    else:
        return jsonify({'message': 'User not found'}), 404

# Retrieve a specific article by ID
@app.route('/articles/<int:article_id>', methods=['GET'])
def get_article(article_id):
    article = Article.query.get(article_id)

    if article:
        article_data = {
            'id': article.id,
            'author': article.author,
            'title': article.title,
            'body': article.body,
        }
        return jsonify(article_data)
    else:
        return jsonify({'message': 'Article not found'}), 404


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
@app.route('/signIn', methods=['POST'])
def signIn():
    user = User.query.filter(User.email == request.json['email'], User.password == request.json['password']).first()
    if user is not None:
        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email
        }
        return jsonify(user_data,{'message': 'Login Successful'})
    else:
        return jsonify({'message': 'Invalid Credentials'})

@app.route('/donateFunds/<int:id>', methods=['POST'])
def donate_funds(id):
    user = User.query.filter(User.id == id).first()
    donation = Donation(user=user, type="Cash", amount=request.json['amount'])
    db.session.add(donation)
    db.session.commit()

    donation_data = {
            'id': donation.id,
            'user_id': donation.user_id,
            'type': donation.type,
            'amount': donation.amount,
            'date': donation.date}
    
    return jsonify(donation_data)
@app.route('/donateFood/<int:id>', methods=['POST'])
def donate_food(id):
    user = User.query.filter(User.id == id).first()
    donation = Donation(user=user, type="Food", amount=request.json['amount'])
    db.session.add(donation)
    db.session.commit()

    donation_data = {
            'id': donation.id,
            'user_id': donation.user_id,
            'type': donation.type,
            'amount': donation.amount,
            'date': donation.date}
    
    return jsonify(donation_data)

@app.route('/userDonations/<int:id>')
def get_user_donations(id):
    user = User.query.filter(User.id == id).first()
    donations = user.donations
    donation_list = []
    for donation in donations:
        donation_list.append({
                    'id': donation.id,
                    'user_id': donation.user_id,
                    'type': donation.type,
                    'amount': donation.amount,
                    'date': donation.date})
    return jsonify(donation_list)    
        
    
    

if __name__ == '__main__':
    app.run(debug=True)