import flask
print("Hello, World!")
# make a webpage that shows the output of this file
app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <html>
        <body>
            <button onclick="myFunction()">Click me</button>
            <p id="demo"></p>
            <div id="ball"></div>
            <script>
            var counter = 0;
            function myFunction() {
                counter++;
                var node = document.createElement("P");
                var textnode = document.createTextNode("Hello, World! " + "Count: " + counter);
                node.appendChild(textnode);
                document.getElementById("demo").appendChild(node);
                document.getElementById("ball").style.animation = "none";
                setTimeout(function() {
                    document.getElementById("ball").style.animation = "";
                }, 10);
            }
            </script>
            <style>
            #ball {
                width: 50px;
                height: 50px;
                background-color: red;
                position: absolute;
                top: 0;
                left: 0;
                border-radius: 50%;
                animation: ball-animation 2s infinite linear;
            }
            @keyframes ball-animation {
                100% {
                    top: 90vh;
                    left: 90vw;
                }
            }
            </style>
        </body>
    </html>
    '''?

    return '''
    <html>
        <body>
            <button onclick="myFunction()">Click me</button>
            <p id="demo"></p>
            <script>
            var counter = 0;
            function myFunction() {
                counter++;
                var node = document.createElement("P");
                var textnode = document.createTextNode("Hello, World! " + "Count: " + counter);
                node.appendChild(textnode);
                document.getElementById("demo").appendChild(node);
            }
            </script>
        </body>
    </html>
    '''
    return '''
    <html>
        <body>
            <button onclick="myFunction()">Click me</button>
            <p id="demo"></p>
            <script>
            function myFunction() {
                var node = document.createElement("P");
                var textnode = document.createTextNode("Hello, World!");
                node.appendChild(textnode);
                document.getElementById("demo").appendChild(node);
            }
            </script>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()
