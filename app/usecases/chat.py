
from app.repositories.chat_messages import ChatMessageRepository
from app.services.openrouter_client import OpenRouterClient
from app.schemas.chat import ChatRequest, ChatHistoryResponse, ChatMessagePublic


class ChatUseCase:
    def __init__(
        self,
        message_repo: ChatMessageRepository,
        openrouter_client: OpenRouterClient
    ):
        self.message_repo = message_repo
        self.openrouter_client = openrouter_client
    
    async def ask(
        self,
        user_id: int,
        request: ChatRequest
    ) -> str:
        messages = []
        
        if request.system:
            messages.append({
                "role": "system",
                "content": request.system
            })
        
        history = await self.message_repo.get_user_history(
            user_id=user_id,
            limit=request.max_history
        )
        
        for msg in history:
            messages.append({
                "role": msg.role,
                "content": msg.content
            })
        
        messages.append({
            "role": "user",
            "content": request.prompt
        })
        
        await self.message_repo.add_message(
            user_id=user_id,
            role="user",
            content=request.prompt
        )
        
        answer = await self.openrouter_client.chat_completion(
            messages=messages,
            temperature=request.temperature
        )
        
        await self.message_repo.add_message(
            user_id=user_id,
            role="assistant",
            content=answer
        )
        
        return answer
    
    async def get_history(self, user_id: int, limit: int = 50) -> ChatHistoryResponse:
        messages = await self.message_repo.get_user_history(
            user_id=user_id,
            limit=limit
        )
        
        items = [ChatMessagePublic.model_validate(msg) for msg in messages]
        
        return ChatHistoryResponse(items=items)
    
    async def clear_history(self, user_id: int) -> None:
        await self.message_repo.delete_user_history(user_id=user_id)