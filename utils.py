import json


def get_candidates_list():
    """
    Получает из json файла список кандидатов для дальнейшей работы с ним
    """
    with open("candidates.json", "r", encoding='utf-8') as candidates:
        candidates_list = json.load(candidates)
        return candidates_list


def get_candidates(candidates_list):
    """
    Выводит список кандидатов в представленном формате
    """
    candidates = '<pre>'
    for candidate in candidates_list:
        name = f"Имя кандидата - {candidate['name']}\n"
        position = f"Позиция кандидата - {candidate['position']}\n"
        skills = f"Навыки через запятую - {candidate['skills']}\n\n"
        candidates += name + position + skills
    candidates += '<pre>'
    return candidates


def get_candidates_id(candidates_list, candidate_id):
    """
    Возвращает данные кандидата по id
    """
    for candidate in candidates_list:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_skills(candidates_list, candidate_skill):
    """
    Выводит тех кандидатов, в списке навыков у которых содержится заданный skill
    """
    candidates = []
    for candidate in candidates_list:
        candidate_skills = candidate["skills"].lower().split(", ")
        if candidate_skill.lower() in candidate_skills:
            candidates.append(candidate)
    return candidates
