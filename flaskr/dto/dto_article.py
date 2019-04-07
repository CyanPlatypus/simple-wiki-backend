class DtoArticleInfo:
  
    ##id
    ##title
    ##author
    #release_date

    def __init__(self, title, author, content, id = None):
        self.title = title
        self.author = author #string
        self.content = content
        self.id = id
        #self.release_date = release_date