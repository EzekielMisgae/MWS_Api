from celery import shared_task

@shared_task
def fetch_order_history():
    """
    Fetch the order history of the logged in user from Amazon's API and
    insert it into the database using Django models
    """
    # Import necessary modules
    from django.contrib.auth.models import User
    from .models import Order
    import requests

    # Get the currently logged in user
    user = User.objects.get(username=request.user)

    # Make a request to Amazon's API to fetch the user's order history
    response = requests.get(
        'https://your-amazon-api-endpoint.com/orders',
        headers={'Authorization': 'Bearer ' + user.access_token}
    )

    # Parse the response and insert the orders into the database
    orders = response.json()
    for order in orders:
        Order.objects.create(user=user, **order)

@shared_task
def send_email_notification():
    """
    Send an email notification to the user when a new order is placed
    """
    # Import necessary modules
    from django.contrib.auth.models import User
    from django.core.mail import send_mail

    # Get the user who placed the order
    user = User.objects.get(username=request.user)

    # Send the email notification
    send_mail(
        'New Order Placed',
        'You have placed a new order on our website.',
        'from@example.com',
        [user.email],
        fail_silently=False,
    )

# @shared_task
# def update_order_status():
#     """
#     Update the status of an order