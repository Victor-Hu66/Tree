from rest_framework import serializers
from .models import Linktree, Button
                

class LinkbuttonsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Button
        fields = '__all__'
        

        
class LinktreeSerializer(serializers.ModelSerializer): 
    button = LinkbuttonsSerializer(many=True)

    class Meta:
        model = Linktree
        fields = ["name", "button"]


    def create(self, validated_data):
        print(validated_data) 
        linkbuttons_data = validated_data.pop('linkbuttons')
        # print(linkbuttons_data)
        linktree = Linktree.objects.create(**validated_data)
        
        for button in linkbuttons_data:
            linktree.button.add(Button.objects.create(**button))
        linktree.save()    
        
        return linktree
    
    