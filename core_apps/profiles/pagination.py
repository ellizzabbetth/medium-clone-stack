# there are two options to do this either a set up, a global pagination in the settings of file or set
# a pagination on a per model basis. We are going to use the latter where we are setting up pagination on a per model basis.

from rest_framework.pagination import PageNumberPagination


class ProfilePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 20