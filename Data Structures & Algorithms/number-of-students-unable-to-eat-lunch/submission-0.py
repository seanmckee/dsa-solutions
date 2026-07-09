from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)

        rotations = 0

        while students and sandwiches:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                rotations = 0
            else:
                students.append(students.popleft())
                rotations += 1

            if rotations == len(students):
                return len(students)

        return 0