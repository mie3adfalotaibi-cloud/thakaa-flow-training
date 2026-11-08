profile = {
    "name": "Mieaad Alotaibi",
    "age": 21,
    "city": "Riyadh",
    "skills": ["Python", "Git", "VS Code"],
    "courses": {
        "Thakaa Flow Training": "in progress",
        "Python Course (Abdelrahman Gamal)": "in progress",
        "Intro to AI": "in progress"
    }
}

# 2) new skill this week
profile["skills"].append("Data structures")

# 3) update a course and add a planned one
profile["courses"]["Intro to AI"] = "done"
profile["courses"]["Pandas"] = "planned"

# 4) add github, delete city
profile["github"] = "mie3adfalotaibi-cloud"
del profile["city"]

# 5) print info
print("Keys:", list(profile.keys()))
print("Number of skills:", len(profile["skills"]))
print("SQL in skills?", "SQL" in profile["skills"])
print("Thakaa Flow Training:", profile["courses"]["Thakaa Flow Training"])
print("Machine Learning:", profile["courses"].get("Machine Learning", "Not found"))

# 6) summary line
skills_count = len(profile["skills"])
courses_count = len(profile["courses"])
print(f"{profile['name']} | {skills_count} skills | {courses_count} courses | github.com/{profile['github']}")