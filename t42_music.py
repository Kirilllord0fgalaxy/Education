def music(note):
    note = note.upper()
    valnote={'C4': 261.63,
             'D4': 293.66,
             'E4':329.63,
             'F4': 349.23,
             'G4': 392.00,
             'A4': 440.00,
             'B4': 493.88}
    return f'Частота ноты {note} равна {valnote[note]}'

print(music(input()))