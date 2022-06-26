# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

# Например

from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get(self, mid=None, **kwargs):
        query = self.session.query(Movie)
        if mid:
            return query.get(mid)
        if kwargs:
            for key, value in kwargs.items():
                query = query.filter(eval(f"Movie.{key}") == int(value))
        return query.all()

    def create(self, data):
        movie = Movie(**data)
        with self.session.begin():
            self.session.add(movie)
        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        movie = self.get(mid)
        if not movie:
            return
        self.session.delete(movie)
        self.session.commit()
