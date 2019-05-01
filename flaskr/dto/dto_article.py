class DtoArticleInfo:
  
    ##id
    ##title
    ##author
    #release_date

    def __init__(self, title, author, content, date, id = None):
        self.title = title
        self.author = author #string
        self.content = content
        self.id = id
        self.date = date