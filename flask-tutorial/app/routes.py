from datetime import datetime 
from flask import (
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)
from werkzeug.urls import url_parse

from app import (
    app,
    db,
)
from app.forms import (
    EditProfileForm,
    LoginForm,
    NoteForm,
    RegistrationForm,
)
from app.models import (
    Note,
    User,
)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user! Please Sign In to continue.')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = NoteForm()
    if form.validate_on_submit():
        note = Note(body=form.note.data, author=current_user)
        db.session.add(note)
        db.session.commit()
        flash('Your note is now live!')
        return redirect(url_for('index'))

    page = request.args.get('page', 1, type=int)
    notes = current_user.followed_notes().paginate(
        page, app.config['NOTES_PER_PAGE'], False)
    prev_url = url_for('index', page=notes.prev_num) if notes.has_prev else None
    next_url = url_for('index', page=notes.next_num) if notes.has_next else None

    bindings = dict(
        title='Home',
        form=form,
        notes=notes.items,
        prev_url=prev_url,
        next_url=next_url,
    )
    return render_template('index.html', **bindings)

@app.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    notes = Note.query.order_by(Note.timestamp.desc()).paginate(
        page, app.config['NOTES_PER_PAGE'], False)
    prev_url = url_for('explore', page=notes.prev_num) if notes.has_prev else None
    next_url = url_for('explore', page=notes.next_num) if notes.has_next else None
    bindings = dict(
        title='Explore',
        form=None,
        notes=notes.items,
        prev_url=prev_url,
        next_url=next_url,
    )
    return render_template('index.html', **bindings)


@app.route('/user/<username>')
@login_required
def user(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    notes = Note.query.filter_by(user_id=user.id).paginate(
        page, app.config['NOTES_PER_PAGE'], False)
    prev_url = url_for('user', username=user.username, page=notes.prev_num) if notes.has_prev else None
    next_url = url_for('user', username=user.username, page=notes.next_num) if notes.has_next else None
    bindings = dict(
        user=user,
        notes=notes.items,
        prev_url=prev_url,
        next_url=next_url,
    )
    return render_template('user.html', **bindings)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    bindings = dict(
        title='Edit Profile',
        form=form,
    )
    return render_template('edit_profile.html', **bindings)

@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}!'.format(username))
    return redirect(url_for('user', username=username))

@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {}.'.format(username))
    return redirect(url_for('user', username=username))
