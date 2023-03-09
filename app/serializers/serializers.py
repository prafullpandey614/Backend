from rest_framework import serializers
from app.models import Question,Answer
class AddQuestionSerializer(serializers.ModelSerializer):
    img_desc = serializers.ImageField(required=False)
    
    class Meta:
        model = Question
        fields = "__all__"
        read_only_fields = ['id', 'asked_by', 'upvotes', 'downvotes', 'best_answer_found', 'reports']
    
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['asked_by'] = user
        return super().create(validated_data)

class AddAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
        read_only_fields = ['id','author','upvotes','downvotes','reports']
    # def create(self, validated_data):
    #     author = self.context['request'].user
    #     validated_data['author'] = author
    #     return super().create(validated_data)
    