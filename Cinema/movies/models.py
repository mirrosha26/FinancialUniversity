from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)
    description = models.TextField()
    duration = models.DurationField()

    def __str__(self):
        return self.title


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    rental_start_date = models.DateField()
    rental_end_date = models.DateField()
    rental_cost = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.client} - {self.movie}"
        
        
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateField()

    def __str__(self):
        return f"{self.client} - {self.movie}"
