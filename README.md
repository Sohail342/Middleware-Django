
# Django Site Under Construction Middleware

This Django middleware displays a "Site Under Construction" page for all incoming requests. It is a useful feature when you're working on your site and want to prevent users from accessing it until it's ready

# What is Middleware?

Middleware is a way to process requests globally before they reach the view layer in a Django application. It is a framework of hooks into Django's request/response processing. Middleware can be used for various purposes, such as:

 - Modifying the request before it reaches the view.
 - Processing the response before it is sent to the client.
 - Handling exceptions or logging.
 - Adding functionality like authentication, session management, and more.

 In this project, the middleware intercepts all requests and serves a custom HTML page indicating that the site is under construction, effectively preventing users from accessing the rest of the application until it’s ready.


## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sohail342/Middleware-Django.git
   ```

2. **Create a virtual environment and activate it:** (optional)
    ```bash
    python -m venv venv
    Source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Add the middleware to your Django project settings:**
    ```bash
    MIDDLEWARE = [
    ...
    'path.core.SiteUnderConstruction',
    ...
    ]
    ```
5. **Run the development server:**
    ```bash
    python manage.py runserver

    ```


## Contact

If you have any questions or feedback, feel free to reach out:

<p align="left">
<a href="https://wa.me/+923428041928" target="blank"><img align="center" src="https://img.icons8.com/color/48/000000/whatsapp.png" alt="WhatsApp" height="30" width="40" /></a>
<a href="https://www.hackerrank.com/sohail_ahmad342" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/hackerrank.svg" alt="sohail_ahmad342" height="30" width="40" /></a>
<a href="https://www.linkedin.com/in/sohailahmad3428041928/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="sohail-ahmad342" height="30" width="40" /></a>
<a href="https://instagram.com/sohail_ahmed113" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="sohail_ahmed113" height="30" width="40" /></a>
<a href="mailto:sohailahmed34280@gmail.com" target="blank"><img align="center" src="https://img.icons8.com/ios-filled/50/000000/email-open.png" alt="Email" height="30" width="40" /></a>
</p>



