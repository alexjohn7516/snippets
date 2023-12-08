from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# We can use a model serializer to make this implicit so we dont have to
# Type out all of this code

# * The explicit way of describing a serializer
# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={"base_template": "textarea.html"})
#     linenons = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default="python")
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default="friendly")

#     def create(self, validated_date):
#         """
#         Create and return a new 'Snippet' instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_date)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing 'Snippet' instance, given the validated data.
#         """
#         instance.title = validated_data.get("title", instance.title)
#         instance.code = validated_data.get("code", instance.code)
#         instance.linenos = validated_data.get("linenos", instance.linenos)
#         instance.language = validated_data.get("language", instance.language)
#         instance.style = validated_data.get("style", instance.style)
#         instance.save()
#         return instance


class SnippetSerializer(serializers.ModelSerializer):
    """
    * Implicit way of describing a serializer
    The serializer will pull in the model you are working with in the meta class
    You decide which columns it takes with the fields array
    #! has simple default methods for update and create
    """

    class Meta:
        model = Snippet
        fields = ["id", "title", "code", "linenons", "language", "style"]
