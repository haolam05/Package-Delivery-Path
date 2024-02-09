from flask import Blueprint, render_template, redirect, request
from ..forms import ShippingForm
from ..map import map
from ..models import db, Package

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/")
def status_package():
  packages = Package.query.all()
  for package in packages:
    package.path = package.shortest_path()
  return render_template('package_status.html', packages = packages)


@bp.route("/new_package", methods=['GET', 'POST'])
def new_package():
  form = ShippingForm()

  """ Handling Post Request """
  if request.method == "POST":
    package = Package(
      sender = request.form['sender_name'],
      recipient = request.form['recipient_name'],
      origin = request.form['origin'],
      destination = request.form['destination'],
      location = request.form['origin'],
      has_express = ('has_express' in request.form),
    )
    db.session.add(package)
    db.session.commit()
    Package.advance_all_locations()
    return redirect("/")


  """ Handling Get Request """
  cities = map.keys()
  form.origin.choices = [(city, f"{city}, US") for city in cities]
  form.destination.choices = [(city, f"{city}, US") for city in cities]

  return render_template('shipping_request.html', form = form)
