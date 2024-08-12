import tkinter as tk
from tkinter import ttk, messagebox, font
from PIL import Image, ImageTk
import random

# Données de livres avec couverture et descriptions
books = [
    {"title": "The Great Gatsby", "genre": "Fiction", "cover": "https://via.placeholder.com/100?text=Gatsby", "description": "A novel by F. Scott Fitzgerald."},
    {"title": "To Kill a Mockingbird", "genre": "Fiction", "cover": "https://via.placeholder.com/100?text=Mockingbird", "description": "A novel by Harper Lee."},
    {"title": "1984", "genre": "Dystopian", "cover": "https://via.placeholder.com/100?text=1984", "description": "A novel by George Orwell."},
    {"title": "Pride and Prejudice", "genre": "Romance", "cover": "https://via.placeholder.com/100?text=Pride", "description": "A novel by Jane Austen."},
    {"title": "The Catcher in the Rye", "genre": "Fiction", "cover": "https://via.placeholder.com/100?text=Catcher", "description": "A novel by J.D. Salinger."},
    {"title": "The Hobbit", "genre": "Fantasy", "cover": "https://via.placeholder.com/100?text=Hobbit", "description": "A novel by J.R.R. Tolkien."},
    {"title": "Harry Potter and the Sorcerer's Stone", "genre": "Fantasy", "cover": "https://via.placeholder.com/100?text=Potter", "description": "A novel by J.K. Rowling."},
    {"title": "The Da Vinci Code", "genre": "Thriller", "cover": "https://via.placeholder.com/100?text=DaVinci", "description": "A novel by Dan Brown."},
    {"title": "The Alchemist", "genre": "Adventure", "cover": "https://via.placeholder.com/100?text=Alchemist", "description": "A novel by Paulo Coelho."},
]

# Données utilisateur simulées
user_ratings = {
    "user1": {"Fiction": 4, "Fantasy": 5},
    "user2": {"Dystopian": 5, "Thriller": 3},
}

def recommend_books(preferences):
    # Recommandations basées sur les préférences de genre
    recommendations = [book for book in books if book["genre"] in preferences]
    return recommendations

def get_recommendations():
    preferences = preferences_entry.get().split(',')
    preferences = [p.strip().capitalize() for p in preferences if p.strip()]
    
    if not preferences:
        messagebox.showerror("Error", "Please enter at least one genre.")
        return
    
    recommendations = recommend_books(preferences)
    display_books(recommendations)

def get_top_rated_books():
    top_rated_genres = [genre for user in user_ratings.values() for genre in user if user[genre] >= 4]
    recommendations = recommend_books(top_rated_genres)
    display_books(recommendations)

def get_random_recommendations():
    recommendations = random.sample(books, min(5, len(books)))  # Afficher jusqu'à 5 livres au hasard
    display_books(recommendations)

def search_books():
    search_query = search_entry.get().strip().lower()
    recommendations = [book for book in books if search_query in book["title"].lower()]
    display_books(recommendations)

def display_books(books_to_display):
    result_frame.pack_forget()
    result_frame.pack(fill=tk.BOTH, expand=True)
    
    for widget in result_frame.winfo_children():
        widget.destroy()

    if not books_to_display:
        ttk.Label(result_frame, text="No books found.", font=bold_font).pack(padx=5, pady=5)
    else:
        for book in books_to_display:
            ttk.Label(result_frame, text=book["title"], font=bold_font).pack(anchor=tk.W, padx=5, pady=2)
            ttk.Label(result_frame, text=book["description"], wraplength=400, anchor=tk.W).pack(anchor=tk.W, padx=5, pady=2)
            
            try:
                cover_image = Image.open(requests.get(book["cover"], stream=True).raw)
                cover_image = cover_image.resize((100, 150))
                cover_image = ImageTk.PhotoImage(cover_image)
                cover_label = ttk.Label(result_frame, image=cover_image)
                cover_label.image = cover_image
                cover_label.pack(padx=5, pady=5)
            except:
                pass

def reset_form():
    preferences_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)
    result_frame.pack_forget()
    result_frame.pack(fill=tk.BOTH, expand=True)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Book Recommendation System")

# Définir une police pour les textes
bold_font = font.Font(family="Helvetica", size=12, weight="bold")
normal_font = font.Font(family="Helvetica", size=10)

# Ajouter des éléments à la fenêtre
frame = ttk.Frame(root, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

# Champ pour entrer les préférences
preferences_label = ttk.Label(frame, text="Enter preferred genres (comma-separated):", font=bold_font)
preferences_label.pack(anchor=tk.W, padx=5, pady=5)

preferences_entry = ttk.Entry(frame, width=40)
preferences_entry.pack(anchor=tk.W, padx=5, pady=5)

# Champ pour rechercher des livres
search_label = ttk.Label(frame, text="Search for a book title:", font=bold_font)
search_label.pack(anchor=tk.W, padx=5, pady=5)

search_entry = ttk.Entry(frame, width=40)
search_entry.pack(anchor=tk.W, padx=5, pady=5)

# Boutons pour obtenir des recommandations
recommend_button = tk.Button(frame, text="Get Recommendations", command=get_recommendations, bg="#4CAF50", fg="white", font=bold_font)
recommend_button.pack(anchor=tk.W, padx=5, pady=10)

top_rated_button = tk.Button(frame, text="Top Rated Books", command=get_top_rated_books, bg="#2196F3", fg="white", font=bold_font)
top_rated_button.pack(anchor=tk.W, padx=5, pady=10)

random_button = tk.Button(frame, text="Random Recommendations", command=get_random_recommendations, bg="#FF5722", fg="white", font=bold_font)
random_button.pack(anchor=tk.W, padx=5, pady=10)

search_button = tk.Button(frame, text="Search", command=search_books, bg="#FFC107", fg="white", font=bold_font)
search_button.pack(anchor=tk.W, padx=5, pady=10)

# Bouton pour réinitialiser le formulaire
reset_button = tk.Button(frame, text="Reset", command=reset_form, bg="#f44336", fg="white", font=bold_font)
reset_button.pack(anchor=tk.W, padx=5, pady=10)

# Frame pour afficher les résultats
result_frame = ttk.Frame(frame, padding="10")
result_frame.pack(fill=tk.BOTH, expand=True)

root.mainloop()
