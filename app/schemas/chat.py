from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict


class ChatRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=4000, description="Текст запроса пользователя")
    system: Optional[str] = Field(None, max_length=1000, description="Системная инструкция для модели")
    max_history: int = Field(default=10, ge=0, le=50, description="Количество сообщений истории для контекста")
    temperature: float = Field(default=0.7, ge=0.0, le=2.0, description="Креативность модели (0.0-2.0)")


class ChatResponse(BaseModel):
    answer: str = Field(..., description="Текст ответа от LLM")


class ChatMessagePublic(BaseModel):
    id: int
    role: str
    content: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class ChatHistoryResponse(BaseModel):
    items: List[ChatMessagePublic]