import flask_app


@app.route('/')
def contact(request):
    db_file = open("db.txt", "a")
    if request.GET.get('name',):
        db_file.write("Name:"+ name)
    if request.GET.get('mail;',):
        db_file.write("Mail Id::"+ mail)
    if request.GET.get('subject;',):
        db_file.write("Subject:"+ subject)
    if request.GET.get('message;',):
        db_file.write("Message:"+ message)

    #open and read the file after the appending:
    db_file = open("db.txt", "r")
    print(db_file.read())

