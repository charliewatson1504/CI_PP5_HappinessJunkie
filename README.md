# Project Title

**CI_PP5_Happiness Junkie**

## Project Overview

Happiness Junkie is an ecommerce store for a business that sells handmade knits, stickers and foil prints. It has been developed as part of the code institute diploma in full stack software development and is the 5th project of the course.

2 user accounts have been set up:

- An admin user account has been set up with username = charlie and password = admin123
- A standard user account has been set up with username = johnsmith and password = User123!
- Making a payment as a user, a test credit card of 4242424242424242 has been set up for the card number
- The expiry date, cvc and postal code/state code can use any mix of numbers but must meet the minimum amount for it to work

![Main Mockup](https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/mockup/main_mockup.png)

[Link to live site](https://happiness-junkie.herokuapp.com/)

---

# Table of Contents

- [UX](#ux)
  * [Project Goals](#project-goals)
    + [Primary goals of the website for site users are as follows:](#primary-goals-of-the-website-for-site-users-are-as-follows-)
    + [Primary goals of the website for the site owners are as follows:](#primary-goals-of-the-website-for-the-site-owners-are-as-follows-)
  * [User Stories](#user-stories)
- [Design Choices](#design-choices)
  * [Colors](#colors)
  * [Fonts](#fonts)
  * [Database](#database)
    + [Physical database model](#physical-database-model)
- [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Frameworks, libraries and other tools](#frameworks--libraries-and-other-tools)
- [Testing](#testing)
- [Deployment](#deployment)
  * [Creating an Application with Heroku](#creating-an-application-with-heroku)
    + [Heroku Settings](#heroku-settings)
    + [Heroku Deployment](#heroku-deployment)
- [Credit](#credit)
- [Acknowledgements](#acknowledgements)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


# UX

## Project Goals

### Primary goals of the website for site users are as follows:

- To register for an account on the website and receive an email after successful registration
- To login or logout from the website
- To recover my password in case it is forgotten
- To have a personalised user profile with showing booked classes
- To post a comment on a blog post
- To view website news, and comment on a news item

### Primary goals of the website for the site owners are as follows:

- To add, edit and delete PT sessions
- To add, edit and delete website news and events information

## User Stories

Epic 1 - Core Functionality:

1. As a **user** I can **experience the site on mobile or desktop** so that **I can have the same experience whether on the go or at home**
2. As a **user** I can **navigate the site intuitively** so that **I can have an enjoyable experience and see all that is offered by the site**
3. As a **user** I can **access all parts of the site through a navigation bar or footer links** so that **I can view all content of the site**
4. As a **user** I can **receive feedback from the site when I interact with the site** so that **I know if there are any issues or confirmations when using the **site functions

Epic 2 - Products:

5. As a **user** I can **view all products** so that **I can see all that the store has on offer to buy**
6. As a **user** I can **filter products into categories** so that **I can only view products that I want to see**
7. As a **user** I can **see if the products have any variations** so that **I can get the exact product I want**
8. As a **user** I can **add a product to a wish list** so that **I can save products I like for a future purchase**

Epic 3 - Orders/Cart:

9. As a **user** I can **view all items added to the cart** so that **make any amendments I wish to make**
10. As a **user** I can **purchase the items in the cart using my payment card**
11. As a **user** I can **get confirmation/error messages when interacting with the cart** so that **I am aware if there are any issues or payment has been taken successfully**

Epic 4 - Admin Functionality:

12. As an **admin user** I can **add/update/delete products from the store** so that **the store is kept up to date**
13. As an **admin user** I can **log in to the backend admin site** so that **I can manage any potential issues**
14. As an **admin user** I can **log in on the frontend and make changes to products** so that **the store is kept up to date**

Epic 5 - User Account:

15. As a **user** I can **register for an account** so that **I can save delivery information and order history**
16. As a returning user I can **log in to my account and view order history and/or update saved delivery detail**
17. As a **user** I can **clearly see if I am logged in or not**
18. As a **user** I can **reset my password via if I forget it** so that **I can use my account without having to wait for an admin to do it manually**
19. As an **admin user** only I can **see admin functions that a standard user shouldn't be able to access** so that **changes to the site can only be performed by the site staff**
20. As a **user** I can **have my account information auto-populated when logged in** so that **I don't have to waste time typing out the information again**

Epic 6 - Exhibition Information:

21. As a **user** I can **view blog posts on the site** so that **I am updated with what is happening with the business**
22. As a **user** I can **comment on the blog posts** so that **I feel I am contributing to the sites community**
23. As an **admin user** I can **add/update/delete blog posts** so that **the site can keep its community up to date with what it is doing**
24. As an **admin user** I can **approve comments left by users** so that **checks are in place to keep in line with community guidelines, for example profanity**
25. As a **user** I can **view blog posts without being logged in** so that **if I am viewing the site for the first time up-to-date information isn't hidden**

Epic 7 - Marketing:

26. As an **admin user** I have **created a Facebook business page to give the business a social presence to create engagement and boost the marketing of the site**
27. As an **admin user** I have **researched search terms and keywords that are used within the site to boost the site's visibility on search engine websites**
28. As a **user** I can **sign up to a newsletter** so that **I am kept up to date with the latest offerings from the store directly to my email inbox without having to visit the site**

# Design Choices

## Colors

![Colour Pallette](https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/color-pallet/color-pallet.png)

The color scheme was taken from the colors found in the hero image

## Fonts

I have used Roboto as the body text and Abril Fatface for the headers. Both fonts are from google fonts and compliment well. Sans-serif is in place as a backup should the browser not be able to load the primary fonts.

## Wireframes
The wireframes for the site were created in Figma and are linked below for Desktop, Tablet and Mobile devices.
### Homepage
<details><summary>Desktop/Tablet/Mobile</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/wireframes/index.pdf"></details>

### Blog
<details><summary>Desktop/Tablet/Mobile</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/wireframes/blog.pdf"></details>

### Blog Post
<details><summary>Desktop/Tablet/Mobile</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/wireframes/blog_post.pdf"></details>


### Product Detail
<details><summary>Desktop/Tablet/Mobile</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/wireframes/product_detail.pdf"></details>


### Products
<details><summary>Desktop/Tablet/Mobile</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/wireframes/products.pdf"></details>


### Profile Page
<details><summary>Desktop/Tablet/Mobile</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/wireframes/profile_page.pdf"></details>

### Shopping Cart
<details><summary>Desktop/Tablet/Mobile</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/wireframes/shopping_cart.pdf"></details>


## Database
### Physical database model
The below diagram shows all of the fields stored in the database, with details of their data types, and how it is structured.

![Database](https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/database-model/database_models.png)

# Technologies Used
## Languages
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
## Frameworks, libraries and other tools
- [Git](https://git-scm.com/)
Used for version control of the site and push code from VScode to Github
- [Github](https://github.com/)
Used as the remote repository to store the code. Github pages is also where the live site is hosted.
- [Visual Studio Code](https://code.visualstudio.com/)
Used as the IDE for writing the code and file management
- [Adobe Photoshop](https://www.adobe.com/uk/products/photoshop.html)
Used to edit and crop all image sizes on the site as original filesize were too large and affected performance
- [Google Fonts](https://fonts.google.com/)
Used for Spectral font throughout the site
- [Font Awesome](https://fontawesome.com/)
Used for various icons throughout the site
- [Bootstrap](https://getbootstrap.com/)
Used for creating a responsive navigation bar used in every header of each page. Also used for creting a modal for a booking form used on each page. Modals were used for services page in which an accordion was created using bootstrap for each service category. Bootstrap also used for creating a carousel for the review section
- [jQuery](https://jquery.com/)
Used for cleaner JavaScript code where necessary and datepicker function for booking form
- [Google Maps](https://www.google.com/maps)


# Testing

I started the project with completing test driven development and saw a real benefit to it however due to time constraints I was unable to continue. Below is the coverage report for the test that have been written:

![cover_report](https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/testing/coverage_report.png)

# Deployment
## Creating an Application with Heroku

*Code Institute* tutorial and [Django Blog cheatsheat](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf) were followed to complete deployment.

- Enter following command in the terminal so that the relevant files needed for Heroku to install your project dependencies are created - `pip3 freeze --local > requirements.txt`. A `Procfile` is also required that specifies the commands that are executed by the app on startup.

1. Go to [Heroku.com](https://dashboard.heroku.com/apps) and log in or create and account if you do not already have one.
2. Click the `New` dropdown and select `Create New App`.
3. Enter a name for your new project, all Heroku apps need to have a unique name, you will be prompted if you need to change it.
4. Select the region you are working in.

### Heroku Settings
Environment Variables need to be set up - this is key to make sure your application is deployed properly.
- In the resources tab install 'Heroku Postgres'
- In the Settings tab, click on `Reveal Config Vars` and set the following variables:
    - SECRET_KEY - your chosen key


### Heroku Deployment
In the Deploy tab:
1. Connect your Heroku account to your Github Repository following these steps:
    1. Click the `Deploy` tab then `Github-Connect to Github`.
    2. Enter GitHub repository name and click `Search`.
    3. Choose the correct repository and click `Connect`.
2. Choose to deploy the project manually whilst getting deployment correct. Automatic deployment can be set after and will generate a new application every time you push a change to Github.
3. Click `Deploy Branch` your application will be built and once complete click `open app` to view deployed application.

# Credit
- Bootstrap for the following components: navbar, modals
- Colormind for creating the colour pallette
- YouTube for many tutorial videos on different javascript aspects.
- w3school and mdn web docs for a great resource when stuck with how to get a specific piece of javascript code to work.
- stackoverflow for various issues along the way

# Acknowledgements
My family for supporting throughout this process