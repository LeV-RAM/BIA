# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

class Intern():
    def __init__(self, company, name, course, period, gpa, skills):
        self.company = company
        self.name = name
        self.course = course
        self.period = period
        self.gpa = gpa
        self.skills = skills

    def get_company(self):
        return self.company
    def get_name(self):
        return self.name
    def get_course(self):
        return self.course
    def get_period(self):
        return self.period
    def get_gpa(self):
        return self.gpa
    def get_skills(self):
        return self.skills


def openAccount():
    from login import Account
    with open("C:/Users/Asus/OneDrive/Desktop/BIA/data/account.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
        acc = line.strip().split("#")
    return Account(acc[0], acc[1], acc[2], acc[3], acc[4], acc[5], acc[6], acc[7], acc[8], acc[9], acc[10], acc[11], acc[12]) 

acc = openAccount()
intern = []
file_path = "C:/Users/Asus/OneDrive/Desktop/BIA/data/intern.txt"
minimum_gpa = 3.9
required_skill = acc.get_skill()


def recommend_internships(file_path, min_gpa, required_skill):
    with open(file_path, 'r') as file:
        data = file.read()
    
    rows = data.split('\n')
    rows = [row for row in rows if row.strip()]
    
    programs = []
    for row in rows:
        columns = row.split('#')
        programs.append(columns)

    filtered_programs = []
    for program in programs:
        if float(program[4]) >= min_gpa or required_skill.lower() in program[5].lower():
            filtered_programs.append(program)

    recommended_programs = filtered_programs[:6]

    for program in recommended_programs:
        # print(f"Company: {program[0]}")
        # print(f"Program: {program[0]} Internship Program")
        # print(f"Location: {program[1]}")
        # print(f"Related Course: {program[2]}")
        # print(f"Period: {program[3]}")
        # print(f"Minimum GPA Score: {program[4]}")
        # print(f"Skill Required: {program[5]}")
        # print("=" * 30)
        intern.append(Intern(program[0], program[0]+" Internship Program", program[1], program[2], program[3], program[4], program[5]))


# Call the function to recommend internships
recommend_internships(file_path, minimum_gpa, required_skill)