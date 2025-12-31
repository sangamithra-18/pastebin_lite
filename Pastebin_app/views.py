from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Pastebin_content
from .serializers import PasteCreateSerializer
from django.shortcuts import render

def home(request):
    pastes = Pastebin_content.objects.all()
    active_pastes = [p for p in pastes if not p.is_expired()]

    return render(request, "Home.html", {
        "pastes": active_pastes
    })

@api_view(['POST'])
def create_paste(request):
    
    serializer = PasteCreateSerializer(data=request.data)
 
    if serializer.is_valid():
        paste = serializer.save()
        return Response({
        "id": str(paste.id),
        "url": request.build_absolute_uri(f"/p/{paste.id}/")
       
       }, status=201)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_paste(request, paste_id):
    paste = get_object_or_404(Pastebin_content, id=paste_id)
 
    # Check if expired
    if paste.is_expired():
        return Response({"error": "Paste not available"}, status=status.HTTP_404_NOT_FOUND)
    
    # Increment view count
    paste.views_count += 1
    paste.save()

    return Response({
        "content": paste.content_paste,
        "remaining_views": None if paste.max_views is None else max(paste.max_views - paste.views_count, 0),
        "expires_at": paste.expires_at
    })


@api_view(['GET'])
def view_paste(request, paste_id):
    paste = get_object_or_404(Pastebin_content, id=paste_id)

    if paste.is_expired():
        return render(request, "404.html", status=404)

    # Increment view count
    paste.views_count += 1
    paste.save()

    return render(request, "paste_view.html", {"paste": paste})
