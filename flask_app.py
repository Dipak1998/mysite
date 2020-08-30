from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/index.html')

''' Data save in File '''

@app.route('/contact.html',methods=['POST','GET'])
def contact():
    db_file = open("db.txt", "a")
    # if request.method =='GET':
        # if 'name' in request.args:
        #     name = request.args['name']
        #     # print(name)
        #     mail = request.args['mail']
        #     print(mail)
        #     subject = request.args['subject']
        #     print(subject)
        #     message = request.args['message']
        #     print(message)
        
        # db_file = open("db.txt", "a")
        # db_file.write("Name:"+name ,end = ' ')    
        # db_file.write("Mail Id::"+ mail ,end = ' ')      
        # db_file.write("Subject:"+ subject ,end = ' ')
        # db_file.write("Message:"+ message ,end = ' ')
        # db_file.close()

    
    # db_file = open("db.txt", "r")
    # print(db_file.read())
    return render_template('/contact.html')

@app.route('/<string:page>')
def send_template(page):
    return render_template(page)

if __name__ == "__main__":  
    app.run(port=3000, debug=True)