# DecoBot v2.0

DecoBot is a fully rule-based Python chatbot built with dictionary lookups, input sanitization, alias handling, and a simple fallback response. It does not use machine learning, APIs, databases, or a GUI.

## Project Structure

- `chatbot.py` - main application logic and chat loop
- `responses.py` - knowledge base, aliases, and lookup tables
- `README.md` - project overview and usage

## Features

- Rule-based responses only
- Name memory during the current session
- Alias handling for natural phrasing and common typos
- Input sanitization and error handling
- Exit commands and fallback response

## How to Run

```bash
python chatbot.py
```

## Notes

- The chatbot response text is unchanged.
- The project is intentionally kept simple and transparent.
- No additional dependencies are required beyond Python's standard library.

## Concepts Demonstrated

- Rule-Based AI
- Dictionaries (Hash Maps)
- Input Sanitization
- String Processing
- Control Flow
- Session Memory
- Error Handling

## Demo

![Demo](screenshots/demo.png)
