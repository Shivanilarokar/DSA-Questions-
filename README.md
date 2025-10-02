# Movie Analyzer README

## Overview

Movie Analyzer is a Python application designed for managing and analyzing a collection of movies. It allows users to fetch movie data from an API, store it, and perform various analyses like calculating average ratings and filtering by genre. This latest version introduces new features and classes for improved functionality.

## What's New

- **New Classes**:
  - `Movie`: Represents a movie with attributes like title, year, rating, and genre.
  - `MovieFetcher`: A utility class to fetch movie details from an external API.
  - `MovieAnalyzer`: Handles a collection of movies and provides analysis functionalities.

- **New Functions**:
  - `__init__(self, title: str, year: int, rating: float, genre: str)`: Initializes a `Movie` instance.
  - `__repr__(self)`: Returns a user-friendly string representation of the `Movie`.
  - `add_movie(self, movie: Movie)`: Adds a movie to the analyzer.
  - `save_to_file(self, filename="movies.json")`: Saves the current movie list to a JSON file.
  - `load_from_file(self, filename="movies.json")`: Loads movies from a JSON file.
  - `main()`: Entry point to run the Movie Analyzer application.
  
- **Deprecated Functions**:
  - Function `add(a, b)` removed.

## Installation

To install the required dependencies, ensure you have Python 3.x installed and run:

```bash
pip install requests
```

## Usage

### Adding a Movie

To add a movie to the analyzer, you can use the `add_movie` method:

```python
from baby import Movie, MovieAnalyzer

analyzer = MovieAnalyzer()
new_movie = Movie(title="Inception", year=2010, rating=8.8, genre="Sci-Fi")
analyzer.add_movie(new_movie)
```

### Saving and Loading Movies

Movies can be saved to and loaded from a file using:

```python
# Save movies to file
analyzer.save_to_file("my_movies.json")

# Load movies from file
analyzer.load_from_file("my_movies.json")
```

### Running the Application

To run the Movie Analyzer, you can simply call the `main()` function:

```python
from baby import main

if __name__ == "__main__":
    main()
```

### Example of Fetching a Movie

Here's how to fetch a movie using the `MovieFetcher` class:

```python
from baby import MovieFetcher

movie_data = MovieFetcher.fetch_movie("Inception")
print(movie_data)
```

## API Documentation

### Classes

#### Movie

```python
class Movie:
    def __init__(self, title: str, year: int, rating: float, genre: str)
    def __repr__(self)
```

#### MovieFetcher

```python
class MovieFetcher:
    API_URL = "https://www.omdbapi.com/"
    API_KEY = "demo"
    
    @classmethod
    def fetch_movie(cls, title: str) -> Dict[str, Any]
```

#### MovieAnalyzer

```python
class MovieAnalyzer:
    def __init__(self)
    def add_movie(self, movie: Movie)
    def average_rating(self) -> float
    def top_rated(self, n=3) -> List[Movie]
    def by_genre(self, genre: str) -> List[Movie]
    def save_to_file(self, filename="movies.json")
    def load_from_file(self, filename="movies.json")
```

### Functions

```python
def main()
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 

For any queries or contributions, please feel free to create an issue or pull request.