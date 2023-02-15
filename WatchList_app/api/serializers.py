from rest_framework import serializers

from ..models import WatchList, StreamPlatform, Review


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     desc = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movies.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.desc = validated_data.get('desc', instance.desc)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

# class MovieSerializer(serializers.ModelSerializer):
#     # len_name = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Movies
#         fields = "__all__"
#
#     # def get_len_name(self, object):
#     #     return len(object.name)
#
#     def validate(self, attrs):
#         if attrs['name'] == attrs['desc']:
#             raise serializers.ValidationError('Name and desc must not be same!')
#         return attrs
#
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Name is too short!')
#         else:
#             return value
class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ("watchlist",)
        # fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    # reviews = ReviewSerializer(many=True, read_only=True) # Remove review on watchlist
    platform = serializers.CharField(source='platform.name')

    class Meta:
        model = WatchList
        fields = "__all__"

    # def get_len_name(self, object):
    #     return len(object.name)

    # def validate(self, attrs):
    #     if attrs['name'] == attrs['desc']:
    #         raise serializers.ValidationError('Name and desc must not be same!')
    #     return attrs
    #
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name is too short!')
    #     else:
    #         return value


class StreamPlatformSerializer(serializers.ModelSerializer):  # HyperlinkedModelSerializer
    # len_name = serializers.SerializerMethodField()
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"
