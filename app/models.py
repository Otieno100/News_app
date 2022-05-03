from urllib import response


class News :
 def __init__(self,title,description,urlToImage,publishedAt,url):
     self.title = title
     self.description = description 
     self.urlToImage =urlToImage
     self.publishedAt = publishedAt
     self.url = url


class Review:
    all_reviews = []

    def __init__(self,title,urlToImage,review, url):
        self.title = title
        self.urlToImage = urlToImage
        self.url = url
        self.review = review
        


    def  save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def get_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,title) :
        response = []
        for review in cls.all_reviews:
            if review.title == title:
                response.append(review)
                

        return response        


