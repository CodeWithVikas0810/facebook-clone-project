# Facebook Clone - Project Overview

## Project Description

Facebook Clone is a social networking application built using Django. The project focuses on implementing the core functionality of a modern social platform, including authentication, posts, comments, likes, and user following.

The goal is to understand database relationships, Django ORM, authentication, CRUD operations, and scalable application architecture.

---

# Technology Stack 

## Backend

* Python
* Django
* Django ORM

## Database

* PostgreSQL  

## Frontend

* HTML5
* Tailwind CSS
* Django Templates
* JavaScript

## Deployment

* Render

## Version Control

* Git
* GitLab

---

# Core Features

## Authentication

* User Registration
* User Login
* User Logout
* Session Management
* Route Protection

## Social Features

* Create Posts
* View Feed
* Like Posts
* Comment on Posts
* Reply to Comments
* Follow Users
* View User Profiles

---

# Database Design

## User

Stores authentication and account information.

### Fields

* id
* username
* email
* password
* created_at

---

## Post

Stores content created by users.

### Fields

* id
* user_id
* content
* created_at

### Relationship

* One User can create many Posts.

---

## Comment

Stores comments and threaded replies.

### Fields

* id
* user_id
* post_id
* parent_comment_id
* content
* created_at

### Relationships

* One User can create many Comments.
* One Post can have many Comments.
* One Comment can have many child Comments.

---

## Like

Stores user likes on posts.

### Fields

* id
* user_id
* post_id
* created_at

### Relationships

* One User can like many Posts.
* One Post can receive many Likes.

### Constraints

* Unique (user_id, post_id)

---

## Follow

Stores user follow relationships.

### Fields

* id
* follower_id
* following_id
* created_at

### Relationships

* One User can follow many Users.
* One User can be followed by many Users.

### Constraints

* Unique (follower_id, following_id)

---

# Planned Features

## User Profile

* Bio
* Profile Picture
* Profile Editing

## Notifications

* Like Notifications
* Comment Notifications
* Follow Notifications

## Search

* Search Users
* Search Posts

## Media Uploads

* Image Uploads
* Media Storage

## Messaging

* Direct Messages
* Chat Threads

---

# Learning Objectives

This project is designed to practice:

* Django Authentication
* Django ORM
* Database Modeling
* Foreign Keys
* Self Referencing Relationships
* CRUD Operations
* Template Inheritance
* Static and Media Files
* PostgreSQL Integration

---

# Future Improvements

* Real-time chat
* Infinite scrolling
* REST API
* Docker support
* CI/CD
* Cloud storage for media
* Redis caching
