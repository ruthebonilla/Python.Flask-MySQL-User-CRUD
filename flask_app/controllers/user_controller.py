from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.users import User




@app.route("/")
def index():
    return redirect("/users")

@app.route("/users")
def users():
    return render_template("users.html", users=User.get_users())


@app.route("/user/new")
def new():
    return render_template("new_users.html")


@app.route("/user/create", methods=["POST"])
def create_user():
    User.save(request.form)
    return redirect("/users")


@app.route("/users/<int:user_id>")
def show_user(user_id):
    data = {"user_id" : user_id}
    user = User.user(data)
    return render_template("one_user.html", user = user )


@app.route("/users/<int:user_id>/edit")
def edit_user(user_id):
    data = {
        "user_id" : user_id
    }
    user = User.user(data)
    return render_template("edit_user.html", user=user)



@app.route("/user/update/<int:user_id>", methods=["POST"])
def update_user(user_id):
    data = {
        #this side matches sql dtaa base == this side matches html declaration 
        "user_id": user_id,
        "first_name": request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email']
    }
    User.update(data)
    return redirect("/users")


# delete user
@app.route("/users/<int:user_id>/delete")
def delete_user(user_id):
    data = {
        "user_id" : user_id
    }
    print (data)
    User.delete_one_user(data)
    return redirect("/users")
