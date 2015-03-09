class courseInfo(object):

    def __init__(self, courseName):
        self.courseName = courseName
        self.psetsDone = []
        self.grade = "No Grade"

    def setPset(self, pset, score):
        self.psetsDone.append((pset, score))

    def getPset(self, pset):
        for (p, score) in self.psetsDone:
            if p == pset:
                return score

    def setGrade(self, grade):
        if self.grade == "No Grade":
            self.grade = grade

    def getGrade(self):
        return self.grade



class edx(object):
    def __init__(self, courses): # courses: list
        self.myCourses = {} # list of courseInfo
        for course in courses:
            self.myCourses[course] = courseInfo(course)

    def setGrade(self, grade, course="6.01x"):
        """
        grade: integer greater than or equal to 0 and less than or equal to 100
        course: string

        This method sets the grade in the courseInfo object named by `course`.

        If `course` was not part of the initialization, then no grade is set, and no
        error is thrown.

        The method does not return a value.
        """
        #   fill in code to set the grade
        newCourse = courseInfo("6.01x")
        newCourse.setGrade(grade)
        self.myCourses[course] = newCourse

    def getGrade(self, course="6.02x"):
        """
        course: string

        This method gets the grade in the the courseInfo object named by `course`.

        returns: the integer grade for `course`.
        If `course` was not part of the initialization, returns -1.
        """
        #   fill in code to get the grade
        course = self.myCourses.get(course, -1)
        if course == -1:
            return course
        else:
            return course.getGrade()

    def setPset(self, pset, score, course="6.00x"):
        """
        pset: a string or a number
        score: an integer between 0 and 100
        course: string

        The `score` of the specified `pset` is set for the
        given `course` using the courseInfo object.

        If `course` is not part of the initialization, then no pset score is set,
        and no error is thrown.
        """
        #   fill in code to set the pset
        newCourse = courseInfo(course)
        newCourse.setPset(pset, score)
        self.myCourses[course] = newCourse

    def getPset(self, pset, course="6.00x"):
        """
        pset: a string or a number
        course: string

        returns: The score of the specified `pset` of the given
        `course` using the courseInfo object.
        If `course` was not part of the initialization, returns -1.
        """
        #   fill in code to get the pset
        course = self.myCourses.get(course, -1)
        if course == -1:
            return course
        else:
            return course.getPset(pset)


edX = edx( ["6.00x","6.01x","6.02x"] )
edX.setGrade(100, "6.00x")
edX.setGrade(90, "6.01x")
edX.setGrade(80, "6.02x")
edX.setGrade(50)

print edX.getGrade("6.00x")

print edX.getGrade("6.01x")

print edX.getGrade("6.02x")

print edX.getGrade()
