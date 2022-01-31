from django.db import models



 
    

class Button(models.Model):
    title = models.CharField(max_length=30)
    url_name = models.URLField()
    
    def __str__(self):
        return self.title
    

class Linktree(models.Model):
    name = models.CharField(max_length=30)
    button = models.ManyToManyField(Button,  related_name="button")

    
    def __str__(self):
        return self.name
    
    # @property
    # def linkbuttons(self):
    #     return self.LinkButtons_set.all()
    
    
    
    
    

    
    
    

    
    
# ##################################################################  URLS

# from django.urls import path


# urlpatterns = [
#     path("list/", Linktree.as_view(), name="list"),
#     path("create/", LinkButtonListCreateView.as_view(), name="Linktree_Button_Create")

# ]
