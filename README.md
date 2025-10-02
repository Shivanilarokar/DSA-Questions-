```markdown
# MovieAnalyzer

MovieAnalyzer is a Python application for managing and analyzing movies. It fetches movie data using the OMDb API, allows you to add movies, and provides functionalities for analyzing the added movie data including rating averages and genre-based filtering.

## What's New

- **New Classes**:
  - `Movie`: Represents a movie object with attributes for title, year, rating, and genre.
  - `MovieFetcher`: Handles fetching movies from the OMDb API.
  - `MovieAnalyzer`: Manages a collection of movies for analysis.
  
- **New Methods in `MovieAnalyzer`**:
  - `add_movie(self, movie: Movie)`: Add a movie to the analyzer.
  - `save_to_file(self, filename="movies.json")`: Save all movies to a JSON file.
  - `load_from_file(self, filename="movies.json")`: Load movies from a JSON file.
  - `average_rating(self) -> float`: Calculate the average rating of all movies.
  - `top_rated(self, n=3)`: Return the top n rated movies.
  - `by_genre(self, genre: str)`: Filter movies by genre.

- **New Functions**:
  - `main()`: The main function to run the analyzer.

- **Deprecated Function**:
  - The function `add(a, b)` has been removed. This functionality is no longer part of this package.

## Installation

To use MovieAnalyzer, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/movie-analyzer.git
cd movie-analyzer
pip install -r requirements.txt
```

## Usage

Below are examples of how to use the new functionality in MovieAnalyzer.

### Creating a Movie Instance

```python
from baby import Movie

# Create a new Movie instance
movie = Movie(title="Inception", year=2010, rating=8.8, genre="Sci-Fi")
print(movie)  # Output will be in the format: Inception (2010) ⭐8.8 [Sci-Fi]
```

### Fetching Movies with MovieFetcher

```python
from baby import MovieFetcher

# Fetch movie data
movie_data = MovieFetcher.fetch_movie("Inception")
print(movie_data)  # Returns a dictionary with movie details
```

### Analyzing Movies

```python
from baby import MovieAnalyzer, Movie

# Initialize the movie analyzer
analyzer = MovieAnalyzer()

# Add movie instances
analyzer.add_movie(movie)

# Calculate average rating
average = analyzer.average_rating()
print(f"Average Rating: {average}")

# Get top rated movies
top_movies = analyzer.top_rated(3)
print(f"Top Rated: {top_movies}")

# Filter movies by genre
sci_fi_movies = analyzer.by_genre("Sci-Fi")
print(f"Sci-Fi Movies: {sci_fi_movies}")

# Save movies to file
analyzer.save_to_file() 

# Load movies from file
analyzer.load_from_file()
```

### Main Function

To run the complete movie analysis workflow, including fetching and displaying movies:

```python
from baby import main

if __name__ == "__main__":
    main()
```

## API Documentation

### Classes

#### `Movie`

```python
class Movie:
    def __init__(self, title: str, year: int, rating: float, genre: str)
    def __repr__(self)
```

#### `MovieFetcher`

```python
class MovieFetcher:
    API_URL = "https://www.omdbapi.com/"
    API_KEY = "demo"

    @classmethod
    def fetch_movie(cls, title: str) -> Dict[str, Any]
```

#### `MovieAnalyzer`

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

## Contributing

Contributions are welcome! Please submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```
