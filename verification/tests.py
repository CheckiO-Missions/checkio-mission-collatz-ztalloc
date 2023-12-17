"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["ududududddddudddd"],
            "answer": 15,
        },
        {
            "input": [135],
            "answer": "udududduddddududdudduddddudududdudddudddd",
        },
        {
            "input": ["dudududdudddudddd"],
            "answer": 14,
        },
        {
            "input": [10],
            "answer": "dudddd",
        },
        {
            "input": ["uduuudddd"],
            "answer": None,
        },
    ],
    "Extra": [
        {
            "input": ["d"],
            "answer": 2,
        },
        {
            "input": [18],
            "answer": "duddudududdudddudddd",
        },
        {
            "input": ["uuududdddduuuuuuudddddd"],
            "answer": None,
        },
        {
            "input": [101],
            "answer": "uddddududddududdudddudddd",
        },
        {
            "input": ["duuudddddddd"],
            "answer": None,
        },
    ]
}
