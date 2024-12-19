
genre_mapping = {"comedy", "thriller", "animation", "sci-fiction", "adventure",
                     "action", "crime", "war", "drama", "history", "fantasy"
                     "biography", "romantic"}

def genre_mapping(question): 
    Q1 = input('How are you feeling today?')
    Q2 = input('What kind of film do you like?')
    Q3 = input('Are you going to watch movies alone?')
    Q4 = input('Do you pay attention to imbd scores?')
    Q5 = input('Which country movies do you usually like?')
    Q6 = input('Do you have a favourite actor?')
    Q7 = input('How much time do you have to watch movies?')            
    print(Q1)
    
    
def questions_function(): 
    questions = [
        "How are you feeling today?", 
        "What kind of film do you like?",
        "Are you going to watch movies alone?",
        "Do you pay attention to imbd scores?",
        "Which country movies do you usually like?",
        "Do you have a favourite actor?",
        "How much time do you have to watch movies?" 
        ]
    answers = {}
    for question in questions :
        answer = input(question)
        answers[question] = answer 
    for question, answer in answers.items():
        print(f"{question}: {answer}")
    return answers

user_answers = questions_function()

        
    
    