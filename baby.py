import requests
import logging
import json
import os
import statistics
from typing import List, Dict, Any

# ----------------- Logging Setup -----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("movie_analyzer.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("MovieAnalyzer")

# ----------------- Movie Class -----------------
class Movie:
    def __init__(self, title: str, year: int, rating: float, genre: str):
        self.title = title
        self.year = year
        self.rating = rating
        self.genre = genre

    def __repr__(self):
        return f"{self.title} ({self.year}) ⭐{self.rating} [{self.genre}]"

# ----------------- Movie Data Fetcher -----------------
class MovieFetcher:
    API_URL = "https://www.omdbapi.com/"
    API_KEY = "demo"  # OMDb demo key, limited usage

    @classmethod
    def fetch_movie(cls, title: str) -> Dict[str, Any]:
        try:
            response = requests.get(
                cls.API_URL,
                params={"t": title, "apikey": cls.API_KEY},
                timeout=5
            )
            data = response.json()
            if data.get("Response") == "True":
                return data
            else:
                logger.warning(f"Movie not found: {title}")
                return {}
        except Exception as e:
            logger.error(f"Error fetching movie {title}: {e}")
            return {}

# ----------------- Movie Analyzer -----------------
class MovieAnalyzer:
    def __init__(self):
        self.movies: List[Movie] = []

    def add_movie(self, movie: Movie):
        self.movies.append(movie)
        logger.info(f"Added movie: {movie}")

    def average_rating(self) -> float:
        if not self.movies:
            return 0.0
        return round(statistics.mean([m.rating for m in self.movies]), 2)

    def top_rated(self, n=3) -> List[Movie]:
        return sorted(self.movies, key=lambda m: m.rating, reverse=True)[:n]

    def by_genre(self, genre: str) -> List[Movie]:
        return [m for m in self.movies if m.genre.lower() == genre.lower()]

    def save_to_file(self, filename="movies.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([m.__dict__ for m in self.movies], f, indent=4)
        logger.info(f"Saved {len(self.movies)} movies to {filename}")

    def load_from_file(self, filename="movies.json"):
        if not os.path.exists(filename):
            logger.warning("No saved file found.")
            return
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            for m in data:
                self.movies.append(Movie(**m))
        logger.info(f"Loaded {len(self.movies)} movies from {filename}")

# ----------------- Main Function -----------------
def main():
    analyzer = MovieAnalyzer()

    # Load old data if exists
    analyzer.load_from_file()

    # Movies to fetch
    titles = ["Inception", "The Matrix", "The Dark Knight", "Interstellar", "Fight Club"]

    for title in titles:
        data = MovieFetcher.fetch_movie(title)
        if data:
            try:
                movie = Movie(
                    title=data["Title"],
                    year=int(data["Year"].split("–")[0]),
                    rating=float(data["imdbRating"]),
                    genre=data["Genre"].split(",")[0]
                )
                analyzer.add_movie(movie)
            except Exception as e:
                logger.error(f"Error processing movie {title}: {e}")

    # Show results
    logger.info("\nAll Movies:")
    for m in analyzer.movies:
        print(m)

    logger.info(f"Average Rating: {analyzer.average_rating()}")

    logger.info("Top 3 Rated:")
    for m in analyzer.top_rated(3):
        print(m)

    logger.info("Sci-Fi Movies:")
    for m in analyzer.by_genre("Sci-Fi"):
        print(m)

    # Save results
    analyzer.save_to_file()


if __name__ == "__main__":
    main()
