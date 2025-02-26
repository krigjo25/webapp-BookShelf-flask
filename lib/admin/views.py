#   Admin interface view
from flask_admin.contrib.sqla import ModelView


class BooksView(ModelView):
    """
        *   Books view class
        *   Define the admin interface
    """
    column_list = ('bookID','title', 'author', 'year', 'genre', 'description', 'cover', 'rating', 'reviews')
    column_labels = dict(bookID='ID',title='Title', author='Author', year='Year', genre='Genre', description='Description', cover='Cover', rating='Rating', reviews='Reviews')
    column_filters = ('title', 'author', 'year', 'genre')