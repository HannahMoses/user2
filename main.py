#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        textarea1_label ="<label style='background-color:pink'>Username : </label>"
        textarea1 = "<input type ='text' name='Username'/>"
        textarea2_label ="<label style='background-color:pink'>Password : </label>"
        textarea2 = "<input type ='text' name='password'/>"
        textarea3_label ="<label style='background-color:pink'>Verify password : </label>"
        textarea3 = "<input type ='text' name='Username'/>"
        textarea4_label ="<label>Username : </label>"
        textarea4 = "<input type ='text' name='Username'/>"


        message = "All other textareas  will work soon !"
        textarea = "<textarea type='number'>"+message+"</textarea>"

        body = "<body style='background-color:rgb(0,180,200)'"
        submit="<input type='submit'/>"
        form= ("<form>"+

        textarea1_label+textarea1+"<br><br>"+
        textarea2_label+textarea2+"<br><br>"+
        textarea3_label+textarea3+"<br><br>"+
        textarea4_label+textarea4+"<br><br>"+
        textarea+"<br><br>"+submit+
        "</form>")
        self.response.out.write(body+form)

app = webapp2.WSGIApplication([
    ('/',MainHandler)
    ],debug=True)
