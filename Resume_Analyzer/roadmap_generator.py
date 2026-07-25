"""
roadmap_generator.py
Takes the list of missing skills (skills the resume lacks for a job)
and generates simple learning suggestions for each one.
"""

# a small lookup of learning resources per skill
# in a real product this could come from an API, but a dictionary
# is enough for our project
LEARNING_RESOURCES = {
    "python": "Learn Python basics -> freeCodeCamp Python course",
    "sql": "Learn SQL -> W3Schools SQL Tutorial + practice on LeetCode SQL",
    "machine learning": "Andrew Ng's Machine Learning course on Coursera",
    "power bi": "Microsoft's free Power BI learning path",
    "excel": "Excel Skills for Business - Coursera",
    "react": "React official docs + build 2-3 small projects",
    "django": "Django official tutorial (Polls app)",
    "aws": "AWS Cloud Practitioner Essentials (free course)",
    "docker": "Docker for beginners - freeCodeCamp YouTube",
    "git": "Git and GitHub crash course",
}

DEFAULT_MESSAGE = "Search for a beginner tutorial on this skill and practice with a small project."


def generate_roadmap(missing_skills: list[str]) -> dict[str, str]:
    """
    For each missing skill, return a suggested resource/learning step.
    If we don't have a resource in our dictionary, give a default tip.
    """
    roadmap = {}
    for skill in missing_skills:
        roadmap[skill] = LEARNING_RESOURCES.get(skill, DEFAULT_MESSAGE)
    return roadmap


# quick test
if __name__ == "__main__":
    missing = ["python", "docker", "some_random_skill"]
    for skill, tip in generate_roadmap(missing).items():
        print(f"{skill}: {tip}")
