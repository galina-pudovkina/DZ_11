from flask import Flask, render_template

from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def page_main():
    candidates = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:idx>')
def page_candidate(idx):
    candidate = get_candidate(load_candidates_from_json(), id)
    return render_template('card.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def search_candidate_page(candidate_name):
    candidates = get_candidates_by_name(load_candidates_from_json(), candidate_name)
    return render_template('search.html', candidates=candidates)


@app.route('/skill/<skill_name>')
def get_by_skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    return render_template('skill.html', skill=skill_name, candidates=candidates)


app.run()

