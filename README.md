# Dolce Vita Venice Blog

Venice is a magical city with 118 islands, 400 bridges and 170 canals. However, the fact is that such unique beauty attracts millions of tourists all rushing their way between St Mark’s Square and the Rialto, trying to get that perfect canal selfie and best value glass-blown souvenir. It’s hungry and thirsty work.

This blog aims to take the beauty of Venice and combine it with the flavours of Venice, so that their time in Venice is ecpperienced the Italian way with good food and drink. Or alternatively to just learn about Venice's food and drink culture.

This blog is made for site users that are on a short visit to Venice. Time is valuable so they want to get to know about good food  at a reasonable price. If the site user is a full time expat they can read about the latest food and drink news happening in the city. The site user can also give back, by leaving comments of their real life experiences based on blog posts. They can also add their own incredible food and drink finds. This blog is made as a way to to provide users practical tips and interesting information.

## Portfolio Project 4

P4 Project for the Code Institute

[Live Site](https://estii20.github.io/)

[Website Mock-up](https:)

![Dolce Vita Venice Blog](assets/images/readme-images/am-i-responsive.png "Am I Responsive Mockup of Dolce Vita Venice Blog")

## Table of contents

- [Dolce Vita Venice Blog](#dolce-vita-venice-blog)
  - [Portfolio Project 4](#portfolio-project-4)
  - [Table of contents](#table-of-contents)
  - [UX Design](#ux-design)
    - [User stories](#user-stories)
    - [Data Model](#data-model)
    - [Site map](#site-map)
    - [Design](#design)
  - [Features](#features)
    - [Future Features](#future-features)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks and Libraries Used](#frameworks-and-libraries-used)
    - [Software and Web Applications Used](#software-and-web-applications-used)
  - [Testing](#testing)
    - [Browser Testing](#browser-testing)
    - [Responsiveness](#responsiveness)
    - [Validator Testing](#validator-testing)
      - [W3C Markup Validator](#w3c-markup-validator)
      - [W3C CSS Validator](#w3c-css-validator)
      - [JSHint](#jshint)
      - [PEP8 Online](#pep8-online)
      - [Lighthouse](#lighthouse)
      - [Django testing tools](#django-testing-tools)
    - [User Stories testing](#user-stories-testing)
    - [Further Testing](#further-testing)
    - [Solved bugs](#solved-bugs)
    - [Unresolved bugs](#unresolved-bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
    - [Acknowledgements](#acknowledgements)

## UX Design

The purpose of this blog is to offer user-generated content that is authentic and offers readers genuine value for their time visiting the site.

It intended to attract site users to read and join in with all things food and drink related in Venice, Italy.

The primary user of the site will be English speaking visitors / expats to Venice.

The aim of the site is to create a user-friendly and engaging food and drink blog. It is therefore essential to attract and retain readers. Here are some user experience (UX) principles included in this food and drink blog:

- Clean and Responsive Design:
Ensure the blog has a clean and visually appealing design that is easy on the eyes.
Use a responsive design that adapts to various screen sizes and devices, including smartphones and tablets.

- Clear Navigation:
Implement an intuitive and organised menu structure. Categories like "Restaurants," "Bars," "Food," and "Drinks" help users quickly find what they're looking for.
Clear and descriptive labels for navbar.

- High-Quality Imagery:
High-resolution images of food and drink to entice readers.

- Readable Typography:
Readable fonts which maintain consistent typography throughout the blog.
Appropriate font sizes, line spacing, and contrast for readability.

- Engaging Content:
Compelling and informative articles with clear headings and subheadings.

- Mobile Optimisation:
Blog can be viewed on various mobile devices to ensure a seamless mobile experience.
Mobile-friendly navigation menus and buttons.

- Social Sharing and Comments:
Easy for readers to share the content on social media platforms.
Enable comments to foster community engagement and discussions.

- Accessibility:
Blog is accessible to all users, including those with disabilities. The use of alt text for images. Text color chosen contrasts well to the background color to improve user visibility.

- Security Measures:
Security measures to protect the blog and user data, including SSL certificates.

- Feedback Mechanism:
Contact information so readers can reach out with questions or suggestions.

- Branding and Personality:
Unique brand identity for the blog that reflects the style and personality of Venice.
Consistant use of branding elements such as logos and colour schemes.

__Project Aims__

The primary goal for this project is to create a food and drink blog, with full CRUD functionality to registered users so that they can Create, Read, Update and Delete both blog posts and comments. The site user has full control over their posts and comments.

__Project Strategy__

Using An Agile methodology, this project was planned using a Kanban board in the GitHub Project with linked Issues based on a saved template. To cover the aims of this project, a total of ## User Stories were planned, each with their own acceptance criterias and tasks to complete. A total of ## User Stories were completed working on this project.

For more information: [Kanban Board - User Stories](https://github.com/users/estii20/projects/9/archive)

### User stories

### Data Model

### Site map

### Design

__Skeleton__

Webpage and mobile version made using [Balsamiq](https://balsamiq.cloud/skgv95c/pk5rjyb).

![Balsamiq design of index.html](assets/images/readme-images/index.png "Balsamiq Design for index.html")

__Surface__

To create a clear visual guide to the site user.

__Color Pallette__

`# 219C90`
`# E9B824`
`# EE9322`
`# D83F31`
`rgb(33, 156, 144)`
`rgb(233, 184, 36)`
`rgb(238, 147, 34)`
`rgb(216, 63, 49)`

[Colorspace](https://mycolor.space/) used to check the palette works together.

__Fonts__

The fonts chosen reflects the rich and delicious nature of Italian cuisine whilst maintaining readability.

- Garamond: Garamond is a timeless serif font that offers a sense of tradition.
- Pacifico: Pacifico is a fun and informal script font used for blog titles or special callouts.
- Bodoni: Bodoni is a classic serif font which is elegant and sophisticated.
- Sans-serif used as an alternative font.

- Fonts imported from [Google Fonts](https://fonts.google.com/).
- [Font Awesome](https://fontawesome.com/) used to add visual cues to the logo, headings, contact information, and social media links.
- Used [fontjoy](https://fontjoy.com/) to find the font for the logo and headings.

## Features

__Homepage__

- Header with Logo and Navigation Links. Logged in user navbar can Add Post, Logout, see their Username. Not logged in user can Sign in, and Register.
- Brief description of the blog content so that site visitors can know what the blog is about.
- Latest blog posts, paginated by 6 posts per page.
- Category link to relevant category group on blog post card above the blog title.
- Blog post card footer details the read time of the post, number of likes and date created on.
- Blog post card with default picture of restaurant table in Venice or alternative uploaded image reflecting the blog content.
- Link to read more which goes to the post_detail.html page.
- Footer with associated social media links, about page link, categories links and contact information.

![Logo and Navigation Links](assets/images/readme-images/logo.png "Logo and Navigation Links")

__Hero Image__

Bootstrap fully responsive carousel - three rolling images of Venice. Overlay text informs users about what the blog is about.

__Navbar__

The navbar is present on all pages of the site. It is fully responsive, on smaller devices the navbar will collapse and the navigation links are accessed using a ”hamburger menu”.
Navbar Logo is font awesome icon `fa-solid fa-wine-glass`.

- Logged-in navbar left
  - Home
  - Add Post
  - Signout
- Logged-in navbar right
  - Username with Font Awesome icon `fa-regular fa-user`
- Not logged-in user
  - Home
  - Register
  - Signin

__Jumbotron Header__

Easy to read information about the blog purpose and use. Font awesome icons used to show the main features of the blog.

- Eat Venice `fa-solid fa-pizza-slice`
- Drink Venice `fa-solid fa-wine-glass`
- Share your stories `fa-solid fa-share`

__Blockquote__

Italian quote to give the feel and branding of the site.

__Blog Post Card__

Bootsrap card layout. CSS style added to reflect the look of the blog site.

- Category Title and link
- Blog Title
- Featured Image
- Excerpt
- Read more link
- Card footer with date created, number of likes and readtime of post

__Pagination__

Bootstrap pagination with CSS style added to reflect the look of the blog site. Paginate blog posts by six per page.

__Footer__

![Footer with links to the Social Media platforms, Categories and About Page](assets/images/readme-images/footer.png "Footer with links to the Social Media platforms")

About link to about.html so that visitors can know more about the blog site.

Non-logged in user can see links to Register or Login.

Links to the main social media are used and are centered left within the footer.
The links are colored to compliment the Logo and headers.
Links have been given aria labels to help with user accessibility, they open in a separate window so the user can navigate easily between sites.

Categories menu links so that users can directly visit posts related to a particular genre.

Contact information so that users can get in touch with feedback and suggestions.
- Phone `fa fa-phone mr-3`
- Email `fa fa-envelope-o mr-3`

Copyright of Unsplash.com where images have been used.

Blog purpose as educational only website.

__Post_Detail page__

When a user clicks on a blog post, they are brought to the Post detail page. The user is shown the whole post with a commenting feature below. The user will be able to interact with the content depending on user status.

The following information will be presented to the user:

- Header with Logo and Navigation Links
- Blog Title
- Read Time
- Post Author `fa-regular fa-user`
- Created-on Date `fa-regular fa-clock`
- Featured image
- Blog content
- Author Bio - if added
- Option if logged-in user to edit/delete post if post author.
  - Delete: `fa-solid fa-delete`
  - Update: `fa-regular fa-pen-to-square`
- Likes - if logged in like functionality:
  - Unclicked `fa-regular fa-thumbs-up`
  - Clicked: `fa-solid fa-thumbs-up`
  - Counts the number of likes
- Comments - Edit/Delete comments if user if authenticated and comment author. Order the comments by date ascending.
  - Delete: `fa-solid fa-delete`
  - Update: `fa-regular fa-pen-to-square`
- Add Comments form - if user is logged-in. Alternatively, a reminder to users to login or register in order to comment.
- Footer with links to the Social Media platforms, About page, Categories and Contact Information.

Features dependent on user status:

- Comment - The comment form is presented to the user and the user can comment on the post. Once the user clicks on Submit, the comment is automatically approved and added to the list of comments. Automatically approving comments will encourage the user to continue commenting on posts, without any delays.

- Likes - Counts the number of post likes if user is logged-in.
  
- Edit Post/Delete Post - The post author will have full CRUD functionality. They can update or delete their posts.

- Edit Comment/Delete Comment - The comment author will have full CRUD functionality. They can update or delete their comments.

__Add_Post page__

- Header with Logo and Navigation Links
- 
- 
- 
- 
- Author Bio - if added.
- Footer with links to the Social Media platforms, About page, Categories and Contact Information.

__Update_Post page__

__Delete_Post page__

__Update_Comment page__

__Delete_Post page__

__Login_page__

User CRUD functionality on posts and comments, or the ability to like/unlike a post, requires users to login to the site.
The Login page can be accessed:

- Navbar link - site-wide
- Login link, in the Comment section on the Post Detail page
- In the Footer section on the homepage

The user needs to enter the following information:

- Valid username
- Correct password

__Register_page__

To fully use the site features, a user is required to register and login.
Unregistered users will be able to access the Register page:

- Navbar link - site-wide
- Register link, in the Footer section on the homepage
- Register link, in the Comment section on the Post Detail page

A new account can be easily created. The user needs to provide the following information:

- Username - must be unique
- E-mail - optional
- Password - entered twice
  
Once all fields are entered correctly, the user clicks on register and new account is automatically created and the user is redirected to the homepage.

__Logout_page__

Users enter a correct username with a matching password and clicks on Login, they are logged in and redirected to the homepage.

The Logout page can be accessed in the navbar link when a user is logged in. When the user clicks on Logout, they are directly logged out of their account and redirected to the homepage. If the user chooses to click on Cancel instead, the user will be returned to the previous page visited.

__About_page__

__Category_page__

__Admin_page__

To manage the blog content, a superuser account was created. A superuser can administer the site. The Admin page is accessed by logging in to the /admin URL with the superuser account username and password.
From the admin panel, the superuser will be able to delete and approve a specific post, comment or user. This functionality is necessary to maintain the blog and remove unwanted content. Also, a superuser can create post-drafts that can be published at a later time.

__Additional_Features__

Messages are  displayed to the user as feedback when certain actions are completed. The message will appear at the top of the screen and after 2.5 seconds it will be automatically removed.

### Future Features

- US#. Title:
  - This user story was prioritized as a could-have feature and will not be implemented at this stage due to low priority.

## Technologies Used

__Image Resizer__

[Simple Image Resizer](https://www.simpleimageresizer.com/upload)
Images resized to 300 px 300 px so that the images could be curved at the corner to soften them.

__Balsamiq__

[Balsamiq](https://balsamiq.cloud/skgv95c/pk5rjyb) used to design the arrangement of the site.

__Colorspace__

[Colorspace](https://mycolor.space/) used to check the palette works together.

__Font Awesome__

[Font Awesome](https://fontawesome.com/) provides visual cues to the user on the pages and was used for the social media icons.

### Languages Used

- HTML5
- CSS3
- JavaScript
- Python

### Frameworks and Libraries Used

- [Bootstrap:](https://getbootstrap.com/) Bootstrap CSS Framework used for styling and to build responsive web pages.
- [Cloudinary:](https://cloudinary.com/) Used to store all blog images and uploaded images.
- [Coverage:](https://coverage.readthedocs.io/en/latest/index.html) Used for measuring code coverage of Python test files.
- [Django:](https://www.djangoproject.com/) Main Python framework used in the development.
- [Django Allauth:](https://django-allauth.readthedocs.io/en/latest/index.html) Used for authentication and account registration.
- [Django Crispy Forms:](https://django-crispy-forms.readthedocs.io/en/latest/) Used to simplify the rendering of Django forms.
- [dj_database_url:](https://pypi.org/project/dj-database-url/) Used to allow database urls to connect to the postgres database.
- [Gunicorn:](https://gunicorn.org/) Green Unicorn, used as the Web Server to run Django on Heroku.
- [psycopg2:](https://pypi.org/project/psycopg2/) Used PostgreSQL database adapter.
- [Summernote:](https://github.com/summernote/django-summernote) To provide a WYSIWYG editor for customizing new blog content and add images.
- [django-social-share 2.3.0:](https://pypi.org/project/django-social-share/) Used to allow users to share blog posts to their social media accounts.

### Software and Web Applications Used

## Testing

### Browser Testing

### Responsiveness

### Validator Testing

#### W3C Markup Validator

[W3C HTML Validator](https://validator.w3.org/)

Screenshot of W3C Validator test, all pages passed

#### W3C CSS Validator

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

Screenshot of W3C Validator test, all pages passed

![Dolce Vita Venice Blog Website](assets/images/readme-images/html.png "Dolce Vita Blog wesbite validator test")

#### JSHint

#### PEP8 Online

#### Lighthouse

#### Django testing tools

Coverage test result:

### User Stories testing

### Further Testing

### Solved bugs

### Unresolved bugs

## Deployment

To access this project in GitHub;

1. Firstly Log into [Github](https://github.com/).

2. Select repository [estii20/dolce_vita_blog
](https://github.com/estii20/dolce_vita_blog).

1. Select settings from menu.

2. Select Pages from left menu bar.

3. Scroll and select Master branch from the drop down menu to deploy the website.

4. Retrieve the automatically generated link from the GitHub pages section.

__Running the project locally;__

1. To create a clone of this project follow the instructions below;

2. Create a GitPod account [Gitpod](https://gitpod.io/login/).

3. Open the Chrome browser.

4. Click to the top of the Chrome navigation bar and enable the extension Gitpod Browser Extension for Chrome.

5. Link it.

6. Restart the browser when prompted to do so.

7. Log into GitPod with your account username and password.

8. Select the project in GitHub repositories.

9. Click on the green “Gitpod” button to the top right of the page.

10. A new gitpod workspace opens.

11. It is now possible to work locally on the project.

To make updates, it is necessary to commit with commit-m and push with git push so that the updates are pushed to Github.

Cloning the project will link the changes to the project repo and will be sent for approval.

Forking the project will create a new repo and the code will belong to the user. Any changes made will notify the user and will give them the option to pull this new code to their repo.

Changes pushed to the main branch will automatically update on the site.

## Credits

__Content__

Content information researched at:
[Venice Travel Tips](https://devourtours.com/blog/visit-italy/venice-travel-tips/) and 
[Hotel Blog Post Ideas](https://hotelblogpostideas.com/)

[Quote](https://amindfultravellerblog.wordpress.com/2018/05/06/5-italian-phrases/#:~:text=Chi%20viaggia%20vive%20due%20volte,Those%20who%20travel%20live%20twice!)

[Blog name generato](https://www.brandcrowd.com/business-name-generator?code=25OFFSEM&gclid=CjwKCAjw69moBhBgEiwAUFCx2ARv8JJSpPUvebSc7X7321mn9VZpFilr4s2KJTCrzHoEyGUWFXvyHRoCbsEQAvD_BwE)

[Blog Post Content Chat GPT](https://chat.openai.com/auth/login)

[Ordinarycoders.com - Bootstrap Footers](https://ordinarycoders.com/blog/article/bootstrap-footers)

[Forum djangoproject.com - URL not found](https://forum.djangoproject.com/t/url-not-found/4588/3)

[Stack Overflow - Context Processors to show categories](https://stackoverflow.com/questions/72977293/how-to-show-list-of-categories-in-navbar-using-django-framework)

[Real Python - Category View](https://realpython.com/build-a-blog-from-scratch-django/)

[Docs - djangoproject.com - Using success messages](https://docs.djangoproject.com/en/3.2/ref/contrib/messages/#using-messages-in-views-and-templates)

[legionscript.medium.com - Add, edit and delete posts and comments](https://legionscript.medium.com/building-a-social-media-site-with-python-and-django-part-4-edit-delete-posts-add-comments-8e6ca1ef0441)

[Django Testing for Beginners, Alice Campkin](https://alicecampkin.medium.com/django-testing-for-beginners-146bd285a178)

[learndjango.com - Django Testing Tutorial](https://learndjango.com/tutorials/django-testing-tutorial )

[medium.com - Class Based Views & CRUD](https://medium.com/jungletronics/a-django-blog-in-vs-code-3b6fc8eb19aa)

[finxter.com - Add Read Time to a Blog](https://blog.finxter.com/how-i-made-a-django-blog-audio-versions-of-my-blog-articles-auto-gen/)

[freecodecamp.org - CSS Shadow Effect](https://www.freecodecamp.org/news/how-to-create-beautiful-box-shadows-in-html-and-css/)

[studygyaan.com - Social Share Button](https://studygyaan.com/django/adding-a-social-share-button-to-your-django-website)

[Code Institute Template and Walkthrough Project - I think therefore I Blog](https://learn.codeinstitute.net/) - provided the project code for blog site extension and customisation.

__Media__

[Images](https://unsplash.com/)
- Hero Image 1 - Alberto Caliman on Unsplash
- Hero Image 2 - Cristina Gottardi on Unsplash
- Hero Image 3 - Andrea Cairone on Unsplash
- Default Featured Image -
- Image Blog Post 1 -
- Image Blog Post 2 -
- Image Blog Post 3 -
- Image Blog Post 4 -
- Image Blog Post 5 -
- Image Blog Post 6 -

### Acknowledgements

Mentor - Brian Macharia, for help, feedback and always spending that bit extra time to explain things to me. Thanks so much!

Support of Code Institute Team

[Code Institute Slack Portfolio Project 4](code-institute-room.slack.com)
