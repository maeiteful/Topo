import json
from collections import deque

data = {
    "ARB100": {
        "Name": "Arabic",
        "Prereqs": [
            "ARB099"
        ]
    },
    "NE101": {
        "Name": "National Education",
        "Prereqs": [
            "ARB099"
        ]
    },
    "ENGL099": {
        "Name": "English II",
        "Prereqs": []
    },
    "ENGL101": {
        "Name": "English III",
        "Prereqs": [
            "ENGL099"
        ]
    },
    "ENGL102": {
        "Name": "English IV",
        "Prereqs": [
            "ENGL101"
        ]
    },
    "ENGL201": {
        "Name": "English V",
        "Prereqs": [
            "ENGL102"
        ]
    },
    "ENGL202": {
        "Name": "English VI",
        "Prereqs": [
            "ENGL201"
        ]
    },
    "MILS100": {
        "Name": "Military Science *For Jordanian Only",
        "Prereqs": []
    },
    "GERL101": {
        "Name": "German I",
        "Prereqs": []
    },
    "ARB099": {
        "Name": "Arabic 99",
        "Prereqs": []
    },
    "GERL102": {
        "Name": "German II",
        "Prereqs": [
            "GERL101"
        ]
    },
    "NEE101": {
        "Name": "National Education in English",
        "Prereqs": []
    },
    "GERL102B2": {
        "Name": "German II B2-TRACK",
        "Prereqs": [
        ]
    },
    "SFTS101": {
        "Name": "Soft Skills",
        "Prereqs": [
            "ENGL101"
        ]
    },
    "IC101": {
        "Name": "Intercultural Communications",
        "Prereqs": [
            "ENGL101"
        ]
    },
    "SE301": {
        "Name": "Social Entrepreneurship and Enterprises",
        "Prereqs": [
            "ENGL101"
        ]
    },
    "DES101": {
        "Name": "Arts' Appreciation",
        "Prereqs": [
            "ARB099"
        ]
    },
    "EI101": {
        "Name": "Leadership and Emotional Intelligence",
        "Prereqs": [
            "ENGL101"
        ]
    },
    "BE302": {
        "Name": "Business Entrepreneurship",
        "Prereqs": [
            "ENGL101"
        ]
    },
    "TW303": {
        "Name": "Technical and Workplace Writing",
        "Prereqs": []
    },
    "PE101": {
        "Name": "Sports and Health",
        "Prereqs": [
            "ARB099"
        ]
    },
    "CE352": {
        "Name": "Computer Networks",
        "Prereqs": [
            "CE201",
            "CS116"
        ]
    },
    "MATH101": {
        "Name": "Calculus I",
        "Prereqs": [
            "MATH099"
        ]
    },
    "MATH102": {
        "Name": "Calculus II",
        "Prereqs": [
            "MATH101"
        ]
    },
    "MATH099": {
        "Name": "Pre math",
        "Prereqs": []
    },
    "GERL201": {
        "Name": "German III",
        "Prereqs": [
            "GERL102"
        ]
    },
    "GERL202": {
        "Name": "German IV",
        "Prereqs": [
            "GERL201"
        ]
    },
    "CS116": {
        "Name": "Computing Fundamentals",
        "Prereqs": []
    },
    "CS1160": {
        "Name": "Computing Fundamentals LAB",
        "Prereqs": []
    },
    "CE212": {
        "Name": "Digital Systems",
        "Prereqs": []
    },
    "CE2120": {
        "Name": "Digital Systems Lab",
        "Prereqs": []
    },
    "ECE317": {
        "Name": "Linear Algebra",
        "Prereqs": [
            "MATH102"
        ]
    },
    "GERL201B2": {
        "Name": "German III B2-TRACK",
        "Prereqs": [
            "GERL102B2"
        ]
    },
    "GERL202B2": {
        "Name": "German IV B2-TRACK",
        "Prereqs": [
            "GERL201B2"
        ]
    },
    "CS201": {
        "Name": "Discrete Structures",
        "Prereqs": []
    },
    "CE354": {
        "Name": "Computer Security",
        "Prereqs": [
            "CE352"
        ]
    },
    "CE355": {
        "Name": "Data Communication",
        "Prereqs": [
            "CE331"
        ]
    },
    "CE391": {
        "Name": "Field Training",
        "Prereqs": []
    },
    "CE493": {
        "Name": "International Internship",
        "Prereqs": []
    },
    "CE502": {
        "Name": "Parallel Architectures and Parallel Algorithms",
        "Prereqs": [
            "CE201",
            "CS222",
            "CS223"
        ]
    },
    "IE121": {
        "Name": "Workshop",
        "Prereqs": []
    },
    "CE477": {
        "Name": "Machine Learning",
        "Prereqs": [
            "ECE317"
        ]
    },
    "CE594": {
        "Name": "Senior Project II",
        "Prereqs": [
            "CE592"
        ]
    },
    "CE201": {
        "Name": "Computer Architecture and Organization",
        "Prereqs": [
            "CE212",
            "CE2120"
        ]
    },
    "CE331": {
        "Name": "Signals and Systems",
        "Prereqs": [
            "MATH203"
        ]
    },
    "GERL301": {
        "Name": "German V",
        "Prereqs": [
            "GERL202"
        ]
    },
    "GERL302": {
        "Name": "German VI",
        "Prereqs": [
            "GERL301"
        ]
    },
    "CS342": {
        "Name": "Software Engineering",
        "Prereqs": [
            "CS214",
        ]
    },
    "PHYS103": {
        "Name": "Physics I",
        "Prereqs": []
    },
    "PHYS104": {
        "Name": "physics II",
        "Prereqs": [
            "PHYS103"
        ]
    },
    "PHYS106": {
        "Name": "General physics Lab",
        "Prereqs": []
    },
    "MATH203": {
        "Name": "Applied Mathematics For Engineers",
        "Prereqs": [
            "MATH102"
        ]
    },
    "MATH205": {
        "Name": "Differential Equations",
        "Prereqs": [
            "MATH102"
        ]
    },
    "CHEM103": {
        "Name": "General Chemistry I",
        "Prereqs": []
    },
    "CS222": {
        "Name": "Theory Of Algorithms",
        "Prereqs": [
            "CS201",
            "CS116",
            "CS1160"
        ]
    },
    "CS223": {
        "Name": "Data Structures",
        "Prereqs": [
            "CS116",
            "CS1160"
        ]
    },
    "ENE211": {
        "Name": "Electrical Circuits I",
        "Prereqs": [
            "PHYS104"
        ]
    },
    "ENE212": {
        "Name": "Electrical Circuits II",
        "Prereqs": [
            "ENE211"
        ]
    },
    "BM371": {
        "Name": "Numerical Methods for Engineers",
        "Prereqs": [
            "CS116",
            "MATH203",
            "MATH205"
        ]
    },
    "ENE213": {
        "Name": "Electrical Circuits lab",
        "Prereqs": [
            "ENE211"
        ]
    },
    "BM3710": {
        "Name": "Numerical Methods for Engineers Lab",
        "Prereqs": []
    },
    "CE3561": {
        "Name": "Computer Networks lab",
        "Prereqs": [
            "CE201",
            "CS116"
        ]
    },
    "GERL301IT": {
        "Name": "German 5 technical for computer science, computer engineering, electrical and communication engineering",
        "Prereqs": []
    },
    "GERL302IT": {
        "Name": "German 6 technical for computer science, computer engineering, electrical and communication engineering",
        "Prereqs": []
    },
    "ECE241": {
        "Name": "Electronics I",
        "Prereqs": [
            "ENE211"
        ]
    },
    "ECE2410": {
        "Name": "Electronics I Lab",
        "Prereqs": []
    },
    "CE441": {
        "Name": "Embedded System Design",
        "Prereqs": [
            "CE201"
        ]
    },
    "CE592": {
        "Name": "Senior Project I",
        "Prereqs": []
    },
    "CE452": {
        "Name": "Network Protocols",
        "Prereqs": [
            "CE352"
        ]
    },
    "CS214": {
        "Name": "Object Oriented Programming",
        "Prereqs": [
            "CS116",
            "CS1160"
        ]
    },
}

def topological_sort_courses(data):
    sortedCourses = []
    graph = {}
    Edges = {}

    for course, courseData in data.items():
        prerequisites = courseData["Prereqs"]
        graph[course] = prerequisites
        Edges[course] = 0
        for prerequisite in prerequisites:
            Edges[prerequisite] = Edges.get(prerequisite, 0) + 1

    queue = deque()
    for course, inDegree in Edges.items():
        if inDegree == 0:
            queue.append(course)

    semesters = [[] for _ in range(10)]  # 5 years * 2 semesters

    while queue:
        course = queue.popleft()
        sortedCourses.append(course)
        prerequisites = graph[course]
        semester = find_semester(semesters, prerequisites)
        semesters[semester].append(course)
        for prerequisite in prerequisites:
            Edges[prerequisite] -= 1
            if Edges[prerequisite] == 0:
                queue.append(prerequisite)

    if len(sortedCourses) == len(data):
        return semesters
    else:
        raise ValueError("The course prerequisites contain a cycle.")

def find_semester(semesters, prerequisites):
    for i, semester in enumerate(semesters):
        if len(semester) + len(prerequisites) <= 6:
            return i
    return -1



sortedCourses = topological_sort_courses(data)

total_semesters = len(sortedCourses)
current_year = 5
current_semester = 2

for i, semester in enumerate(sortedCourses):
    print("Year", current_year, "Semester", current_semester, ":")
    courses_in_semester = semester[:6]  # Limit to 6 courses per semester
    for course in courses_in_semester:
        print(data[course]["Name"], "(", course, ")")
    print()

    if current_semester == 2:
        current_semester = 1
    else:
        current_year -= 1
        current_semester = 2