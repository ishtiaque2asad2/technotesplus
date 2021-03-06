from ..models import Note, Tag, SharedNote
from rest_framework import serializers


class BaseMixin:
    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and request.user:
            validated_data['created_by'] = request.user
            validated_data['updated_by'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if request and request.user:
            validated_data['updated_by'] = request.user
        return super().update(instance, validated_data)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name", "id"]


class NoteListRetrieveSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    owned_by = serializers.SerializerMethodField()
    tag_string = serializers.SerializerMethodField()

    def get_tag_string(self, obj):
        tag_string = ""
        for tag in obj.tags.all():
            tag_string = tag_string + tag.name + ","
        return tag_string[:-1]

    def get_owned_by(self, obj):
        return obj.created_by.first_name + " " + obj.created_by.last_name

    class Meta:
        model = Note
        fields = ["tags", "title", "note", "owned_by", "unique_id","tag_string"]


class NoteCreateUpdateSerializer(BaseMixin, serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Note
        fields = ["tags", "title", "note", "unique_id"]


class SharedNoteSerializer(serializers.ModelSerializer):
    note_title = serializers.SerializerMethodField()
    shared_with_name = serializers.SerializerMethodField()
    shared_by = serializers.SerializerMethodField()

    def get_shared_by(self,obj):
        return obj.created_by.first_name+" "+obj.created_by.last_name

    def get_shared_with_name(self,obj):
        return obj.shared_with.first_name+" "+obj.shared_with.last_name

    def get_note_title(self,obj):
        return obj.note.title
    class Meta:
        model = SharedNote
        fields = ['shared_with_name','unique_id','is_read','read_datetime',"note_title","shared_by"]

