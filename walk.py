
import tkinter as tk
import random

root = tk.Tk()
root.title("Maths Quiz")
root.geometry("300x220")
root.configure(bg="#b3e6ff")

# Question + answer variables
num1 = tk.IntVar()
num2 = tk.IntVar()
correct_answer = tk.IntVar()

# Function to generate a new question
def new_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    num1.set(a)
    num2.set(b)
    correct_answer.set(a + b)
    question_label.config(text=f"What is {a} + {b}?")
    answer_entry.delete(0, tk.END)
    feedback_label.config(text="")

def check_answer():
    try:
        user_answer = int(answer_entry.get())
        if user_answer == correct_answer.get():
            feedback_label.config(text="✅ Correct!", fg="green")
            root.after(1500, new_question)  # after 1.5s, new question
        else:
            feedback_label.config(text=f"❌ Oops! It’s {correct_answer.get()}", fg="red")
            root.after(1500, new_question)
    except:
        feedback_label.config(text="Please enter a number.", fg="orange")

def end_quiz():
    root.destroy()

# Widgets
question_label = tk.Label(root, font=("Arial", 14), bg="#b3e6ff")
question_label.pack(pady=10)

answer_entry = tk.Entry(root, font=("Arial", 14))
answer_entry.pack(pady=5)

feedback_label = tk.Label(root, text="", font=("Arial", 12), bg="#b3e6ff")
feedback_label.pack(pady=5)

submit_button = tk.Button(root, text="Check Answer", command=check_answer, font=("Arial", 12))
submit_button.pack(pady=5)

end_button = tk.Button(root, text="End Quiz", command=end_quiz, font=("Arial", 12), bg="red", fg="white")
end_button.pack(pady=5)

# Start first question
new_question()

root.mainloop()
