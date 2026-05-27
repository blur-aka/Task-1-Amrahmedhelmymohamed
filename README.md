# Rule-Based AI Chatbot

## Project Overview
This project is a simple rule-based AI chatbot developed using Python.

The chatbot interacts with users by responding to predefined inputs using rule-based logic and conditional matching. It continuously runs in a loop until the user decides to exit the conversation.

The project focuses on understanding the basics of Artificial Intelligence concepts such as control flow, input processing, and decision-making logic.

---

## Technologies Used
- Python
- Dictionaries
- While Loop
- If-Else Logic

---

## Project Files

| File Name | Format | Purpose |
|------------|---------|----------|
| Task1_decode.py | .py | Main chatbot source code |
| README.md | .md | Project documentation and instructions |

---

## How the System Works

1. The user enters a message.
2. The chatbot cleans the input using lower() and strip().
3. The system searches for a matching response inside a dictionary.
4. If a match is found, the chatbot replies with the predefined response.
5. If no match exists, the chatbot displays a default fallback message.

---

## Features
- Handles greetings
- Handles exit commands
- Uses rule-based responses
- Runs in a continuous loop
- Includes fallback responses for unknown inputs

---

## How to Run the Project

Run the following command:

```bash
python Task1_decode.py
```

---

## Example

### Input
```text
hello
```

### Output
```text
Hi how can i help you ?
```

### Input
```text
how are you
```

### Output
```text
Im pretty good and excited to talk to you
```
