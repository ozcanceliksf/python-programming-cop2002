# Exercise 10 - Simple Text File Organizer
# COP2002 - Python Programming
# Ozcan Celik

import os

def write_notes(filename, notes):
    """Write a list of notes to a text file."""
    with open(filename, "w") as f:
        for i, note in enumerate(notes, 1):
            f.write(f"{i}. {note}\n")
    print(f"Notes saved to '{filename}'.")

def read_notes(filename):
    """Read and display notes from a file."""
    if not os.path.exists(filename):
        print(f"File '{filename}' not found.")
        return []

    notes = []
    with open(filename, "r") as f:
        lines = f.readlines()
        print(f"\n--- Notes from '{filename}' ---")
        for line in lines:
            print(line.strip())
            notes.append(line.strip())
    return notes

def append_note(filename, new_note):
    """Append a single note to an existing file."""
    with open(filename, "a") as f:
        f.write(f"{new_note}\n")
    print(f"Note appended to '{filename}'.")

def count_words_in_file(filename):
    """Count total words in a file."""
    if not os.path.exists(filename):
        print(f"File '{filename}' not found.")
        return 0

    with open(filename, "r") as f:
        content = f.read()
        words = content.split()
        print(f"Total words in '{filename}': {len(words)}")
        return len(words)

if __name__ == "__main__":
    filename = "my_notes.txt"

    # Sample notes
    notes = [
        "Study Python file I/O",
        "Complete COP2002 lab assignment",
        "Review networking chapter 5",
        "Practice Linux commands",
    ]

    write_notes(filename, notes)
    read_notes(filename)
    append_note(filename, "5. Upload exercise to GitHub")
    read_notes(filename)
    count_words_in_file(filename)

    # Cleanup
    if os.path.exists(filename):
        os.remove(filename)
        print(f"\nFile '{filename}' cleaned up.")
