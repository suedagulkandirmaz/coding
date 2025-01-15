from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import csv
import random


def cache_data():
    with open("movies1.csv", "r", encoding="utf-8") as read_file:
        csv_reader = csv.reader(read_file)
        list_of_movies = list(csv_reader)
    return list_of_movies


def filter_genre(genres):
    for i in range(len(movie_data)):
        if any(genre in movie_data[i][3] for genre in genres):
            filtered.append(movie_data[i])


def year_answer_true():
    if yearAnswerTrue:
        yearAnswerFalse.set(False)


def year_answer_false():
    if yearAnswerFalse:
        yearAnswerTrue.set(False)


def partner_answer_true():
    if partnerAnswerTrue:
        partnerAnswerFalse.set(False)


def partner_answer_false():
    if partnerAnswerFalse:
        partnerAnswerTrue.set(False)


def children_answer_true():
    if childrenAnswerTrue:
        childrenAnswerFalse.set(False)
        durationAnswerTrue.set(False)
        durationAnswerFalse.set(True)
        DurationAnswerOne.configure(state=DISABLED)
        DurationAnswerTwo.configure(state=DISABLED)


def children_answer_false():
    if childrenAnswerFalse:
        childrenAnswerTrue.set(False)
        durationAnswerTrue.set(False)
        durationAnswerFalse.set(False)
        DurationAnswerOne.configure(state=ACTIVE)
        DurationAnswerTwo.configure(state=ACTIVE)


def duration_answer_true():
    if durationAnswerTrue:
        durationAnswerFalse.set(False)


def duration_answer_false():
    if durationAnswerFalse:
        durationAnswerTrue.set(False)


def imdb_answer_true():
    if imdbAnswerTrue:
        imdbAnswerFalse.set(False)


def imdb_answer_false():
    if imdbAnswerFalse:
        imdbAnswerTrue.set(False)


def find_movie_button_click():
    errors = check_all_completed()
    if errors:
        messagebox.showerror("Oops!", "\n".join(errors))
    else:
        filter_movies()
        if len(filtered) > 2:
            recommendation = random.sample(filtered, 3)
        else:
            recommendation = filtered
            recommendation.extend(random.sample(movie_data, 3 - len(filtered)))

        messagebox.showinfo("Movie Recommendation", messageTemplate.format(recommendation[0][0],recommendation[0][4],recommendation[0][5]
                             ,recommendation[1][0],recommendation[1][4],recommendation[1][5]
                             ,recommendation[2][0],recommendation[2][4],recommendation[2][5]),)




def check_all_completed():
    errors = []
    if moodComboBox.get() == "":
        errors.append('Mood should be selected.')

    if yearAnswerTrue.get() is False and yearAnswerFalse.get() is False:
        errors.append('Year question should be answered.')

    if partnerAnswerTrue.get() is False and partnerAnswerFalse.get() is False:
        errors.append('Partner question should be answered.')

    if childrenAnswerTrue.get() is False and childrenAnswerFalse.get() is False:
        errors.append('Children question should be answered.')

    if durationAnswerTrue.get() is False and durationAnswerFalse.get() is False:
        errors.append('Duration question should be answered.')

    if imdbAnswerTrue.get() is False and imdbAnswerFalse.get() is False:
        errors.append('Imdb score should be answered.')

    return errors


def filter_movies():
    global genre_list
    if moodComboBox.get() == "sad":
        genre_list = ["Drama", "History"]
    elif moodComboBox.get() == "happy":
        genre_list = ["Comedy", "Fantasy", "Music"]
    elif moodComboBox.get() == "bored":
        genre_list = ["Action", "Adventure", "Mystery", "Sci-Fi"]

    if childrenAnswerTrue.get():
        genre_list = ["Family", "Animation", "Adventure"]
    elif partnerAnswerTrue.get():
        genre_list.append("Romance")
    else:
        genre_list.extend(["History", "War", "Thriller"])

    filter_genre(genre_list)

    if yearAnswerTrue.get():
        for movie in filtered[:]:
            if int(movie[1]) >= 2000:
                filtered.remove(movie)
    else:
        for movie in filtered[:]:
            if int(movie[1][:4]) < 2000:
                filtered.remove(movie)

    if imdbAnswerTrue.get():
        for movie in filtered[:]:
            if float(movie[4]) < 8:
                filtered.remove(movie)

    if durationAnswerTrue.get():
        for movie in filtered[:]:
            if int(movie[2][:3].strip()) > 150:
                filtered.remove(movie)


messageTemplate = "I have 3 movie recomendation for you today \n\n\
The first one is : {}\nImdb score: {}\nSummary : {}\n\n\
The second one is : {}\nImdb score: {}\nSummary : {}\n\n\
And the last one is : {}\nImdb score: {}\nSummary : {}"
movie_data = cache_data()
window = Tk()
filtered = []
genre_list = []

frame = Frame(window)
frame.pack()

formFrame = LabelFrame(frame, text="Movie Form")
formFrame.grid(row=0, column=0, padx=10, pady=10, sticky="news")

moodQuestion = Label(formFrame, text="How do you feel today ?")
moodQuestion.grid(row=0, column=0, padx=10, pady=10)

moodComboBox = Combobox(formFrame, values=["Happy", "Sad", "Bored"])
moodComboBox.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

yearQuestion = Label(formFrame, text="Do you like old movies or new ones ?")
yearQuestion.grid(row=1, column=0)

yearAnswerTrue = BooleanVar()
yearAnswerFalse = BooleanVar()

yearAnswerOne = Checkbutton(formFrame, text="Old", variable=yearAnswerTrue, command=year_answer_true)
yearAnswerOne.grid(row=1, column=1)

yearAnswerTwo = Checkbutton(formFrame, text="New", variable=yearAnswerFalse, command=year_answer_false)
yearAnswerTwo.grid(row=1, column=2)

partnerQuestion = Label(formFrame, text="Are you going to watch with your partner?")
partnerQuestion.grid(row=2, column=0)

partnerAnswerTrue = BooleanVar()
partnerAnswerFalse = BooleanVar()

partnerAnswerOne = Checkbutton(formFrame, text="Yes", variable=partnerAnswerTrue, command=partner_answer_true)
partnerAnswerOne.grid(row=2, column=1)

partnerAnswerTwo = Checkbutton(formFrame, text="No", variable=partnerAnswerFalse, command=partner_answer_false)
partnerAnswerTwo.grid(row=2, column=2)

ChildrenQuestion = Label(formFrame, text="Are you going to watch a movie with children")
ChildrenQuestion.grid(row=3, column=0)

childrenAnswerTrue = BooleanVar()
childrenAnswerFalse = BooleanVar()

ChildrenAnswerOne = Checkbutton(formFrame, text="Yes", variable=childrenAnswerTrue, command=children_answer_true)
ChildrenAnswerOne.grid(row=3, column=1)

ChildrenAnswerTwo = Checkbutton(formFrame, text="No", variable=childrenAnswerFalse, command=children_answer_false)
ChildrenAnswerTwo.grid(row=3, column=2)

DurationQuestion = Label(formFrame, text="Do you like to watch to long movies?")
DurationQuestion.grid(row=4, column=0)

durationAnswerTrue = BooleanVar()
durationAnswerFalse = BooleanVar()

DurationAnswerOne = Checkbutton(formFrame, text="Yes", variable=durationAnswerTrue, command=duration_answer_true)
DurationAnswerOne.grid(row=4, column=1)

DurationAnswerTwo = Checkbutton(formFrame, text="No", variable=durationAnswerFalse, command=duration_answer_false)
DurationAnswerTwo.grid(row=4, column=2)

IMDBQuestion = Label(formFrame, text="Do you pay attention to imbd scores?")
IMDBQuestion.grid(row=5, column=0)

imdbAnswerTrue = BooleanVar()
imdbAnswerFalse = BooleanVar()

IMDBAnswerOne = Checkbutton(formFrame, text="Yes", variable=imdbAnswerTrue, command=imdb_answer_true)
IMDBAnswerOne.grid(row=5, column=1)

IMDBAnswerTwo = Checkbutton(formFrame, text="No", variable=imdbAnswerFalse, command=imdb_answer_false)
IMDBAnswerTwo.grid(row=5, column=2)

findMovieButton = Button(formFrame, text="Find Movie", command=find_movie_button_click)
findMovieButton.grid(row=6, column=0, columnspan=3)

for widget in formFrame.winfo_children():
    widget.config(font=("comic sans", 12, "bold"))
    widget.grid_configure(padx=10, pady=5)

movieImage = PhotoImage(file="movie.png")
window.iconphoto(True, movieImage)
window.title("Movie Recommender")
window.resizable(False, False)
window.mainloop()
