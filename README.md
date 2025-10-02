# Movie Analyzer

A simple movie analysis tool that allows users to fetch movie data, analyze ratings, and manage movie collections.

## What's New
- **Added** new `Movie`, `MovieFetcher`, and `MovieAnalyzer` classes to handle movie objects, fetching movie data from the OMDb API, and analyzing a collection of movies.
- **Introduced** methods for saving/loading movie data as JSON.
- **Added** logging capabilities to track actions during movie analysis.
- **Deprecated** the redundant `add` function for summing two numbers.

## Getting Started

### Prerequisites
Make sure you have Python 3.x installed. You can check your Python version by running:

```bash
python --version
```

### Installation
Clone the repository:

```bash
git clone https://github.com/yourusername/repo.git
cd repo
```

### Usage
To run the Movie Analyzer, simply execute the `baby.py` script:

```bash
python baby.py
```

### API Documentation

#### Movie Class
- **`class Movie`**
  - A class representing a Movie object.
  
  **Methods**
  - **`__init__(self, title: str, year: int, rating: float, genre: str)`**  
    Initializes the Movie object with the specified attributes.
    
  - **`__repr__(self)`**  
    Returns a string representation of the Movie object.

#### MovieFetcher Class
- **`class MovieFetcher`**
  - A class responsible for fetching movie data from the OMDb API.
  
  **Class Variables**
  - `API_URL`: URL of the OMDb API.
  - `API_KEY`: Key for accessing the OMDb API.
  
  **Methods**
  - **`fetch_movie(cls, title: str) -> Dict[str, Any]`**  
    Fetches movie data from the OMDb API for the given title. Returns a dictionary with movie data if found; otherwise, logs a warning and returns an empty dictionary.

#### MovieAnalyzer Class
- **`class MovieAnalyzer`**
  - A class for analyzing a collection of Movie objects.
  
  **Methods**
  - **`__init__(self)`**  
    Initializes a new MovieAnalyzer with an empty movie list.
    
  - **`add_movie(self, movie: Movie)`**  
    Adds a Movie object to the analyzer's collection and logs the action.
  
  - **`average_rating(self) -> float`**  
    Returns the average rating of the movies in the collection.
  
  - **`top_rated(self, n=3) -> List[Movie]`**  
    Returns the top `n` rated movies from the collection.
  
  - **`by_genre(self, genre: str) -> List[Movie]`**  
    Returns a list of movies that match the specified genre.
  
  - **`save_to_file(self, filename="movies.json")`**  
    Saves the current movie collection to a specified JSON file.
  
  - **`load_from_file(self, filename="movies.json")`**  
    Loads movie data from a specified JSON file into the analyzer's collection.

#### Main Function
- **`main()`**  
  The main function to run the Movie Analyzer. It loads existing movie data, fetches new movie data, and displays results.

## Usage Examples
Here are some basic usage examples to illustrate how to working with the new classes.

### Adding Movies
```python
from baby import Movie, MovieAnalyzer

analyzer = MovieAnalyzer()
new_movie = Movie("Inception", 2010, 8.8, "Sci-Fi")
analyzer.add_movie(new_movie)
```

### Fetching a Movie
```python
from baby import MovieFetcher

movie_data = MovieFetcher.fetch_movie("The Matrix")
print(movie_data)
```

### Analyzing Movies
```python
average_rating = analyzer.average_rating()
print(f"Average Movie Rating: {average_rating}")

top_movies = analyzer.top_rated(5)
print("Top Rated Movies:")
for movie in top_movies:
    print(movie)
```

### Saving and Loading Movies
```python
analyzer.save_to_file("my_movies.json")

# Later...
new_analyzer = MovieAnalyzer()
new_analyzer.load_from_file("my_movies.json")
```

### Deprecated Functions
- **`add(a, b)`** was removed. Please use the `MovieAnalyzer` methods for movie-related operations instead.

## Logging
The Movie Analyzer logs all operations in `movie_analyzer.log`. Check this file for detailed operational logs.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.