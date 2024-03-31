import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle


def on_button_click():
    print("Button clicked!")

    text_input_values = [
        initial_population_size_input.get(),
        number_of_generations_input.get(),
        number_of_bits_input.get(),
        value_threshold_input.get(),
    ]

    slider_values = [
        domain_min_slider.get(),
        domain_max_slider.get(),
        crossover_rate_slider.get(),
        mutation_rate_slider.get(),
    ]

    print("Text Inputs:", text_input_values)
    print("Sliders:", slider_values)


root = tk.Tk()
root.title("UI with Inputs and Sliders")

style = ThemedStyle(root)
style.set_theme("equilux")


input_frame = ttk.Frame(root, padding="20")
input_frame.grid(row=0, column=0, padx=10, pady=10)

initial_population_size_label = ttk.Label(input_frame, text="Initial population size:")
initial_population_size_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
initial_population_size_input = ttk.Entry(input_frame, width=10)
initial_population_size_input.grid(row=0, column=1, padx=5, pady=5)

number_of_generations_label = ttk.Label(input_frame, text="Number of generations:")
number_of_generations_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
number_of_generations_input = ttk.Entry(input_frame, width=10)
number_of_generations_input.grid(row=1, column=1, padx=5, pady=5)

number_of_bits_label = ttk.Label(input_frame, text="Number of bits:")
number_of_bits_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
number_of_bits_input = ttk.Entry(input_frame, width=10)
number_of_bits_input.grid(row=2, column=1, padx=5, pady=5)

value_threshold_label = ttk.Label(input_frame, text="Value threshold:")
value_threshold_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
value_threshold_input = ttk.Entry(input_frame, width=10)
value_threshold_input.grid(row=3, column=1, padx=5, pady=5)

domain_min_label = ttk.Label(input_frame, text="Domain min:")
domain_min_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")
domain_min_slider = ttk.Scale(
    input_frame,
    from_=-500,
    to=500,
    length=150,
    value=-10,
    command=lambda value: domain_min_value.set(value),
)
domain_min_slider.grid(row=0, column=3, padx=5, pady=5)
domain_min_value = tk.StringVar()
domain_min_label = ttk.Label(input_frame, textvariable=domain_min_value)
domain_min_label.grid(row=0, column=4, padx=5, pady=5)
domain_min_value.set(domain_min_slider.get())


domain_max_label = ttk.Label(input_frame, text="Domain max:")
domain_max_label.grid(row=1, column=2, padx=5, pady=5, sticky="w")
domain_max_slider = ttk.Scale(
    input_frame,
    from_=-500,
    to=500,
    length=150,
    value=10,
    command=lambda value: domain_max_value.set(value),
)
domain_max_slider.grid(row=1, column=3, padx=5, pady=5)
domain_max_value = tk.StringVar()
domain_max_label = ttk.Label(input_frame, textvariable=domain_max_value)
domain_max_label.grid(row=1, column=4, padx=5, pady=5)
domain_max_value.set(domain_max_slider.get())


crossover_rate_label = ttk.Label(input_frame, text="Crossover rate:")
crossover_rate_label.grid(row=2, column=2, padx=5, pady=5, sticky="w")
crossover_rate_slider = ttk.Scale(
    input_frame,
    from_=0,
    to=1,
    length=150,
    value=0.07,
    command=lambda value: crossover_rate_value.set(value),
)
crossover_rate_slider.grid(row=2, column=3, padx=5, pady=5)
crossover_rate_value = tk.StringVar()
crossover_rate_label = ttk.Label(input_frame, textvariable=crossover_rate_value)
crossover_rate_label.grid(row=2, column=4, padx=5, pady=5)
crossover_rate_value.set(crossover_rate_slider.get())


mutation_rate_label = ttk.Label(input_frame, text="Mutation rate:")
mutation_rate_label.grid(row=3, column=2, padx=5, pady=5, sticky="w")
mutation_rate_slider = ttk.Scale(
    input_frame,
    from_=0,
    to=1,
    length=150,
    value=0.01,
    command=lambda value: crossover_rate_value.set(value),
)
mutation_rate_slider.grid(row=3, column=3, padx=5, pady=5)
mutation_rate_value = tk.StringVar()
mutation_rate_label = ttk.Label(input_frame, textvariable=mutation_rate_value)
mutation_rate_label.grid(row=3, column=4, padx=5, pady=5)
mutation_rate_value.set(mutation_rate_slider.get())

button = ttk.Button(root, text="Maximize function", command=on_button_click)
button.grid(row=1, column=0, padx=10, pady=10)


def run_app():
    root.mainloop()
