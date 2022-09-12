import json

# возвращает список всех кандидатов
def load_candidates_from_json():
    with open("candidates.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        return data

#возвращает одного кандидата по его id
def get_candidate(data, id):
    for i in data:
        if i["id"] == id:
            return i

#возвращает кандидатов по имени
def get_candidates_by_name(data, name):
    result = []
    for i in data:
        if i["name"] == name:
            result.append(i)
    return result
#возвращает кандидатов по навыку
def get_candidates_by_skill(skill):
    data = load_candidates_from_json()
    result = []
    for i in data:
        if skill in i["skills"].lower().split(", "):
            result.append(i)
    return result
