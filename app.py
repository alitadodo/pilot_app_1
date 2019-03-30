# from flask import Flask, render_template, redirect, request
from flask import *
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["SECRET_KEY"] = "bietchetlien11"
from services import Services

@app.route('/')
def func_name():
  session["logged"] = False
  return render_template('homepage.html')


@app.route('/all_service')
def all_service():
  if session["logged"]:
    services = Services.find()
    return render_template('all_service.html', services=services)
  else:
    return redirect('/login')



# @app.route('/all_service/male')
# def male_service():
#     services = Services.find({ "gender":"male" })
#     return render_template('all_service.html', services=services)


# @app.route('/all_service/female')
# def female_service():
#     services = Services.find({ "gender":"female" })
#     return render_template('all_service.html', services=services)



@app.route('/all_service/<gender>')
def male_service(gender):
  services = Services.find({ "gender":gender })
  return render_template('all_service.html', services=services)


    

# @app.route('/all_service/detail/<id>')
# def detail(id):
#     detail_services = Services.find_one({ "_id": ObjectId(id) })
#     return str(detail_services)

@app.route('/all_service/detail/<id>')
def detail(id):
  detail_services = Services.find_one({ "_id": ObjectId(id) })
  return render_template("detail_service.html", detail_services=detail_services)




@app.route('/delete/<id>')
def delete(id):
  print("hihi")
  delete_service = Services.find_one({"_id": ObjectId(id)})
  if delete_service is not None:
    Services.delete_one(delete_service)
    return redirect('/all_service')
  else:
    return"Not Found service!"



@app.route('/update/<id>', methods=["GET", "POST"])
def update(id):
  edit_service = Services.find_one({"_id": ObjectId(id)})
  if request.method == "GET":
    return render_template("update_service.html", edit_service=edit_service)
  elif request.method == "POST":
    form = request.form
    name = form["full_name"]
    age = form["age"]
    address = form["address"]
    gender = form["gender"]
    available = form["available"]
    new_value = { "$set": {
      "name": name,
      "age": age,
      "address": address,
      "gender": gender,
      "available": available,
    } }
    Services.update_one(edit_service, new_value)
    return redirect('/all_service/detail/{0}'.format(id))

@app.route('/login', methods=["GET", "POST"])
def login():
  if not session["logged"]:
    if request.method == "GET":
      return render_template('login.html')
    elif request.method == "POST":
      form = request.form
      username = form["username"]
      password = form["password"]

      if username == "adminc4e" and password == "adminc4e":
        session["logged"] = True
        return redirect('/all_service')
      else:
        return redirect('/login')
  else: # dang nhap roi
    return redirect('/all_service')
@app.route('/logout')
def logout():
  # del session["logged"] #cach 1
  session["logged"] = False #cach 2
  return redirect('/login')

if __name__ == '__main__':
  app.run(debug=True)