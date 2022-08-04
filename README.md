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

Epic 6 - Blog:

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
- [Figma](https://www.figma.com/)
Used for creating the wireframes

# Validation
## HTML Validation
[W3c Markup Validation Service](https://validator.w3.org/) has been used to validate all of the HTML code within the site. All pages have passed with 0 errors and 0 warnings. Click on the below to see each screenshot:
1. <details><summary>Homepage</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/html/index-html.png"></details>
1. <details><summary>Blog</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/html/blog-html.png"></details>
1. <details><summary>Blog Post</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/html/blog-post-html.png"></details>
1. <details><summary>Checkout</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/html/checkout-html.png"></details>
1. <details><summary>Login</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/html/login-html.png"></details>
1. <details><summary>Product filtered on category</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/html/product-category-html.png"></details>
1. <details><summary>Product Detail</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/html/product-detail-html.png"></details>
1. <details><summary>Products</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/html/products-html.png"></details>
1. <details><summary>Signup</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/html/signup-html.png"></details>


## CSS Validation
[W3c CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate the CSS of the site. The stylesheet.css file returned with 0 errors. When running on the whole page it returned with 15 errors all of which can be attributed to Bootstrap v5.0. See below link to screenshot:
1. <details><summary>Whole Page</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/css/whole-page-css.png"></details>
1. <details><summary>Base.css</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/css/base-css.png"></details>

## Accessibility Validation
[WAVE WebAIM web accessibility evaluation tool](https://wave.webaim.org/) has been used to validate the site to the recognised standards when it comes to accessibility. All pages have passed with 0 errors. Click on the below to see each screenshot:
1. <details><summary>Homepage</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/wave/index-wave.png"></details>
1. <details><summary>Blog Post</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/wave/blog-post-wave.png"></details>
1. <details><summary>Blog</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/wave/blog-wave.png"></details>
1. <details><summary>Cart</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/wave/cart-wave.png"></details>
1. <details><summary>Login</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/wave/login-wave.png"></details>
1. <details><summary>Product Detail</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/wave/product-detail-wave.png"></details>
1. <details><summary>Products</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/wave/products-wave.png"></details>
1. <details><summary>Signup</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/wave/signup-wave.png"></details>


## Pyhton - PEP8
[PEP8](http://pep8online.com) has been used to validate all of the python code within the site. All files have passed with 0 errors. Click on the below to see each screenshot:
1. <details><summary>Blog - Forms</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/blog-forms-pep8.png"></details>
1. <details><summary>Blog - Models</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/blog-models-pep8.png"></details>
1. <details><summary>Blog - URLS</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/blog-urls-pep8.png"></details>
1. <details><summary>Blog - Views</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/blog-views-pep8.png"></details>
1. <details><summary>Cart - Context</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/cart-context-pep8.png"></details>
1. <details><summary>Cart - URLS</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/cart-urls-pep8.png"></details>
1. <details><summary>Cart - Views</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/cart-views-pep8.png"></details>
1. <details><summary>Checkout - Forms</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/checkout-forms-pep8.png"></details>
1. <details><summary>Checkout - Models</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/checkout-models-pep8.png"></details>
1. <details><summary>Checkout - Signals</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/checkout-signals-pep8.png"></details>
1. <details><summary>Checkout - URLS</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/checkout-urls-pep8.png"></details>
1. <details><summary>Checkout - Views</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/checkout-views-pep8.png"></details>
1. <details><summary>Checkout - Webhook Handler</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/checkout-webhook-handler-pep8.png"></details>
1. <details><summary>Checkout - Webhooks</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/checkout-webhooks-pep8.png"></details>
1. <details><summary>Products - Forms</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/products-forms-pep8.png"></details>
1. <details><summary>Products - Models</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/products-models-pep8.png"></details>
1. <details><summary>Products - URLS</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/products-urls-pep8.png"></details>
1. <details><summary>Products - Views</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/products-views-pep8.png"></details>
1. <details><summary>Products - Widgets</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/products-widgets-pep8.png"></details>
1. <details><summary>Profiles - Forms</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/profiles-forms-pep8.png"></details>
1. <details><summary>Profiles - Models</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/profiles-models-pep8.png"></details>
1. <details><summary>Profiles - URLS</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/profiles-urls-pep8.png"></details>
1. <details><summary>Profiles - Views</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/pep8/profiles-views-pep8.png"></details>


## JavaScrtip - JSHint
[JSHint](https://jshint.com) has been used to validate all of the JavaScript code within the site. All files have passes with 0 errors. Click on the below to see each screenshot:
1. <details><summary>email.js</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/jshint/emailjs-jshint.png"></details>
1. <details><summary>Products Script</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/jshint/products-jshint.png"></details>
1. <details><summary>Quantity Input Script</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/jshint/quantity-input-jshint.png"></details>
1. <details><summary>Toasts Script</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/validation/jshint/toasts-jshint.png"></details>


# Testing

I started the project with completing test driven development and saw a real benefit to it however due to time constraints I was unable to continue. Below is the coverage report for the test that have been written:

![cover_report](https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/testing/coverage_report.png)

## Testing of User Stories
### 1. As a **user** I can **experience the site on mobile or desktop** so that **I can have the same experience whether on the go or at home**

The application has been built with the thought of it being viewing on various devices. Below are screenshots of the different medias:

<details><summary>Screenshot to show user story test - mobile</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/testing/user-story-1-2.png"></details>
<details><summary>Screenshot to show user story test - tablet</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/testing/user-story-1-1.png"></details>
<details><summary>Screenshot to show user story test - desktop</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/testing/user-story-1-3.png"></details>

### 2. As a **user** I can **navigate the site intuitively** so that **I can have an enjoyable experience and see all that is offered by the site**

|Feature|Action|Expected Result|Actual Result|
|---|---|---|---| 
|Open products page|Click on shop button on homepage|Products page loads with listed products available|Works as expected|

<details><summary>Screenshot to show user story test</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/testing/user-story-2.png"></details>

### 3. As a **user** I can **access all parts of the site through a navigation bar or footer links** so that **I can view all content of the site**

|Feature|Action|Expected Result|Actual Result|
|---|---|---|---| 
|Use navbar to navigate pages|Open homepage and click on all products link in navbar|Products page loads with listed products available|Works as expected|

<details><summary>Screenshot to show user story test</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/testing/user-story-3.png"></details>

### 4. As a **user** I can **receive feedback from the site when I interact with the site** so that **I know if there are any issues or confirmations when using the site functions**

|Feature|Action|Expected Result|Actual Result|
|---|---|---|---| 
|Login success message|Open homepage and click on my account link in navbar. Then select login from the dropdown menu. Enter login information and press sign in. Success message will be displayed |Success message displayed when correct credentials are used|Works as expected|

<details><summary>Screenshot to show user story test</summary><img src="https://github.com/charliewatson1504/CI_PP5_HappinessJunkie/blob/main/docs/testing/user-story-4.png"></details>

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
- unsplash for the blog post images

# Acknowledgements
My family for supporting throughout this process