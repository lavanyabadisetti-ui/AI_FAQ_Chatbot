# AI_FAQ_Chatbot

🤖 AI FAQ Chatbot using Python & Fuzzy Matching

## 📌 Project Overview

This project is a simple yet intelligent **AI FAQ Chatbot** developed using **Python** as part of **Task 2 of the CodeAlpha AI Internship Program**.

The chatbot is designed to answer frequently asked questions (FAQs) by matching user queries with predefined questions stored in a knowledge base. Instead of relying on exact keyword matching, the chatbot uses Python's **Fuzzy Matching Technique** (`difflib.get_close_matches`) to understand user inputs even when they contain spelling mistakes, different wording, or minor variations.

This makes the chatbot more flexible, user-friendly, and intelligent compared to traditional rule-based chatbots.

---

## 🎯 Internship Task Information

**Internship:** AI Internship Program

**Organization:** CodeAlpha

**Task Number:** Task 2

**Project Title:** AI FAQ Chatbot

**Technology Used:** Python

**AI Concept Implemented:** Fuzzy String Matching

---

## 🚀 Features

✅ Interactive command-line chatbot

✅ Answers frequently asked questions

✅ Uses fuzzy matching to understand similar questions

✅ Handles minor spelling mistakes

✅ User-friendly conversation flow

✅ Exit command support

✅ Lightweight and easy to run

✅ No external libraries required

✅ Beginner-friendly AI project

---

## 🧠 How It Works

### Step 1: Knowledge Base Creation

A dictionary (`faqs`) is created containing predefined questions and answers.

Example:

```python
faqs = {
    "hi": "Hello! How can I help you?",
    "what is your name?": "I am the FAQ chatbot",
    "what do you do?": "I answer frequently asked questions"
}
````

---

### Step 2: User Input

The chatbot continuously asks the user to enter a question.

```python
user_input = input("USER: ").strip().lower()
```

---

### Step 3: Fuzzy Matching

The chatbot uses Python's built-in `difflib` module.

```python
from difflib import get_close_matches
```

It compares the user's question with all available FAQ questions.

```python
matches = get_close_matches(
    user_input,
    faqs.keys(),
    n=1,
    cutoff=0.6
)
```

#### Parameters:

| Parameter     | Description                       |
| ------------- | --------------------------------- |
| `user_input`  | User's question                   |
| `faqs.keys()` | Available FAQ questions           |
| `n=1`         | Returns best matching question    |
| `cutoff=0.6`  | Minimum similarity score required |

---

### Step 4: Response Generation

If a matching question is found:

```python
print("BOT:", faqs[best_match])
```

Otherwise:

```python
print("BOT: Sorry, I couldn't find an answer.")
```

---

## 🔍 Understanding Fuzzy Matching

Fuzzy Matching is a technique used to find strings that are approximately similar rather than exactly identical.

### Example

| User Input      | Stored Question    | Match Result |
| --------------- | ------------------ | ------------ |
| hii             | hi                 | ✅ Matched    |
| whats your name | what is your name? | ✅ Matched    |
| good mornng     | good morning       | ✅ Matched    |
| what do u do    | what do you do?    | ✅ Matched    |

This improves chatbot usability and creates a better user experience.

---

## 📂 Project Structure


AI-FAQ-Chatbot/
│
├── chatbot_faq.py
├── README.md


---

## 🛠 Technologies Used

| Technology                | Purpose                   |
| ------------------------- | ------------------------- |
| Python                    | Core programming language |
| difflib                   | Fuzzy string matching     |
| Dictionary Data Structure | FAQ knowledge base        |
| Command Line Interface    | User interaction          |

---

## 💡 Applications

This chatbot concept can be used in:

* Customer Support Systems
* Educational FAQ Assistants
* College Information Bots
* Company Help Desks
* Product Information Systems
* Banking FAQ Assistants
* Healthcare Information Chatbots
* E-commerce Customer Service

---

## 🔮 Future Enhancements

Some improvements that can be added in future versions:

* GUI using Tkinter
* Web Interface using Flask
* Database Integration
* Speech Recognition
* Text-to-Speech Responses
* NLP-based Intent Recognition
* Machine Learning Integration
* OpenAI API Integration
* Multi-language Support
* Context-Aware Conversations

---

## 📚 Learning Outcomes

Through this project, I learned:

* Python programming fundamentals
* Dictionary-based knowledge representation
* String similarity concepts
* Fuzzy matching algorithms
* User input handling
* Command-line application development
* Basic AI chatbot development

---

## 📖 Key Concepts Used

### Artificial Intelligence

The chatbot demonstrates a basic AI approach by interpreting user queries and providing relevant responses.

### Natural Language Interaction

Users communicate with the chatbot using natural language questions.

### Fuzzy String Matching

Allows the chatbot to recognize similar questions even when they are not typed exactly.

### Rule-Based Response System

Responses are generated from a predefined FAQ database.

---

## 🏆 Project Highlights

* Developed as part of the **CodeAlpha AI Internship**
* Implements an intelligent FAQ system
* Uses fuzzy matching instead of exact keyword matching
* Beginner-friendly AI application
* Demonstrates practical use of Python's built-in AI-related utilities

---

## 👩‍💻 Author

**Lavanya Badisetti**

AI Intern – CodeAlpha

Task 2: AI FAQ Chatbot

---

## 📜 License

This project is developed for educational and internship purposes under the CodeAlpha AI Internship Program.

