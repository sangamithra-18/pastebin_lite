from rest_framework import serializers
from django.utils import timezone
from datetime import timedelta
from .models import Pastebin_content
from datetime import timedelta
from django.utils import timezone
from .expiry import EXPIRY_MAP




class PasteCreateSerializer(serializers.ModelSerializer):
    # ttl_seconds = serializers.IntegerField(required=False, min_value=1, write_only=True)

    class Meta:
        model = Pastebin_content
        fields = ["content_paste", "expiry", "category", "max_views"]

    def create(self, validated_data):
        expiry = validated_data.get("expiry", "never")
        config = EXPIRY_MAP.get(expiry, {})

        # Handle expiry time
        if "delta" in config:
            validated_data["expires_at"] = timezone.now() + config["delta"]

        # Burn after read
        if expiry == "burn":
            validated_data["max_views"] = 1

        return Pastebin_content.objects.create(**validated_data)
    
