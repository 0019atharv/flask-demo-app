from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Flask Docker App</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background: linear-gradient(to right, #6a11cb, #2575fc);
                color: white;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            .card {
                background-color: rgba(255, 255, 255, 0.1);
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 8px 16px rgba(0,0,0,0.2);
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>✅ Hello from Dockerized Flask App by ATV How Are You!</h1>
            <p class="lead">Your Flask app is up and running inside a Docker container 🚀</p>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
