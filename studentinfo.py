student_info = {
    "name": "John",
    "age": 20,
    "subjects": ["Math", "Science", "English"],
    "grades": {
        "Math": 95,
        "Science": 88,
        "English": 90
    }
}
for key, value in student_info.items():
    print(f"{key}: {value}")

# asks for user input and capitalize it so that it matches the subject in the dictionary
user_input = input("Enter a subject: ").strip().capitalize()
if user_input in student_info["subjects"]:
    print(f"Grade for {user_input}: {student_info['grades'][user_input]}")
else:
    print("Subject not found")
for grade in student_info["grades"].values():
    print(grade)
average = sum(student_info["grades"].values()) / len(student_info["grades"])
print(f"Average grade: {average}")


student_info["grades"]["History"] = 96
student_info["subjects"].append("History")
print(student_info)











