import csv
from extractor.wwr_parser import *
from extractor.indeed_parser import *


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
            for job in self.jobs:
                writer.writerow([job[j]for j in agenda])


def main():
    skill = "python"
    jobs = get_wwr_job_list(skill) + get_indeed_job_list(skill)
    writer = Writer(skill, jobs)
    writer.save()

if __name__ == "__main__":
    main()
