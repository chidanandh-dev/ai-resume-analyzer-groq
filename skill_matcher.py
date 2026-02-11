import json

def load_skill_db(path="skill_task_db.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def match_skills(resume_text, skill_db):
    resume_text = resume_text.lower()
    matched = {}

    for skill, tasks in skill_db.items():
        if skill.lower() in resume_text:
            matched[skill] = tasks

    return matched
