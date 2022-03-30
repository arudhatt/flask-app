from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from app import db
from app.models import Settings
from app.settings.forms import SettingsForm

settings = Blueprint('settings', __name__)


@login_required
@settings.route("/change_settings", methods=['GET', 'POST'])
def change_settings():
    form = SettingsForm()
    if form.validate_on_submit():
        # premises = True
        # waitlist = False
        if form.premises_full.data == 'True':
            premises = True
        else:
            premises = False
        if form.waitlist.data == 'True':
            waitlist = True
        else:
            waitlist = False
        settings = Settings(premises_full=premises, waitlist=waitlist)
        db.session.add(settings)
        db.session.commit()
        flash('Your changes has been saved!', 'success')
        return redirect(url_for('main.home'))
    return render_template('settings.html', title='Settings',
                           form=form, legend='Change Settings')


