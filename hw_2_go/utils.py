import json


def load_candidates_from_json(path):
    """возвращает список всех кандидатов"""
    with open(path, "r", encoding="UTF-8") as file:
        return json.load(file)

def get_candidate(candidate_id):
    """возвращает одного кандидата по его id"""
    data = load_candidates_from_json("candidates.json")

    for candidate in data:
        if candidate_id == candidate['id']:
            return candidate
    return "No candidate"

def get_candidates_by_name(candidate_name):
    """Возвращает кандидатов по имени"""
    data = load_candidates_from_json("candidates.json")
    candidates = []

    for candidate in data:
        if candidate_name in candidate['name']:
            candidates.append(candidate)
    return candidates

def get_candidates_by_skill(skill_name):
    """Возвращает кандидатов по навыку"""
    data = load_candidates_from_json("candidates.json")
    candidates = []

    for candidate in data:
        if skill_name in candidate['skills']:
            candidates.append(candidate)
    return candidates

