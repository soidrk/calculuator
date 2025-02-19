#!/usr/bin/env python3
"""
 Advanced Calculator Website
----------------------------------
A full-featured, web-based version of our Mega Advanced Calculator
covering topics from Arithmetic to Unit Conversions.

Author: Your Name
Date: 2025-02-17
"""

from flask import Flask, request, render_template_string, url_for
import math
import statistics

app = Flask(__name__)

# --------------------------------
# Base Template with Navigation
# --------------------------------
base_template = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title> Jameson's Calculator</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    {% raw %}
    <style>
      body { padding-bottom: 50px; }
      .navbar-brand { font-weight: bold; }
      footer { 
        position: fixed; 
        bottom: 0; 
        width: 100%; 
        height: 50px; 
        background-color: #f8f9fa; 
        text-align: center; 
        line-height: 50px; 
      }
    </style>
    {% endraw %}
  </head>
  <body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
      <div class="container-fluid">
<a class="navbar-brand" href="{{ url_for('index') }}">Jameson's Personal Calculator</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" 
          aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
<ul class="navbar-nav">
    <li class="nav-item"><a class="nav-link active" href="{{ url_for('arithmetic') }}">Arithmetic</a></li>
    <li class="nav-item"><a class="nav-link active" href="{{ url_for('algebra') }}">Algebra</a></li>
    <li class="nav-item"><a class="nav-link active" href="{{ url_for('geometry') }}">Geometry</a></li>
    <li class="nav-item"><a class="nav-link active" href="{{ url_for('trigonometry') }}">Trigonometry</a></li>
    <li class="nav-item"><a class="nav-link active" href="{{ url_for('statistics') }}">Statistics/Probability</a></li>
    <li class="nav-item"><a class="nav-link active" href="{{ url_for('calculus') }}">Calculus</a></li>
    <li class="nav-item"><a class="nav-link active" href="{{ url_for('financial') }}">Financial Math</a></li>
    <li class="nav-item"><a class="nav-link active" href="{{ url_for('conversions') }}">Unit Conversions</a></li>
</ul>
        </div>
      </div>
    </nav>
    <!-- Main Content -->
    <div class="container">
      {{ content|safe }}
    </div>
    <footer>
      &copy; 2025 jameson personal Calculator
    </footer>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>
"""



def render_page(content):
    return render_template_string(base_template, content=content)

# ---------------------------
# Index / Home Page
# ---------------------------
@app.route("/")
def index():
    content = """
    <div class="text-center">
      <h1 class="display-4">Jamesons Calculator</h1>
      <p class="lead">Welcome! Use the navigation bar to choose a topic.</p>
    </div>
    """
    return render_page(content)

# ===================================
# 1. Arithmetic Routes
# ===================================
@app.route("/arithmetic")
@app.route("/arithmetic")
def arithmetic():
    content = """
    <h2>Arithmetic Operations</h2>
    <ul>
      <li><a href="/arithmetic/basic">Basic Operations (Add, Subtract, Multiply, Divide)</a></li>
      <li><a href="/arithmetic/exponentiation">Exponentiation, Roots, & Logarithms</a></li>
      <li><a href="/arithmetic/percentage">Percentage Calculations</a></li>
      <li><a href="/arithmetic/others">Other Operations (Modulus, Floor Division, Rounding, Factorial)</a></li>
    </ul>
    """
    return render_page(content)


@app.route("/arithmetic/basic", methods=["GET", "POST"])
def arithmetic_basic():
    result = ""
    if request.method == "POST":
        try:
            op = request.form.get("operation")
            num1 = float(request.form.get("num1"))
            num2 = float(request.form.get("num2"))
            if op == "addition":
                res = num1 + num2
                result = f"{num1} + {num2} = {res}"
            elif op == "subtraction":
                res = num1 - num2
                result = f"{num1} - {num2} = {res}"
            elif op == "multiplication":
                res = num1 * num2
                result = f"{num1} * {num2} = {res}"
            elif op == "division":
                if num2 == 0:
                    result = "Error: Division by zero"
                else:
                    res = num1 / num2
                    result = f"{num1} / {num2} = {res}"
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Arithmetic - Basic Operations</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">First Number</label>
        <input type="number" step="any" class="form-control" name="num1" required>
      </div>
      <div class="mb-3">
        <label class="form-label">Second Number</label>
        <input type="number" step="any" class="form-control" name="num2" required>
      </div>
      <div class="mb-3">
        <label class="form-label">Operation</label>
        <select class="form-select" name="operation">
          <option value="addition">Addition</option>
          <option value="subtraction">Subtraction</option>
          <option value="multiplication">Multiplication</option>
          <option value="division">Division</option>
        </select>
      </div>
      <button type="submit" class="btn btn-primary">Calculate</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/arithmetic" class="btn btn-secondary">Back to Arithmetic Menu</a>
    """
    return render_page(content)

@app.route("/arithmetic/exponentiation", methods=["GET", "POST"])
def arithmetic_exponentiation():
    result = ""
    if request.method == "POST":
        op = request.form.get("operation")
        try:
            if op == "exponentiation":
                base_val = float(request.form.get("base"))
                exponent = float(request.form.get("exponent"))
                res = math.pow(base_val, exponent)
                result = f"{base_val}^{exponent} = {res}"
            elif op == "nth_root":
                num = float(request.form.get("number"))
                n = float(request.form.get("root"))
                if n == 0:
                    result = "Error: Zeroth root undefined"
                else:
                    res = math.pow(num, 1/n)
                    result = f"{n}-th root of {num} = {res}"
            elif op == "logarithm":
                a = float(request.form.get("a"))
                base_log = float(request.form.get("base_log"))
                if a <= 0 or base_log <= 0 or base_log == 1:
                    result = "Error: Invalid input for logarithm"
                else:
                    res = math.log(a, base_log)
                    result = f"log base {base_log} of {a} = {res}"
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Arithmetic - Exponentiation, Roots, & Logarithms</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Select Operation</label>
        <select class="form-select" name="operation" id="expSelect" onchange="showExpFields()">
          <option value="exponentiation">Exponentiation (a^b)</option>
          <option value="nth_root">nth Root (b-th root of a)</option>
          <option value="logarithm">Logarithm (log_b(a))</option>
        </select>
      </div>
      <div id="expFields"></div>
      <button type="submit" class="btn btn-primary">Calculate</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/arithmetic" class="btn btn-secondary">Back to Arithmetic Menu</a>
    <script>
      function showExpFields() {{
        var op = document.getElementById("expSelect").value;
        var html = "";
        if(op == "exponentiation") {{
          html += '<div class="mb-3"><label class="form-label">Base (a)</label><input type="number" step="any" class="form-control" name="base" required></div>';
          html += '<div class="mb-3"><label class="form-label">Exponent (b)</label><input type="number" step="any" class="form-control" name="exponent" required></div>';
        }} else if(op == "nth_root") {{
          html += '<div class="mb-3"><label class="form-label">Number (a)</label><input type="number" step="any" class="form-control" name="number" required></div>';
          html += '<div class="mb-3"><label class="form-label">Root Degree (n)</label><input type="number" step="any" class="form-control" name="root" required></div>';
        }} else if(op == "logarithm") {{
          html += '<div class="mb-3"><label class="form-label">Number (a)</label><input type="number" step="any" class="form-control" name="a" required></div>';
          html += '<div class="mb-3"><label class="form-label">Base (b)</label><input type="number" step="any" class="form-control" name="base_log" required></div>';
        }}
        document.getElementById("expFields").innerHTML = html;
      }}
      window.onload = showExpFields;
    </script>
    """
    return render_page(content)

@app.route("/arithmetic/percentage", methods=["GET", "POST"])
def arithmetic_percentage():
    result = ""
    if request.method == "POST":
        op = request.form.get("operation")
        try:
            if op == "percent_of":
                percent = float(request.form.get("percent"))
                number = float(request.form.get("number"))
                res = (percent / 100) * number
                result = f"{percent}% of {number} = {res}"
            elif op == "what_percent":
                part = float(request.form.get("part"))
                whole = float(request.form.get("whole"))
                if whole == 0:
                    result = "Error: Division by zero"
                else:
                    res = (part / whole) * 100
                    result = f"{part} is {res}% of {whole}"
            else:
                result = "Unknown operation."
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Arithmetic - Percentage Calculations</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Select Operation</label>
        <select class="form-select" name="operation" id="percSelect" onchange="showPercFields()">
          <option value="percent_of">What is X% of Y?</option>
          <option value="what_percent">X is what percent of Y?</option>
        </select>
      </div>
      <div id="percFields"></div>
      <button type="submit" class="btn btn-primary">Calculate</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/arithmetic" class="btn btn-secondary">Back to Arithmetic Menu</a>
    <script>
      function showPercFields() {{
        var op = document.getElementById("percSelect").value;
        var html = "";
        if(op == "percent_of") {{
          html += '<div class="mb-3"><label class="form-label">Percentage (X)</label><input type="number" step="any" class="form-control" name="percent" required></div>';
          html += '<div class="mb-3"><label class="form-label">Number (Y)</label><input type="number" step="any" class="form-control" name="number" required></div>';
        }} else if(op == "what_percent") {{
          html += '<div class="mb-3"><label class="form-label">Part (X)</label><input type="number" step="any" class="form-control" name="part" required></div>';
          html += '<div class="mb-3"><label class="form-label">Whole (Y)</label><input type="number" step="any" class="form-control" name="whole" required></div>';
        }}
        document.getElementById("percFields").innerHTML = html;
      }}
      window.onload = showPercFields;
    </script>
    """
    return render_page(content)

@app.route("/arithmetic/others", methods=["GET", "POST"])
def arithmetic_others():
    result = ""
    if request.method == "POST":
        op = request.form.get("operation")
        try:
            if op in ["modulus", "floor_division", "rounding"]:
                num1 = float(request.form.get("num1"))
                num2 = float(request.form.get("num2"))
                if op == "modulus":
                    if num2 == 0:
                        result = "Error: Division by zero"
                    else:
                        res = num1 % num2
                        result = f"{num1} % {num2} = {res}"
                elif op == "floor_division":
                    if num2 == 0:
                        result = "Error: Division by zero"
                    else:
                        res = num1 // num2
                        result = f"{num1} // {num2} = {res}"
                elif op == "rounding":
                    result = f"Rounded: {num1} -> {round(num1)}, {num2} -> {round(num2)}"
            elif op == "factorial":
                n = int(request.form.get("n"))
                if n < 0:
                    result = "Error: Factorial undefined for negative numbers"
                else:
                    res = math.factorial(n)
                    result = f"{n}! = {res}"
            else:
                result = "Unknown operation."
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Arithmetic - Other Operations</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Select Operation</label>
        <select class="form-select" name="operation" id="otherSelect" onchange="showOtherFields()">
          <option value="modulus">Modulus</option>
          <option value="floor_division">Floor Division</option>
          <option value="rounding">Rounding</option>
          <option value="factorial">Factorial</option>
        </select>
      </div>
      <div id="otherFields"></div>
      <button type="submit" class="btn btn-primary">Calculate</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/arithmetic" class="btn btn-secondary">Back to Arithmetic Menu</a>
    <script>
      function showOtherFields() {{
        var op = document.getElementById("otherSelect").value;
        var html = "";
        if(op == "modulus" || op == "floor_division" || op == "rounding") {{
          html += '<div class="mb-3"><label class="form-label">First Number</label><input type="number" step="any" class="form-control" name="num1" required></div>';
          html += '<div class="mb-3"><label class="form-label">Second Number</label><input type="number" step="any" class="form-control" name="num2" required></div>';
        }} else if(op == "factorial") {{
          html += '<div class="mb-3"><label class="form-label">Enter a non-negative integer</label><input type="number" class="form-control" name="n" required></div>';
        }}
        document.getElementById("otherFields").innerHTML = html;
      }}
      window.onload = showOtherFields;
    </script>
    """
    return render_page(content)

# ===================================
# 2. Algebra Routes
# ===================================
@app.route("/algebra")
def algebra():
    content = """
    <h2>Algebra Operations</h2>
    <ul>
      <li><a href="/algebra/linear">Solve Linear Equation (ax + b = 0)</a></li>
      <li><a href="/algebra/quadratic">Solve Quadratic Equation (ax² + bx + c = 0)</a></li>
      <li><a href="/algebra/system">Solve 2-Variable System of Equations</a></li>
    </ul>
    """
    return render_page(content)

@app.route("/algebra/linear", methods=["GET", "POST"])
def algebra_linear():
    result = ""
    if request.method == "POST":
        try:
            a = float(request.form.get("a"))
            b = float(request.form.get("b"))
            if a == 0:
                result = "No unique solution (a cannot be 0)."
            else:
                x = -b / a
                result = f"Solution: x = {x}"
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Algebra - Solve Linear Equation (ax + b = 0)</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Coefficient a</label>
        <input type="number" step="any" class="form-control" name="a" required>
      </div>
      <div class="mb-3">
        <label class="form-label">Coefficient b</label>
        <input type="number" step="any" class="form-control" name="b" required>
      </div>
      <button type="submit" class="btn btn-primary">Solve</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/algebra" class="btn btn-secondary">Back to Algebra Menu</a>
    """
    return render_page(content)

@app.route("/algebra/quadratic", methods=["GET", "POST"])
def algebra_quadratic():
    result = ""
    if request.method == "POST":
        try:
            a = float(request.form.get("a"))
            b = float(request.form.get("b"))
            c = float(request.form.get("c"))
            if a == 0:
                result = "Coefficient a cannot be 0 for a quadratic equation."
            else:
                disc = b**2 - 4*a*c
                if disc > 0:
                    x1 = (-b + math.sqrt(disc)) / (2*a)
                    x2 = (-b - math.sqrt(disc)) / (2*a)
                    result = f"Two real roots: x₁ = {x1}, x₂ = {x2}"
                elif disc == 0:
                    x = -b / (2*a)
                    result = f"One real root: x = {x}"
                else:
                    real_part = -b / (2*a)
                    imag_part = math.sqrt(-disc) / (2*a)
                    result = f"Two complex roots: x = {real_part} ± {imag_part}i"
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Algebra - Solve Quadratic Equation (ax² + bx + c = 0)</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Coefficient a</label>
        <input type="number" step="any" class="form-control" name="a" required>
      </div>
      <div class="mb-3">
        <label class="form-label">Coefficient b</label>
        <input type="number" step="any" class="form-control" name="b" required>
      </div>
      <div class="mb-3">
        <label class="form-label">Coefficient c</label>
        <input type="number" step="any" class="form-control" name="c" required>
      </div>
      <button type="submit" class="btn btn-primary">Solve</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/algebra" class="btn btn-secondary">Back to Algebra Menu</a>
    """
    return render_page(content)

@app.route("/algebra/system", methods=["GET", "POST"])
def algebra_system():
    result = ""
    if request.method == "POST":
        try:
            a1 = float(request.form.get("a1"))
            b1 = float(request.form.get("b1"))
            c1 = float(request.form.get("c1"))
            a2 = float(request.form.get("a2"))
            b2 = float(request.form.get("b2"))
            c2 = float(request.form.get("c2"))
            det = a1 * b2 - a2 * b1
            if det != 0:
                x = (c1 * b2 - c2 * b1) / det
                y = (a1 * c2 - a2 * c1) / det
                result = f"Unique solution: x = {x}, y = {y}"
            else:
                result = "No unique solution (determinant is 0)."
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Algebra - Solve 2-Variable System</h2>
    <p>Equation 1: a₁x + b₁y = c₁</p>
    <p>Equation 2: a₂x + b₂y = c₂</p>
    <form method="post">
      <div class="mb-3"><label class="form-label">a₁</label><input type="number" step="any" class="form-control" name="a1" required></div>
      <div class="mb-3"><label class="form-label">b₁</label><input type="number" step="any" class="form-control" name="b1" required></div>
      <div class="mb-3"><label class="form-label">c₁</label><input type="number" step="any" class="form-control" name="c1" required></div>
      <div class="mb-3"><label class="form-label">a₂</label><input type="number" step="any" class="form-control" name="a2" required></div>
      <div class="mb-3"><label class="form-label">b₂</label><input type="number" step="any" class="form-control" name="b2" required></div>
      <div class="mb-3"><label class="form-label">c₂</label><input type="number" step="any" class="form-control" name="c2" required></div>
      <button type="submit" class="btn btn-primary">Solve</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/algebra" class="btn btn-secondary">Back to Algebra Menu</a>
    """
    return render_page(content)

# ===================================
# 3. Geometry Routes
# ===================================
@app.route("/geometry")
def geometry():
    content = """
    <h2>Geometry Operations</h2>
    <ul>
      <li><a href="/geometry/area">Area Calculation</a></li>
      <li><a href="/geometry/perimeter">Perimeter/Circumference Calculation</a></li>
      <li><a href="/geometry/volume">Volume Calculation</a></li>
      <li><a href="/geometry/surface_area">Surface Area Calculation</a></li>
      <li><a href="/geometry/coordinate">Coordinate Geometry</a></li>
    </ul>
    """
    return render_page(content)

# Geometry - Area Calculation
@app.route("/geometry/area", methods=["GET", "POST"])
def geometry_area():
    result = ""
    if request.method == "POST":
        shape = request.form.get("shape")
        try:
            if shape == "triangle":
                base = float(request.form.get("base"))
                height = float(request.form.get("height"))
                res = 0.5 * base * height
                result = f"Area of Triangle = 0.5 * {base} * {height} = {res}"
            elif shape == "rectangle":
                length = float(request.form.get("length"))
                width = float(request.form.get("width"))
                res = length * width
                result = f"Area of Rectangle = {length} * {width} = {res}"
            elif shape == "circle":
                radius = float(request.form.get("radius"))
                res = math.pi * radius**2
                result = f"Area of Circle = π * {radius}² = {res}"
            elif shape == "trapezoid":
                a = float(request.form.get("a"))
                b = float(request.form.get("b"))
                height = float(request.form.get("height"))
                res = 0.5 * (a + b) * height
                result = f"Area of Trapezoid = 0.5 * ({a} + {b}) * {height} = {res}"
            elif shape == "parallelogram":
                base = float(request.form.get("base"))
                height = float(request.form.get("height"))
                res = base * height
                result = f"Area of Parallelogram = {base} * {height} = {res}"
            elif shape == "ellipse":
                a = float(request.form.get("a"))
                b = float(request.form.get("b"))
                res = math.pi * a * b
                result = f"Area of Ellipse = π * {a} * {b} = {res}"
            elif shape == "regular":
                n = int(request.form.get("n"))
                s = float(request.form.get("s"))
                res = (n * s**2) / (4 * math.tan(math.pi/n))
                result = f"Area of Regular Polygon = (n * s²) / (4 * tan(π/n)) = {res}"
            else:
                result = "Unknown shape."
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Geometry - Area Calculation</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Select Shape</label>
        <select class="form-select" name="shape" id="areaShape" onchange="showAreaFields()">
          <option value="triangle">Triangle</option>
          <option value="rectangle">Rectangle</option>
          <option value="circle">Circle</option>
          <option value="trapezoid">Trapezoid</option>
          <option value="parallelogram">Parallelogram</option>
          <option value="ellipse">Ellipse</option>
          <option value="regular">Regular Polygon</option>
        </select>
      </div>
      <div id="areaFields"></div>
      <button type="submit" class="btn btn-primary">Calculate</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/geometry" class="btn btn-secondary">Back to Geometry Menu</a>
    <script>
      function showAreaFields() {{
        var shape = document.getElementById("areaShape").value;
        var html = "";
        if(shape == "triangle") {{
          html += '<div class="mb-3"><label class="form-label">Base</label><input type="number" step="any" class="form-control" name="base" required></div>';
          html += '<div class="mb-3"><label class="form-label">Height</label><input type="number" step="any" class="form-control" name="height" required></div>';
        }} else if(shape == "rectangle") {{
          html += '<div class="mb-3"><label class="form-label">Length</label><input type="number" step="any" class="form-control" name="length" required></div>';
          html += '<div class="mb-3"><label class="form-label">Width</label><input type="number" step="any" class="form-control" name="width" required></div>';
        }} else if(shape == "circle") {{
          html += '<div class="mb-3"><label class="form-label">Radius</label><input type="number" step="any" class="form-control" name="radius" required></div>';
        }} else if(shape == "trapezoid") {{
          html += '<div class="mb-3"><label class="form-label">Side a</label><input type="number" step="any" class="form-control" name="a" required></div>';
          html += '<div class="mb-3"><label class="form-label">Side b</label><input type="number" step="any" class="form-control" name="b" required></div>';
          html += '<div class="mb-3"><label class="form-label">Height</label><input type="number" step="any" class="form-control" name="height" required></div>';
        }} else if(shape == "parallelogram") {{
          html += '<div class="mb-3"><label class="form-label">Base</label><input type="number" step="any" class="form-control" name="base" required></div>';
          html += '<div class="mb-3"><label class="form-label">Height</label><input type="number" step="any" class="form-control" name="height" required></div>';
        }} else if(shape == "ellipse") {{
          html += '<div class="mb-3"><label class="form-label">Semi-major axis (a)</label><input type="number" step="any" class="form-control" name="a" required></div>';
          html += '<div class="mb-3"><label class="form-label">Semi-minor axis (b)</label><input type="number" step="any" class="form-control" name="b" required></div>';
        }} else if(shape == "regular") {{
          html += '<div class="mb-3"><label class="form-label">Number of sides (n)</label><input type="number" class="form-control" name="n" required></div>';
          html += '<div class="mb-3"><label class="form-label">Side length (s)</label><input type="number" step="any" class="form-control" name="s" required></div>';
        }}
        document.getElementById("areaFields").innerHTML = html;
      }}
      window.onload = showAreaFields;
    </script>
    """
    return render_page(content)

# Geometry - Perimeter/Circumference Calculation
@app.route("/geometry/perimeter", methods=["GET", "POST"])
def geometry_perimeter():
    result = ""
    if request.method == "POST":
        shape = request.form.get("shape")
        try:
            if shape == "triangle":
                a = float(request.form.get("a"))
                b = float(request.form.get("b"))
                c = float(request.form.get("c"))
                res = a + b + c
                result = f"Perimeter of Triangle = {a} + {b} + {c} = {res}"
            elif shape == "rectangle":
                l = float(request.form.get("length"))
                w = float(request.form.get("width"))
                res = 2 * (l + w)
                result = f"Perimeter of Rectangle = 2 * ({l} + {w}) = {res}"
            elif shape == "circle":
                r = float(request.form.get("radius"))
                res = 2 * math.pi * r
                result = f"Circumference of Circle = 2π * {r} = {res}"
            elif shape == "trapezoid":
                a = float(request.form.get("a"))
                b = float(request.form.get("b"))
                c = float(request.form.get("c"))
                d = float(request.form.get("d"))
                res = a + b + c + d
                result = f"Perimeter of Trapezoid = {a} + {b} + {c} + {d} = {res}"
            elif shape == "regular":
                n = int(request.form.get("n"))
                s = float(request.form.get("s"))
                res = n * s
                result = f"Perimeter of Regular Polygon = {n} * {s} = {res}"
            else:
                result = "Unknown shape."
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Geometry - Perimeter/Circumference Calculation</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Select Shape</label>
        <select class="form-select" name="shape" id="perimShape" onchange="showPerimFields()">
          <option value="triangle">Triangle</option>
          <option value="rectangle">Rectangle</option>
          <option value="circle">Circle</option>
          <option value="trapezoid">Trapezoid</option>
          <option value="regular">Regular Polygon</option>
        </select>
      </div>
      <div id="perimFields"></div>
      <button type="submit" class="btn btn-primary">Calculate</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/geometry" class="btn btn-secondary">Back to Geometry Menu</a>
    <script>
      function showPerimFields() {{
        var shape = document.getElementById("perimShape").value;
        var html = "";
        if(shape == "triangle") {{
          html += '<div class="mb-3"><label class="form-label">Side a</label><input type="number" step="any" class="form-control" name="a" required></div>';
          html += '<div class="mb-3"><label class="form-label">Side b</label><input type="number" step="any" class="form-control" name="b" required></div>';
          html += '<div class="mb-3"><label class="form-label">Side c</label><input type="number" step="any" class="form-control" name="c" required></div>';
        }} else if(shape == "rectangle") {{
          html += '<div class="mb-3"><label class="form-label">Length</label><input type="number" step="any" class="form-control" name="length" required></div>';
          html += '<div class="mb-3"><label class="form-label">Width</label><input type="number" step="any" class="form-control" name="width" required></div>';
        }} else if(shape == "circle") {{
          html += '<div class="mb-3"><label class="form-label">Radius</label><input type="number" step="any" class="form-control" name="radius" required></div>';
        }} else if(shape == "trapezoid") {{
          html += '<div class="mb-3"><label class="form-label">Side a</label><input type="number" step="any" class="form-control" name="a" required></div>';
          html += '<div class="mb-3"><label class="form-label">Side b</label><input type="number" step="any" class="form-control" name="b" required></div>';
          html += '<div class="mb-3"><label class="form-label">Side c</label><input type="number" step="any" class="form-control" name="c" required></div>';
          html += '<div class="mb-3"><label class="form-label">Side d</label><input type="number" step="any" class="form-control" name="d" required></div>';
        }} else if(shape == "regular") {{
          html += '<div class="mb-3"><label class="form-label">Number of sides (n)</label><input type="number" class="form-control" name="n" required></div>';
          html += '<div class="mb-3"><label class="form-label">Side length (s)</label><input type="number" step="any" class="form-control" name="s" required></div>';
        }}
        document.getElementById("perimFields").innerHTML = html;
      }}
      window.onload = showPerimFields;
    </script>
    """
    return render_page(content)

# Geometry - Volume Calculation
@app.route("/geometry/volume", methods=["GET", "POST"])
def geometry_volume():
    result = ""
    if request.method == "POST":
        shape = request.form.get("shape")
        try:
            if shape == "cube":
                s = float(request.form.get("s"))
                res = s**3
                result = f"Volume of Cube = {s}³ = {res}"
            elif shape == "prism":
                l = float(request.form.get("l"))
                w = float(request.form.get("w"))
                h = float(request.form.get("h"))
                res = l * w * h
                result = f"Volume of Rectangular Prism = {l} * {w} * {h} = {res}"
            elif shape == "cylinder":
                r = float(request.form.get("r"))
                h = float(request.form.get("h"))
                res = math.pi * r**2 * h
                result = f"Volume of Cylinder = π * {r}² * {h} = {res}"
            elif shape == "sphere":
                r = float(request.form.get("r"))
                res = (4/3) * math.pi * r**3
                result = f"Volume of Sphere = (4/3)π * {r}³ = {res}"
            elif shape == "cone":
                r = float(request.form.get("r"))
                h = float(request.form.get("h"))
                res = (1/3) * math.pi * r**2 * h
                result = f"Volume of Cone = (1/3)π * {r}² * {h} = {res}"
            elif shape == "pyramid":
                base_area = float(request.form.get("base_area"))
                h = float(request.form.get("h"))
                res = (1/3) * base_area * h
                result = f"Volume of Pyramid = (1/3) * {base_area} * {h} = {res}"
            else:
                result = "Unknown solid."
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Geometry - Volume Calculation</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Select Solid</label>
        <select class="form-select" name="shape" id="volShape" onchange="showVolFields()">
          <option value="cube">Cube</option>
          <option value="prism">Rectangular Prism</option>
          <option value="cylinder">Cylinder</option>
          <option value="sphere">Sphere</option>
          <option value="cone">Cone</option>
          <option value="pyramid">Pyramid</option>
        </select>
      </div>
      <div id="volFields"></div>
      <button type="submit" class="btn btn-primary">Calculate</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/geometry" class="btn btn-secondary">Back to Geometry Menu</a>
    <script>
      function showVolFields() {{
        var shape = document.getElementById("volShape").value;
        var html = "";
        if(shape == "cube") {{
          html += '<div class="mb-3"><label class="form-label">Side length (s)</label><input type="number" step="any" class="form-control" name="s" required></div>';
        }} else if(shape == "prism") {{
          html += '<div class="mb-3"><label class="form-label">Length (l)</label><input type="number" step="any" class="form-control" name="l" required></div>';
          html += '<div class="mb-3"><label class="form-label">Width (w)</label><input type="number" step="any" class="form-control" name="w" required></div>';
          html += '<div class="mb-3"><label class="form-label">Height (h)</label><input type="number" step="any" class="form-control" name="h" required></div>';
        }} else if(shape == "cylinder") {{
          html += '<div class="mb-3"><label class="form-label">Radius (r)</label><input type="number" step="any" class="form-control" name="r" required></div>';
          html += '<div class="mb-3"><label class="form-label">Height (h)</label><input type="number" step="any" class="form-control" name="h" required></div>';
        }} else if(shape == "sphere") {{
          html += '<div class="mb-3"><label class="form-label">Radius (r)</label><input type="number" step="any" class="form-control" name="r" required></div>';
        }} else if(shape == "cone") {{
          html += '<div class="mb-3"><label class="form-label">Radius (r)</label><input type="number" step="any" class="form-control" name="r" required></div>';
          html += '<div class="mb-3"><label class="form-label">Height (h)</label><input type="number" step="any" class="form-control" name="h" required></div>';
        }} else if(shape == "pyramid") {{
          html += '<div class="mb-3"><label class="form-label">Base Area</label><input type="number" step="any" class="form-control" name="base_area" required></div>';
          html += '<div class="mb-3"><label class="form-label">Height (h)</label><input type="number" step="any" class="form-control" name="h" required></div>';
        }}
        document.getElementById("volFields").innerHTML = html;
      }}
      window.onload = showVolFields;
    </script>
    """
    return render_page(content)

# Geometry - Surface Area Calculation
@app.route("/geometry/surface_area", methods=["GET", "POST"])
def geometry_surface_area():
    result = ""
    if request.method == "POST":
        shape = request.form.get("shape")
        try:
            if shape == "cube":
                s = float(request.form.get("s"))
                res = 6 * s**2
                result = f"Surface Area of Cube = 6 * {s}² = {res}"
            elif shape == "prism":
                l = float(request.form.get("l"))
                w = float(request.form.get("w"))
                h = float(request.form.get("h"))
                res = 2*(l*w + l*h + w*h)
                result = f"Surface Area of Rectangular Prism = 2*(lw+lh+wh) = {res}"
            elif shape == "cylinder":
                r = float(request.form.get("r"))
                h = float(request.form.get("h"))
                res = 2 * math.pi * r * (r + h)
                result = f"Surface Area of Cylinder = 2πr(r+h) = {res}"
            elif shape == "sphere":
                r = float(request.form.get("r"))
                res = 4 * math.pi * r**2
                result = f"Surface Area of Sphere = 4πr² = {res}"
            elif shape == "cone":
                r = float(request.form.get("r"))
                h = float(request.form.get("h"))
                l = math.sqrt(r**2 + h**2)
                res = math.pi * r * (r + l)
                result = f"Surface Area of Cone = πr(r+l) where l = √(r²+h²) = {res}"
            else:
                result = "Unknown solid."
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Geometry - Surface Area Calculation</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Select Solid</label>
        <select class="form-select" name="shape" id="saShape" onchange="showSAFields()">
          <option value="cube">Cube</option>
          <option value="prism">Rectangular Prism</option>
          <option value="cylinder">Cylinder</option>
          <option value="sphere">Sphere</option>
          <option value="cone">Cone</option>
        </select>
      </div>
      <div id="saFields"></div>
      <button type="submit" class="btn btn-primary">Calculate</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/geometry" class="btn btn-secondary">Back to Geometry Menu</a>
    <script>
      function showSAFields() {{
        var shape = document.getElementById("saShape").value;
        var html = "";
        if(shape == "cube") {{
          html += '<div class="mb-3"><label class="form-label">Side length (s)</label><input type="number" step="any" class="form-control" name="s" required></div>';
        }} else if(shape == "prism") {{
          html += '<div class="mb-3"><label class="form-label">Length (l)</label><input type="number" step="any" class="form-control" name="l" required></div>';
          html += '<div class="mb-3"><label class="form-label">Width (w)</label><input type="number" step="any" class="form-control" name="w" required></div>';
          html += '<div class="mb-3"><label class="form-label">Height (h)</label><input type="number" step="any" class="form-control" name="h" required></div>';
        }} else if(shape == "cylinder") {{
          html += '<div class="mb-3"><label class="form-label">Radius (r)</label><input type="number" step="any" class="form-control" name="r" required></div>';
          html += '<div class="mb-3"><label class="form-label">Height (h)</label><input type="number" step="any" class="form-control" name="h" required></div>';
        }} else if(shape == "sphere") {{
          html += '<div class="mb-3"><label class="form-label">Radius (r)</label><input type="number" step="any" class="form-control" name="r" required></div>';
        }} else if(shape == "cone") {{
          html += '<div class="mb-3"><label class="form-label">Radius (r)</label><input type="number" step="any" class="form-control" name="r" required></div>';
          html += '<div class="mb-3"><label class="form-label">Height (h)</label><input type="number" step="any" class="form-control" name="h" required></div>';
        }}
        document.getElementById("saFields").innerHTML = html;
      }}
      window.onload = showSAFields;
    </script>
    """
    return render_page(content)

# Geometry - Coordinate Geometry
@app.route("/geometry/coordinate", methods=["GET", "POST"])
def geometry_coordinate():
    result = ""
    if request.method == "POST":
        op = request.form.get("operation")
        try:
            x1 = float(request.form.get("x1"))
            y1 = float(request.form.get("y1"))
            x2 = float(request.form.get("x2"))
            y2 = float(request.form.get("y2"))
            if op == "distance":
                res = math.sqrt((x2-x1)**2 + (y2-y1)**2)
                result = f"Distance = √(({x2}-{x1})² + ({y2}-{y1})²) = {res}"
            elif op == "slope_midpoint":
                if x2 - x1 == 0:
                    slope = "undefined (vertical line)"
                else:
                    slope = (y2 - y1) / (x2 - x1)
                midpoint = ((x1+x2)/2, (y1+y2)/2)
                result = f"Slope = {slope}, Midpoint = {midpoint}"
            elif op == "line_equation":
                if x2 - x1 == 0:
                    result = f"Line is vertical: x = {x1}"
                else:
                    m = (y2-y1)/(x2-x1)
                    b = y1 - m*x1
                    result = f"Line equation: y = {m}x + {b}"
            else:
                result = "Unknown operation."
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Geometry - Coordinate Geometry</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Select Operation</label>
        <select class="form-select" name="operation">
          <option value="distance">Distance between two points</option>
          <option value="slope_midpoint">Slope and Midpoint</option>
          <option value="line_equation">Equation of a line</option>
        </select>
      </div>
      <div class="mb-3">
        <label class="form-label">Point 1 (x1, y1)</label>
        <input type="number" step="any" class="form-control" name="x1" placeholder="x1" required>
        <input type="number" step="any" class="form-control mt-1" name="y1" placeholder="y1" required>
      </div>
      <div class="mb-3">
        <label class="form-label">Point 2 (x2, y2)</label>
        <input type="number" step="any" class="form-control" name="x2" placeholder="x2" required>
        <input type="number" step="any" class="form-control mt-1" name="y2" placeholder="y2" required>
      </div>
      <button type="submit" class="btn btn-primary">Calculate</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/geometry" class="btn btn-secondary">Back to Geometry Menu</a>
    """
    return render_page(content)

# ===================================
# 4. Trigonometry Routes
# ===================================
@app.route("/trigonometry")
def trigonometry():
    content = """
    <h2>Trigonometry Operations</h2>
    <ul>
      <li><a href="/trigonometry/basic">Basic Trigonometric Functions</a></li>
      <li><a href="/trigonometry/inverse">Inverse Trigonometric Functions</a></li>
      <li><a href="/trigonometry/angle">Angle Conversion (Degrees ↔ Radians)</a></li>
      <li><a href="/trigonometry/right">Solve Right Triangle</a></li>
      <li><a href="/trigonometry/oblique">Solve Oblique Triangle (Law of Sines/Cosines)</a></li>
    </ul>
    """
    return render_page(content)

@app.route("/trigonometry/basic", methods=["GET", "POST"])
def trigonometry_basic():
    result = ""
    if request.method == "POST":
        try:
            func = request.form.get("function")
            angle = float(request.form.get("angle"))
            rad = math.radians(angle)
            if func == "sin":
                res = math.sin(rad)
                result = f"sin({angle}°) = {res}"
            elif func == "cos":
                res = math.cos(rad)
                result = f"cos({angle}°) = {res}"
            elif func == "tan":
                res = math.tan(rad)
                result = f"tan({angle}°) = {res}"
            else:
                result = "Unknown function."
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Trigonometry - Basic Functions</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Select Function</label>
        <select class="form-select" name="function">
          <option value="sin">Sine</option>
          <option value="cos">Cosine</option>
          <option value="tan">Tangent</option>
        </select>
      </div>
      <div class="mb-3">
        <label class="form-label">Angle (in degrees)</label>
        <input type="number" step="any" class="form-control" name="angle" required>
      </div>
      <button type="submit" class="btn btn-primary">Calculate</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/trigonometry" class="btn btn-secondary">Back to Trigonometry Menu</a>
    """
    return render_page(content)

@app.route("/trigonometry/inverse", methods=["GET", "POST"])
def trigonometry_inverse():
    result = ""
    if request.method == "POST":
        try:
            func = request.form.get("function")
            value = float(request.form.get("value"))
            if func in ["arcsin", "arccos"] and (value < -1 or value > 1):
                result = f"Error: {func} is defined for values between -1 and 1."
            else:
                if func == "arcsin":
                    res = math.degrees(math.asin(value))
                    result = f"arcsin({value}) = {res}°"
                elif func == "arccos":
                    res = math.degrees(math.acos(value))
                    result = f"arccos({value}) = {res}°"
                elif func == "arctan":
                    res = math.degrees(math.atan(value))
                    result = f"arctan({value}) = {res}°"
                else:
                    result = "Unknown function."
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Trigonometry - Inverse Functions</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Select Function</label>
        <select class="form-select" name="function">
          <option value="arcsin">arcsin</option>
          <option value="arccos">arccos</option>
          <option value="arctan">arctan</option>
        </select>
      </div>
      <div class="mb-3">
        <label class="form-label">Value</label>
        <input type="number" step="any" class="form-control" name="value" required>
      </div>
      <button type="submit" class="btn btn-primary">Calculate</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/trigonometry" class="btn btn-secondary">Back to Trigonometry Menu</a>
    """
    return render_page(content)

@app.route("/trigonometry/angle", methods=["GET", "POST"])
def trigonometry_angle():
    result = ""
    if request.method == "POST":
        try:
            conv = request.form.get("conversion")
            value = float(request.form.get("value"))
            if conv == "to_radians":
                res = math.radians(value)
                result = f"{value}° = {res} radians"
            elif conv == "to_degrees":
                res = math.degrees(value)
                result = f"{value} radians = {res}°"
            else:
                result = "Unknown conversion."
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Trigonometry - Angle Conversion</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Select Conversion</label>
        <select class="form-select" name="conversion">
          <option value="to_radians">Degrees to Radians</option>
          <option value="to_degrees">Radians to Degrees</option>
        </select>
      </div>
      <div class="mb-3">
        <label class="form-label">Value</label>
        <input type="number" step="any" class="form-control" name="value" required>
      </div>
      <button type="submit" class="btn btn-primary">Convert</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/trigonometry" class="btn btn-secondary">Back to Trigonometry Menu</a>
    """
    return render_page(content)

@app.route("/trigonometry/right", methods=["GET", "POST"])
def trigonometry_right():
    result = ""
    if request.method == "POST":
        try:
            angle = float(request.form.get("angle"))
            hypotenuse = float(request.form.get("hypotenuse"))
            if angle <= 0 or angle >= 90:
                result = "Error: Angle must be between 0 and 90°."
            else:
                rad = math.radians(angle)
                opp = hypotenuse * math.sin(rad)
                adj = hypotenuse * math.cos(rad)
                result = f"For angle {angle}° and hypotenuse {hypotenuse}: Opposite = {opp}, Adjacent = {adj}"
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Trigonometry - Solve Right Triangle</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Acute Angle (°)</label>
        <input type="number" step="any" class="form-control" name="angle" required>
      </div>
      <div class="mb-3">
        <label class="form-label">Hypotenuse</label>
        <input type="number" step="any" class="form-control" name="hypotenuse" required>
      </div>
      <button type="submit" class="btn btn-primary">Solve</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/trigonometry" class="btn btn-secondary">Back to Trigonometry Menu</a>
    """
    return render_page(content)

@app.route("/trigonometry/oblique", methods=["GET", "POST"])
def trigonometry_oblique():
    result = ""
    if request.method == "POST":
        method = request.form.get("method")
        try:
            if method == "law_of_sines":
                # We'll require one known side-angle pair and one known angle for the unknown
                known_side = float(request.form.get("known_side"))
                known_angle = float(request.form.get("known_angle"))
                unknown_angle = float(request.form.get("unknown_angle"))
                # Compute missing side using law of sines: side/sin(angle) = known_side/sin(known_angle)
                unknown_side = known_side * math.sin(math.radians(unknown_angle)) / math.sin(math.radians(known_angle))
                result = f"Using Law of Sines: Unknown side = {unknown_side}"
            elif method == "law_of_cosines":
                # Option 1: find side given two sides and included angle
                side1 = float(request.form.get("side1"))
                side2 = float(request.form.get("side2"))
                angle_included = float(request.form.get("angle_included"))
                unknown_side = math.sqrt(side1**2 + side2**2 - 2*side1*side2*math.cos(math.radians(angle_included)))
                result = f"Using Law of Cosines: Unknown side = {unknown_side}"
            else:
                result = "Unknown method."
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Trigonometry - Solve Oblique Triangle</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Select Method</label>
        <select class="form-select" name="method" id="obliqueSelect" onchange="showObliqueFields()">
          <option value="law_of_sines">Law of Sines</option>
          <option value="law_of_cosines">Law of Cosines (find side)</option>
        </select>
      </div>
      <div id="obliqueFields"></div>
      <button type="submit" class="btn btn-primary">Solve</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/trigonometry" class="btn btn-secondary">Back to Trigonometry Menu</a>
    <script>
      function showObliqueFields() {{
        var method = document.getElementById("obliqueSelect").value;
        var html = "";
        if(method == "law_of_sines") {{
          html += '<div class="mb-3"><label class="form-label">Known side</label><input type="number" step="any" class="form-control" name="known_side" required></div>';
          html += '<div class="mb-3"><label class="form-label">Known angle (°)</label><input type="number" step="any" class="form-control" name="known_angle" required></div>';
          html += '<div class="mb-3"><label class="form-label">Unknown angle (°)</label><input type="number" step="any" class="form-control" name="unknown_angle" required></div>';
        }} else if(method == "law_of_cosines") {{
          html += '<div class="mb-3"><label class="form-label">Side 1</label><input type="number" step="any" class="form-control" name="side1" required></div>';
          html += '<div class="mb-3"><label class="form-label">Side 2</label><input type="number" step="any" class="form-control" name="side2" required></div>';
          html += '<div class="mb-3"><label class="form-label">Included Angle (°)</label><input type="number" step="any" class="form-control" name="angle_included" required></div>';
        }}
        document.getElementById("obliqueFields").innerHTML = html;
      }}
      window.onload = showObliqueFields;
    </script>
    """
    return render_page(content)

# ===================================
# 5. Statistics/Probability Routes
# ===================================
@app.route("/statistics")
def statistics():
    content = """
    <h2>Statistics/Probability Operations</h2>
    <ul>
      <li><a href="/statistics/central">Central Tendencies (Mean, Median, Mode)</a></li>
      <li><a href="/statistics/dispersion">Variance & Standard Deviation</a></li>
      <li><a href="/statistics/range">Range and Quartiles</a></li>
      <li><a href="/statistics/combinatorics">Permutations & Combinations</a></li>
      <li><a href="/statistics/probability">Basic Probability</a></li>
    </ul>
    """
    return render_page(content)


@app.route("/statistics/central", methods=["GET", "POST"])
def stats_central():
    result = ""
    if request.method == "POST":
        try:
            data = [float(x) for x in request.form.get("data").split(",") if x.strip() != ""]
            mean_val = statistics.mean(data)
            median_val = statistics.median(data)
            modes = statistics.multimode(data)
            if len(modes) == 1:
                mode_str = f"{modes[0]}"
            else:
                mode_str = ", ".join(map(str, modes)) + " (multiple modes)"
            result = f"Data: {data}<br>Mean = {mean_val}<br>Median = {median_val}<br>Mode = {mode_str}"
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Statistics - Central Tendencies</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Enter numbers (comma-separated)</label>
        <input type="text" class="form-control" name="data" placeholder="e.g., 1,2,3,4,5" required>
      </div>
      <button type="submit" class="btn btn-primary">Calculate</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/statistics" class="btn btn-secondary">Back to Statistics Menu</a>
    """
    return render_page(content)

@app.route("/statistics/dispersion", methods=["GET", "POST"])
def stats_dispersion():
    result = ""
    if request.method == "POST":
        try:
            data = [float(x) for x in request.form.get("data").split(",") if x.strip() != ""]
            if len(data) < 2:
                result = "At least two numbers are required."
            else:
                var_val = statistics.variance(data)
                stdev_val = statistics.stdev(data)
                result = f"Data: {data}<br>Variance = {var_val}<br>Standard Deviation = {stdev_val}"
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Statistics - Variance & Standard Deviation</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Enter numbers (comma-separated)</label>
        <input type="text" class="form-control" name="data" placeholder="e.g., 1,2,3,4,5" required>
      </div>
      <button type="submit" class="btn btn-primary">Calculate</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/statistics" class="btn btn-secondary">Back to Statistics Menu</a>
    """
    return render_page(content)

@app.route("/statistics/range", methods=["GET", "POST"])
def stats_range():
    result = ""
    if request.method == "POST":
        try:
            data = sorted([float(x) for x in request.form.get("data").split(",") if x.strip() != ""])
            if not data:
                result = "No data provided."
            else:
                range_val = data[-1] - data[0]
                median_val = statistics.median(data)
                mid = len(data) // 2
                lower = data[:mid] if len(data)%2==0 else data[:mid]
                upper = data[mid+1:] if len(data)%2==1 else data[mid:]
                Q1 = statistics.median(lower) if lower else None
                Q3 = statistics.median(upper) if upper else None
                result = f"Data: {data}<br>Range = {range_val}<br>Median = {median_val}<br>Q1 = {Q1}, Q3 = {Q3}"
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Statistics - Range and Quartiles</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Enter numbers (comma-separated)</label>
        <input type="text" class="form-control" name="data" placeholder="e.g., 1,2,3,4,5,6,7" required>
      </div>
      <button type="submit" class="btn btn-primary">Calculate</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/statistics" class="btn btn-secondary">Back to Statistics Menu</a>
    """
    return render_page(content)

@app.route("/statistics/combinatorics", methods=["GET", "POST"])
def stats_combinatorics():
    result = ""
    if request.method == "POST":
        try:
            n = int(request.form.get("n"))
            r = int(request.form.get("r"))
            if r > n or n < 0 or r < 0:
                result = "Invalid values. Ensure 0 <= r <= n."
            else:
                perm = math.factorial(n) // math.factorial(n - r)
                comb = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
                result = f"nPr = {perm}<br>nCr = {comb}"
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Statistics - Permutations & Combinations</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">n (total items)</label>
        <input type="number" class="form-control" name="n" required>
      </div>
      <div class="mb-3">
        <label class="form-label">r (items to choose)</label>
        <input type="number" class="form-control" name="r" required>
      </div>
      <button type="submit" class="btn btn-primary">Calculate</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/statistics" class="btn btn-secondary">Back to Statistics Menu</a>
    """
    return render_page(content)

@app.route("/statistics/probability", methods=["GET", "POST"])
def stats_probability():
    result = ""
    if request.method == "POST":
        try:
            favorable = float(request.form.get("favorable"))
            total = float(request.form.get("total"))
            if total == 0:
                result = "Error: Total outcomes cannot be zero."
            else:
                prob = favorable / total
                result = f"Probability = {favorable} / {total} = {prob} ({prob*100}%)"
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Statistics - Basic Probability</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Favorable outcomes</label>
        <input type="number" step="any" class="form-control" name="favorable" required>
      </div>
      <div class="mb-3">
        <label class="form-label">Total outcomes</label>
        <input type="number" step="any" class="form-control" name="total" required>
      </div>
      <button type="submit" class="btn btn-primary">Calculate</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/statistics" class="btn btn-secondary">Back to Statistics Menu</a>
    """
    return render_page(content)

# ===================================
# 6. Calculus Routes
# ===================================
@app.route("/calculus")
def calculus():
    content = """
    <h2>Calculus Operations</h2>
    <ul>
      <li><a href="/calculus/derivative">Derivative of a Polynomial at a Point</a></li>
      <li><a href="/calculus/indefinite">Indefinite Integral of a Polynomial</a></li>
      <li><a href="/calculus/definite">Definite Integral of a Polynomial</a></li>
    </ul>
    """
    return render_page(content)

@app.route("/calculus/derivative", methods=["GET", "POST"])
def calc_derivative():
    result = ""
    if request.method == "POST":
        try:
            degree = int(request.form.get("degree"))
            coeffs = []
            for i in range(degree, -1, -1):
                coeffs.append(float(request.form.get(f"coeff_{i}")))
            x_val = float(request.form.get("x_val"))
            # Derivative: multiply coefficient by its exponent
            deriv = 0
            for i in range(degree, 0, -1):
                deriv += coeffs[degree - i] * i * (x_val ** (i-1))
            result = f"The derivative at x = {x_val} is {deriv}"
        except Exception as e:
            result = "Error: " + str(e)
    # Generate fields dynamically based on degree using JavaScript
    content = f"""
    <h2>Calculus - Derivative at a Point</h2>
    <form method="post" id="derivForm">
      <div class="mb-3">
        <label class="form-label">Degree of Polynomial</label>
        <input type="number" class="form-control" id="degree" name="degree" required>
      </div>
      <div id="coeffFields"></div>
      <div class="mb-3">
        <label class="form-label">Evaluate derivative at x = </label>
        <input type="number" step="any" class="form-control" name="x_val" required>
      </div>
      <button type="submit" class="btn btn-primary">Calculate Derivative</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/calculus" class="btn btn-secondary">Back to Calculus Menu</a>
    <script>
      document.getElementById("degree").addEventListener("change", function() {{
          var deg = parseInt(this.value);
          var html = "";
          for(var i = deg; i >= 0; i--) {{
              html += '<div class="mb-3"><label class="form-label">Coefficient for x^' + i + '</label><input type="number" step="any" class="form-control" name="coeff_' + i + '" required></div>';
          }}
          document.getElementById("coeffFields").innerHTML = html;
      }});
    </script>
    """
    return render_page(content)

@app.route("/calculus/indefinite", methods=["GET", "POST"])
def calc_indefinite():
    result = ""
    if request.method == "POST":
        try:
            degree = int(request.form.get("degree"))
            coeffs = []
            for i in range(degree, -1, -1):
                coeffs.append(float(request.form.get(f"coeff_{i}")))
            # Compute antiderivative: new coefficient = coeff / (power+1)
            terms = []
            for i in range(degree, -1, -1):
                new_coeff = coeffs[degree - i] / (i+1)
                if i+1 == 0:
                    term = f"{new_coeff:.3f}"
                elif i+1 == 1:
                    term = f"{new_coeff:.3f}x"
                else:
                    term = f"{new_coeff:.3f}x^{i+1}"
                terms.append(term)
            result = " + ".join(terms) + " + C"
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Calculus - Indefinite Integral</h2>
    <form method="post" id="indefForm">
      <div class="mb-3">
        <label class="form-label">Degree of Polynomial</label>
        <input type="number" class="form-control" id="degIndef" name="degree" required>
      </div>
      <div id="coeffIndef"></div>
      <button type="submit" class="btn btn-primary">Calculate Indefinite Integral</button>
    </form>
    <br><h4>Antiderivative:</h4><p>{result}</p>
    <a href="/calculus" class="btn btn-secondary">Back to Calculus Menu</a>
    <script>
      document.getElementById("degIndef").addEventListener("change", function() {{
          var deg = parseInt(this.value);
          var html = "";
          for(var i = deg; i >= 0; i--) {{
              html += '<div class="mb-3"><label class="form-label">Coefficient for x^' + i + '</label><input type="number" step="any" class="form-control" name="coeff_' + i + '" required></div>';
          }}
          document.getElementById("coeffIndef").innerHTML = html;
      }});
    </script>
    """
    return render_page(content)

@app.route("/calculus/definite", methods=["GET", "POST"])
def calc_definite():
    result = ""
    if request.method == "POST":
        try:
            degree = int(request.form.get("degree"))
            coeffs = []
            for i in range(degree, -1, -1):
                coeffs.append(float(request.form.get(f"coeff_{i}")))
            lower = float(request.form.get("lower"))
            upper = float(request.form.get("upper"))
            def poly_integral(x):
                total = 0
                for i in range(degree, -1, -1):
                    total += coeffs[degree - i] * (x ** (i+1)) / (i+1)
                return total
            res = poly_integral(upper) - poly_integral(lower)
            result = f"Definite Integral from {lower} to {upper} is {res}"
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Calculus - Definite Integral</h2>
    <form method="post" id="defForm">
      <div class="mb-3">
        <label class="form-label">Degree of Polynomial</label>
        <input type="number" class="form-control" id="degDef" name="degree" required>
      </div>
      <div id="coeffDef"></div>
      <div class="mb-3">
        <label class="form-label">Lower Limit</label>
        <input type="number" step="any" class="form-control" name="lower" required>
      </div>
      <div class="mb-3">
        <label class="form-label">Upper Limit</label>
        <input type="number" step="any" class="form-control" name="upper" required>
      </div>
      <button type="submit" class="btn btn-primary">Calculate Definite Integral</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/calculus" class="btn btn-secondary">Back to Calculus Menu</a>
    <script>
      document.getElementById("degDef").addEventListener("change", function() {{
          var deg = parseInt(this.value);
          var html = "";
          for(var i = deg; i >= 0; i--) {{
              html += '<div class="mb-3"><label class="form-label">Coefficient for x^' + i + '</label><input type="number" step="any" class="form-control" name="coeff_' + i + '" required></div>';
          }}
          document.getElementById("coeffDef").innerHTML = html;
      }});
    </script>
    """
    return render_page(content)

# ===================================
# 7. Financial Math Routes
# ===================================
@app.route("/financial")
def financial():
    content = """
    <h2>Financial Math Operations</h2>
    <ul>
      <li><a href="/financial/simple">Simple Interest</a></li>
      <li><a href="/financial/compound">Compound Interest</a></li>
      <li><a href="/financial/loan">Loan Payment Calculation</a></li>
    </ul>
    """
    return render_page(content)

@app.route("/financial/simple", methods=["GET", "POST"])
def financial_simple():
    result = ""
    if request.method == "POST":
        try:
            principal = float(request.form.get("principal"))
            rate = float(request.form.get("rate"))
            time = float(request.form.get("time"))
            interest = principal * (rate/100) * time
            result = f"Simple Interest = {interest}"
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Financial Math - Simple Interest</h2>
    <form method="post">
      <div class="mb-3"><label class="form-label">Principal Amount</label><input type="number" step="any" class="form-control" name="principal" required></div>
      <div class="mb-3"><label class="form-label">Annual Interest Rate (%)</label><input type="number" step="any" class="form-control" name="rate" required></div>
      <div class="mb-3"><label class="form-label">Time (years)</label><input type="number" step="any" class="form-control" name="time" required></div>
      <button type="submit" class="btn btn-primary">Calculate</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/financial" class="btn btn-secondary">Back to Financial Menu</a>
    """
    return render_page(content)

@app.route("/financial/compound", methods=["GET", "POST"])
def financial_compound():
    result = ""
    if request.method == "POST":
        try:
            principal = float(request.form.get("principal"))
            rate = float(request.form.get("rate"))
            n = int(request.form.get("n"))
            years = float(request.form.get("years"))
            amount = principal * (1 + (rate/100)/n)**(n*years)
            result = f"Compound Amount after {years} years = {amount}"
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Financial Math - Compound Interest</h2>
    <form method="post">
      <div class="mb-3"><label class="form-label">Principal Amount</label><input type="number" step="any" class="form-control" name="principal" required></div>
      <div class="mb-3"><label class="form-label">Annual Interest Rate (%)</label><input type="number" step="any" class="form-control" name="rate" required></div>
      <div class="mb-3"><label class="form-label">Times Compounded per Year</label><input type="number" class="form-control" name="n" required></div>
      <div class="mb-3"><label class="form-label">Number of Years</label><input type="number" step="any" class="form-control" name="years" required></div>
      <button type="submit" class="btn btn-primary">Calculate</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/financial" class="btn btn-secondary">Back to Financial Menu</a>
    """
    return render_page(content)

@app.route("/financial/loan", methods=["GET", "POST"])
def financial_loan():
    result = ""
    if request.method == "POST":
        try:
            principal = float(request.form.get("principal"))
            rate = float(request.form.get("rate"))
            years = float(request.form.get("years"))
            monthly_rate = (rate/100)/12
            n_payments = years * 12
            if monthly_rate == 0:
                payment = principal / n_payments
            else:
                payment = principal * (monthly_rate*(1+monthly_rate)**n_payments)/((1+monthly_rate)**n_payments - 1)
            result = f"Monthly Payment = {payment}"
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Financial Math - Loan Payment Calculation</h2>
    <form method="post">
      <div class="mb-3"><label class="form-label">Loan Principal</label><input type="number" step="any" class="form-control" name="principal" required></div>
      <div class="mb-3"><label class="form-label">Annual Interest Rate (%)</label><input type="number" step="any" class="form-control" name="rate" required></div>
      <div class="mb-3"><label class="form-label">Loan Term (years)</label><input type="number" step="any" class="form-control" name="years" required></div>
      <button type="submit" class="btn btn-primary">Calculate</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/financial" class="btn btn-secondary">Back to Financial Menu</a>
    """
    return render_page(content)

# ===================================
# 8. Unit Conversions Routes
# ===================================
@app.route("/conversions")
def conversions():
    content = """
    <h2>Unit Conversions</h2>
    <ul>
      <li><a href="/conversions/length">Length Conversion</a></li>
      <li><a href="/conversions/area">Area Conversion</a></li>
      <li><a href="/conversions/volume">Volume Conversion</a></li>
      <li><a href="/conversions/temperature">Temperature Conversion</a></li>
      <li><a href="/conversions/weight">Weight/Mass Conversion</a></li>
    </ul>
    """
    return render_page(content)

@app.route("/conversions/length", methods=["GET", "POST"])
def conv_length():
    result = ""
    if request.method == "POST":
        try:
            value = float(request.form.get("value"))
            from_unit = request.form.get("from_unit").lower()
            to_unit = request.form.get("to_unit").lower()
            factors = {"m":1, "km":1000, "mi":1609.34, "ft":0.3048, "in":0.0254}
            if from_unit in factors and to_unit in factors:
                meters = value * factors[from_unit]
                res = meters / factors[to_unit]
                result = f"{value} {from_unit} = {res} {to_unit}"
            else:
                result = "Invalid units."
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Unit Conversions - Length</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Value</label>
        <input type="number" step="any" class="form-control" name="value" required>
      </div>
      <div class="mb-3">
        <label class="form-label">From (m, km, mi, ft, in)</label>
        <input type="text" class="form-control" name="from_unit" required>
      </div>
      <div class="mb-3">
        <label class="form-label">To (m, km, mi, ft, in)</label>
        <input type="text" class="form-control" name="to_unit" required>
      </div>
      <button type="submit" class="btn btn-primary">Convert</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/conversions" class="btn btn-secondary">Back to Conversions Menu</a>
    """
    return render_page(content)

@app.route("/conversions/area", methods=["GET", "POST"])
def conv_area():
    result = ""
    if request.method == "POST":
        try:
            value = float(request.form.get("value"))
            from_unit = request.form.get("from_unit").lower()
            to_unit = request.form.get("to_unit").lower()
            factors = {"sqm":1, "sqft":0.092903, "acre":4046.86, "hectare":10000}
            if from_unit in factors and to_unit in factors:
                sqm = value * factors[from_unit]
                res = sqm / factors[to_unit]
                result = f"{value} {from_unit} = {res} {to_unit}"
            else:
                result = "Invalid units."
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Unit Conversions - Area</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Area Value</label>
        <input type="number" step="any" class="form-control" name="value" required>
      </div>
      <div class="mb-3">
        <label class="form-label">From (sqm, sqft, acre, hectare)</label>
        <input type="text" class="form-control" name="from_unit" required>
      </div>
      <div class="mb-3">
        <label class="form-label">To (sqm, sqft, acre, hectare)</label>
        <input type="text" class="form-control" name="to_unit" required>
      </div>
      <button type="submit" class="btn btn-primary">Convert</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/conversions" class="btn btn-secondary">Back to Conversions Menu</a>
    """
    return render_page(content)

@app.route("/conversions/volume", methods=["GET", "POST"])
def conv_volume():
    result = ""
    if request.method == "POST":
        try:
            value = float(request.form.get("value"))
            from_unit = request.form.get("from_unit").lower()
            to_unit = request.form.get("to_unit").lower()
            factors = {"l":1, "ml":0.001, "gal":3.78541, "m3":1000}
            if from_unit in factors and to_unit in factors:
                liters = value * factors[from_unit]
                res = liters / factors[to_unit]
                result = f"{value} {from_unit} = {res} {to_unit}"
            else:
                result = "Invalid units."
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Unit Conversions - Volume</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Volume Value</label>
        <input type="number" step="any" class="form-control" name="value" required>
      </div>
      <div class="mb-3">
        <label class="form-label">From (L, mL, gal, m3)</label>
        <input type="text" class="form-control" name="from_unit" required>
      </div>
      <div class="mb-3">
        <label class="form-label">To (L, mL, gal, m3)</label>
        <input type="text" class="form-control" name="to_unit" required>
      </div>
      <button type="submit" class="btn btn-primary">Convert</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/conversions" class="btn btn-secondary">Back to Conversions Menu</a>
    """
    return render_page(content)

@app.route("/conversions/temperature", methods=["GET", "POST"])
def conv_temperature():
    result = ""
    if request.method == "POST":
        try:
            value = float(request.form.get("value"))
            from_unit = request.form.get("from_unit").upper()
            to_unit = request.form.get("to_unit").upper()
            if from_unit == to_unit:
                res = value
            elif from_unit == "C":
                if to_unit == "F":
                    res = (value * 9/5) + 32
                elif to_unit == "K":
                    res = value + 273.15
            elif from_unit == "F":
                if to_unit == "C":
                    res = (value - 32) * 5/9
                elif to_unit == "K":
                    res = (value - 32) * 5/9 + 273.15
            elif from_unit == "K":
                if to_unit == "C":
                    res = value - 273.15
                elif to_unit == "F":
                    res = (value - 273.15) * 9/5 + 32
            else:
                res = "Invalid conversion"
            result = f"{value} {from_unit} = {res} {to_unit}"
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Unit Conversions - Temperature</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Temperature Value</label>
        <input type="number" step="any" class="form-control" name="value" required>
      </div>
      <div class="mb-3">
        <label class="form-label">From (C, F, K)</label>
        <input type="text" class="form-control" name="from_unit" required>
      </div>
      <div class="mb-3">
        <label class="form-label">To (C, F, K)</label>
        <input type="text" class="form-control" name="to_unit" required>
      </div>
      <button type="submit" class="btn btn-primary">Convert</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/conversions" class="btn btn-secondary">Back to Conversions Menu</a>
    """
    return render_page(content)

@app.route("/conversions/weight", methods=["GET", "POST"])
def conv_weight():
    result = ""
    if request.method == "POST":
        try:
            value = float(request.form.get("value"))
            from_unit = request.form.get("from_unit").lower()
            to_unit = request.form.get("to_unit").lower()
            factors = {"kg":1, "g":0.001, "lb":0.453592, "oz":0.0283495}
            if from_unit in factors and to_unit in factors:
                kg = value * factors[from_unit]
                res = kg / factors[to_unit]
                result = f"{value} {from_unit} = {res} {to_unit}"
            else:
                result = "Invalid units."
        except Exception as e:
            result = "Error: " + str(e)
    content = f"""
    <h2>Unit Conversions - Weight/Mass</h2>
    <form method="post">
      <div class="mb-3">
        <label class="form-label">Weight/Mass Value</label>
        <input type="number" step="any" class="form-control" name="value" required>
      </div>
      <div class="mb-3">
        <label class="form-label">From (kg, g, lb, oz)</label>
        <input type="text" class="form-control" name="from_unit" required>
      </div>
      <div class="mb-3">
        <label class="form-label">To (kg, g, lb, oz)</label>
        <input type="text" class="form-control" name="to_unit" required>
      </div>
      <button type="submit" class="btn btn-primary">Convert</button>
    </form>
    <br><h4>Result:</h4><p>{result}</p>
    <a href="/conversions" class="btn btn-secondary">Back to Conversions Menu</a>
    """
    return render_page(content)

# ---------------------------
# Run the App
# ---------------------------
if __name__ == '__main__':
    app.run(debug=True)
