import os
from datetime import datetime

valid_genre = [
    'Action', 
    'Comedy',
    'nonsensical',
    'Sci-Fi', 
    'Horror',  
    'Drama',
    'Romance', 
    'Documentary', 
    'Anime', 
    'War',
    'Coming of Age'
]

def add_movie_review(title, rating , brief_review, genre, watchDate ,file_path='./media/rating.md'):
    """
    Add a new movie review to the markdown file.
    
    :param title: Title of the movie
    :param rating: Rating as a number, will be scaled down to stars (e.g., "★★★☆☆")
    :param brief_review: Short review text
    :param genre: Movie genre
    :param file_path: Path to the markdown file (default: ../media/reviews.md)
    """

    if genre not in valid_genre:
        
        raise ValueError(f"Invalid genre '{genre}' . Must be one of: {', '.join(valid_genre)}")

    # Scale rating to star format
    scaled_rating = rating // 2
    str_rating = scaled_rating * "★" + ( 5 - scaled_rating ) * "☆"
    
    # Read existing content
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()
    
    # If file doesn't exist, start with a basic markdown structure
    except FileNotFoundError:
        content = [
            "---\n",
            "layout: page\n",
            "title: Movie Reviews\n",
            "permalink: /reviews/\n",
            "---\n",
            "\n",
            "# Movie Reviews\n\n"
        ]
    
    # Prepare the new review entry
    new_review = f"""
### {title}
- **Rating**: {str_rating + " " + str(rating)}
- **Genre**: {genre}
- **Date** : {watchDate}
- **Brief Review**: {brief_review}
"""
    
    # To append movie at the top, use index 8
    # insertion_index = 8

    # To append movie at the end
    # insertion_index = len(content)
    content.insert(insertion_index, new_review + "\n")
    
    # Write back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(content)
    
    print(f"Successfully added review for '{title}' to {file_path}")

# Example usage
def main():
    # Demonstration of how to use the function
    add_movie_review(
        title="Fatherhood (Kevin Hart)",
        rating= 4,
        brief_review="""
        Cliche, theek hai tho
        Powerful story 
        """,
        genre="Documentary",
        watchDate="31 October 2023"
    )

if __name__ == "__main__":
    main()
