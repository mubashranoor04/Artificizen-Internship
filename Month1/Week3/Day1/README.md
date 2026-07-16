# Day 1 – Introduction to LLMs, Generative AI & Groq API

## Overview

This project introduces the fundamentals of Large Language Models (LLMs), Generative AI, prompt engineering, and practical interaction with AI models using the Groq API.

The goal of this practice was to understand how modern AI systems work at a high level and learn how to communicate with LLMs through API calls. The implementation focused on securely connecting with Groq, experimenting with model parameters, creating reusable API functions, controlling model behavior through system prompts, and comparing different LLM models.

By completing this practice, I learned how to:

- Understand the difference between Artificial Intelligence, Machine Learning, Deep Learning, and Generative AI.
- Understand how Large Language Models generate responses using tokens and next-token prediction.
- Work with the Groq API to call open-source language models.
- Securely manage API keys using environment variables.
- Understand the impact of temperature on LLM output.
- Create reusable wrapper functions for AI API calls.
- Use system prompts to control model behavior and output format.
- Compare different LLM models based on response quality and token usage.

---

# Technologies Used

- Python
- Groq API
- Llama Models
- python-dotenv
- Virtual Environment (venv)

---

# Project Structure

```
Day1/
│
├── .env
├── .gitignore
├── requirements.txt
│
├── utils.py
│
├── q1_setup.py
├── q2_first_call.py
├── q3_temperature.py
├── q4_wrapper_function.py
├── q5_system_prompt.py
├── q6_model_comparison.py
│
└── README.md
```

---

# Files Description

## utils.py

Contains the reusable Groq API configuration and wrapper function.

Responsibilities:

- Loads environment variables.
- Initializes Groq client.
- Provides the reusable `ask()` function.
- Handles model selection, system prompts, temperature, and token limits.

---

## q1_setup.py

Verifies that the Groq API key is correctly loaded from the `.env` file.

---

## q2_first_call.py

Makes the first API call using the Groq API and generates a response from an LLM.

---

## q3_temperature.py

Tests the effect of temperature values on LLM creativity and response consistency.

---

## q4_wrapper_function.py

Demonstrates how to use the reusable `ask()` function created in `utils.py`.

---

## q5_system_prompt.py

Tests how system prompts influence model behavior and output formatting.

---

## q6_model_comparison.py

Compares different Groq models using the same prompt and evaluates response quality and token usage.

---

# Environment Setup

## Create Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

---

## Install Dependencies

```bash
pip install groq python-dotenv
```

---

## Configure API Key

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

The API key is loaded using:

```python
load_dotenv()
```

and accessed using:

```python
os.getenv("GROQ_API_KEY")
```

The API key is not directly written inside Python files to maintain security.

---

# Concepts Learned

## Artificial Intelligence (AI)

Artificial Intelligence is the broader field of creating systems capable of performing tasks that normally require human intelligence.

Examples:

- Voice assistants
- Recommendation systems
- Autonomous vehicles

---

## Machine Learning (ML)

Machine Learning is a branch of AI where systems learn patterns from data instead of being explicitly programmed.

Example:

A model learning to predict house prices from previous examples.

---

## Deep Learning

Deep Learning is a subset of Machine Learning that uses artificial neural networks with multiple layers to learn complex patterns.

Examples:

- Image recognition
- Speech processing
- Natural language processing

---

## Generative AI

Generative AI refers to systems that can create new content such as:

- Text
- Images
- Code
- Audio

Examples:

- AI chatbots
- AI coding assistants
- Image generation systems

---

# Large Language Models (LLMs)

Large Language Models are AI models trained on massive amounts of text data to understand and generate human-like language.

LLMs work by predicting the next most likely token based on previous context.

Example:

Input:

```
The sky is
```

The model predicts:

```
blue
```

---

# Tokens

Tokens are small units of text processed by language models.

A token may represent:

- A complete word
- Part of a word
- A symbol

Tokens are important because:

- API usage is measured in tokens.
- Context limits depend on token count.
- Longer prompts consume more resources.

---

# Context Window

The context window represents the maximum amount of information a model can process at one time.

Exceeding the context limit may result in:

- Missing information
- Truncated input
- Reduced response quality

---

# Groq API

Groq is an inference provider that allows developers to run open-source AI models at very high speed using specialized hardware.

Groq provides access to models including:

- llama-3.1-8b-instant
- llama-3.3-70b-versatile
- Mixtral models

Groq provides model inference but does not create the underlying models.

---

# Practice Question 1: API Setup

## Objective

Securely load the Groq API key using environment variables.

## Implementation

The API key was stored inside `.env` and loaded using `python-dotenv`.

Example:

```python
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
```

## Output

```
API key loaded successfully!
```

## What I Learned

- How to store sensitive information securely.
- Why API keys should never be hardcoded.
- How environment variables are used in real applications.

---

# Practice Question 2: First Groq API Call

## Objective

Make the first LLM request using the Groq API.

## Model Used

```
llama-3.1-8b-instant
```

## Prompt

```
Summarise what a transformer model does in 3 sentences.
```

## What Was Implemented

- Initialized Groq client.
- Sent a chat completion request.
- Retrieved generated response.
- Displayed token usage information.

## What I Learned

- How API-based AI applications communicate with language models.
- How responses are retrieved from the API response object.
- How token usage is tracked.

---

# Practice Question 3: Temperature Experiment

## Objective

Understand how temperature affects LLM responses.

The same prompt was executed multiple times using:

```
temperature = 0
```

and

```
temperature = 1.0
```

## Results

### Temperature = 0

The model generated:

- More predictable responses.
- Similar outputs across multiple runs.
- Less variation.

### Temperature = 1.0

The model generated:

- More creative responses.
- More diverse ideas.
- Increased randomness.

## Observation

```
Lower temperature produces deterministic and consistent responses, while higher temperature increases creativity and variation in generated outputs.
```

## What I Learned

Temperature controls the randomness of token selection during generation.

---

# Practice Question 4: Wrapper Function

## Objective

Create a reusable function for Groq API calls.

## Implementation

A reusable function named:

```python
ask()
```

was created inside:

```
utils.py
```

The function handles:

- Prompt input.
- System messages.
- Model selection.
- Temperature.
- Maximum output tokens.

Example:

```python
response = ask(
    "Explain what a transformer model does."
)
```

## What I Learned

- How abstraction improves code reusability.
- How AI services can be wrapped into simple functions.
- How reusable components simplify future AI application development.

---

# Practice Question 5: System Prompt Experiment

## Objective

Test how system instructions influence LLM behavior.

## System Prompt

```
You are a strict JSON-only responder.
Never output anything outside a JSON object.
```

## Implementation

The model was instructed to return information about Python programming only in JSON format.

## Example Response

```json
{
  "name": "Python",
  "description": "High-level, interpreted programming language",
  "usecases": [
    "Web development",
    "Data analysis",
    "Machine learning"
  ]
}
```

## Observation

The model successfully followed the system instruction and returned only JSON output.

## What I Learned

- System prompts define model behavior.
- Prompt engineering can control response format.
- LLM instructions can influence output structure.

---

# Practice Question 6: Model Comparison

## Objective

Compare different Groq models using the same prompt.

## Prompt Used

```
Explain deep learning in simple words.
```

## Models Compared

1. llama-3.1-8b-instant
2. llama-3.3-70b-versatile

---

# Results

## llama-3.1-8b-instant

Characteristics:

- Faster response generation.
- Simpler explanation.
- Suitable for lightweight applications.

Total Tokens:

```
243
```

Response Style:

The model explained deep learning using simple examples and focused on beginner-level understanding.

---

## llama-3.3-70b-versatile

Characteristics:

- More detailed reasoning.
- Better structured explanation.
- Higher-quality responses.

Total Tokens:

```
243
```

Response Style:

The model explained deep learning using neural network layers and provided more technical detail.

---

# Comparison Observation

The llama-3.3-70b-versatile model produced a more detailed and structured explanation, while llama-3.1-8b-instant generated a simpler response with faster inference.

The larger model is more suitable for tasks requiring stronger reasoning and deeper explanations, while the smaller model is useful for applications where speed and efficiency are more important.

---

# Additional Concepts Learned

## Chat Completion Format

LLM APIs use different message roles:

### System

Defines model behavior.

Example:

```
You are a helpful assistant.
```

### User

Contains the user request.

Example:

```
Explain AI.
```

### Assistant

Contains the generated response.

---

## Important API Parameters

### Temperature

Controls randomness.

Lower value:

- More predictable output.

Higher value:

- More creative output.

---

### Max Tokens

Controls maximum response length.

---

### Top P

Controls the range of token choices considered during generation.

---

### Stop

Defines sequences where generation should stop.

---

# Summary

By completing Day 1, I learned the fundamentals of Large Language Models and practical AI development using the Groq API.

I implemented API communication, secure environment configuration, temperature experimentation, reusable AI functions, system prompt engineering, and model comparison.

These concepts provide the foundation required for future topics including:

- Prompt Engineering
- Embeddings
- Retrieval-Augmented Generation (RAG)
- AI-powered applications