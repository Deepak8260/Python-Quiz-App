Quiz Application
================

This project is a simple command-line quiz application built using Python. The application loads questions from a JSON file, presents them to the user, and calculates their score based on their answers.

Features
--------

*   Loads quiz questions from a JSON file.
    
*   Displays multiple-choice questions with four options.
    
*   Calculates and displays the user's score at the end.
    
*   User-friendly command-line interface.
    

Files
-----

1.  **app.py** - The Python script that runs the quiz application.
    
2.  **x.json** - A JSON file containing the quiz questions, options, and correct answers.
    

Requirements
------------

*   Python 3.x
    

How It Works
------------

1.  **Load Questions:** The QuizApp class loads quiz questions from the JSON file x.json.
    
2.  **Ask Questions:** The ask\_question method displays each question along with four options.
    
3.  **User Input:** The user selects an answer by entering a number corresponding to one of the four options.
    
4.  **Score Calculation:** The user's score is updated after each question based on whether their answer is correct or not.
    
5.  **Display Results:** After all questions are answered, the final score is displayed.
    

JSON File Format
----------------

The x.json file contains an array of questions. Each question is represented by a dictionary with the following keys:

*   **question**: The question text.
    
*   **options**: A list of four possible answer options.
    
*   **answer**: The correct answer.
    

Example of a question in the JSON file:

```bash
{
    "question": "What is the capital of France?",
    "options": ["Paris", "Berlin", "Rome", "Madrid"],
    "answer": "Paris"
}

```

How to Run the Project
----------------------

1.  Clone this repository to your local machine.
    
2.  Make sure you have Python 3.x installed.
    
3.  Place your JSON file (e.g., x.json) in the same directory as app.py.
    
4.  bashCopy codepython app.py
    
5.  The quiz will start, and you will be prompted to answer the questions.
    

Example Output
--------------
```bash
Welcome to the Quiz!

What is the capital of France?
1. Paris
2. Berlin
3. Rome
4. Madrid
Your choice (1/2/3/4): 1
Correct! 🎉

What is 2 + 2?
1. 3
2. 4
3. 5
4. 6
Your choice (1/2/3/4): 2
Correct! 🎉

Which programming language is known for its simplicity and readability?
1. Python
2. Java
3. C++
4. Ruby
Your choice (1/2/3/4): 1
Correct! 🎉

What is the largest planet in our solar system?
1. Earth
2. Mars
3. Jupiter
4. Saturn
Your choice (1/2/3/4): 3
Correct! 🎉

Who wrote the play 'Romeo and Juliet'?
1. Charles Dickens
2. William Shakespeare
3. Mark Twain
4. Jane Austen
Your choice (1/2/3/4): 2
Correct! 🎉

Quiz over! Your score: 5/5

```

Error Handling
--------------

*   If the JSON file is not found or contains invalid data, an error message will be displayed, and the quiz will not run.
    
*   The application handles invalid user input (e.g., entering a number outside the range 1-4) and prompts the user again.
    

Customization
-------------

*   You can modify the x.json file to add more questions, change existing ones, or update the options and answers.
    

License
-------

This project is open source and available under the MIT License.
