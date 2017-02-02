#buildup.py
#builds Signup page for GET method
import webapp2
import cgi
def display_user(Username):
    textarea_label="<label type='text' style='display:inline-block;width:150px;color:red'>" +Username+"</label>"
    textarea = "<input type='text' name='username'/>"
    return textarea_label + textarea
def display_pwd(Password):
    textarea_label="<label type='text' style='display:inline-block;width:150px;color:red'>" +Password+"</label>"
    textarea = "<input type='text' name='password'/>"
    return textarea_label + textarea
def display_vpwd(VerifyPassword):
    textarea_label="<label type='text' style='display:inline-block;width:150px;color:red'>" +VerifyPassword+"</label>"
    textarea = "<input type='text' name='Vpassword'/>"
    return textarea_label + textarea
def display_email(EmailOptional):
    textarea_label="<label type='text' style='display:inline-block;width:150px;color:red'>" +EmailOptional+"</label>"
    textarea = "<input type='text' name='email'/>"
    return textarea_label + textarea
def build_signup():
    body = "<body style='background-color:white;'>Hi.</body>"
    submit = "<input type='submit' value='Submit Query'/>"
    form =("<form method='post'>"+
            display_user("Username")+"<br><br>"+
            display_pwd("Password")+"<br><br>"+
            display_vpwd("Verify Password")+"<br><br>"+
            display_email("Email Optional")+"<br><br>"+
            submit+
            "</form>")
    return body + form
