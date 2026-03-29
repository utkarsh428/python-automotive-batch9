# Student class
class Student:
    def __init__(self, std_id):
        # Store student ID
        self.std_id = std_id

    def queue_logic(self):
        # Split 'std_001' → ['std', '001']
        # Convert '001' → 1
        return int(self.std_id.split('_')[1])


# ParticipationQueue class (inherits Student)
class ParticipationQueue(Student):

    # Class-level lists (shared by all students)
    even_students = []
    odd_students = []

    def apply_logic(self):
        # Get number from student ID
        number = self.queue_logic()

        # Check even or odd
        if number % 2 == 0:
            ParticipationQueue.even_students.append(self.std_id)
        else:
            ParticipationQueue.odd_students.append(self.std_id)

        # Return processed student ID
        return self.std_id


# List of student IDs
student_list = [ 'std_001', 'std_002', 'std_003',
                 'std_004','std_005','std_006',
                 'std_007','std_008','std_009',
                 'std_010' ]

# Process each student one by one
for i in student_list:
    student = ParticipationQueue(i)
    print("Processed:", student.apply_logic())

# Show final queues
print("\nEven Students:", ParticipationQueue.even_students)
print("Odd Students:", ParticipationQueue.odd_students)