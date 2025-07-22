from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')  # 목록에서 보여줄 필드
    list_display_links = ('title',)               # 클릭 가능한 필드
    search_fields = ('title', 'context')          # 검색 가능 필드
    list_filter = ('created_at',)                 # 필터 사이드바
    ordering = ('-created_at',)                   # 최신순 정렬