data = [
  {
    "question": "What is the largest mammal?",
    "options": ["Blue Whale", "Giraffe", "Elephant", "Rhino"],
    "answer": "a"
  },
  {
    "question": "Who invented Python?",
    "options": ["Guido van Rossum", "Bjarne Stroustrup", "Brendan Eich", "James Gosling"],
    "answer": "a"
  }
]
points = 0
print("Hello here are the questions\n")
for x in data:
  print(x["question"])
  print(x["options"])
  myanswer = str(input())
  if myanswer == x["answer"]:
    print("yes")
    points = points+1
  else:
    print(f"wrong, correct answer: {x["answer"]}")

print(f"Total Points:{points}")