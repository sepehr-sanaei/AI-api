lesson_count = int(input("How many lesson do you want to study today? "))
free_hours = int(input("How many hours are you free per day? "))

lesson = {}


for i in range (lesson_count):
    lesson_name =input("Enter name of Lesson: ")
    credits = int(input("How many credits is the lesson? "))
    lesson[lesson_name] = credits

total_credits = sum(lesson.values())
hour_per_credit= free_hours / total_credits

print("\nstudy plan: ")
for name, credit in lesson.items():
    hours = credit * hour_per_credit
    print(f"{name}: {hours:.2f} hours")
