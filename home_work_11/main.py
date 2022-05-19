from flask import Flask, render_template, abort
import utils

app = Flask(__name__)


@app.route("/")
def list_candidates():
    """Главная страница приложения"""

    candidates = utils.load_candidates_from_json("candidates.json")
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:candidate_id>")
def page_candidate(candidate_id):
    """Страница кандидата"""

    candidate = utils.get_candidate(candidate_id)
    if candidate:
        return render_template("card.html", candidate=candidate)
    else:
        abort(404)


@app.route("/search/<candidate_name>")       #роут отображает только заголовок с количеством найденных кандидатов
def get_candidate_by_name(candidate_name):   #но ссылок на этих кандидатов нет
    """Поиск кандидата по имени"""

    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates, candidates_count=len(candidates))


@app.route("/skill/<string:skill_name>")     #Наставник пожалуйста помоги? я не понимаю почему не работает этот роут
def get_candidates_by_skill(skill_name):
    """Поиск кандидата по навыку"""

    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template("skill.html", candidates=candidates, candidates_count=len(candidates))


app.run()
