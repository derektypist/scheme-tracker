# Scheme Tracker

Scheme Tracker is designed to monitor the progress of schemes, which can be domestic (e.g. around the house
such as Replacement of Kitchen Taps) or commercial (e.g. School having a new sports hall).  Schemes can be created or edited as well
as being viewed.  It is an e-commerce site with products designed for various schemes
(e.g. Flash Drive for IT Projects such as Documentary on Holidays and a new personal website, Fire Extinguisher for Sports Hall).

## UX

Users can be individuals or businesses.  Examples of individuals include students, artists and homeowners.
Examples of businesses include London Borough of Bromley, Cambridgeshire County Council and Drax Power.

As a user, I want to edit a scheme in order to update my progress for example.  If the completion is
currently 30 and the building has been complete, but Health & Safety requirements have not been started,
I would change it to 70.  This is a rough estimate, as different businesses have different Health &
Safety Requirements.  For example, someone running a business from home may not need a Fire Extinguisher.

As a user, I want to get products for my scheme(s) in the place that I live in for my home or business or the site in which the works are to be carried out.

Help Text is provided where the fields do not look straightforward as they would be.  For example in the completion field,
the user may enter Not Complete.  It should be a whole number as a percentage (e.g. 25 for partially complete or 100 for complete). 
A default (e.g. 0) has been provided in the completion field.

Wireframes are supplied in the wireframes folder.  Documentation (narrative and presentation) is supplied in the documentation folder.

Links to my social media (e.g. LinkedIn) are provided.

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

Products are classed according to categories.

* Ga - Garden
* He - Health & Safety
* I - Information Technology
* Li - Lighting
* Ot - Other

## Technologies Used

* HTML5
* CSS
* Bootstrap
* Django
* JavaScript

Bootstrap - To Facilitate FontAwesome.

## Testing

Vary the width of the browser window.  Use different browsers (e.g. Microsoft Edge, Safari).

Automated Testing was done using Travis-CI.  Make sure requests==2.21 is in the requirements.txt.
Also remove the import env statement in settings.py.

Credit Card Testing - Use the credit card number of 4242424242424242 and any security key.
I do not use my own credit card for testing purposes.

Test with the stripe account that has not been activated and the message regarding unable to
take payment appears.

External links (e.g. PDF) will open in a new tab using target="_blank".  All links have been manually tested to ensure that
they are pointing to the correct destination.

In the terminal window use the command

    python3 manage.py test products

## Deployment

It will be deployed to Heroku.  Make sure requirements.txt is up to date by using 
the command

    pip3 freeze > requirements.txt

after adding new libraries (e.g. Stripe).

## Credits

### Content

Taken from Mini Projects of DjangoBlog and Ecommerce for ideas.
Also from www.github.com/derektypist/bootstrap

Visited DjangoProject Website for ideas such as help text.

    https://docs.djangoproject.com/en/1.11/topics/db/models/

For the help text, 

    https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.Field.help_text

Did a Google Search on Royal Cambridge Hotel.  In openday-info.pdf, the address was obtained from the Contact Page of the
Royal Cambridge Hotel Website.

    https://theroyalcambridgehotel.co.uk

### Media

The fire extinguisher in fireextinguishers.png was taken from clipart search of fire extinguisher in Word 2010 (Starter).  A
screenshot was taken.  Accessed 26 June 2019.

The rest of the photos (profile.jpg, colouredstakelight.jpg and flashdrive.jpg) are taken by myself.

### Acknowledgements

Mentor - Oluwaseun Owonikoku

[![Build Status](https://travis-ci.org/derektypist/scheme-tracker.svg?branch=master)](https://travis-ci.org/derektypist/scheme-tracker)