import os
import sys

sys.path.append(os.getcwd)

from sqlalchemy import (create_engine, PrimaryKeyConstraint, Column, String, Integer)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from sqlalchemy.orm import session


Base = declarative_base()
engine = create_engine('sqlite:///db/restaurants.db', echo=True)



class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

    def full_review(self):
        return f'Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars.'

    def __repr__(self):
        return f'Review (Rating: {self.star_rating})'
    


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    price = Column(Integer)

Restaurant.reviews = relationship('Review', back_populates='restaurant')

def restaurant(self):
        return self.restaurant

def reviews(self):
        return self.reviews

def customers(self):
        return [review.customer for review in self.reviews]

@classmethod
def fanciest(cls):
        fanciest_restaurant = cls.query.first()
        for restaurant in cls.query[1:]:
            if restaurant.price > fanciest_restaurant.price:
                fanciest_restaurant = restaurant
        return fanciest_restaurant

def all_reviews(self):
        return [review.full_review() for review in self.reviews]

def __repr__(self):
        return f'Restaurant: {self.name}'



class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

Customer.reviews = relationship('Review', back_populates='customer')

def customer(self):
        return self.customer

def reviews(self):
        return self.reviews

def restaurants(self):
        return [review.restaurant for review in self.reviews]

def full_name(self):
        return f'{self.first_name} {self.last_name}'

def favorite_restaurant(self):
        if not self.reviews:
            return None
        favorite_restaurant = self.reviews[0].restaurant
        for review in self.reviews[1:]:
            if review.star_rating > favorite_restaurant.reviews[-1].star_rating:
                favorite_restaurant = review.restaurant
        return favorite_restaurant

def add_review(self, restaurant, rating):
        new_review = Review(restaurant=restaurant, customer=self, star_rating=rating)
        self.reviews.append(new_review)
        session.add(new_review)
        session.commit()

def delete_reviews(self, restaurant):
        for review in self.reviews:
            if review.restaurant_id == restaurant.id:
                session.delete(review)
                session.commit()

def __repr__(self):
        return f'Customer: {self.first_name} {self.last_name}' 

