from flask import Flask

def create_app():
	app = Flask(__name__)
	
	#Register BP if needed
	#app.register_blueprint(main_bp)
	return app
