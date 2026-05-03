import os

# Environment
DEBUG = os.getenv("DEBUG", "False") == "True"

# Response settings
RESPONSE_VARIATION = True  # Use random responses
ENABLE_EMOJI = True        # Include emojis
MAX_RESPONSE_LENGTH = 4096  # Telegram limit

# Rate limiting
RATE_LIMIT_ENABLED = True
RATE_LIMIT_PER_MINUTE = 10

# Confidence thresholds
CONFIDENCE_HIGH = 0.8
CONFIDENCE_MEDIUM = 0.5
CONFIDENCE_LOW = 0.3

# Categories
MAIN_CATEGORIES = [
    "technical_analysis",
    "support_resistance",
    "breakouts_fakeouts",
    "candlesticks",
    "trends",
    "risk_stop_loss",
    "risk_position_sizing",
    "risk_reward_ratio",
    "psychology_discipline",
    "psychology_patience",
    "psychology_emotions",
    "psychology_loss",
    "psychology_success",
    "forex_basics",
    "crypto_basics",
    "beginner_advice",
    "advanced_strategies",
    "market_sessions",
    "volatility_news",
    "common_mistakes",
    "general",
]

# Logging
LOG_FILE = "trade_chat.log"
LOG_LEVEL = "INFO"

# Personality
BOT_PERSONALITY = {
    "style": "professional_mentor",
    "tone": "confident_friendly",
    "formality": "casual_knowledgeable",
}

# Response quality
MIN_RESPONSE_QUALITY = 0.6
USE_ADVANCED_NLP = True

# User tracking
TRACK_USERS = True
MAX_CONTEXT_MEMORY = 100