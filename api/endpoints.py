class Endpoints:
    USERS = "/users"
    PRODUCTS = "/products"
    POSTS = "/posts"
    COMMENTS = "/comments"

    @staticmethod
    def user_by_id(user_id):
        return f"/users/{user_id}"

    @staticmethod
    def product_by_id(product_id):
        return f"/products/{product_id}"