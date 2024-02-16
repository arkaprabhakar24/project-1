# main.py
from kivymd.app import MDApp
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

# Load the KV file
Builder.load_file('studentattendance.kv')

class StudentAttendanceApp(MDApp):
    def build(self):
        self.students = {}

        layout = MDBoxLayout(orientation='vertical', spacing=10)

        label = MDLabel(text="Student Attendance Management System", size_hint_y=None, height=50)
        layout.add_widget(label)

        self.student_name_input = MDTextField(hint_text="Enter Student Name")
        layout.add_widget(self.student_name_input)

        add_student_button = MDRaisedButton(text="Add Student", on_release=self.add_student)
        layout.add_widget(add_student_button)

        mark_attendance_button = MDRaisedButton(text="Mark Attendance", on_release=self.mark_attendance)
        layout.add_widget(mark_attendance_button)

        view_attendance_button = MDRaisedButton(text="View Attendance", on_release=self.view_attendance)
        layout.add_widget(view_attendance_button)

        self.present_list = ScrollView()
        layout.add_widget(self.present_list)

        self.absent_list = ScrollView()
        layout.add_widget(self.absent_list)

        return layout

    def add_student(self, instance):
        student_name = self.student_name_input.text.strip()
        if student_name:
            self.students[student_name] = []
            self.update_attendance_list()
            self.student_name_input.text = ""
        else:
            print("Please enter a valid student name!")

    def mark_attendance(self, instance):
        student_name = self.student_name_input.text.strip()
        if student_name in self.students:
            is_present = True  # For simplicity, assume present
            self.students[student_name].append("Present" if is_present else "Absent")
            self.update_attendance_list()
        else:
            print(f"Student {student_name} not found!")

    def update_attendance_list(self):
        present_text = ""
        absent_text = ""
        for student, attendance in self.students.items():
            student_info = f"{student}: {', '.join(attendance)}\n"
            if "Present" in attendance:
                present_text += student_info
            else:
                absent_text += student_info

        self.present_list.clear_widgets()
        self.present_list.add_widget(MDLabel(text="Present Students:\n" + present_text))

        self.absent_list.clear_widgets()
        self.absent_list.add_widget(MDLabel(text="Absent Students:\n" + absent_text))

    def view_attendance(self, instance):
        self.update_attendance_list()

if __name__ == '__main__':
    StudentAttendanceApp().run()