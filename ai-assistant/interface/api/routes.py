# AI-persona-framework
# Copyright (C) 2025 Kenneth Haider
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

#placeholder

from flask import Flask, url_for
from app import App

import json
import os


# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@App.route('/')
def UrlFn_Index():
    '''handler for welcome page / index '''
    return 'API - INDEX PAGE:\n 1. Select Persona\n 2. Settings...maybe..?'

@App.route("/selector")
def UrlFn_Selector():
    '''handler for AI persona selection'''

    # Specify the relative path to the JSON file
    file_path = os.path.join("subdirectory", "data.json")

    # Open and read the JSON file
    with open(file_path, "r", encoding="utf-8") as file:
        json_data = json.load(file)
    # Assuming the JSON contains an array at the top level or within a key
    json_list = json_data if isinstance(json_data, list) else json_data.get("personas", [])
    
    print(json_list)  # This will print the list extracted from the JSON
    return json_list

# with App.test_request_context():
#     print(url_for('/'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))