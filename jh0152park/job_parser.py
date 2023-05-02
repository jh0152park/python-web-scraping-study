import csv
from flask import *
from extractor.wwr_parser import *
from extractor.indeed_parser import *


DB = {}


class Writer:
    def __init__(self, skill, jobs):
        self.jobs = jobs
        self.skill = skill

    def save(self):
        agenda = [
            "company",
            "title",
            "locate",
            "type",
            "link"
        ]
        with open(f"{self.skill}_job_list.csv", "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(agenda)
            for job in self.jobs:
                writer.writerow([job[j]for j in agenda])


def main():
    app = Flask("JobScrapper")

    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/search")
    def search():
        global DB
        skill = request.args.get("skill")
        if not skill:
            return redirect("/")

        if skill in DB:
            jobs = DB[skill]
        else:
            jobs = get_wwr_job_list(skill) + get_indeed_job_list(skill)
            DB[skill] = jobs
            writer = Writer(skill, jobs)
            writer.save()
        return render_template("search.html", skill=skill, jobs=jobs)

    @app.route("/export")
    def export():
        global DB

        skill = request.args.get("skill")
        if not skill:
            return redirect("/")
        if skill not in DB:
            return redirect(f"/search?skill={skill}")
        return send_file(f"{skill}_job_list.csv", as_attachment=True)

    app.run("0.0.0.0")

if __name__ == "__main__":
    main()
