from io import BytesIO
from celery import task
from xhtml2pdf import pisa
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order
from orders.utils import render_to_pdf


@task
def payment_completed(order_id):
    """Task to send an e-mail notification when an order is successfully created."""

    order = Order.objects.get(id=order_id)
    subject = f'My Shop - EE Invoice no. {order.id}'
    message = 'Please, find attached the invoice for your recent purchase.'
    email = EmailMessage(subject, message, 'admin@myshop.com', [order.email])

    pdf = render_to_pdf('admin/orders/order/pdf.html', {'order': order})
    email.attach(f'order_{order.id}.pdf', pdf.getvalue(), 'application/pdf')
    email.send()
