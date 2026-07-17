# Week 3 - Day 2: Prompt Engineering

## Overview

This project demonstrates fundamental prompt engineering techniques using the Groq API and Large Language Models (LLMs). The exercises focus on designing effective prompts, controlling model behavior, structuring outputs, and understanding common prompting strategies.

The project consists of six practice tasks covering zero-shot prompting, few-shot prompting, chain-of-thought reasoning, role prompting, prompt chaining, and prompt injection defense.

---

## Topics Covered

- Zero-shot Prompting
- Few-shot Prompting
- Chain-of-Thought (CoT) Prompting
- Role Prompting
- Prompt Chaining
- Prompt Injection
- Output Format Control
- Negative Constraints
- Instruction Clarity

---

## Project Structure

```
Day2/
│── .env
│── utils.py
│── zero_shot.py
│── few_shot.py
│── cot.py
│── role_prompting.py
│── 3_step_prompt.py
│── prompt_injection.py
│── README.md
```

---

## Requirements

Install the required packages before running the programs.

```bash
pip install groq python-dotenv
```

---

## Environment Variables

Create a `.env` file in the project directory and add your Groq API key.

```env
GROQ_API_KEY=your_api_key_here
```

---

## Files Description

### `utils.py`

Contains the reusable `ask()` function responsible for sending prompts to the Groq API.

---

### `zero_shot.py`

Classifies customer messages into one of the following categories without providing any examples:

- Complaint
- Question
- Compliment

---

### `few_shot.py`

Performs the same classification task as the zero-shot example but includes labeled examples inside the prompt to guide the model.

---

### `cot.py`

Compares model responses with and without Chain-of-Thought prompting using a simple logic puzzle.

---

### `role_prompting.py`

Uses a system prompt to assign the model the role of a senior Python code reviewer that provides concise and actionable feedback.

---

### `3_step_prompt.py`

Implements a three-step prompt chain:

1. Extract action items from a meeting transcript.
2. Assign priorities to each action item.
3. Convert the results into a structured JSON array.

---

### `prompt_injection.py`

Demonstrates a basic prompt injection attack and then shows how stronger system instructions can prevent the model from following malicious embedded instructions.

---

## Learning Outcomes

After completing this project, the following prompt engineering concepts were practiced:

- Designing effective prompts
- Using examples to improve consistency
- Encouraging step-by-step reasoning
- Controlling model behavior with system prompts
- Structuring model outputs
- Breaking complex tasks into prompt chains
- Defending against prompt injection
- Writing clear and specific instructions

---

## Model Used

- Llama 3.1 8B Instant
- Provider: Groq

---

## How to Run

Run any Python file individually.

Example:

```bash
python zero_shot.py
```

or

```bash
python few_shot.py
```

Similarly, run the remaining scripts:

```bash
python cot.py
python role_prompting.py
python 3_step_prompt.py
python prompt_injection.py
```

---

## Notes

- Ensure the `.env` file contains a valid Groq API key.
- Install all required dependencies before running the scripts.
- Each file demonstrates a different prompt engineering technique and can be executed independently.