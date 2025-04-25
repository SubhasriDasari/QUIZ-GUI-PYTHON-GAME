
import tkinter as tk
from tkinter import messagebox

# Question Bank
questions = [
    {
        "PROMPT": "WHO DEVELOPED PYTHON PROGRAMMING LANGUAGE?",
        "OPTIONS": ["A. GUIDO VAN ROSSUM", "B. DENNIS RITCHIE", "C. RASMUS LERDORF", "D. NONE"],
        "ANSWER": "A"
    },
    {
        "PROMPT": "WHICH TYPE OF PROGRAMMING DOES PYTHON SUPPORT?",
        "OPTIONS": ["A. OBJECT ORIENTED PROGRAMMING", "B. STRUCTURED PROGRAMMING", "C. FUNCTIONAL PROGRAMMING", "D. ALL OF THE MENTIONED"],
        "ANSWER": "D"
    },
    {
        "PROMPT": "IS PYTHON CASE SENSITIVE WHEN DEALING WITH IDENTIFIERS?",
        "OPTIONS": ["A. NO", "B. YES", "C. MACHINE DEPENDENT", "D. NONE"],
        "ANSWER": "B"
    },
    {
        "PROMPT": "WHICH OF THE FOLLOWING IS THE CORRECT EXTENSION OF PYTHON FILE?",
        "OPTIONS": ["A. .python", "B. .pl", "C. .py", "D. .p"],
        "ANSWER": "C"
    },
    {
        "PROMPT": "WHAT IS THE OUTPUT OF: PRINT(2 ** 3 ** 2)?",
        "OPTIONS": ["A. 64", "B. 512", "C. 256", "D. 36"],
        "ANSWER": "B"
    },
    {
        "PROMPT": "WHICH KEYWORD IS USED FOR FUNCTION IN PYTHON?",
        "OPTIONS": ["A. FUNCTION", "B. DEF", "C. FUN", "D. DEFINE"],
        "ANSWER": "B"
    },
    {
        "PROMPT": "WHICH OF THE FOLLOWING DATA TYPES IS IMMUTABLE IN PYTHON?",
        "OPTIONS": ["A. LIST", "B. SET", "C. DICTIONARY", "D. TUPLE"],
        "ANSWER": "D"
    },
    {
        "PROMPT": "WHAT WILL BE THE OUTPUT OF: PRINT(TYPE([]))?",
        "OPTIONS": ["A. <class 'list'>", "B. <class 'tuple'>", "C. <class 'array'>", "D. <class 'set'>"],
        "ANSWER": "A"
    },
    {
        "PROMPT": "WHAT DOES THE LEN() FUNCTION DO?",
        "OPTIONS": ["A. RETURNS THE NUMBER OF ITEMS IN AN OBJECT", "B. RETURNS THE VALUE OF LAST ELEMENT", "C. CREATES A LIST", "D. PRINTS LENGTH ON SCREEN"],
        "ANSWER": "A"
    },
    {
        "PROMPT": "WHICH OF THE FOLLOWING IS USED TO DEFINE A BLOCK OF CODE IN PYTHON?",
        "OPTIONS": ["A. CURLY BRACKETS", "B. INDENTATION", "C. PARENTHESES", "D. SQUARE BRACKETS"],
        "ANSWER": "B"
    }
]

# Quiz App Class
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz App")
        self.root.geometry("700x450")
        self.root.resizable(False, False)

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), wraplength=650, justify="left")
        self.question_label.pack(pady=30)

        self.var = tk.StringVar()
        self.options = []

        for i in range(4):
            radio = tk.Radiobutton(root, text="", variable=self.var, value="", font=("Helvetica", 14))
            radio.pack(anchor="w", padx=40, pady=5)
            self.options.append(radio)

        self.submit_btn = tk.Button(root, text="Submit", command=self.check_answer, font=("Helvetica", 14), bg="skyblue")
        self.submit_btn.pack(pady=30)

        self.load_question()

    def load_question(self):
        question = questions[self.current_question]
        self.question_label.config(text=f"Q{self.current_question + 1}: {question['PROMPT']}")
        self.var.set(None)

        for i, option in enumerate(question["OPTIONS"]):
            self.options[i].config(text=option, value=option[0])

    def check_answer(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("Warning", "Please select an option!")
            return

        correct = questions[self.current_question]["ANSWER"]

        if selected == correct:
            self.score += 1
            messagebox.showinfo("Result", "✅ Correct!")
        else:
            messagebox.showinfo("Result", f"❌ Wrong! Correct Answer: {correct}")

        self.current_question += 1

        if self.current_question < len(questions):
            self.load_question()
        else:
            messagebox.showinfo("Quiz Completed", f"🎉 Your final score is: {self.score}/{len(questions)}")
            self.root.destroy()

# Run the Quiz App
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
