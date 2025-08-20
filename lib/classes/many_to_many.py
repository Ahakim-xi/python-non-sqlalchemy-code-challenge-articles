class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be an instance of Magazine")
        if not isinstance (title, str):
            raise TypeError("title must be a string")
        if not(5 <= len(title) <= 50):
            raise ValueError("title must be between 5 and 50 characters long")
        
        self._title = title
        self._author = author
        self._magazine = magazine
        

        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    
    @property 
    def author(self):
        return self._author
    
    @property
    def magazine(self):
        return self._magazine
    

class Author:
    def __init__(self, name):
        if not isinstance(name,str):
            raise TypeError("name must be a string")
        if len(name) == 0:
            raise ValueError("name cannot be empty")
        self._name = name

    @property
    def name(self):
        return self._name
    
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
         return None
        return list({article.magazine.category for article in self.articles()})

class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self.__name
    

    @name.setter
    def name(self, magazine_name):
        if not isinstance(magazine_name, str):
            raise TypeError("Name must be a string")
        if not (2 <= len(magazine_name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters long")
        self.__name = magazine_name

    @property
    def category(self):
        return self.__category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("category must be a string")
        if len(value) == 0:
            raise ValueError("category cannot be empty")
        self.__category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
      titles = [article.title for article in self.articles()]
      return titles if titles else None
    
    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1

        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None
#create authors
author1 = Author("Mark Twain")
author2 = Author("Jane Chebet")

 #create magazines
magazine1 = Magazine("Literary Digest", "Literature")
magazine2 = Magazine("Science Monthly", "Science")


#articles
article1 = author1.add_article(magazine1, "The Adventures of Tom Sawyer")
article2 = author2.add_article(magazine1, "Pride and Prejudice")
article3 = author1.add_article(magazine2, "A Connecticut Yankee in King Arthur's Court")
article4 = author2.add_article(magazine2, "Future Visions of Science")

# Print all articles
print("All articles:", [a.title for a in Article.all])
print("Articles in Literary Digest:", magazine1.article_titles())
print("Contributors to Literary Digest:", [a.name for a in magazine1.contributors()])
print("Mark Twain's magazines:", [m.name for m in author1.magazines()])
print("Mark Twain's topic areas:", author1.topic_areas())


    
    