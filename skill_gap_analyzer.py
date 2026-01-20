job_roles = {
    "Data Scientist": {
        "required": ["python", "machine learning", "statistics", "data analysis", "sql"]
    },
    "AI Engineer": {
        "required": ["python", "deep learning", "neural networks", "tensorflow", "pytorch"]
    },
    "Web Developer": {
        "required": ["html", "css", "javascript", "backend", "frontend"]
    }
}

print("🧠 AI Skill Gap Analyzer \n")

role = input("Enter target job role: ").title()

if role not in job_roles:
    print("❌ Role not found")
    exit()

user_skills = input("Enter your skills (comma separated): ").lower().split(",")

required = job_roles[role]["required"]

user_skills = [s.strip() for s in user_skills]

missing = [skill for skill in required if skill not in user_skills]
matched = [skill for skill in required if skill in user_skills]

print("\n🎯 Skill Analysis Result")
print("Matched skills:", matched)
print("Missing skills:", missing)

if not missing:
    print("\n🎉 You are job-ready!")
else:
    print("\n📚 Suggested learning path:")
    for skill in missing:
        print("• Learn", skill)
