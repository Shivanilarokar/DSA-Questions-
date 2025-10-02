# Movie Analyzer

## Overview

The Movie Analyzer is a Python application that helps users fetch, analyze, and store information about movies. Users can retrieve movie data from an API, evaluate ratings, and categorize their collection based on various criteria.

## What's New

- **Added Classes**:
  - `Movie`: Represents a movie with attributes like `title`, `year`, `rating`, and `genre`.
  - `MovieFetcher`: Fetches movie data using an external API.
  - `MovieAnalyzer`: Analyzes the fetched movie data, calculates average ratings, and allows saving/loading movie data.

- **Added Functions**:
  - `__init__(self, title: str, year: int, rating: float, genre: str)` for `Movie`: Initializes a new movie instance.
  - `__repr__(self)`: Provides a string representation of the movie.
  - `add_movie(self, movie: Movie)`: Adds a movie to the analyzer.
  - `save_to_file(self, filename="movies.json")`: Saves the movie list to a JSON file.
  - `load_from_file(self, filename="movies.json")`: Loads movie data from a JSON file.
  - `main()`: The main entry point of the application.

- **Deprecated**:
  - The function `add(a, b)` has been removed from the application.

## Installation

Make sure you have Python installed on your machine. Use the following command to clone the repository:

```bash
git clone https://github.com/yourusername/movie-analyzer.git
```

Navigate to the project directory:

```bash
cd movie-analyzer
```

## Dependencies

Before running the application, ensure that you have the required dependencies installed. You can install them using:

```bash
pip install requests
```

## Usage

Run the application using the command:

```bash
python baby.py
```

### Example Usage

Below are examples demonstrating how to utilize the new functionality:

```python
# Create a movie instance
movie = Movie(title="Inception", year=2010, rating=8.8, genre="Sci-Fi")
print(movie)

# Create a MovieAnalyzer and add movies
analyzer = MovieAnalyzer()
analyzer.add_movie(movie)

# Save movies to a file
analyzer.save_to_file()

# Load movies from a file
analyzer.load_from_file()

# Fetch movies using MovieFetcher
fetched_data = MovieFetcher.fetch_movie("The Matrix")
if fetched_data:
    matrix_movie = Movie(
        title=fetched_data["Title"],
        year=int(fetched_data["Year"].split("–")[0]),
        rating=float(fetched_data["imdbRating"]),
        genre=fetched_data["Genre"].split(",")[0]
    )
    analyzer.add_movie(matrix_movie)

# Calculate average rating
average = analyzer.average_rating()
print(f"Average Rating: {average}")

# Get top-rated movies
top_movies = analyzer.top_rated(3)
print("Top 3 Rated Movies:")
for top_movie in top_movies:
    print(top_movie)

# List Sci-Fi movies
sci_fi_movies = analyzer.by_genre("Sci-Fi")
print("Sci-Fi Movies:")
for sci_fi_movie in sci_fi_movies:
    print(sci_fi_movie)
```

## API Documentation

### Movie Class

- **`class Movie`**  
  Represents a movie.
  
  - **`__init__(self, title: str, year: int, rating: float, genre: str)`**
    Initializes a new instance of `Movie`.

  - **`__repr__(self)`**
    Returns a string representation of the movie.

### MovieFetcher Class

- **`class MovieFetcher`**  
  Fetches movie data from an external API.

  - **`fetch_movie(cls, title: str) -> Dict[str, Any]`**
    Fetches movie information based on the title.

### MovieAnalyzer Class

- **`class MovieAnalyzer`**  
  Analyzes and manages a collection of movies.
  
  - **`__init__(self)`**
    Initializes a list to hold movies.

  - **`add_movie(self, movie: Movie)`**
    Adds a movie to the collection.

  - **`average_rating(self) -> float`**
    Returns the average rating of the movies in the collection.

  - **`top_rated(self, n=3) -> List[Movie]`**
    Returns the top `n` rated movies.

  - **`by_genre(self, genre: str) -> List[Movie]`**
    Returns a list of movies filtered by the specified genre.

  - **`save_to_file(self, filename="movies.json")`**
    Saves the movie collection to a JSON file.

  - **`load_from_file(self, filename="movies.json")`**
    Loads movies from a JSON file into the collection.

## Contributing

We welcome contributions to the Movie Analyzer! Please create an issue or submit a pull request to propose changes or enhancements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 

## Acknowledgements

- Thanks to the OMDb API for providing movie data.
- Logging is managed using Python's in-built logging library.