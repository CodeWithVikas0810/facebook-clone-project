# Entity Relationship Diagram

## Description

The application consists of five main entities:

1. User
2. Post
3. Comment
4. Like
5. Follow

Relationships:

* A User can create multiple Posts.
* A User can create multiple Comments.
* A User can Like multiple Posts.
* A User can Follow multiple Users.
* A Post can have multiple Comments.
* A Post can have multiple Likes.
* A Comment can have child Comments (threaded replies).

## Mermaid ER Diagram

```mermaid
erDiagram

    USER ||--o{ POST : creates
    USER ||--o{ COMMENT : writes
    USER ||--o{ LIKE : gives

    USER ||--o{ FOLLOW : follower
    USER ||--o{ FOLLOW : following

    POST ||--o{ COMMENT : contains
    POST ||--o{ LIKE : receives

    COMMENT ||--o{ COMMENT : replies_to

    USER {
        int id
        string username
        string email
        string password
        datetime created_at
    }

    POST {
        int id
        int user_id
        text content
        datetime created_at
    }

    COMMENT {
        int id
        int user_id
        int post_id
        int parent_comment_id
        text content
        datetime created_at
    }

    LIKE {
        int id
        int user_id
        int post_id
        datetime created_at
    }

    FOLLOW {
        int id
        int follower_id
        int following_id
        datetime created_at
    }
```

## Future Enhancements

* User Profile
* Notifications
* Search Functionality
* Media Uploads
* Messaging System
* Elasticsearch Integration
* Celery-based Data Export
