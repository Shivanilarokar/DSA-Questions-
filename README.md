```markdown
# Movie Analyzer

The Movie Analyzer is a Python application designed to fetch, analyze, and store movies using the OMDb API. This README provides information about the project's structure, usage examples, and details about recent changes.

## Table of Contents
- [What's New](#whats-new)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## What's New
- **Added Classes:**
  - `Movie`: Represents a movie with title, year, rating, and genre.
  - `MovieFetcher`: Fetches movie data from the OMDb API.
  - `MovieAnalyzer`: Handles movie data operations including adding movies and generating statistics.

- **Added Functions:**
  - `__init__(self, title: str, year: int, rating: float, genre: str)` in the `Movie` class.
  - `__repr__(self)` for a string representation of a `Movie`.
  - `add_movie(self, movie: Movie)` method in the `MovieAnalyzer` class to add a movie.
  - `save_to_file(self, filename="movies.json")` to save movies to a file.
  - `load_from_file(self, filename="movies.json")` to load movies from a file.
  - `main()` function to run the application.

- **Removed Functionality:**
  - **Deprecated Function:** `add(a, b)` has been removed.

## Installation

To get started with Movie Analyzer, clone the repository and install the required packages.

```bash
git clone https://github.com/yourusername/movie-analyzer.git
cd movie-analyzer
pip install requests
```

## Usage

To use the Movie Analyzer, you can run the main function which initializes and manages movie data.

```python
from baby import main

if __name__ == "__main__":
    main()
```

### Example
Here’s an example of how to create a movie and add it using the `MovieAnalyzer` class:

```python
from baby import Movie, MovieAnalyzer

analyzer = MovieAnalyzer()

# Create a movie instance
movie = Movie(title="Inception", year=2010, rating=8.8, genre="Sci-Fi")

# Add the movie to the analyzer
analyzer.add_movie(movie)

# Calculate average rating
average_rating = analyzer.average_rating()
print(f"Average rating: {average_rating}")

# Save to file
analyzer.save_to_file()
```

## API Documentation

### Class Definitions

#### `class Movie`
Represents a movie.

- **`__init__(self, title: str, year: int, rating: float, genre: str)`**
  - Initializes a new Movie instance.

- **`__repr__(self)`**
  - Returns a string representation of the Movie instance.

#### `class MovieFetcher`
Handles fetching movie data from the OMDb API.

- **`fetch_movie(cls, title: str) -> Dict[str, Any]`**
  - Fetches movie data by title.

#### `class MovieAnalyzer`
Processes and analyzes movie data.

- **`__init__(self)`**
  - Initializes the MovieAnalyzer instance.

- **`add_movie(self, movie: Movie)`**
  - Adds a movie to the collection.

- **`average_rating(self) -> float`**
  - Returns the average rating of the analyzed movies.

- **`top_rated(self, n=3) -> List[Movie]`**
  - Returns the top n rated movies.

- **`by_genre(self, genre: str) -> List[Movie]`**
  - Returns a list of movies from a specific genre.

- **`save_to_file(self, filename="movies.json")`**
  - Saves the current movie list to a specified file.

- **`load_from_file(self, filename="movies.json")`**
  - Loads movies from a specified file.

### Removed Functions
- **Deprecated Function:** `add(a, b)` has been removed.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is open source and available under the MIT License.
```
