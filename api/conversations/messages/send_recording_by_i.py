from typing , Any, list, Optional
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-04-15"

async def send_new_message(
    conversation_id: str,
    message_type: str,
    contact_id: str,
    headers: dict[str, str],
    message: str | None,
    html: str | None,
    subject: str | None,
    appointment_id: str | None,
    attachments: list[str] | None = None,
    email_from: str | None,
    email_to: str | None,
    email_cc: list[str] | None = None,
    email_bcc: list[str] | None = None,
    email_reply_mode: str | None,
    reply_message_id: str | None,
    template_id: str | None,
    thread_id: str | None,
    scheduled_timestamp: int | None,
    conversation_provider_id: str | None,
    from_number: str | None,
    to_number: str | None
) -> dict[str, Any]:
    """
    Send a new message in a conversation.
    
    Args:
        conversation_id: ID of the conversation
        message_type: Type of message (SMS, Email, WhatsApp, IG, FB, Custom, Live_Chat)
        contact_id: ID of the contact receiving the message
        headers: Dictionary containing Authorization and Version headers
        message: Text content of the message
        html: HTML content of the message
        subject: Subject line for email messages
        appointment_id: ID of the associated appointment
        attachments: Array of attachment URLs
        email_from: Email address to send from
        email_to: Email address to send to
        email_cc: Array of CC email addresses
        email_bcc: Array of BCC email addresses
        email_reply_mode: Mode for email replies (reply, reply_all)
        reply_message_id: ID of message being replied to
        template_id: ID of message template
        thread_id: ID of message thread
        scheduled_timestamp: UTC Timestamp for scheduled messages
        conversation_provider_id: ID of conversation provider
        from_number: Phone number used as the sender
        to_number: Recipient phone number
        
    Returns:
        Dictionary containing the created message data
        
    Raises:
        Exception: If the API request fails or if required headers are missing
    """
    # Validate required headers
    if not headers.get("Authorization") or not headers["Authorization"].startswith("Bearer "):
        raise Exception("Missing or invalid Authorization header. Must be in format: 'Bearer {token}'")

    if not headers.get("Version"):
        # Set default version if not provided
        headers["Version"] = API_VERSION
    
    # Prepare request headers
    request_headers = {
        "Authorization": headers["Authorization"],
        "Version": headers["Version"],
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    # Prepare request payload
    payload = {
        "type": message_type,
        "contactId": contact_id 
    }
    
    # Add optional fields if provided
    if message:
        payload["message"] = message
    if html:
        payload["html"] = html
    if subject:
        payload["subject"] = subject
    if appointment_id:
        payload["appointmentId"] = appointment_id
    if attachments:
        payload["attachments"] = attachments
    if email_from:
        payload["emailFrom"] = email_from
    if email_to:
        payload["emailTo"] = email_to
    if email_cc:
        payload["emailCc"] = email_cc
    if email_bcc:
        payload["emailBcc"] = email_bcc
    if email_reply_mode:
        payload["emailReplyMode"] = email_reply_mode
    if reply_message_id:
        payload["replyMessageId"] = reply_message_id
    if template_id:
        payload["templateId"] = template_id
    if thread_id:
        payload["threadId"] = thread_id
    if scheduled_timestamp:
        payload["scheduledTimestamp"] = scheduled_timestamp
    if conversation_provider_id:
        payload["conversationProviderId"] = conversation_provider_id
    if from_number:
        payload["fromNumber"] = from_number
    if to_number:
        payload["toNumber"] = to_number
    
    logging.info(f"Sending new message in conversation: {conversation_id}")
    
    try:
        # Make the API request to send message
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(
                f"{API_BASE_URL}/conversations/messages",
                headers=request_headers,
                json=payload
            )
            
            # Check if request was successful
            response.raise_for_status()
            return response.json()
            
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred while sending message: {e}")
        raise Exception(f"Failed to send message: {e}")
    except Exception as e:
        logging.error(f"Error occurred while sending message: {e}")
        raise Exception(f"Failed to send message: {e}")