def trivia():
    embed = "https://Project-1.danevestal.repl.run"
    title = "Trivia Game"
    section = {"embed": embed, "title": title}
    return section

def guess():
    embed = "https://Guess-the-number-2.idamobini.repl.run"
    title = "Guess the Number"
    section = {"embed": embed, "title": title}
    return section

def hangman():
    embed = "https://Hangman-1.crystalwidjaja.repl.run"
    title = "Hangman"
    section = {"embed": embed, "title": title}
    return section

def reaction():
    embed = "https://reaction-time-final.crystalwidjaja.repl.run"
    title = "Reaction Time"
    section = {"embed": embed, "title": title}
    return section

def all_games():
    return [trivia(), guess(), hangman(), reaction()]
