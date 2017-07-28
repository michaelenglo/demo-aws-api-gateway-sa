#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import google.cloud.language
import json

class MainHandler(webapp2.RequestHandler):
    def post(self):
        language_client = google.cloud.language.Client()

        text = self.request.get('text')

        document = language_client.document_from_text(text)

        annotations = document.annotate_text(include_sentiment = True,
                                             include_syntax = False,
                                             include_entities = False)

        score = annotations.sentiment.score
        magnitude = annotations.sentiment.magnitude

        self.response.headers["Content-Type"] = "application/json"

        self.response.write(json.dumps({
                "score" : score,
                "magnitude" : magnitude
            }))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
