# 🦁 Velog 클론 BE - 공통 세션용 레포

이 레포는 **멋쟁이사자처럼 동국대학교 13기** 여름학기 세션을 위한 백엔드 코드입니다.

프론트엔드 팀과 협업하여 **Velog 형태의 게시판 기능**을 간단히 구현합니다.  
Backend는 **Django + Django REST framework**를 사용하며, **Function-Based View(FBV)**로 구성되어 있습니다.

---

## 📌 주요 기능

| Method | URL                       | 설명               |
|--------|---------------------------|--------------------|
| GET    | `/api/posts/`            | 전체 post 리스트 조회 |
| GET    | `/api/posts/{post_id}/`  | 개별 post 조회     |
| POST   | `/api/posts/`            | 새 post 작성       |
| DELETE | `/api/posts/{post_id}/`  | post 삭제          |

---

## 📦 Request / Response 예시

### POST 요청 (새 글 작성)

```json
POST /api/posts/
{
  "title": "제목입니다",
  "context": "내용입니다"
}
