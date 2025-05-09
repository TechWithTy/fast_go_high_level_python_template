import httpx
from typing , Any, list, Optional

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def create_social_media_post(
    headers: dict[str, str],
    location_id: str,
    account_ids: list[str],
    summary: str,
    media: list[dict[str, Any]],
    status: str = "draft",
    schedule_date: str | None,
    created_by: str | None,
    follow_up_comment: str | None,
    og_tags_details:dict[str, str] | None,
    post_type: str = "post",
    post_approval_details: dict[str, Any] = None,
    schedule_time_updated: bool = False,
    tags: list[str] | None = None,
    category_id: str | None,
    tiktok_post_details: dict[str, Any] = None,
    gmb_post_details: dict[str, Any] = None,
    user_id: str | None
) -> dict[str, Any]:
    url = f"{API_BASE_URL}/social-media-posting/{location_id}/posts"

    if "Authorization" not in headers or not headers["Authorization"].startswith("Bearer "):
        raise ValueError("Missing or invalid Authorization header. Must be in format: 'Bearer {token}'")

    request_headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Version": headers.get("Version", API_VERSION),
        **headers
    }

    payload = {
        "accountIds": account_ids,
        "summary": summary,
        "media": media,
        "status": status,
        "type": post_type,
        "scheduleTimeUpdated": schedule_time_updated
    }

    if schedule_date:
        payload["scheduleDate"] = schedule_date
    if created_by:
        payload["createdBy"] = created_by
    if follow_up_comment:
        payload["followUpComment"] = follow_up_comment
    if og_tags_details:
        payload["ogTagsDetails"] = og_tags_details
    if post_approval_details:
        payload["postApprovalDetails"] = post_approval_details
    if tags:
        payload["tags"] = tags
    if category_id:
        payload["categoryId"] = category_id
    if tiktok_post_details:
        payload["tiktokPostDetails"] = tiktok_post_details
    if gmb_post_details:
        payload["gmbPostDetails"] = gmb_post_details
    if user_id:
        payload["userId"] = user_id

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=request_headers)

    response.raise_for_status()
    return response.json()