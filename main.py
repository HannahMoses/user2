
"""
FOURTH VERSION WITHOUT TEXTBOX and retaining user info in the field boxes
"""
import webapp2
'''
def valid_user(username):
    if username :
        if username.isdigit:
            warning="This is not a valid user name."
            return warning
#        if " " not in username:
'''

def build_signup():
            # message = "I still need to validate and display the warnings !"
            # textarea = "<textarea type='text' style='width:500px'>"+message+"</textarea>"
            body = "<body style='background-color:white'>.<br><br></body>"
    #        header = "<h2 style='background-color:rgb(0,180,200);color:white;text-align:center'>USER SIGN-UP</h2>"
    #        body = "<body style='background-color:rgb(0,180,200)'>Please note that, the first three fields ar required.<br><br></body>"
            submit="<input type='submit' value='Submit Query'/>"
            form= ("<form method = 'post'>"+
            display_field("Username")+"<br><br>"+
            display_field("Password")+"<br><br>"+
            display_field("Verify Password")+"<br><br>"+
            display_field("Email(optional)")+"<br><br>"+
            submit+
            "</form>")
            return body + form

def display_field(fieldname):
            textarea_label ="<label style='font-size:16px;background-color:white;display:inline-block;width:150px'>"+fieldname+ "</label>"
            textarea =  "<input type ='text' name = 'fieldname'>"
            return textarea_label+ textarea


def valid_Username(textarea):
    for i in textarea :
        if i !=" " :
            return True

 # def display_errmessage(fieldname):
 #      if fieldname == "Username" :
 #          errmessage = "That's not a valid username."
 #      else if fieldname == "Password" :
 #          errmessage = "Passwords don't match."
 #      else if fieldname == "Email(optional)" :
 #          errmessage = "You must enter a valid email address."

#     errmessage_label ="<label style='font-size:16px;color:red;display:inline-block;width:150px'>"+errmessage+ "</label>"
#     return errmessage_label
class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h2 style='font-family: 'Times New Roman';color:black' > Signup</h2>"
        content = build_signup()
        self.response.out.write(header + content)

    def post(self):
        #if (valid_Username and valid_password and valid_VerifyPassword) :
#        User = display_field()
#        if valid_Username(Username) :
        correctinfoheader = "<h2 style='font-family: 'Times New Roman';color:black' > Thankyou !</h2>"
        content = build_signup()
        self.response.write(correctinfoheader+  content)

        # if valid_Username(Username) :
        #     self.response.write(correctinfoheader + content)
        # else:
        #     errorheader = "<h2 style='font-family: 'Times New Roman';color:black' > Please signup again !</h2>"
        #     errormessage = " !"
        #     self.response.write(errorheader + errormessage + content)

app = webapp2.WSGIApplication([
    ('/',MainHandler)
    ],debug=True)


'''
"""
THIRD VERSION POSTING errorheader  .
"""

import webapp2
def display_field(fieldname):
            textarea_label ="<label style='font-size:16px;background-color:white;display:inline-block;width:150px'>"+fieldname+ "</label>"
            textarea =  "<input type ='text' name = 'fieldname'>"
            return textarea_label+ textarea
def build_signup():
    message = "I will validate and display the warnings !"
    textarea = "<textarea type='text' style='width:500px'>"+message+"</textarea>"
    body = "<body style='background-color:white'>.<br><br></body>"
#        header = "<h2 style='background-color:rgb(0,180,200);color:white;text-align:center'>USER SIGN-UP</h2>"
#        body = "<body style='background-color:rgb(0,180,200)'>Please note that, the first three fields ar required.<br><br></body>"
    submit="<input type='submit' value='Submit Query'/>"
    form= ("<form method = 'post'>"+
    display_field("Username")+"<br><br>"+
    display_field("Password")+"<br><br>"+
    display_field("Verify Password")+"<br><br>"+
    display_field("Email(optional)")+"<br><br>"+
    textarea+"<br><br>"+submit+
    "</form>")
    return  body + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h2 style='font-family: 'Times New Roman';color:black' > Signup</h2>"
        content = build_signup()
        self.response.out.write(header + content)

    def post(self):
        error = True
        if error == True :
            errorheader = "<h2 style='font-family: 'Times New Roman';color:black' > Please signup again ! </h2>"
            content = build_signup()
            self.response.write(errorheader + content)
        else :
            correctinfoheader = "<h2 style='font-family: 'Times New Roman';color:black' > Thankyou !</h2>"
            content = build_signup()
            self.response.write(correctinfoheader+  content)


app = webapp2.WSGIApplication([
    ('/',MainHandler)
    ],debug=True)
'''
