from datetime import datetime 

from flask import (
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import (
    current_user,
    login_required,
)

from app import db
from app.main import bp
from app.main.forms import (
    EditProfileForm,
    NoteForm,
)

from app.models import (
    Note,
    User,
)


@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = NoteForm()
    if form.validate_on_submit():
        note = Note(body=form.note.data, author=current_user)
        db.session.add(note)
        db.session.commit()
        flash('Your note is now live!')
        return redirect(url_for('main.index'))

    page = request.args.get('page', 1, type=int)
    notes = current_user.followed_notes().paginate(
        page, current_app.config['NOTES_PER_PAGE'], False)
    prev_url = url_for('main.index', page=notes.prev_num) if notes.has_prev else None
    next_url = url_for('main.index', page=notes.next_num) if notes.has_next else None

    bindings = dict(
        title='Home',
        form=form,
        notes=notes.items,
        prev_url=prev_url,
        next_url=next_url,
    )
    return render_template('index.html', **bindings)

@bp.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    notes = Note.query.order_by(Note.timestamp.desc()).paginate(
        page, current_app.config['NOTES_PER_PAGE'], False)
    prev_url = url_for('main.explore', page=notes.prev_num) if notes.has_prev else None
    next_url = url_for('main.explore', page=notes.next_num) if notes.has_next else None
    bindings = dict(
        title='Explore',
        form=None,
        notes=notes.items,
        prev_url=prev_url,
        next_url=next_url,
    )
    return render_template('index.html', **bindings)


@bp.route('/user/<username>')
@login_required
def user(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    notes = Note.query.filter_by(user_id=user.id).paginate(
        page, current_app.config['NOTES_PER_PAGE'], False)
    prev_url = url_for('main.user', username=user.username, page=notes.prev_num) if notes.has_prev else None
    next_url = url_for('main.user', username=user.username, page=notes.next_num) if notes.has_next else None
    bindings = dict(
        user=user,
        notes=notes.items,
        prev_url=prev_url,
        next_url=next_url,
    )
    return render_template('user.html', **bindings)

@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    bindings = dict(
        title='Edit Profile',
        form=form,
    )
    return render_template('edit_profile.html', **bindings)

@bp.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('main.index'))
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('main.user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}!'.format(username))
    return redirect(url_for('main.user', username=username))

@bp.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('main.index'))
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('main.user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {}.'.format(username))
    return redirect(url_for('main.user', username=username))
