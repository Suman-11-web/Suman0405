from flask import Flask, url_for

app = Flask(__name__, static_folder="static")

@app.route("/")
def home():
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Suman Portfolio</title>
    <style>
        /* --- PREMIUM LIGHT BLUE LIQUID BACKGROUND (MAIN PAGE) --- */
        body {{
            margin: 0;
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: #e0f2fe; 
            color: #1e293b; 
            overflow: hidden; 
            min-height: 100vh;
            position: relative;
        }}

        body::before, body::after {{
            content: '';
            position: absolute;
            width: 60vw;
            height: 60vw;
            border-radius: 50%;
            filter: blur(100px);
            z-index: -1;
            animation: liquid-drift 20s infinite alternate cubic-bezier(0.4, 0, 0.2, 1);
        }}

        body::before {{ background: #bae6fd; top: -20%; left: -10%; }}
        body::after {{ background: #ffffff; bottom: -10%; right: -20%; animation-delay: -10s; }}

        @keyframes liquid-drift {{
            0% {{ transform: translate(0, 0) scale(0.8); }}
            100% {{ transform: translate(15vw, 15vh) scale(1.3); }}
        }}

        /* --- 3D GRADIENT ORB PRELOADER --- */
        #preloader {{
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background: #e2e8f0; /* Soft light gray to match the screenshot vibe */
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            transition: opacity 1s ease-in-out, visibility 1s;
        }}

        .orb-container {{
            position: relative;
            width: 220px;
            height: 220px;
        }}

        .orb {{
            width: 100%;
            height: 100%;
            border-radius: 50%;
            /* Purple, magenta, and blue gradient matching the image */
            background: linear-gradient(135deg, #e879f9 0%, #a855f7 25%, #3b82f6 50%, #d946ef 80%, #fbcfe8 100%);
            background-size: 200% 200%;
            /* 3D Glass Volume: Highlights on top, shadow reflections on bottom */
            box-shadow: 
                inset 15px 15px 35px rgba(255, 255, 255, 0.9), 
                inset -15px -15px 35px rgba(255, 255, 255, 0.5),
                inset 0 0 20px rgba(168, 85, 247, 0.3),
                0 15px 40px rgba(168, 85, 247, 0.3);
            animation: gradient-flow 3s ease infinite, float-orb 3s ease-in-out infinite alternate;
            position: relative;
            overflow: hidden;
        }}

        /* The glossy, wavy reflection across the center */
        .orb::after {{
            content: '';
            position: absolute;
            top: 35%;
            left: -10%;
            width: 120%;
            height: 30%;
            background: radial-gradient(ellipse at center, rgba(255,255,255,0.8) 0%, rgba(255,255,255,0) 60%);
            border-radius: 50%;
            filter: blur(5px);
            transform: rotate(-10deg);
            mix-blend-mode: overlay;
        }}

        @keyframes gradient-flow {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}

        @keyframes float-orb {{
            0% {{ transform: translateY(-10px); }}
            100% {{ transform: translateY(10px); }}
        }}

        .loading-text {{
            margin-top: 50px;
            font-size: 1.2rem;
            font-weight: 700;
            color: #8b5cf6; /* Matching purple text */
            letter-spacing: 8px;
            text-transform: uppercase;
            text-shadow: 0 0 10px rgba(139, 92, 246, 0.4);
            animation: pulse-text 2s ease-in-out infinite;
        }}

        @keyframes pulse-text {{ 
            0%, 100% {{ opacity: 0.6; }} 
            50% {{ opacity: 1; text-shadow: 0 0 15px rgba(139, 92, 246, 0.8); }} 
        }}

        /* --- MAIN CONTENT & PHOTO PLACEMENT --- */
        #main-content {{
            opacity: 0; 
            visibility: hidden;
            transition: opacity 1.5s ease-in;
            padding: 0 0 50px 0; 
            position: relative;
            z-index: 10; 
        }}

        .full-img {{
            /* Made the photo bigger */
            width: 95%; 
            max-width: 900px;
            height: auto;
            max-height: 550px;
            object-fit: cover; 
            display: block;
            /* Moved it further down using 80px top margin */
            margin: 80px auto 40px auto;
            border-radius: 35px;
            box-shadow: 0 20px 40px rgba(2, 132, 199, 0.2);
            border: 4px solid rgba(255, 255, 255, 0.7);
        }}

        /* TRUE LIGHT FROSTED GLASS */
        .card {{
            max-width: 700px;
            margin: 0 auto;
            padding: 50px 40px;
            text-align: center;
            
            background: rgba(255, 255, 255, 0.5); 
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);
            border: 1px solid rgba(255, 255, 255, 0.8); 
            border-radius: 40px;
            box-shadow: 0 30px 60px rgba(0, 50, 100, 0.08); 
            
            transform: translateY(60px);
            transition: transform 1.2s cubic-bezier(0.2, 0.8, 0.2, 1);
            width: 90%;
        }}

        .card.show {{
            transform: translateY(0);
        }}

        h1 {{
            color: #0369a1; 
            margin-bottom: 5px;
            font-size: 2.5rem;
            letter-spacing: -1px;
        }}

        h2 {{
            color: #0ea5e9; 
            margin-top: 30px;
            margin-bottom: 15px;
            font-weight: 700;
            font-size: 1.4rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        p {{
            color: #475569; 
            line-height: 1.8;
            margin: 0;
            font-size: 1.15rem;
            font-weight: 500;
        }}

        .highlight {{
            color: #0284c7;
            font-weight: 700;
        }}
    </style>
</head>
<body>

    <div id="preloader">
        <div class="orb-container">
            <div class="orb"></div>
        </div>
        <div class="loading-text">POWERED BY SUMAN</div>
    </div>

    <div id="main-content">
        <img src="{url_for('static', filename='images/101.jpg')}" class="full-img">

        <div class="card" id="glass-card">
            <h1>Hello, I am Suman</h1>
            <p>Student | Web & Graphics Enthusiast</p>

            <h2>About Me</h2>
            <p>web and graphics beginner.</p>

            <h2>Skills</h2>
            <p>Python, HTML, CSS, Flask</p>

            <h2>Contact</h2>
            <p>Email: <span class="highlight">sumans48750@gmail.com</span></p>
        </div>
    </div>

    <script>
        window.addEventListener('load', () => {{
            setTimeout(() => {{
                const preloader = document.getElementById('preloader');
                const mainContent = document.getElementById('main-content');
                const glassCard = document.getElementById('glass-card');
                
                // Fade out the Orb loader
                preloader.style.opacity = '0';
                preloader.style.visibility = 'hidden';
                
                // Reveal main UI
                document.body.style.overflow = 'auto';
                mainContent.style.opacity = '1';
                mainContent.style.visibility = 'visible';
                
                // Trigger the glass card pop-up animation
                setTimeout(() => {{
                    glassCard.classList.add('show');
                }}, 300);
                
            }}, 2800); // Waits exactly 2.8 seconds before smoothly transitioning
        }});
    </script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)

