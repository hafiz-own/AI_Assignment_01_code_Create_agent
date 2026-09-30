Grades = [
    (85, 4.0),
    (80, 3.7),
    (75, 3.3),
    (70, 3.0),
    (65, 2.7),
    (61, 2.3),
    (58, 2.0),
    (55, 1.7),
    (50, 1.0),
    (0, 0.0),
]

COURSES = {
    1: [
        ("MS-251", "Probability & Statistics", 3.0),
        ("GE-160", "Applications of ICT", 3.0),
        ("GE-169", "Applied Physics", 3.0),
        ("GE-167", "Discrete Structures", 3.0),
        ("HQ-001", "Quran Translation - I", 0.5),
        ("GE-190", "Functional English", 3.0),
    ],
    2: [
        ("CC-112", "Programming Fundamentals", 3.0),
        ("CC-112-L", "Programming Fundamentals Lab", 1.0),
        ("CC-110", "Digital Logic Design", 2.0),
        ("CC-110-L", "Digital Logic Design Lab", 1.0),
        ("MS-252", "Linear Algebra", 3.0),
        ("GE-191", "Expository Writing", 3.0),
        ("GE-163", "Islamic Studies", 2.0),
        ("HQ-002", "Quran Translation - II", 0.5),
    ],
    3: [
        ("CC-211", "Object Oriented Programming", 3.0),
        ("CC-211-L", "Object Oriented Programming Lab", 1.0),
        ("CC-215", "Database Systems", 3.0),
        ("CC-215-L", "Database Systems Lab", 1.0),
        ("CC-210", "Computer Organization & Assembly Language", 3.0),
        ("GE-162", "Calculus & Analytical Geometry", 3.0),
        ("GE-192", "Introduction to Management", 2.0),
        ("HQ-003", "Quran Translation - III", 0.5),
    ],
    4: [
        ("CC-213", "Data Structures", 3.0),
        ("CC-213-L", "Data Structures Lab", 1.0),
        ("CC-312", "Information Security", 3.0),
        ("CC-214", "Computer Networks", 3.0),
        ("CC-212", "Software Engineering", 3.0),
        ("DC-220", "Advanced Database Management Systems", 3.0),
        ("HQ-004", "Quran Translation - IV", 0.5),
    ],
    5: [
        ("CC-313", "Analysis of Algorithms", 3.0),
        ("CC-310", "Artificial Intelligence", 3.0),
        ("DC-320", "Theory of Automata and Formal Languages", 3.0),
        ("DC-321", "Human Computer Interaction", 3.0),
        ("DC-322", "Computer Architecture", 3.0),
        ("EC-330", "Web Technologies / Elective", 3.0),
        ("HQ-005", "Quran Translation - V", 0.5),
    ],
    6: [
        ("CC-311", "Operating Systems", 3.0),
        ("EC-333", "Mobile Application Development / Elective", 3.0),
        ("EC-324", "Software Construction & Development / Elective", 3.0),
        ("EC-335", "Machine Learning / Elective", 3.0),
        ("EC-334", "Game Design and Development / Elective", 3.0),
        ("MS-253", "Multivariable Calculus", 3.0),
        ("HQ-006", "Quran Translation - VI", 0.5),
    ],
    7: [
        ("CC-411", "Final Year Project - I", 2.0),
        ("DC-328", "Parallel & Distributed Computing", 3.0),
        ("EC-345", "Computer Vision / Elective", 3.0),
        ("EC-425", "Software Quality Engineering / Elective", 3.0),
        ("MS-254", "Technical and Business Writing", 3.0),
        ("GE-263", "Entrepreneurship", 2.0),
        ("GE-262", "Professional Practices", 2.0),
        ("HQ-007", "Quran Translation - VII", 0.5),
    ],
    8: [
        ("CC-412", "Final Year Project - II", 4.0),
        ("DC-421", "Compiler Construction", 3.0),
        ("UE-272", "Introduction to Marketing", 3.0),
        ("GE-168", "Ideology and Constitution of Pakistan", 2.0),
        ("GE-363", "Civics and Community Engagement", 2.0),
        ("HQ-008", "Quran Translation - VIII", 0.5),
    ],
}


def calculate_semester_gpa(
    grade_points: list[float], credit_hours: list[float]
) -> float:
    """Calculates the GPA for a single semester.

    Pass two parallel lists: grade_points[i] is the grade point for the course
    whose credit hours are credit_hours[i]. Both lists must be the same length and
    in the same order. Obtain grade points via marks_to_grade_points and credit hours
    via get_semester_courses. Returns the weighted-average GPA (0.0 to 4.0).
    """
    total_grade_points = sum(gp * ch for gp, ch in zip(grade_points, credit_hours))
    total_credit_hours = sum(credit_hours)
    return total_grade_points / total_credit_hours if total_credit_hours > 0 else 0.0


def marks_to_grade_points(marks: int) -> float:
    """Converts a numeric exam mark (0-100) to a grade point on the 4.0 scale.

    Call this once per course before calling calculate_semester_gpa.
    Returns a float such as 4.0, 3.7, 3.3, down to 0.0.
    """
    for threshold, grade_point in Grades:
        if marks >= threshold:
            return grade_point
    return 0.0


def calculate_new_cgpa(
    current_cgpa: float,
    completed_credit_hours: float,
    semester_gpta: float,
    semester_credit_hours: float,
) -> float:
    """Projects the new CGPA after adding one semester's results.

    Use this to answer 'what will my CGPA be after this semester?' or to find
    the best possible CGPA a student can reach.
    - completed_credit_hours: total credit hours already graded (use get_total_credit_hours).
    - semester_gpta: GPA earned (or hypothetical GPA) in the new semester.
    - semester_credit_hours: credit hours of the new semester (use get_total_credit_hours).
    Returns the updated cumulative GPA.
    """
    total_grade_points = (current_cgpa * completed_credit_hours) + (
        semester_gpta * semester_credit_hours
    )
    total_credit_hours = completed_credit_hours + semester_credit_hours
    return total_grade_points / total_credit_hours if total_credit_hours > 0 else 0.0


def calculate_gpa_for_target(
    target_cgpa: float,
    current_cgpa: float,
    completed_credit_hours: float,
    remaining_credit_hours: float,
) -> float:
    """Calculates the GPA a student must average across remaining semesters to hit a target CGPA.

    - target_cgpa: the desired final CGPA (e.g. 3.8).
    - current_cgpa: the student's current CGPA over completed semesters.
    - completed_credit_hours: sum of credit hours already graded; obtain with get_total_credit_hours.
    - remaining_credit_hours: credit hours in the window being planned; obtain with get_total_credit_hours.
    If the returned value exceeds 4.0 the target is impossible in that window - widen the window.
    If the returned value is <= 0.0 the target is already secured.
    """
    total_grade_points_needed = target_cgpa * (
        completed_credit_hours + remaining_credit_hours
    )
    current_grade_points = current_cgpa * completed_credit_hours
    required_grade_points = total_grade_points_needed - current_grade_points
    return (
        required_grade_points / remaining_credit_hours
        if remaining_credit_hours > 0
        else 0.0
    )


def get_semester_courses(semester: int) -> list[tuple[str, str, float]]:
    """Returns the list of courses for a given semester number (1-8).

    Each entry is a tuple of (course_code, course_name, credit_hours).
    Use this to look up credit hours for a specific course or to list all courses
    in a semester. Valid semester numbers are 1 through 8.
    """
    return COURSES.get(semester, [])


def get_total_credit_hours(semesters: list[int]) -> float:
    """Returns the total credit hours for a given list of semester numbers.

    Pass a list of semester integers to get their combined credit-hour total.
    Common uses:
    - Completed credit hours: pass [1, 2, ..., n] for the semesters already graded.
      e.g. if the student has completed 6 semesters: get_total_credit_hours([1,2,3,4,5,6])
    - Remaining credit hours: pass the semesters still to be taken.
      e.g. for a student currently in semester 7: get_total_credit_hours([7, 8])
    - Single-semester credit hours: get_total_credit_hours([7])
    - Full programme total: get_total_credit_hours([1,2,3,4,5,6,7,8])
    Never ask the student for credit-hour totals - always derive them with this tool.
    """
    return sum(
        credit_hours
        for semester in semesters
        for _, _, credit_hours in COURSES.get(semester, [])
    )


def save_report(filename: str, content: str) -> None:
    """Saves a plain-text report to a file on disk.

    Only call this when the student explicitly asks to save.
    - filename: a descriptive name such as 'cgpa_plan.txt'.
    - content: a short plain-text summary of the result and how it was reached.
    """
    with open(filename, "w") as file:
        file.write(content)


tools = [
    calculate_semester_gpa,
    marks_to_grade_points,
    calculate_new_cgpa,
    calculate_gpa_for_target,
    get_semester_courses,
    get_total_credit_hours,
    save_report,
]
