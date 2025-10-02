```markdown
# Movie Analyzer

Welcome to the Movie Analyzer project! This Python application allows users to manage a collection of movies, fetch movie data from the OMDb API, analyze ratings, and save/load movie records from a file.

## What's New

- **Added New Classes and Methods:**
  - `main`: The main function to execute the application.
  - Enhanced `__init__` and `__repr__` methods for the `Movie` class.
  - Methods for handling movie data:
    - `add_movie`: Adds a movie to the collection.
    - `save_to_file`: Saves the current movie collection to a JSON file.
    - `load_from_file`: Loads movies from a JSON file into the collection.
    
- **Removed Functionality:**
  - The classes `Movie`, `MovieFetcher`, and `MovieAnalyzer` have been **deprecated** and removed from the codebase.
  - The function `add(a, b)` has been **deprecated** and removed.

## Installation

To use the Movie Analyzer, clone the repository and install the required packages:

```bash
pip install requests
```

## Usage

### Fetch and Analyze Movies

You can utilize the new features to fetch and analyze movies. Here is an example of how to use the new features in this project:

```python
from baby import MovieAnalyzer, Movie, MovieFetcher

def main():
    # Create an instance of MovieAnalyzer
    analyzer = MovieAnalyzer()

    # Load existing movies
    analyzer.load_from_file()

    # Example to fetch and add movies
    titles = ["Inception", "The Matrix", "The Dark Knight", "Interstellar", "Fight Club"]
    for title in titles:
        data = MovieFetcher.fetch_movie(title)
        if data:  # Only add if movie data is found
            try:
                movie = Movie(
                    title=data["Title"],
                    year=int(data["Year"].split("–")[0]),
                    rating=float(data["imdbRating"]),
                    genre=data["Genre"].split(",")[0]
                )
                analyzer.add_movie(movie)
            except Exception as e:
                print(f"Error processing movie {title}: {e}")

    # Print all movies and average rating
    print("All Movies:")
    for m in analyzer.movies:
        print(m)

    print(f"Average Rating: {analyzer.average_rating()}")
    print("Top 3 Rated:")
    for m in analyzer.top_rated(3):
        print(m)

    print("Sci-Fi Movies:")
    for m in analyzer.by_genre("Sci-Fi"):
        print(m)

    # Save the results
    analyzer.save_to_file()

if __name__ == "__main__":
    main()
```

### Class and Function Definitions

#### Class: Movie

```python
class Movie:
    def __init__(self, title: str, year: int, rating: float, genre: str):
    def __repr__(self):
```

#### Class: MovieFetcher

```python
class MovieFetcher:
    API_URL = "https://www.omdbapi.com/"
    API_KEY = "demo"

    @classmethod
    def fetch_movie(cls, title: str) -> Dict[str, Any]:
```

#### Class: MovieAnalyzer

```python
class MovieAnalyzer:
    def __init__(self):
    def add_movie(self, movie: Movie):
    def average_rating(self) -> float:
    def top_rated(self, n=3) -> List[Movie]:
    def by_genre(self, genre: str) -> List[Movie]:
    def save_to_file(self, filename="movies.json"):
    def load_from_file(self, filename="movies.json"):
```

### Deprecated Functions

- The function `def add(a, b):` has been removed from the codebase.

## Logging

The Movie Analyzer uses logging to provide insights into operations. The log data will be saved to `movie_analyzer.log`.

Feel free to fork the repository, make changes, and submit pull requests. We always welcome contributors!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```