# Safe Hands Guitar Tech Website

![Am I responsive mockup](docs/images/site-mockup.png)

[Click here to view the deployed site!](https://pp4-safe-hands-guitar-tech.herokuapp.com/)

<details>
  <summary>Click to reveal QR code for easy mobile access!</summary>
  <img src="docs/images/qr-code-mobile-link.png" alt="QR code link to deployed site">
</details>

## Introduction

Welcome to the documentation for Safe Hands Guitar Tech! Here we will take an
in-depth look at the process undertaken to deliver the project, from inception
to deployment.

The project is a database-backed Model-View-Template (MVT) full-stack application,
powered by the Django framework. This is similar to the [MVC](https://developer.mozilla.org/en-US/docs/Glossary/MVC)
design pattern. The excellent [MDN Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction)
outlines the Django MVT pattern as follows:

![Django MVT application diagram](docs/images/basic-django.png)

This application allows for Create, Read, Update and Delete (CRUD) functions. At
the heart of this is the Model, or representation of the database tables. Django
interacts with the database by way of an [Object Relational Mapping (ORM),](<https://www.freecodecamp.org/news/what-is-an-orm-the-meaning-of-object-relational-mapping-database-tools/#:~:text=Object%20Relational%20Mapping%20(ORM)%20is,(OOP)%20to%20relational%20databases.>) that connects Django's Python code to the
relational database used for storing the site's back-end data.

We will examine in-depth how the Models for the site were constructed. In short,
Python code is used to create custom objects, which Django converts to [Structured Query Language (SQL)](<https://aws.amazon.com/what-is/sql/#:~:text=Structured%20query%20language%20(SQL)%20is,relationships%20between%20the%20data%20values.>)
commands that the configured relational database uses to construct its tables.

## Agile methodologies

[Agile methodologies](https://www.atlassian.com/agile) were used across the full
development cycle. This is a project management approach that breaks the project
down into phases, with well-defined, weighted tasks to complete in the given
period. It emphasizes continuous improvement through a refining process and has
the flexibility to welcome change if it meets the goals of the project.

Practice of agile methodologies has been evidenced using GitHub's built-in tools.
Namely, the Issues, Milestones and Projects systems. The level of decomposition
for agile items, from biggest to smallest are:

1. Epics - An overarching collection of stories to implement a feature, or collection of features
2. User stories - Stories told from the perspective of a certain user of the site. What do they want and why?
3. Tasks - The actual work that must be undertaken to fulfill the user story
4. Acceptance criteria - An objective metric to assess the completion of a user story

Here is the breakdown of the tools available on GitHub to present each agile
component.

- [Issues](https://github.com/jts272/pp4-safe-hands-guitar-tech/issues) is where
  each individual agile item is created, often using an issue template. First, an
  Epic is defined which states a big feature of the project too large to be broken
  down. Stories are then created from different perspectives that clarify what
  users actually want. Each story is given a set of tasks to be done to make the
  story happen, and acceptance criteria to test their validity.

- [Milestones](https://github.com/jts272/pp4-safe-hands-guitar-tech/milestones)
  are used as collections of agile items. For example, milestones are created for
  each iteration, which is a timeboxed period where certain stories are planned to
  be completed. As a best-practice, timeboxes do not contain more than 60% of their
  items as 'should have' on the [MoSCoW priority level system.](https://en.wikipedia.org/wiki/MoSCoW_method)
  Milestones are also used to hold [Product Backlog Items (PBIs),](https://github.com/jts272/pp4-safe-hands-guitar-tech/milestone/1)
  which is where items are stored before being passed to a given iteration.

- [Projects](https://github.com/jts272/pp4-safe-hands-guitar-tech/projects?query=is%3Aopen)
  are utilized as information radiators for an instant view on an iteration's progress.
  These are best viewed in Board view with the Label field enabled. Here is the
  board for the [first iteration](https://github.com/users/jts272/projects/7/views/1?layout=board&visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%5D)
  as an example. This follows the kanban style whereby an item is brought in as
  a Todo item. It then moves to In Progress when it is being worked on, then
  finally Done once all tasks and acceptance criteria have been met.

Below is an example index card for an item found on the project board:

![Index card example](docs/images/index-card-example.png)

We see that it is a designated story with a title. Each story is linked to an
Epic. This example shows a user story from the perspective of the site admin -
what they want to do and how it will benefit them. We then see the tasks that
must be completed to bring this story to fruition. The acceptance criteria are
tests that must pass to meet the definition of done.

In the right-hand panel, labels are visible for the MoSCoW priority level and
a story point (SP) estimation. These are estimates of effort, assigned using a
[modified Fibonacci](https://www.mountaingoatsoftware.com/blog/why-the-fibonacci-sequence-works-well-for-estimating) weighting scale.
The milestone or timebox the issue belongs to is shown, as well as its status.

Note that Done items are moved by GitHub to the [closed](https://github.com/jts272/pp4-safe-hands-guitar-tech/issues?q=is%3Aissue+is%3Aclosed)
category. This is the same for completed [iterations](https://github.com/jts272/pp4-safe-hands-guitar-tech/milestones?state=closed)

Agile practices help both the developers and product owners. The goals are always
visible, along with the tasks required to achieve them. By using these tools, the
needs of the users are always put first, which guides development to its essential
target. I invite you to explore each milestone to see what was achieved.

---

## Five stages of UX design

The five stages of user experience (UX) design is the pattern that was employed
to bring this project's vision to life. Starting with high-level business needs,
it drills down to the specifics of the what, why and how of each required element
found in the final product

### 1. Strategy

This project is built from the perspective of a small business owner who wants a
website to attract customers to his [Guitar Tech](https://en.wikipedia.org/wiki/Guitar_tech)
business. The owner will also function as the site's admin for CRUD functions
relating to blog posts, services and setup jobs. The site operates on B2C model,
whereby the product owner advertises his services to private customers.

To meet its business needs, the site needs to display certain information.
Visitors would expect to instantly get an impression of what the site is about
on first glance, with intuitive navigation. Service prices need to be easy to
find. Furthermore, the site content needs to be engaging enough to retain viewership
and help to grow the business.

As the key stakeholder, I conducted an existing product audit on the following sites:

- [Northwest Guitars](https://northwestguitajackrs.co.uk/)
- [Jim's Guitar Workshop](https://jimsguitarworkshop.co.uk/)
- [Fraser Callum](https://fcstrings.com/)

This informed me of scope expectations, which are explored in the next stage of
design.

### 2. Scope

The first objective of scope is to work out the [Minimum Viable Product (MVP)](https://www.productplan.com/glossary/minimum-viable-product/) so that there is a clear set of goals to bring a working
product to market. This is intertwined with the agile methodologies outlined
previously, which adds varying perspectives to the needs of the project.

A blog was to be included from the beginning. This helps to build trust and
engagement for users. They can see that the owner knows their trade and maps
common guitar-related scenarios to jobs he can help with. Users can engage in
the conversation with comments and likes. For this, relevant content must be
produced for site visitors.

Naturally, the services on offer must be detailed, with prices included. This
feature was designed to be easily updated by the owner in the event that prices,
service details or even available services changes.

The [Unique Selling Point (USP)](https://en.wikipedia.org/wiki/Unique_selling_proposition)
of this application is the setups section. Here, the owner can proudly display
their work on past customers' instruments, with a detailed specification breakdown.
This offers a unique value proposition as an app within the project, which requires
a highly customized data model.

A testimonials section for registered customers had been considered early on,
similar to that of [Fraser Callum's.](https://fcstrings.com/testimonials/)
However, I had decided to focus on the blog, service information and the unique
setup feature as I believed these features would have the biggest impact.

As a final functional requirement, there must be a way for customers to contact
the owner to book in their service. This is achieved through the contact buttons
at the footer of every page. An email contact form had been considered, although
on inspection, it would have required setup in Django beyond the scope of the
three iterations allotted to this project.

By examining the [Project Boards](https://github.com/jts272/pp4-safe-hands-guitar-tech/projects?query=is%3Aopen)
and [Milestones,](https://github.com/jts272/pp4-safe-hands-guitar-tech/milestones?state=closed)
a clear link between project scope and deliverable items is seen. As an example,
the first iteration was geared towards achieving MVP blog functionality. The
second focussed on customer/business features. Agile keeps scope creep at bay,
with a clear focus on the essentials. The end result of this approach is a product
that meets the needs of the business, whilst being concise enough for visitors
to navigate fluently.

### 3. Structure

Structure concerns organization of site functions. This is represented in the
concept of [Information Architecture (IA).](https://www.usability.gov/what-and-why/information-architecture.html)
This translates to providing the user with key information where they are, what
they can do and what to expect. This is encapsulated by the implementation of
strong [Interaction Design (IXD),](<https://www.interaction-design.org/literature/topics/interaction-design#:~:text=Interaction%20Design%20(IxD)%20is%20the,output%20to%20suit%20precise%20demands.>)
whereby features are implemented with consideration for _how_ they will be used.

Key components of IXD employed are intuitive navigation, that never requires
guesswork from the user. Feedback is delivered on all actions, from form validation
to success messages.

User's expectations are met whilst browsing through the use of templates. In other
words, elements like navigation and footers stay consistent across pages, with
relevant page content in the middle. A common pattern Django is great for is that
of list-view to detail-view. Put simply, a user finds a list of records on a
given topic, which they can click to access a more detailed view of that record.
This pattern is utilized to great effect in the blog and setups sections.

In keeping with intuitive navigation, errors are handled gracefully, whether client
or server-side. Examples include 404 error handling or presence testing a model
for content and reacting accordingly. Both examples are explored in their relevant
features section.

### 4. Skeleton

In the skeleton phase, we give form to function by way of the User Interface (UI).

Navigation is the first concern when a user visits the site. The brand name is
the first feature, which follows convention by serving as a link home. Then follows
the sections for blog, services and setups.

This tells a story in that the user reads a blog post that catches their interest.
From there they decide to check out the service prices. Then they can check records
of past services from satisfied customers.

On the far side of the navbar is authentication information. A first-time user
can clearly see that account registration is a feature - the gateway to interaction
with the site's content.

From the moment the visitor first lands on the page, they instantly gain an impression
of what the site is about. A familiar image of a Fender Stratocaster greets them.
A bullet-pointed list shows key jobs that are undertaken by the business owner.

An accordion invites user interaction - do they identify with one of the use-cases
and could they benefit from the services on offer? This is followed by a brief
text summary of the key points to visit on the site and why the visitor might
want to go there. Finally an invitation is made to get in contact using the
social call-to-action (CTA) buttons.

The following section highlights the five most recent blog posts, with counters
for likes and comments. This lets users know there is room for interaction. A
brief excerpt is show to capture their attention for reading the specific blog
post in full.

The following wireframe mock ups were constructed to visualize how this information
may appear on the screen. One of the design philosophies implemented was that of
[Mobile First,](https://www.browserstack.com/guide/how-to-implement-mobile-first-design)
which considers the smaller screen before the larger one. In this approach, the
elements are displayed in such a way that mobile users do not have to compromise
on content. From there, the elements can be positioned in such a way that they
can take advantage of ever-increasing screen sizes.

The mockups here target a desktop view, as this presents the information in a more
straightforward way. In the mobile view, elements stack vertically with no loss
of information.

<details>
  <summary>Homepage</summary>
  <img src="docs/images/wireframes/wf-home.png" alt="Homepage mock up">
</details>

<details>
  <summary>Services</summary>
  <img src="docs/images/wireframes/wf-services.png" alt="Services mock up">
</details>

<details>
  <summary>List view for Blog and Setups</summary>
  <img src="docs/images/wireframes/wf-blog-and-setup-list.png" alt="Blog and Setups list view mock up">
</details>

<details>
  <summary>Blog detail</summary>
  <img src="docs/images/wireframes/wf-blog-detail.png" alt="Blog detail mock up">
</details>

<details>
  <summary>Setups detail</summary>
  <img src="docs/images/wireframes/wf-setup-detail.png" alt="Setups detail mock up">
</details>

Wireframe images were produced with [draw.io desktop](https://github.com/jgraph/drawio-desktop/releases/)

### 5. Surface

~ Practical elements
~ Colour
~ Typography
~ Imagery
~ Blog content
~ Customer-related content
~ Responsive design
~ Overall value proposition presented

---

## Features

~

### Navigation

~ Responsive navbar

### Footer

~ Business information

### Blog

~ Comments, likes

### Service information

~ Pricing (database backed)

### Testimonials

~ Data model

### Guitar job spec database (admin panel)

~

---

## Authentication

~ Role-based login; content restriction
~ Login state shown

### Levels

~ Admin
~ User

### Abilities

~ Admin panel; creating blog posts
~ Commenting, liking

---

## Data modelling

~ How Django models create database structure (OOP)
~ Interaction between tables
~ Database configuration

![Initial schema]
![Production schema]

### Blog model

~

### Testimonials model

~

### Guitar spec model

~

---

## Testing

~ Automated and manual as appropriate
~ Coverage
~ Images of test file ran

### Python testing

~

### JavaScript testing

~

### UX/story testing

~ How this relates to acceptance criteria (stories must pass before being completed)

---

## Validation

~

### HTML validation

~

### CSS validation

~

### JavaScript validation

~

### Python validation

~

### WAVE accessibility validation

~

### Lighthouse reports

---

## Version control

~ Git best practices
~ Clean code

## Deployment

~ All steps and services to register
~ Procfile, requirements.txt

## Cloning and Forking

~ Cloning
~ Forking

## Technologies used

~ Hardware: Screens, devices
~ Software: linters, extensions, WSL2

## Additional credits

~

## Closing words

~
