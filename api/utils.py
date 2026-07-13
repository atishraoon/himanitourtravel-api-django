from django.core.mail import send_mail
from django.conf import settings


def send_subscription_confirmation_email(email):

    subject = "Welcome to Himani Tour & Travel Newsletter ✈️ | Himani Tour & Travel"

    message = """
Dear Traveler,

Thank you for subscribing to the Himani Tour & Travel newsletter.

From now on, you'll receive travel updates, exclusive tour packages, special offers, travel tips, and the latest news from Himani Tour & Travel.

If you have any questions or need assistance planning your next trip, feel free to contact us.

Email: info@himanitourtravel.com

Thank you for being a part of the Himani Tour & Travel community.

Best Regards,
Himani Tour & Travel
"""

    html_message = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Newsletter Subscription Confirmation</title>
</head>

<body style="margin:0;padding:0;background:#f4f4f4;font-family:Arial,Helvetica,sans-serif;">

<table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f4f4;padding:40px 0;">
<tr>
<td align="center">

<table width="650" cellpadding="0" cellspacing="0"
style="background:#ffffff;border-radius:12px;overflow:hidden;box-shadow:0 10px 25px rgba(0,0,0,.08);">

<!-- Header -->
<tr>
<td align="center" style="background:#111111;padding:35px;">

<img
src="https://res.cloudinary.com/iyiqdcpr/image/upload/v1783761532/profile_logo_ghuymz.jpg"
alt="Himani Tour & Travel"
style="max-width:320px;width:100%;height:auto;">

</td>
</tr>

<!-- Content -->
<tr>
<td style="padding:45px;">

<h2 style="margin-top:0;color:#C9A227;font-size:30px;">
Welcome to Our Newsletter! ✈️
</h2>

<p style="font-size:16px;color:#555;line-height:1.8;">
Dear Traveler,
</p>

<p style="font-size:16px;color:#555;line-height:1.8;">
Thank you for subscribing to the <strong>Himani Tour & Travel</strong> newsletter.
</p>

<div style="background:#FFF8E8;border-left:5px solid #C9A227;padding:25px;border-radius:8px;margin:35px 0;">

<h3 style="margin-top:0;color:#C9A227;">
🎉 You're Successfully Subscribed!
</h3>

<p style="margin:0;color:#555;font-size:16px;line-height:1.8;">
From now on, you'll receive:
</p>

<ul style="color:#555;font-size:16px;line-height:2;margin-top:15px;padding-left:20px;">
<li>Exclusive tour packages</li>
<li>Special travel offers & discounts</li>
<li>Latest travel updates</li>
<li>Helpful travel tips</li>
<li>News from Himani Tour & Travel</li>
</ul>

</div>

<p style="font-size:16px;color:#555;line-height:1.8;">
If you have any questions or need assistance planning your next trip, feel free to contact us anytime.
</p>

<p style="font-size:16px;">
📧
<a href="mailto:info@himanitourtravel.com"
style="color:#C9A227;text-decoration:none;font-weight:bold;">
info@himanitourtravel.com
</a>
</p>

<p style="font-size:16px;color:#555;line-height:1.8;">
Thank you for being a part of the Himani Tour & Travel community.
</p>

<p style="font-size:16px;color:#555;line-height:1.8;">
Best Regards,<br>
<strong>Himani Tour & Travel</strong>
</p>

</td>
</tr>

<!-- Social -->

<tr>
<td align="center" style="padding:0 40px 40px;">

<h3 style="color:#222;margin-bottom:20px;">
Follow Us
</h3>

<a href="https://www.facebook.com/profile.php?id=61591582268690"
style="display:inline-block;margin:6px;padding:12px 22px;background:#1877F2;color:#fff;text-decoration:none;border-radius:5px;font-weight:bold;">
Facebook
</a>

<a href="https://www.instagram.com/himanitourtravel/"
style="display:inline-block;margin:6px;padding:12px 22px;background:#E1306C;color:#fff;text-decoration:none;border-radius:5px;font-weight:bold;">
Instagram
</a>

<a href="https://x.com/himanitour"
style="display:inline-block;margin:6px;padding:12px 22px;background:#000;color:#fff;text-decoration:none;border-radius:5px;font-weight:bold;">
X
</a>

<a href="https://www.youtube.com/@himanitourtravels"
style="display:inline-block;margin:6px;padding:12px 22px;background:#FF0000;color:#fff;text-decoration:none;border-radius:5px;font-weight:bold;">
YouTube
</a>

</td>
</tr>

<!-- Footer -->

<tr>
<td style="background:#111111;padding:35px;text-align:center;">

<h2 style="margin:0;color:#C9A227;">
Himani Tour & Travel
</h2>

<p style="margin:15px 0;color:#dddddd;font-size:15px;line-height:1.8;">
Creating unforgettable journeys with trusted travel experiences across Himachal Pradesh and beyond.
</p>

<p style="margin:8px 0;">
<a href="mailto:info@himanitourtravel.com"
style="color:#C9A227;text-decoration:none;">
📧 info@himanitourtravel.com
</a>
</p>

<p style="margin-top:30px;color:#888;font-size:12px;">
© 2026 Himani Tour & Travel. All Rights Reserved.
</p>

</td>
</tr>

</table>

</td>
</tr>
</table>

</body>
</html>
"""

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        html_message=html_message,
        fail_silently=False,
    )



def send_travel_inquiry_confirmation_email(email, full_name):
    subject = "Your Travel Inquiry Has Been Received ✈️ | Himani Tour & Travel"

    message = f"""
Dear {full_name},

Thank you for contacting Himani Tour & Travel.

We have successfully received your travel inquiry and appreciate your interest in traveling with us.

Our travel experts are now reviewing your request. Within the next 24 hours, we'll prepare a personalized travel plan based on your requirements, including:

• Best available packages
• Hotel recommendations
• Transportation options
• Sightseeing itinerary
• Transparent pricing

If we require any additional information, one of our travel consultants will contact you.

Need immediate assistance?

Email: info@himanitourtravel.com

Thank you for choosing Himani Tour & Travel.

Best Regards,

Himani Tour & Travel
"""

    html_message = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Travel Inquiry Confirmation</title>
</head>

<body style="margin:0;padding:0;background:#f4f4f4;font-family:Arial,Helvetica,sans-serif;">

<table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f4f4;padding:40px 0;">
<tr>
<td align="center">

<table width="650" cellpadding="0" cellspacing="0"
style="background:#ffffff;border-radius:12px;overflow:hidden;box-shadow:0 10px 25px rgba(0,0,0,.08);">

<!-- Header -->
<tr>
<td align="center" style="background:#111111;padding:35px;">

<img
src="https://res.cloudinary.com/iyiqdcpr/image/upload/v1783761532/web_logo_exgxhk.jpg"
alt="Himani Tour & Travel"
style="max-width:320px;width:100%;height:auto;">

</td>
</tr>

<!-- Content -->
<tr>
<td style="padding:45px;">

<h2 style="margin-top:0;color:#C9A227;font-size:30px;">
Thank You, {full_name}! ✈️
</h2>

<p style="font-size:16px;color:#555;line-height:1.8;">
We've successfully received your travel inquiry.
</p>

<p style="font-size:16px;color:#555;line-height:1.8;">
Thank you for choosing <strong>Himani Tour & Travel</strong>. Our travel experts are reviewing your request and preparing the best travel options for you.
</p>

<div style="background:#FFF8E8;border-left:5px solid #C9A227;padding:25px;border-radius:8px;margin:35px 0;">

<h3 style="margin-top:0;color:#C9A227;">
📌 What Happens Next?
</h3>

<ul style="color:#555;font-size:16px;line-height:1.9;padding-left:20px;">
<li>Your inquiry has been assigned to our travel team.</li>
<li>We'll prepare a personalized itinerary.</li>
<li>You'll receive hotel, sightseeing, transport and pricing details.</li>
<li>One of our travel consultants will contact you within <strong>24 hours</strong>.</li>
</ul>

</div>

<div style="background:#F7F7F7;padding:20px;border-radius:8px;margin-bottom:30px;">

<h3 style="margin-top:0;color:#222;">
Why Choose Us?
</h3>

<p style="margin:0;color:#555;line-height:1.8;">
✅ Customized Tour Packages<br>
✅ Affordable Pricing<br>
✅ Trusted Local Travel Experts<br>
✅ Comfortable Hotels & Transport<br>
✅ 24×7 Customer Support
</p>

</div>

<p style="font-size:16px;color:#555;">
Need immediate assistance?
</p>

<p style="font-size:16px;">
📧
<a href="mailto:info@himanitourtravel.com"
style="color:#C9A227;text-decoration:none;font-weight:bold;">
info@himanitourtravel.com
</a>
</p>

</td>
</tr>

<!-- Social -->

<tr>
<td align="center" style="padding:0 40px 40px;">

<h3 style="color:#222;margin-bottom:20px;">
Stay Connected
</h3>

<a href="https://www.facebook.com/profile.php?id=61591582268690"
style="display:inline-block;margin:6px;padding:12px 22px;background:#1877F2;color:#fff;text-decoration:none;border-radius:5px;font-weight:bold;">
Facebook
</a>

<a href="https://www.instagram.com/himanitourtravel/"
style="display:inline-block;margin:6px;padding:12px 22px;background:#E1306C;color:#fff;text-decoration:none;border-radius:5px;font-weight:bold;">
Instagram
</a>

<a href="https://x.com/himanitour"
style="display:inline-block;margin:6px;padding:12px 22px;background:#000;color:#fff;text-decoration:none;border-radius:5px;font-weight:bold;">
X
</a>

<a href="https://www.youtube.com/@himanitourtravels"
style="display:inline-block;margin:6px;padding:12px 22px;background:#FF0000;color:#fff;text-decoration:none;border-radius:5px;font-weight:bold;">
YouTube
</a>

</td>
</tr>

<!-- Footer -->

<tr>
<td style="background:#111111;padding:35px;text-align:center;">

<h2 style="margin:0;color:#C9A227;">
Himani Tour & Travel
</h2>

<p style="margin:15px 0;color:#dddddd;font-size:15px;line-height:1.8;">
Creating unforgettable journeys with trusted travel experiences across Himachal Pradesh and beyond.
</p>

<p style="margin:8px 0;">
<a href="mailto:info@himanitourtravel.com"
style="color:#C9A227;text-decoration:none;">
📧 info@himanitourtravel.com
</a>
</p>

<p style="margin-top:30px;color:#888;font-size:12px;">
© 2026 Himani Tour & Travel. All Rights Reserved.
</p>

</td>
</tr>

</table>

</td>
</tr>
</table>

</body>
</html>
"""

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        html_message=html_message,
        fail_silently=False,
    )



def send_payment_success_email(package, amount_paid):
    """
    Sends a branded payment confirmation email after a successful
    Razorpay payment, matching the Himani Tour & Travel newsletter style.

    package      : PackagePayment instance (already updated/saved)
    amount_paid  : Decimal - the amount paid in THIS transaction
                   (pass this in before current_amount_to_pay gets
                   overwritten in _mark_package_paid)
    """

    subject = "Payment Received ✅ | Himani Tour & Travel"

    if package.status == "complete":
        status_text = "Your package is now fully paid. No further payments are due. 🎉"
        balance_line = ""
    else:
        status_text = "We've recorded this installment against your package."
        balance_line = (
            f"\nRemaining balance: Rs. {package.current_amount_to_pay} "
            f"out of Rs. {package.total_package_amount} total.\n"
        )

    message = f"""
Dear {package.full_name},

We've received your payment of Rs. {amount_paid} for:
{package.package_detail}

{status_text}
{balance_line}
Payment ID: {package.razorpay_payment_id}

If you have any questions, feel free to contact us.

Email: info@himanitourtravel.com

Thank you for choosing Himani Tour & Travel.

Best Regards,
Himani Tour & Travel
"""

    if package.status == "complete":
        status_html_block = """
<div style="background:#EAF7EE;border-left:5px solid #2E9E4E;padding:25px;border-radius:8px;margin:35px 0;">
<h3 style="margin-top:0;color:#2E9E4E;">🎉 Fully Paid!</h3>
<p style="margin:0;color:#555;font-size:16px;line-height:1.8;">
Your package is now fully paid. No further payments are due.
</p>
</div>
"""
    else:
        status_html_block = f"""
<div style="background:#FFF8E8;border-left:5px solid #C9A227;padding:25px;border-radius:8px;margin:35px 0;">
<h3 style="margin-top:0;color:#C9A227;">Installment Received</h3>
<p style="margin:0;color:#555;font-size:16px;line-height:1.8;">
Remaining balance: <strong>Rs. {package.current_amount_to_pay}</strong>
out of <strong>Rs. {package.total_package_amount}</strong> total.
</p>
</div>
"""

    html_message = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Payment Confirmation</title>
</head>

<body style="margin:0;padding:0;background:#f4f4f4;font-family:Arial,Helvetica,sans-serif;">

<table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f4f4;padding:40px 0;">
<tr>
<td align="center">

<table width="650" cellpadding="0" cellspacing="0"
style="background:#ffffff;border-radius:12px;overflow:hidden;box-shadow:0 10px 25px rgba(0,0,0,.08);">

<!-- Header -->
<tr>
<td align="center" style="background:#111111;padding:35px;">

<img
src="https://res.cloudinary.com/iyiqdcpr/image/upload/v1783761532/profile_logo_ghuymz.jpg"
alt="Himani Tour & Travel"
style="max-width:320px;width:100%;height:auto;">

</td>
</tr>

<!-- Content -->
<tr>
<td style="padding:45px;">

<h2 style="margin-top:0;color:#C9A227;font-size:30px;">
Payment Received ✅
</h2>

<p style="font-size:16px;color:#555;line-height:1.8;">
Dear {package.full_name},
</p>

<p style="font-size:16px;color:#555;line-height:1.8;">
We've received your payment of <strong>Rs. {amount_paid}</strong> for:<br>
<strong>{package.package_detail}</strong>
</p>

{status_html_block}

<p style="font-size:16px;color:#555;line-height:1.8;">
<strong>Payment ID:</strong> {package.razorpay_payment_id}
</p>

<p style="font-size:16px;color:#555;line-height:1.8;">
If you have any questions or need assistance, feel free to contact us anytime.
</p>

<p style="font-size:16px;">
📧
<a href="mailto:info@himanitourtravel.com"
style="color:#C9A227;text-decoration:none;font-weight:bold;">
info@himanitourtravel.com
</a>
</p>

<p style="font-size:16px;color:#555;line-height:1.8;">
Thank you for choosing Himani Tour & Travel.
</p>

<p style="font-size:16px;color:#555;line-height:1.8;">
Best Regards,<br>
<strong>Himani Tour & Travel</strong>
</p>

</td>
</tr>

<!-- Social -->

<tr>
<td align="center" style="padding:0 40px 40px;">

<h3 style="color:#222;margin-bottom:20px;">
Follow Us
</h3>

<a href="https://www.facebook.com/profile.php?id=61591582268690"
style="display:inline-block;margin:6px;padding:12px 22px;background:#1877F2;color:#fff;text-decoration:none;border-radius:5px;font-weight:bold;">
Facebook
</a>

<a href="https://www.instagram.com/himanitourtravel/"
style="display:inline-block;margin:6px;padding:12px 22px;background:#E1306C;color:#fff;text-decoration:none;border-radius:5px;font-weight:bold;">
Instagram
</a>

<a href="https://x.com/himanitour"
style="display:inline-block;margin:6px;padding:12px 22px;background:#000;color:#fff;text-decoration:none;border-radius:5px;font-weight:bold;">
X
</a>

<a href="https://www.youtube.com/@himanitourtravels"
style="display:inline-block;margin:6px;padding:12px 22px;background:#FF0000;color:#fff;text-decoration:none;border-radius:5px;font-weight:bold;">
YouTube
</a>

</td>
</tr>

<!-- Footer -->

<tr>
<td style="background:#111111;padding:35px;text-align:center;">

<h2 style="margin:0;color:#C9A227;">
Himani Tour & Travel
</h2>

<p style="margin:15px 0;color:#dddddd;font-size:15px;line-height:1.8;">
Creating unforgettable journeys with trusted travel experiences across Himachal Pradesh and beyond.
</p>

<p style="margin:8px 0;">
<a href="mailto:info@himanitourtravel.com"
style="color:#C9A227;text-decoration:none;">
📧 info@himanitourtravel.com
</a>
</p>

<p style="margin-top:30px;color:#888;font-size:12px;">
© 2026 Himani Tour & Travel. All Rights Reserved.
</p>

</td>
</tr>

</table>

</td>
</tr>
</table>

</body>
</html>
"""

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[package.email],
            html_message=html_message,
            fail_silently=False,
        )
        return True
    except Exception as e:
        # Don't let an email failure break the payment flow - just log it.
        # Swap this print for proper logging (Python's logging module,
        # Sentry, etc.) in production.
        print(f"[send_payment_success_email] Failed to send email to "
              f"{package.email}: {e}")
        return False