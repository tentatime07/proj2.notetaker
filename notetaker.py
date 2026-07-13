import json

def show_menu():
    print("\n1. add note")
    print("2. delete notes")
    print("3. view notes")
    print("4. exit")

def add_notes(notes):
    note = input("Type note to add: ").strip()
    if note:
        notes.append(note)
        print("Note added!")
    else:
        print("Note cannot be empty")

def view_notes(notes):
    if not notes:
        print("no notes yet!")
    for index, note in enumerate(notes, start = 1):
        print(f"{index}. {note}")

def delete_notes(notes):
    if not notes:
        print("no notes to delete!")
        return
    view_notes(notes)
    try:
        delete_index = int(input("type number you want to delete")) - 1
        if 0 <= delete_index < len(notes):
            deleted_note = notes.pop(delete_index)
            print(f"Successfully deleted {deleted_note}")
            return
        else:
            print("note number does not exist")
    except ValueError:
        print("not a valid number")

    

def start():
    notes = []
    print("Welcome to your note taker!")

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_notes(notes)
        elif choice == "2":
            delete_notes(notes)
        elif choice == "3":
            view_notes(notes)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
    
start()
        

