# Movie Analyzer

Welcome to the **Movie Analyzer** project! This Python application allows users to manage a collection of movies, fetch movie data from the OMDb API, analyze ratings, and save/load movie records from a file.

## Overview

The Movie Analyzer is a Python application that helps users fetch, analyze, and store information about movies. Users can retrieve movie data from an API, evaluate ratings, and categorize their collection based on various criteria.

### What's New
- Removed the following classes:
  - `Movie`: Represents a movie with attributes like `title`, `year`, `rating`, and `genre`.
  - `MovieFetcher`: Fetches movie data using an external API.
  - `MovieAnalyzer`: Analyzes the fetched movie data, calculates average ratings, and allows saving/loading movie data.
  
- The following functions have been **deprecated** and removed:
  - `main()`
  - `__init__(self, title: str, year: int, rating: float, genre: str)`
  - `__repr__(self)`
  - `add_movie(self, movie: Movie)`
  - `save_to_file(self, filename="movies.json")`
  - `load_from_file(self, filename="movies.json")`

## How to Use

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
pip install -r requirements.txt
```

Run the application using the command:

```bash
python baby.py
```

### Example Usage

Below are examples demonstrating how to utilize the new functionality:

#### 1. Create a Movie Instance
```python
movie = Movie(title="Inception", year=2010, rating=8.8, genre="Sci-Fi")
print(movie)
```

#### 2. Create a MovieAnalyzer and Add Movies
```python
analyzer = MovieAnalyzer()
analyzer.add_movie(movie)
```

#### 3. Save Movies to a File
```python
analyzer.save_to_file()
```

#### 4. Load Movies from a File
```python
analyzer.load_from_file()
```

#### 5. Fetch Movies Using MovieFetcher
```python
fetched_data = MovieFetcher.fetch_movie("The Matrix")
if fetched_data:
    matrix_movie = Movie(
        title=fetched_data["Title"],
        year=int(fetched_data["Year"].split("–")[0]),
        rating=float(fetched_data["imdbRating"]),
        genre=fetched_data["Genre"].split(",")[0]
    )
    analyzer.add_movie(matrix_movie)
```

#### 6. Calculate Average Rating
```python
average = analyzer.average_rating()
print(f"Average Rating: {average}")
```

#### 7. Get Top-Rated Movies
```python
top_movies = analyzer.top_rated(3)
print("Top 3 Rated Movies:")
for top_movie in top_movies:
    print(top_movie)
```

#### 8. List Sci-Fi Movies
```python
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

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the OMDb API for providing movie data.
- Logging is managed using Python's in-built logging library.