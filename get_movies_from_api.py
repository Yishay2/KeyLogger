import requests
import tkinter as tk
from tkinter import messagebox

# Function to fetch movie details from the API
def fetch_movie_details():
    movie_name = entry_movie_name.get()
    if not movie_name:
        messagebox.showwarning("Input Error", "Please enter a movie name.")
        return

    response = requests.get(
        f"http://www.omdbapi.com/?apikey=363f300&t={'+'.join(movie_name.split())}"
    )

    movie_data = response.json()

    if movie_data.get("Response") == "False":
        messagebox.showinfo("Not Found", "The movie wasn't found!")
        return

    # Display the movie details in the result box
    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, f"Title: {movie_data.get('Title', 'N/A')}\n")
    result_box.insert(tk.END, f"Year: {movie_data.get('Year', 'N/A')}\n")
    result_box.insert(tk.END, f"Genre: {movie_data.get('Genre', 'N/A')}\n")
    result_box.insert(tk.END, f"Director: {movie_data.get('Director', 'N/A')}\n")
    result_box.insert(tk.END, f"Actors: {movie_data.get('Actors', 'N/A')}\n")
    result_box.insert(tk.END, f"Plot: {movie_data.get('Plot', 'N/A')}\n")
    result_box.insert(tk.END, f"IMDB Rating: {movie_data.get('imdbRating', 'N/A')}\n")

# Create the main window
root = tk.Tk()
root.title("Movie Search")
root.geometry("500x400")

# Create and place widgets
label_instruction = tk.Label(root, text="Enter movie name:")
label_instruction.pack(pady=10)

entry_movie_name = tk.Entry(root, width=40)
entry_movie_name.pack(pady=5)

btn_search = tk.Button(root, text="Search", command=fetch_movie_details)
btn_search.pack(pady=5)

result_box = tk.Text(root, width=60, height=15)
result_box.pack(pady=10)

# Run the application
root.mainloop()
