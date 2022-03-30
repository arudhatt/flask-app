from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from app import db
from app.models import Visitor
from app.contacts.forms import VisitorForm

contacts = Blueprint('contacts', __name__)


@contacts.route("/new_contact", methods=['GET', 'POST'])
def new_contact():
    form = VisitorForm()
    if form.validate_on_submit():
        visitor = Visitor(name=form.name.data, email=form.email.data, phone=form.phone.data)
        db.session.add(visitor)
        db.session.commit()
        flash('Your contact has been saved!', 'success')
        return redirect(url_for('main.home'))
    return render_template('contact.html', title='Contact Details',
                           form=form, legend='New Contact')


@contacts.route("/contact_details", methods=['GET', 'POST'])
def contact_details():
    page = request.args.get('page', 1, type=int)
    contacts = Visitor.query.order_by(Visitor.id.desc()).paginate(page=page, per_page=5)
    return render_template('display_contacts.html', contacts=contacts)


