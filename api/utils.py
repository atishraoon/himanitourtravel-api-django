from django.core.mail import send_mail
from django.conf import settings


def send_subscription_confirmation_email(email):

    subject = "We've Received Your Travel Inquiry ✈️ | Himani Tour & Travel"

    message = """
Dear Traveler,

Thank you for contacting Himani Tour & Travel.

We have successfully received your travel inquiry.

Our travel experts are reviewing your request and will get back to you within 24 hours with the best travel options, pricing, and itinerary based on your requirements.

If your inquiry is urgent, please feel free to contact us directly.

Email: info@himanitourtravel.com

Thank you for choosing Himani Tour & Travel.

Best Regards,
Himani Tour & Travel
"""

    html_message = """
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
src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=600"
alt="Himani Tour & Travel"
style="max-width:320px;width:100%;height:auto;">

</td>
</tr>

<!-- Content -->
<tr>
<td style="padding:45px;">

<h2 style="margin-top:0;color:#C9A227;font-size:30px;">
Thank You for Your Inquiry! ✈️
</h2>

<p style="font-size:16px;color:#555;line-height:1.8;">
Dear Traveler,
</p>

<p style="font-size:16px;color:#555;line-height:1.8;">
Thank you for reaching out to <strong>Himani Tour & Travel</strong>.
We've successfully received your travel inquiry.
</p>

<div style="background:#FFF8E8;border-left:5px solid #C9A227;padding:25px;border-radius:8px;margin:35px 0;">

<h3 style="margin-top:0;color:#C9A227;">
📌 What Happens Next?
</h3>

<p style="margin:0;color:#555;font-size:16px;line-height:1.8;">
Our travel specialists are reviewing your request.
<br><br>

<strong>Within the next 24 hours</strong>, one of our travel experts will contact you with personalized travel options, package details, pricing, and answers to any questions you may have.
</p>

</div>

<p style="font-size:16px;color:#555;line-height:1.8;">
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
src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=900"
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


