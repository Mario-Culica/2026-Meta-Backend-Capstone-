Little Lemon — Backend Capstone

API paths for peer review:

Menu API — View all menu items
GET http://127.0.0.1:8000/restaurant/menu/items

Menu API — Add a menu item
POST http://127.0.0.1:8000/restaurant/menu/items

Menu API — View a single menu item
GET http://127.0.0.1:8000/restaurant/menu/items/1

Menu API — Update a menu item
PUT http://127.0.0.1:8000/restaurant/menu/items/1

Menu API — Delete a menu item
DELETE http://127.0.0.1:8000/restaurant/menu/items/1

Booking API — View table bookings
GET http://127.0.0.1:8000/restaurant/booking/tables/

Booking API — Create a booking
POST http://127.0.0.1:8000/restaurant/booking/tables/

Authentication — Obtain an API token
POST http://127.0.0.1:8000/restaurant/api-token-auth/

Note: Booking API requests require authentication. Use the token endpoint to obtain a token and include it in the Authorization header as:
Authorization: Token 37abc1441f977c55db4966813d4eb6db0338ee29