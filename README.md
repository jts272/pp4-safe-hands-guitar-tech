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

~ GitHub projects: Kanban, timeboxes, labels, issue templates
~ Epics > Stories > Tasks (with acceptance criteria for definition of done)
~ 'should-have' <=60% of timebox

---

## Five stages of UX design

~

### Strategy (user needs, business objectives)

~ Appropriate, relevant, content type
~ Why a user would want this
~ Stakeholder > Competitors > User research (existing product audit)
~ B2C model

### Scope (functional spec and content requirements)

~ MVP, what's in and out
~ How agile helps
~ How sprints are structured
~ Realistic scope without creep
~ Content requirements
~ Functional requirements
~ How usage scenarios map to user stories

### Structure (interaction design, information design)

~ Organization/functionality of content and features
~ Navigation, information architecture (IA).
~ Interaction design (IXD); expectations, consistency (templates), no luck involved
~ User feedback on actions
~ 404 handling

### Skeleton (interface design, navigation design, information design)

~ Give form to function, UI
~ Wireframes
~ Correct structure of navigation. Tell the story with nav link order etc.
~ User authentication information
~ Blog expectations

### Surface

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
