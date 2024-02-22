from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Restaurant, Customer, Review

engine = create_engine('sqlite:///restaurants.db')
Base.metadata.bind = engine

# sessionmaker
Session = sessionmaker(bind=engine)

# session
session = Session()

# restaurants data
restaurant1 = Restaurant(name='KFC', price=1)
restaurant2 = Restaurant(name='Pizza Inn', price=2)
restaurant3 = Restaurant(name='Galitos', price=3)

# customers data
customer1 = Customer(first_name='John', last_name='Khan')
customer2 = Customer(first_name='Sam', last_name='Daniel')

# reviews data
review1 = Review(star_rating=2, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=3, restaurant=restaurant2, customer=customer1)
review3 = Review(star_rating=2, restaurant=restaurant3, customer=customer1)
review4 = Review(star_rating=4, restaurant=restaurant1, customer=customer2)
review5 = Review(star_rating=5, restaurant=restaurant2, customer=customer2)

# Commit the changes
session.add(restaurant1)
session.add(restaurant2)
session.add(restaurant3)
session.add(customer1)
session.add(customer2)
session.add(review1)
session.add(review2)
session.add(review3)
session.add(review4)
session.add(review5)
session.commit()
