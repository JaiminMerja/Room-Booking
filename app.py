from flask import Flask, render_template, request, redirect

app = Flask(__name__)

reservations = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        
        reservation = {
            "id": len(reservations) + 1,
            "name": request.form["name"],
            "email": request.form["email"],
            "phone": request.form["phone"],
            "date": request.form["date"],
            "time": request.form["time"],
            "guests": request.form["guests"],
            "status": "Pending",
            "special_requests": request.form["special_requests"],
        }
        reservations.append(reservation)
        return redirect("/")

    return render_template("index.html")

@app.route("/admin")
def manage_bookings():
    return render_template("admin.html", reservations=reservations)

@app.route("/update_status/<int:id>", methods=["POST"])
def update_status(id):
    reservation = next((r for r in reservations if r["id"] == id), None)
    if reservation:
        reservation["status"] = request.form["status"]
    return redirect("/admin")

if __name__ == "__main__":
    app.run(debug=True)
