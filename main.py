

'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        textarea1_label ="<label style='background-color:pink;display:inline-block;width:150px'>Username * : </label>"
        textarea1 = "<input type ='text' name='Username'/>"
        textarea2_label ="<label style='background-color:pink;display:inline-block;width:150px'>Password * : </label>"
        textarea2 = "<input type ='text' name='password'/>"
        textarea3_label ="<label style='background-color:pink;display:inline-block;width:150px'>Verify password * : </label>"
        textarea3 = "<input type ='text' name='Username'/>"
        textarea4_label ="<label style=display:inline-block;width:150px>Email(optional) : </label>"
        textarea4 = "<input type ='text' name='email'/>"


        message = "All the textareas  will work soon !"
        textarea = "<textarea type='text' style='width:310px'>"+message+"</textarea>"

        header = "<h2 style='background-color:rgb(0,180,200);color:white;text-align:center'>USER SIGN-UP</h2>"
        body = "<body style='background-color:rgb(0,180,200)'>Please note that, the first three fields ar required.<br><br></body>"
        submit="<input type='submit'/>"
        form= ("<form>"+

        textarea1_label+textarea1+"<br><br>"+
        textarea2_label+textarea2+"<br><br>"+
        textarea3_label+textarea3+"<br><br>"+
        textarea4_label+textarea4+"<br><br>"+
        textarea+"<br><br>"+submit+
        "</form>")
        self.response.out.write(header +body+form)

app = webapp2.WSGIApplication([
    ('/',MainHandler)
    ],debug=True)

'''
"""
SECOND VERSION USIN G THE FUNCTION display_field("fieldname") .
"""

import webapp2
def display_field(fieldname):
            textarea_label ="<label style='font-size:16px;background-color:white;display:inline-block;width:150px'>"+fieldname+ "</label>"
            textarea =  "<input type ='text' name = 'fieldname'>"
            return textarea_label+ textarea
def build_signup():
    message = "I will validate and display the warnings !"
    textarea = "<textarea type='text' style='width:500px'>"+message+"</textarea>"
    body = "<body style='background-color:white'>Please enter your information accurately.<br><br></body>"
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
        errorheader = "<h2 style='font-family: 'Times New Roman';color:black' > Please signup again </h2>"
        content = build_signup()
        self.response.write(errorheader + content)

app = webapp2.WSGIApplication([
    ('/',MainHandler)
    ],debug=True)
