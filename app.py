from flask import Flask,render_template

def create_app():

    app=Flask(__name__)

    @app.route('/')
    def login():
        return render_template('login.html')
    
    @app.route('/home')
    def home():
        return render_template('home.html')

    @app.route('/profile')
    def profile():
        user = {
        'name': 'Walter White',
        'email': 'heisenberg@example.com',
        'joined_date': '2025-08-08'
        }
        return render_template('profile.html', user=user)
    
    return app

app = create_app()

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
