"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename
from forms import UploadPhoto

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/wtform', methods=['POST', 'GET'])
def LogIn():
    login=LogIn()
    if request.method == 'POST':
        if login.validate_on_submit():
            firstname = login.firstname.data
            password = login.password.data
            #should check directory if name and password match before giving access
    return render_template('login.html', firstname=firstname)

@app.route('/uploadphoto', methods=['GET', 'POST'])
def UploadPhoto(): 
    photo = UploadPhoto()
    if request.method == 'POST' and photo.validate_on_submit():
        request.files['photo'] 
        description = photo.description.data

    filename = secure_filename(photo.filename)
    photo.save(os.path.join(app.config['uploads'], filename))
    flash('File Saved', 'success')
    return render_template('uploads.html', form=photo)

@app.route('/files')
def files():
    return render_template('filess.html')
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            
            flash('You were logged in', 'success')
            return redirect(url_for('upload'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out', 'success')
    return redirect(url_for('home'))


###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
    
rootdir = " lab4//app//static//uploads"
#arcpy.env.overwriteOutput = True  
counter=0

rootdir = os.getcwd()
print (rootdir)
for subdir, dirs, files in os.walk(rootdir + '/some/folder'):
    for file in files:
        print (os.path.join(subdir, file)) 


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
