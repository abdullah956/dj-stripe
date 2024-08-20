# views.py

import stripe
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import JsonResponse

# Set your Stripe secret key
stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def create_checkout_session(request):
    if request.method == 'POST':
        YOUR_DOMAIN = "http://localhost:8000"  # Change this to your domain for production

        # Create a Checkout Session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Sample Product',
                        },
                        'unit_amount': 2000,  # amount in cents
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=f'{YOUR_DOMAIN}/payments/success/',
            cancel_url=f'{YOUR_DOMAIN}/payments/cancel/',
        )

        # Redirect to the checkout session URL
        return redirect(checkout_session.url, code=303)

    return JsonResponse({"error": "Invalid request"}, status=400)


def checkout_view(request):
    return render(request, 'checkout.html')


def success_view(request):
    return render(request, 'success.html')


def cancel_view(request):
    return render(request, 'cancel.html')

