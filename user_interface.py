import tkinter as tk
from customtkinter import (
    CTk,
    CTkButton,
    CTkEntry,
    CTkLabel,
    set_appearance_mode,
    set_default_color_theme,
)

from main import *
from constants import *

set_appearance_mode("System")
set_default_color_theme("green")


class App(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Configuration")
        self.geometry("500x400")

        self.title_label = CTkLabel(
            self, text="Configuration", font=("Helvetica", 16, "bold")
        )
        self.title_label.grid(row=0, column=0, columnspan=4, pady=(10, 20))

        self.initial_population_size_label = CTkLabel(
            self, text="Initial population size:"
        )
        self.initial_population_size_label.grid(row=1, column=0, padx=5, pady=5)
        self.initial_population_size_input = CTkEntry(self, width=100)
        self.initial_population_size_input.grid(row=1, column=1, padx=5, pady=5)
        self.initial_population_size_input.insert(0, str(INITIAL_POPULATION_SIZE))

        self.number_of_generations_label = CTkLabel(self, text="Number of generations:")
        self.number_of_generations_label.grid(row=2, column=0, padx=5, pady=5)
        self.number_of_generations_input = CTkEntry(self, width=100)
        self.number_of_generations_input.grid(row=2, column=1, padx=5, pady=5)
        self.number_of_generations_input.insert(0, str(NUMBER_OF_GENERATIONS))

        self.number_of_bits_label = CTkLabel(self, text="Number of bits:")
        self.number_of_bits_label.grid(row=3, column=0, padx=5, pady=5)
        self.number_of_bits_input = CTkEntry(self, width=100)
        self.number_of_bits_input.grid(row=3, column=1, padx=5, pady=5)
        self.number_of_bits_input.insert(0, str(NUMBER_OF_BITS))

        self.value_threshold_label = CTkLabel(self, text="Value threshold:")
        self.value_threshold_label.grid(row=4, column=0, padx=5, pady=5)
        self.value_threshold_input = CTkEntry(self, width=100)
        self.value_threshold_input.grid(row=4, column=1, padx=5, pady=5)
        self.value_threshold_input.insert(0, str(VALUE_THRESHOLD))

        self.domain_min_label = CTkLabel(self, text="Domain min:")
        self.domain_min_label.grid(row=1, column=2, padx=5, pady=5)
        self.domain_min_slider = tk.Scale(
            self, from_=-500, to=450, resolution=0.1, orient=tk.HORIZONTAL
        )
        self.domain_min_slider.set(FUNCTION_DOMAIN["MIN"])
        self.domain_min_slider.grid(row=1, column=3, padx=5, pady=5)

        self.domain_max_label = CTkLabel(self, text="Domain max:")
        self.domain_max_label.grid(row=2, column=2, padx=5, pady=5)
        self.domain_max_slider = tk.Scale(
            self, from_=-450, to=500, resolution=0.1, orient=tk.HORIZONTAL
        )
        self.domain_max_slider.set(FUNCTION_DOMAIN["MAX"])
        self.domain_max_slider.grid(row=2, column=3, padx=5, pady=5)

        self.crossover_rate_label = CTkLabel(self, text="Crossover rate:")
        self.crossover_rate_label.grid(row=3, column=2, padx=5, pady=5)
        self.crossover_rate_slider = tk.Scale(
            self, from_=0, to=1, resolution=0.0001, orient=tk.HORIZONTAL
        )
        self.crossover_rate_slider.set(CROSSOVER_RATE)
        self.crossover_rate_slider.grid(row=3, column=3, padx=5, pady=5)

        self.mutation_rate_label = CTkLabel(self, text="Mutation rate:")
        self.mutation_rate_label.grid(row=4, column=2, padx=5, pady=5)
        self.mutation_rate_slider = tk.Scale(
            self, from_=0, to=1, resolution=0.0001, orient=tk.HORIZONTAL
        )
        self.mutation_rate_slider.set(MUTATION_RATE)
        self.mutation_rate_slider.grid(row=4, column=3, padx=5, pady=5)

        self.button = CTkButton(self, text="RUN", command=self.on_button_click)
        self.button.grid(row=5, column=0, columnspan=4, pady=10)

    def on_button_click(self):
        text_input_values = [
            self.initial_population_size_input.get(),
            self.number_of_generations_input.get(),
            self.number_of_bits_input.get(),
            self.value_threshold_input.get(),
        ]

        slider_values = [
            self.domain_min_slider.get(),
            self.domain_max_slider.get(),
            self.crossover_rate_slider.get(),
            self.mutation_rate_slider.get(),
        ]

        with open("logs/logs.txt", "w") as f:
            pass

        result = run_genetic_algorithm(
            int(text_input_values[0]),
            int(text_input_values[1]),
            slider_values[0],
            slider_values[1],
            int(text_input_values[2]),
            slider_values[2],
            slider_values[3],
            float(text_input_values[3]),
        )


if __name__ == "__main__":
    app = App()
    app.mainloop()
