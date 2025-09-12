# main.py
from Design_pattern import UserService
from Design_pattern import OrderService

if __name__ == "__main__":
    user_service = UserService()
    order_service = OrderService()

    # Fetch a user
    user = user_service.get_user(1)
    print("User:", user)

    # Fetch their orders
    orders = order_service.get_orders(1)
    print("Orders:", orders)
