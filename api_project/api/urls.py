from django.urls import include, path
# from . import views

# urlpatterns = [
#     path('books/', views.BookList.as_view())  
# ]

# using viewset
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    # -------------------------
    # the `include(router.urls)` function includes all the URL patterns generated by the router.
    # List all books: GET /books/
    # Retrieve a specific book: GET /books/<id>/
    # Create a new book: POST /books/
    # Update a specific book: PUT /books/<id>/ or PATCH /books/<id>/
    # Delete a specific book: DELETE /books/<id>/


    # Endpoint for obtaining a token
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]


# -------------------------
# How to Obtain and Use Tokens
# -------------------------
# To use Token Authentication in your Django REST Framework API:
# 
# 1. **Obtain a Token:**
#    - Send a POST request to the `/api/api-token-auth/` endpoint.
#    - Include the user's credentials (`username` and `password`) in the request body.
#    - Example using cURL:
#      ```bash
#      curl -X POST -d "username=your_username&password=your_password" http://localhost:8000/api/api-token-auth/
#      ```
#    - Example using Postman:
#      ```bash
#      POST /api/api-token-auth/
#      Content-Type: application/json
#      {
#          "username": "your_username",
#          "password": "your_password"
#      }
#      ```
#    - The response will include a token, which you must use for subsequent requests.
#    - Example response:
#      ```json
#      {
#          "token": "your_generated_token"
#      }
#      ```
# 
# 2. **Use the Token:**
#    - For all API requests requiring authentication, include the token in the `Authorization` header.
#    - Example using cURL:
#      ```bash
#      curl -H "Authorization: token generated_token" http://localhost:8000/api/books/
#      ```
#    - Example using Postman:
#      - In the Headers tab, add a new key-value pair:
#        - Key: `Authorization`
#        - Value: `token generated_token`
#
#    - Replace `generated_token` with the actual token obtained from the previous step.
# 
# -------------------------
# Permissions and Access Control
# -------------------------
# The `permissions.IsAuthenticated` class is used to ensure that only authenticated users can access certain views.
# 
# - **Authenticated Users:** Only users who provide a valid token in the request headers can access the view.
# - **Unauthenticated Users:** Users without a valid token will receive a 401 Unauthorized response.
# 
# To restrict access to specific views, assign the `permission_classes` attribute to the view class.
# This is demonstrated in the `BookViewSet` class in `api/views.py`.




