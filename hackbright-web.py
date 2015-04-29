from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

import sqlite3

db_connection = sqlite3.connect("hackbright.db", check_same_thread=False)
db_cursor = db_connection.cursor()

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'name')
    first, last, github = hackbright.get_student_by_github(github)
    # return "%s is the GitHub account for %s %s" % (github, first, last)
    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)
    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add") #, methods=['POST'])
def make_new_student():
    """Add a new student and print confirmation.

    Given a first name, last name, and GitHub account, add student to the
    database and print a confirmation message.
    """
    #first_name, last_name, github
    # request.form.get()
    # QUERY = """INSERT INTO Students VALUES (?, ?, ?)"""
    # db_cursor.execute(QUERY, (first_name, last_name, github))
    # db_connection.commit()
    # print "Successfully added student: %s %s" % (first_name, last_name)

    return render_template("student-add.html")


if __name__ == "__main__":
    app.run(debug=True)