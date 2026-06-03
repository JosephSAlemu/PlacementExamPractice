class Movie:
    """
    A class to represent a movie and store the ratings of the movie.
    """
    def __init__(self, title: str, director: str):
        """
        Args:
            title (str): Name of the movie
            director (str): Director of the movie
        """
        self.title = title
        self.director = director
        self.__ratings: list[float] = []

    def add_rating(self, rating: float) -> None:
        """
        Adds a rating to this movie
        Args:
            rating (float): A rating for this movie
        """
        self.__ratings.append(rating)

    def average_rating(self) -> float:
        """
        Returns the average rating for the movie.
        Returns:
            (float): The average rating for this movie
                     If the movie has no ratings, returns -1.0
        """
        if len(self.__ratings) == 0:
            return -1.0
        else:
            sum = 0.0
            for i in self.__ratings:
                sum+=i
            return sum/len(self.__ratings)


class MovieCollection:
    """
    A class to represent a collection of movies
    """
    def __init__(self, name: str):
        """
        Args:
            name (str): Name of the movie collection
        """
        self.name = name
        self.__movies: list[Movie] = []

    def add_movie(self, title: str, director: str, ratings: list[float]) -> None:
        """
        Add a movie to the collection.
        Input:
            title (str): Name of the movie
            director(str): Name of the director for the movie
            ratings (list[float]): A list of ratings for the movie
        Returns:
            None
        """
        m = Movie(title, director)
        for i in ratings:
            m.add_rating(i)
        self.__movies.append(m)


    def rating_range(self, low: float, high: float) -> list[Movie]:
        """
        Returns a list of movies in the collection with average
        ratings between low and high (both inclusive).

        Args:
            low (float): Minimum average rating (inclusive)
            high (float): Maximum average rating (inclusive)
        Returns:
            list[Movie]: A list of movies whose average rating lies
                         between low and high
        """
        movies = []
        for i in self.__movies:
            print(i.title)
            print(i.average_rating())
            if i.average_rating() <= high and i.average_rating() >= low:
                movies.append(i)
        # Implement this method
        return movies

    def num_movies_by_director(self) -> dict[str,int]:
        """
        Returns the number of movies by each director in the collection.
        Returns:
            dict(str,int): The number of movies in the collection by director
        """
        # Implement this method
        directors = {}
        for i in self.__movies:
            print(i.director)
            if i.director not in directors.keys():
                directors[i.director] = 1
            else:
                directors[i.director]+=1

        return directors
    
if __name__ == "__main__":
    m = MovieCollection("jo")
    m.add_movie("DARK", "CHRIS", [1, 1.53, 2.6])
    m.add_movie("IDK", "CHRIS", [7, 5.53, 8.6])
    m.add_movie("TEST", "BUM", [])
    print(m.rating_range(5,8))


