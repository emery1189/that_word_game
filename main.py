import tkinter as tk
import random

window = tk.Tk()
window.title("That Word Game")
window.geometry("450x650")
window.configure(background="gray21")


def get_word():
    with open("words.txt") as words_file:
        the_word = random.choice(words_file.readlines())
        # ⬇️ to show word during testing
        # the_word_label = tk.Label(window, text=f"the word is: {the_word.lower()}", fg="DeepPink2", bg="gray21")
        # the_word_label.grid(row=0, column=0, columnspan=5, pady=10)
        empty_space = tk.Label(window, text="\n", bg="gray21", pady=10)
        empty_space.grid(row=0, column=0, columnspan=5)
        word_list = [x.lower() for x in the_word]
        word_list.remove('\n')
        return word_list


def validate(P):
    # limit entries to only one character
    if len(P) == 1:
        return True
    else:
        return False


# create validate command:
vcmd = (window.register(validate), "%P")

# to keep track of game progress
attempt = 1
reveal = 2
turns_left = 6


def check_word(event=None):
    global attempt, reveal, turns_left, word
    attempt += 2
    guess = [user_guess1.get().lower(), user_guess2.get().lower(), user_guess3.get().lower(),
             user_guess4.get().lower(), user_guess5.get().lower()]
    word_list = list(word)
    guess_list = list(guess)
    word_dict = dict(enumerate(word_list))
    guess_dict = dict(enumerate(guess_list))
    zipped_dictionary = zip(word_dict.keys(), word_dict.values(), guess_dict.values())
    tupled_dictionary = tuple(zipped_dictionary)
    # gives (index, word_letter, guess_letter) tuples
    first, second, third, fourth, fifth = tupled_dictionary[0], tupled_dictionary[1], tupled_dictionary[2],\
        tupled_dictionary[3], tupled_dictionary[4]
    list_of_tuples = [first, second, third, fourth, fifth]

    for i in list_of_tuples:
        # correct letter
        if i[1] == i[2]:
            green_label = tk.Label(window, text=i[2], font=("Times", 28), fg="green2", bg="gray21")
            green_label.grid(row=reveal, column=i[0], padx=10)

        # incorrect letter
        elif i[2] not in word_list:
            black_label = tk.Label(window, text=i[2], font=("Times", 28), fg="black", bg="gray21")
            black_label.grid(row=reveal, column=i[0], padx=10)

        # misplaced letter
        elif i[2] in word_list:
            if word_list.count(i[2]) == 1 and guess_list.count(i[2]) > 1:
                # first duplicate letter will appear black
                black_label = tk.Label(window, text=i[2], font=("Times", 28), fg="black", bg="gray21")
                black_label.grid(row=reveal, column=i[0], padx=10)
                guess_list.remove(i[2])
                # second duplicate letter will appear yellow
            elif word_list.count(i[2]) == 2 and guess_list.count(i[2]) > 2:
                black_label = tk.Label(window, text=i[2], font=("Times", 28), fg="black", bg="gray21")
                black_label.grid(row=reveal, column=i[0], padx=10)
                guess_list.remove(i[2])
            elif word_list.count(i[2]) == 3 and guess_list.count(i[2]) > 3:
                black_label = tk.Label(window, text=i[2], font=("Times", 28), fg="black", bg="gray21")
                black_label.grid(row=reveal, column=i[0], padx=10)
                guess_list.remove(i[2])
            elif word_list.count(i[2]) == 4 and guess_list.count(i[2]) > 4:
                black_label = tk.Label(window, text=i[2], font=("Times", 28), fg="black", bg="gray21")
                black_label.grid(row=reveal, column=i[0], padx=10)
                guess_list.remove(i[2])
            else:
                yellow_label = tk.Label(window, text=i[2], font=("Times", 28), fg="yellow", bg="gray21")
                yellow_label.grid(row=reveal, column=i[0], padx=10)

    # update game progress
    turns_left -= 1
    turns_left_label = tk.Label(window, text=f"{turns_left} remaining", font=("Times", 21), fg="DeepPink2", bg="gray21")
    turns_left_label.grid(row=reveal, column=5, padx=10)
    reveal += 2

    # check to see if player wins
    if guess == word_list:
        turns_left_label.destroy()
        check_button.destroy()
        win_label = tk.Label(window, text='\n🎈🍾🎉', font=("Times", 38), bg="gray21")
        win_label.grid(row=reveal, column=0, columnspan=5)

    # check to see if player loses
    elif turns_left == 0:
        check_button.destroy()
        lose_label = tk.Label(window, text=f"😭😭\n{''.join(word)}", font=("Times", 48), fg="DeepPink2", bg="gray21")
        lose_label.grid(row=reveal, column=0, columnspan=5)

    # clean up for next turn
    else:
        user_guess1.destroy()
        user_guess2.destroy()
        user_guess3.destroy()
        user_guess4.destroy()
        user_guess5.destroy()
        check_button.destroy()
        create_entries()


def create_entries():
    global user_guess1, user_guess2, user_guess3, user_guess4, user_guess5, check_button
    # create Entry widget
    user_guess1 = tk.Entry(width=2, validate="key", validatecommand=vcmd, fg="DeepPink2", bg="gray21")
    # place Entry widget
    user_guess1.grid(row=attempt, column=0, padx=10)
    # move cursor to Entry widget
    user_guess1.focus()
    # move cursor to next widget once letter has been guessed
    user_guess1.bind("<Key>", lambda funct1: user_guess2.focus())
    user_guess2 = tk.Entry(width=2, validate="key", validatecommand=vcmd, fg="DeepPink2", bg="gray21")
    user_guess2.grid(row=attempt, column=1, padx=10)
    user_guess2.bind("<Key>", lambda funct1: user_guess3.focus())
    user_guess3 = tk.Entry(width=2, validate="key", validatecommand=vcmd, fg="DeepPink2", bg="gray21")
    user_guess3.grid(row=attempt, column=2, padx=10)
    user_guess3.bind("<Key>", lambda funct1: user_guess4.focus())
    user_guess4 = tk.Entry(width=2, validate="key", validatecommand=vcmd, fg="DeepPink2", bg="gray21")
    user_guess4.grid(row=attempt, column=3, padx=10)
    user_guess4.bind("<Key>", lambda funct1: user_guess5.focus())
    user_guess5 = tk.Entry(width=2, validate="key", validatecommand=vcmd, fg="DeepPink2", bg="gray21")
    user_guess5.grid(row=attempt, column=4, padx=10)
    user_guess5.bind("<Key>", lambda funct1: check_button.focus())
    check_button = tk.Button(window, text="check", command=check_word)
    check_button.grid(row=attempt, column=5, pady=10)
    check_button.bind("<Return>", check_word)
    return user_guess1, user_guess2, user_guess3, user_guess4, user_guess5


if __name__ == "__main__":
    word = get_word()
    create_entries()

window.mainloop()
