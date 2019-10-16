from flask import Blueprint

router = Blueprint("rou5ter", __name__)

@router.route("/hello")
def check():
    return "Congratulations! Your app works. :)"
@router.route("/hello")
def hello():
    return "hello world"
@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return
