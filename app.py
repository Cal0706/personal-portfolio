
from flask import Flask, render_template, abort

app = Flask(__name__)

# Portfolio projects
projects = {
    "sports-scouting": {
        "title": "Sports Scouting Database",
        "description": (
            "A database designed to organize athlete "
            "information, team records, scouting and NIL reports."
        ),
        "technologies": "Microsoft Access, Database Design, Figma Designs"
    },

    "data-dashboard": {
        "title": "Data Analytics Dashboard",
        "description": (
            "A data visualization project focused on "
            "identifying trends and presenting insights "
            "through interactive dashboards."
        ),
        "technologies": "Tableau, Excel, Access, Python"
    },

    "python-projects": {
        "title": "Python Projects",
        "description": (
            "A collection of Python programs focused on "
            "data processing, programming fundamentals, "
            "and problem-solving."
        ),
        "technologies": "Python"
    },
    "excel-payroll": {
        "title": "Employee Payroll Analysis",
        "description": (
            "An Excel-based analysis of employee payroll data "
            "using calculations, charts, and data visualization "
            "to examine compensation trends."
        ),
        "technologies": "Microsoft Excel, Data Analysis, Charts"
    },

    "tableau-music": {
        "title": "Music Trends & Artist Popularity",
        "description": (
            "A Tableau visualization project exploring artist "
            "popularity, song duration, explicit music, "
            "and trends across different years."
        ),
        "technologies": "Tableau, Data Visualization, Analytics"
    }
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/projects/<project_id>")
def project_detail(project_id):
    project = projects.get(project_id)

    if project is None:
        abort(404)

    return render_template(
        "project.html", 
        project_id=project_id,
        project=project
    )


if __name__ == "__main__":
    app.run(debug=True)
