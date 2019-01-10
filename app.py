from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/vertical_timeline")


def switch_styles():

    input = request.args.get("vertical_timeline ")
    index_file = open('index.html', 'r')


    style_switch=index_file.read()



    if input:


       style_switch= style_switch.replace(" <link class="style1" rel="stylesheet"  href="./static/styles.css" type="text/css">",
       < link class ="style2" rel="alternate stylesheet"  href="./static/styles2.css" type="text/css" >" )

    else:
        style_switch= style_switch.replace("<link class="style1" rel="stylesheet"  href="./static/styles.css" type="text/css">", " ")






    index_file.close()
    return switch_styles


# def index():
#
#     input = request.args.get('refresh')
#
#
#     # open file for reading, 'r'
#     # file is saved to variable
#     index_file = open('index.html', 'r')
#     # read contents of the file
#     my_html = index_file.read()
#
#     if input:
#
#
#         # add use input back into the html
#         my_html = my_html.replace("style1", )
#
#     # close the file out when you're done
#     index_file.close()
#
#     return my_html