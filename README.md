# Scheme Tracker

Scheme Tracker is designed to monitor the progress of schemes, which can be domestic (e.g. around the house
such as Replacement of Kitchen Taps) or commercial (e.g. School having a new sports hall).  Schemes can be created or edited as well
as being viewed.  It is an e-commerce site with products designed for various schemes
(e.g. Flash Drive for IT Projects such as Documentary on Holidays and a new personal website, Fire Extinguisher for Sports Hall).

## UX

As a user, I want to perform an action so that I can perform a goal.  Users can be individuals or businesses.

I want to edit a scheme in order to update my progress for example.

I want to get products for my scheme(s) in the place that I live in for my home or business or the site in which the works are to be carried out.

Help Text is provided where the fields do not look straightforward.  For example in the completion field,
the user may enter Not Complete.  It should be a percentage (e.g. 25 for partially complete or 100 for complete). 

Wireframes are supplied in the wireframes folder.  Documentation (narrative and presentation) is supplied in the documentation folder.

## Features

* Editing, Creating and Viewing Schemes
* E-commerce (Products)
* News
    * Exhibitions
    * Demonstrations
    * Live Music
    * Celebrities

In the news page there are PDF Downloads for News Archives (previous news), Forecasts (line graph
with data table for Total Views against Published Date from 1 July 2019 to 1 December 2019) and
Information about Open Day.

## Technologies Used

* HTML5
* CSS
* Bootstrap
* Django
* JavaScript

## Testing

Vary the width of the browser window.  Use different browsers (e.g. Microsoft Edge, Safari).
Credit Card Testing - Use the credit card number of 4242424242424242 and any security key.
External links (e.g. PDF) open in a new window without leaving the web page.

In the terminal window use python3 manage.py test schemes

## Deployment

It will be deployed to Heroku.  Make sure requirements.txt is up to date by using pip3 freeze > requirements.txt
after adding new libraries (e.g. Stripe).

## Credits

### Content

Taken from Mini Projects of DjangoBlog and Ecommerce for ideas.
The fire extinguisher is taken from a clipart image in Word 2010.  Accessed 26 June 2019.

Visited DjangoProject Website for ideas such as help text.

    https://docs.djangoproject.com/en/1.11/topics/db/models/

For the help text, 

    https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.Field.help_text

Did a Google Search on Royal Cambridge Hotel.  The address was obtained from the Contact Page of the
Royal Cambridge Hotel Website.

    https://theroyalcambridgehotel.co.uk



### Media

### Acknowledgements

Mentor - Oluwaseun Owonikoku