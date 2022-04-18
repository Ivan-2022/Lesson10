from flask import Flask
from utils import get_candidates_list, get_candidates, get_candidates_id, get_candidates_skills

app = Flask(__name__)

candidates_list = get_candidates_list()


@app.route("/")
def page_maine():
    """
    Главная страница, список кандитатов
    """
    return get_candidates(candidates_list)


@app.route("/candidates/<int:candidate_id>")
def page_candidate(candidate_id):
    """
    Страница с данными кандидата по id
    """
    candidate = get_candidates_id(candidates_list, candidate_id)
    return f"<img src={candidate['picture']}> {get_candidates([candidate])}"


@app.route("/skills/<skill>")
def page_skills(skill):
    """
    Страница с кандидатами, в списке навыков у которых содержится заданный skill
    """
    return get_candidates(get_candidates_skills(candidates_list, skill))


app.run()
