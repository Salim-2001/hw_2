from flask import Flask, render_template
from utils import *

candidates = load_candidates_from_json("candidates.json")

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('list.html', candidates=candidates)

@app.route("/candidate/<int:id>")
def get_by_id(id):
    return render_template("single.html", candidate=get_candidate(id))

@app.route("/search/<candidate_name>")
def get_by_name(candidate_name):
    return render_template("search.html", profils=get_candidates_by_name(candidate_name))

@app.route("/skill/<skill_name>")
def get_by_skill(skill_name):
    return render_template("skill.html", candidates=get_candidates_by_skill(skill_name))


app.run()
