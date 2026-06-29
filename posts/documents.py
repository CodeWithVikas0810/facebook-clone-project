from django_elasticsearch_dsl import Document, Index, fields
from .models import Post

post_index = Index("posts")


@post_index.document
class PostDocument(Document):
    """Elastic search document for post"""

    username = fields.TextField(attr="user.username")
    content  = fields.SearchAsYouTypeField()

    class Django:
        """Every post should be a document"""

        model = Post
        fields = ["id", "created_at"]
