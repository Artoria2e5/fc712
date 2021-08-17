from time import strftime
from flask_bootstrap import Bootstrap

from flask import Flask, render_template, flash, request
from wtforms import (
    Form,
    TextField,
    RadioField,
    TextAreaField,
    validators,
)

# TODO: make it False
DEBUG = True
app = Flask(__name__, template_folder=".")
app.config.from_object(__name__)
app.config["SECRET_KEY"] = "Very-secret-very-secret-asbf34f"
bs = Bootstrap(app)


class ReusableForm(Form):
    # Identification
    fullname = TextField("Full Name:", validators=[validators.Required()])
    # I know what the ID looks like, so make the validator know it's P followed by I
    # can't remember how many digits.
    id = TextField(
        "GIC ID:", validators=[validators.Required(), validators.Regexp(r"P\d+")]
    )
    # Full Email validation is hard, so there is a wtforms validator for it! But we
    # aren't using it because we know what GU emails look like.
    email = TextField(
        "Email:",
        description="Use your GUID!",
        validators=[
            validators.Required(),
            validators.Regexp(r"\d+[A-Z]@student\.gla\.ac\.uk"),
        ],
    )

    # Okay, now the real course stuff.
    course_id = TextField(
        "Course ID:",
        description="e.g. FC712",
        validators=[
            validators.Required(),
            validators.Regexp(r"FC\d{3}"),
        ],
    )
    # We could add more rows like this, but this will do for now.
    self_assessment = RadioField(
        label="I have an idea what this course is about.",
        validators=[validators.Required()],
        # Five-point assessment. Good enough, right?
        choices=[(x, x) for x in range(6)],
    )
    # Let's not force people to disclose their deepest fears. No validation; fully optional.
    more_details = TextAreaField(
        "What changes to the course do you think will help with your learning? (optional)"
    )


def get_time():
    time = strftime("%Y-%m-%dT%H:%M")
    return time


def csv_escape(s: str) -> str:
    """Escape a CSV string according to Unix (RFC something) rules:
    Quote if problematic, raw otherwise.

    Quoting is done by doubling up all quotation marks."""
    if '"' in s or "\n" in s or "\r" in s:
        return '"{}"'.format(s.replace('"', '""'))
    else:
        return s


def write_to_disk(form):
    data = open("out_data.csv", "a")
    timestamp = get_time()
    data.write(
        "{timestamp}, {fullname}, {id}, {email}, {course_id}, {self_assessment}, {more_details}\n".format(
            # I think this will work. Anyways, form is going to be a dict, and here we escape all the vals.
            # The timestamp won't need escaping because we can... know it's not problematic.
            timestamp=timestamp,
            **{k: csv_escape(form[k]) for k in form}
        )
    )
    data.close()


@app.route("/", methods=["GET", "POST"])
def hello():
    form = ReusableForm(request.form)

    if request.method == "POST":
        if form.validate():
            rf = request.form
            write_to_disk(request.form)
            flash(
                "Hello {fullname}, your rating for {course_id} has been submitted.".format(
                    **rf
                )
            )
        else:
            flash("Error: Check page messages")

    # The 'title' param is used implicitly via the bootstrap/base.html extend.
    return render_template(
        "index.html", form=form, title="GIC Course Self-Assessment Form"
    )


if __name__ == "__main__":
    app.run()
