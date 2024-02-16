"""
CSC 4110
HOMEWORK4:QUESTION 2
START DATE: 02/ 10 / 2024
BEGIN ROHITH SURESH (02/10/24)
"""

import random
import tkinter as tk
from tkinter import messagebox

class PirateTreasureGame:
    def __init__(self, initial_bank=100, items_in_chest=10):
        self.bank = initial_bank
        self.chest = [random.randint(1, 100) for _ in range(items_in_chest)]
        self.wager = 10
        self.outcomes = []

    def spin_treasure(self):
        result = random.choice(self.chest)
        if result % 2 == 0:
            self.bank += self.wager
            outcome = "You found treasure! 🏴‍☠️"
        else:
            self.bank -= self.wager
            outcome = "No luck this time! 💣"
        return outcome

    def play_game(self):
        # Create main window
        self.root = tk.Tk()
        self.root.title("Pirate's Treasure Game")

        # Create labels
        self.bank_label = tk.Label(self.root, text=f"Current Bank: {self.bank} gold coins")
        self.bank_label.pack()

        self.wager_label = tk.Label(self.root, text="Enter your wager:")
        self.wager_label.pack()

        # Create entry widget for wager
        self.wager_entry = tk.Entry(self.root)
        self.wager_entry.pack()

        # Create spin button
        self.spin_button = tk.Button(self.root, text="Spin Treasure Chest", command=self.spin_treasure_button)
        self.spin_button.pack()

        self.root.mainloop()

    def spin_treasure_button(self):
        # Get the wager entered by the player
        wager = self.wager_entry.get()

        # Validate and process the wager
        try:
            wager = int(wager)
            if wager <= 0:
                messagebox.showerror("Error", "Invalid wager. Please enter a positive number.")
                return
            elif wager > self.bank:
                messagebox.showerror("Error", "Insufficient funds. Please enter a wager within your bank balance.")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid wager.")
            return

        # Spin the treasure and update the bank label
        outcome = self.spin_treasure()
        self.bank_label.config(text=f"Current Bank: {self.bank} gold coins\n{outcome}")

        # Check if game over
        if self.bank <= 0:
            messagebox.showinfo("Game Over", "Oh no! You've gone bankrupt. Game over.")
            self.root.destroy()

if __name__ == "__main__":
    pirate_game = PirateTreasureGame()
    pirate_game.play_game()


"""
FINAL DATE: 15/ 02/ 2024
END ROHITH SURESH
"""