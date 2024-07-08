class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        raise AttributeError("Name is immutable")

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        return new_article
    
    def articles(self):
        return self._articles
    
    def magazines(self):
        return list(set(article.magazine for article in self._articles))
    
    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not 2 <= len(value) <= 16:
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        if len(value) == 0:
            raise ValueError("Category must have a length greater than 0")
        self._category = value
    
    def add_article(self, article):
        self._articles.append(article)
    
    def articles(self):
        return self._articles
    
    def contributors(self):
        return list(set(article.author for article in self._articles))


class Article:
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        magazine.add_article(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        raise AttributeError("Title is immutable")
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        self._magazine = value