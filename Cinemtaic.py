import os
import time

def clear_console():
    """Clears the console screen."""
    os.system("cls" if os.name == "nt" else "clear")

def rolling_text_perfect(text, speed=0.1, lines=10):
    """Moves each letter from bottom to top correctly and keeps it in place."""
    
    displayed_text = [" " * len(text)] * lines  # Empty screen with spaces

    for letter_index, letter in enumerate(text):  # Process each letter one by one
        for i in range(lines - 1, -1, -1):  # Move the letter upwards
            clear_console()
            
            # Update the displayed text with the moving letter
            temp_display = displayed_text[:]  # Copy current state
            temp_display[i] = temp_display[i][:letter_index] + letter + temp_display[i][letter_index + 1:]  # Place letter
            
            # Print the screen
            for line in temp_display:
                print(line)
            
            time.sleep(speed)  # Control speed

        # Once the letter reaches the top, permanently add it to its place
        displayed_text[0] = displayed_text[0][:letter_index] + letter + displayed_text[0][letter_index + 1:]

# Run the effect
rolling_text_perfect("Hello, World!", speed=0.1, lines=10)