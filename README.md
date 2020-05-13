# django-myshop

This project is a shop website made with Django, it contains the following features:
- add items to cart using sessions
- store products in several categories that you can filter
- make an order
- pay for the ordered items using Braintree
- sending asynchronous confirmation emails using Celery and RabbitMQ (also with a rendered pdf as attachment)
- the admin page has extended features, such as generating a pdf file for each order as well as a csv file
- Polish translation for all templates as well as the models
- a coupon system for discounts
