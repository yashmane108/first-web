from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Test Web</title>
    <style>
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            background-color: #f0f2f5; 
            margin: 0; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            height: 100vh; 
        }
        .card { 
            background: white; 
            padding: 3rem; 
            border-radius: 15px; 
            box-shadow: 0 10px 25px rgba(0,0,0,0.1); 
            text-align: center; 
            max-width: 500px;
        }
        h1 { color: #1a73e8; margin-bottom: 1rem; }
        p { color: #5f6368; font-size: 1.1rem; line-height: 1.6; }
        .status-badge {
            display: inline-block;
            background-color: #e6f4ea;
            color: #1e8e3e;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            margin-top: 1rem;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 Deployment Successful!</h1>
        <p>This is a simple <strong>Flask</strong> application running inside a <strong>Kubernetes</strong> cluster.</p>
        <div class="status-badge">App Status: Healthy ✅</div>
        <hr style="margin: 2rem 0; border: 0; border-top: 1px solid #eee;">
        <p style="font-size: 0.9rem;">No Database Connection Required.</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    # Running on port 80 to match your previous EKS/Docker config
    app.run(host='0.0.0.0', port=80)
