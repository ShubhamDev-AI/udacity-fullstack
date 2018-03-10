import time

file_loc = ".\\notes.txt"

def take_note():
    note = raw_input('Enter Note --->')
    note_file = open(file_loc, 'a')
    note_file.write('---' + time.strftime(' %c: ') + note + '\n')
    note_file.close()


def view_notes():
    note_file = open(file_loc, 'r')
    print("Your Notes:")
    print(note_file.read())
    note_file.close()


def run():
    print(' [1] View Notes')
    print(' [2] Take Note')
    print(' [e] Exit')
    select = raw_input('Enter Selection --->')
    if(select == '1'):
        view_notes()
    elif(select == '2'):
        take_note()
    else:
        return False
    return True


while(run()):
    continue
