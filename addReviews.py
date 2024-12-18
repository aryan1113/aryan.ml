import os
from datetime import datetime

def add_movie_review(title, rating , brief_review, genre, watchDate ,file_path='media/rating.md'):
    """
    Add a new movie review to the markdown file.
    
    :param title: Title of the movie
    :param rating: Rating as a number, will be scaled down to stars (e.g., "★★★☆☆")
    :param brief_review: Short review text
    :param genre: Movie genre
    :param file_path: Path to the markdown file (default: _pages/reviews.md)
    """
    # # Validate inputs
    # if not all([title, rating, brief_review, genre, watchDate]):
    #     raise ValueError("All fields must be filled out")
    
    # Scale rating to star format
    rating = rating // 2
    str_rating = rating * "★" + ( 5 - rating ) * "☆"
    
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
- **Rating**: {str_rating}
- **Genre**: {genre}
- **Date** : {watchDate}
- **Brief Review**: {brief_review}
"""
    
    # To append movie at the end
    insertion_index = 8
    content.insert(insertion_index, new_review + "\n")
    
    # Write back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(content)
    
    print(f"Successfully added review for '{title}' to {file_path}")

# Example usage
def main():
    # Demonstration of how to use the function
    add_movie_review(
        title="alsonewstuff",
        rating= 0,
        brief_review="""
        sample review
        """,
        genre="Science Fiction",
        watchDate="17 April 2024"
    )

if __name__ == "__main__":
    main()
