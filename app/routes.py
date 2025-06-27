from flask import Flask, render_template, request, redirect, url_for, flash, session
from app.ldap_auth import LDAPAuthenticator
from app.database import add_url, get_all_history, get_active_urls
from app.utils import is_valid_url
from config import LDAP_SERVER, LDAP_BASE_DN, SECRET_KEY

# Flask app initialization
app = Flask(__name__)
app.secret_key = SECRET_KEY

# LDAP authentication setup
ldap_auth = LDAPAuthenticator(LDAP_SERVER, LDAP_BASE_DN)

@app.route('/')
def login():
    # Show login page
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_user():
    username = request.form['username']
    password = request.form['password']
    
    # Authenticate user via LDAP
    role = ldap_auth.authenticate(username, password)
    
    if role == "admin":
        session['role'] = 'admin'
        flash("Logged in as Admin", "success")
        return redirect(url_for('admin'))
    elif role == "teacher":
        session['role'] = 'teacher'
        flash("Logged in as Teacher", "success")
        return redirect(url_for('teacher'))
    else:
        flash("Invalid credentials, please try again.", "danger")
        return redirect(url_for('login'))

@app.route('/admin')
def admin():
    if session.get('role') != 'admin':
        flash("Unauthorized access!", "danger")
        return redirect(url_for('login'))
    return render_template('admin.html')

@app.route('/teacher')
def teacher():
    if session.get('role') != 'teacher':
        flash("Unauthorized access!", "danger")
        return redirect(url_for('login'))
    return render_template('teacher.html')

@app.route('/manage_url', methods=['GET', 'POST'])
def manage_url():
    if request.method == 'POST':
        action = request.form['action']
        url = request.form['url']

        # Validate URL
        if not is_valid_url(url):
            flash("Enter a valid URL!", "danger")
            return redirect(url_for('manage_url'))

        # Add URL to the database
        add_url(session['role'], url, action, "12:00", "2024-11-23")
        flash(f"URL {action.lower()}ed successfully!", "success")
    return render_template('manage_url.html')

@app.route('/view_history')
def view_history():
    # Get URL history from the database
    history = get_all_history()
    return render_template('view_history.html', history=history)

@app.route('/active_urls')
def active_urls():
    # Get active URLs from the database
    urls = get_active_urls()
    return render_template('active_urls.html', urls=urls)

@app.route('/logout')
def logout():
    # Clear session and redirect to login page
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))
