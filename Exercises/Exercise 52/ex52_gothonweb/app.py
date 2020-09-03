# Gothonweb SIMPLE HTML Engine
from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothonweb import planisphere


app = Flask(__name__)


@app.route("/")
def index():
    # This is used to "setup" the session with starting values
    session['room_name'] = planisphere.START
    return redirect(url_for("game"))


terminating_rooms = ['The End', 'The End Winner']


@app.route("/game", methods=['GET', 'POST'])
def game():
    room_name = session.get('room_name')
    terminate = False
    if room_name in terminating_rooms:
        terminate = True

    if request.method == "GET":
        if room_name != "Death":
            room = planisphere.load_room(room_name)
            return render_template("show_room.html", room=room, done=terminate)
        else:
            # why is there here? do you need it?
            return render_template("you_died.html")
    else:
        action = request.form.get('action')

        if room_name and action:
            room = planisphere.load_room(room_name)
            next_room = room.go(action)

            if not next_room:
                # If the input is not valid, repeat currenrt room.
                session['room_name'] = planisphere.name_room(room)
            else:
                # If the input is valid, go on to next room.
                session['room_name'] = planisphere.name_room(next_room)

        return redirect(url_for("game"))


# YOU SHOULD CHANGE THIS IF YOU PUT ON THE INTERNET
app.secret_key = 'arandomkey'

if __name__ == "__main__":
    app.run()
