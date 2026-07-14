import json

def show_menu():
    print("\n1. add note")
    print("2. delete notes")
    print("3. edit notes")
    print("4. view notes")
    print("5. search notes")
    print("6. clear notes")
    print("7. exit")


def add_notes(notes):
    note = input("Type note to add: \n").strip()
    if note:
        notes.append(note)
        print("Note added!")
        save_notes(notes)
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
        delete_index = int(input("type number you want to delete:\n")) - 1
        if 0 <= delete_index < len(notes):
            deleted_note = notes.pop(delete_index)
            print(f"Successfully deleted {deleted_note}")
            save_notes(notes)
            return
        else:
            print("note number does not exist")
    except ValueError:
        print("not a valid number")

def search_notes(notes):
    if not notes:
        print("no notes to search!")
        return
    search_note = input("enter word or phrase to search for:\n").strip().lower()
    if not search_note:
        print("search cannot be empty")
        return
    found = []
    for index, note in enumerate(notes, start = 1):
        if search_note in note.lower():
            found.append(f"{index}. {note}")
    if not found:
        print("no matches found")
        return
    print("\nMatching notes:")
    for note in found:
        print(note)

def edit_notes(notes):
    if not notes:
        print("no notes to edit!")
        return
    view_notes(notes)
    try:
        edit_index = int(input("type number you want to edit:\n")) - 1
        if 0 <= edit_index < len(notes):
            edited_note = input("Enter the updated note:\n").strip()
            if not edited_note:
                print("note cannot be empty")
                return
            notes[edit_index] = edited_note
            print(f"Successfully edited note!")
            save_notes(notes)
            return
        else:
            print("note number does not exist")
    except ValueError:
        print("not a valid number")

def clear_notes(notes):
    if not notes:
        print("no notes to clear!")
    else:
        notes.clear()
        save_notes(notes)
        print("all notes cleared!")

def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent = 4)

def load_notes():
    try:
        with open("notes.json", "r") as file:
            res = json.load(file)
        if isinstance(res, list):
            return res
        else:
            print("file has unexpected format, starting with empty list")
            return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("file corrupted, starting with empty list")
        return []


def start():
    notes = load_notes()
    
    print("Welcome to your note taker!")

    while True:
        show_menu()
        choice = input("Choose an option: \n").strip()

        if choice == "1":
            add_notes(notes)
        elif choice == "2":
            delete_notes(notes)
        elif choice == "3":
            edit_notes(notes)
        elif choice == "4":
            view_notes(notes)
        elif choice == "5":
            search_notes(notes)
        elif choice == "6":
            clear_notes(notes)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
    
start()
        

