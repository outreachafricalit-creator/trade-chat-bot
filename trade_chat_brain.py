import re
from trade_chat_keywords import KEYWORDS_DATABASE
from trade_chat_config import *

def analyze_intent(user_text):
    """
    Analyze user intent and extract category
    Returns dict with category, confidence, keywords
    """
    user_text_lower = user_text.lower()
    
    # Score each category
    category_scores = {}
    found_keywords = []
    
    for category, keywords in KEYWORDS_DATABASE.items():
        score = 0
        matched_keywords = []
        
        for keyword in keywords:
            if keyword.lower() in user_text_lower:
                score += 1
                matched_keywords.append(keyword)
        
        if score > 0:
            category_scores[category] = score
            found_keywords.extend(matched_keywords)
    
    # Determine best category
    if category_scores:
        best_category = max(category_scores, key=category_scores.get)
        max_score = category_scores[best_category]
        confidence = min(1.0, max_score / 3.0)  # Normalize confidence
    else:
        best_category = "general"
        confidence = 0.5
    
    # Handle specific patterns
    if re.search(r'\b(loss|lost|losing|down)\b', user_text_lower):
        best_category = "psychology_loss"
        confidence = 0.95
    
    if re.search(r'\b(profit|win|winning|up|green)\b', user_text_lower):
        best_category = "psychology_success"
        confidence = 0.95
    
    if re.search(r'\b(how|what|why|explain|teach|tell)\b', user_text_lower):
        confidence = min(1.0, confidence + 0.2)
    
    return {
        'category': best_category,
        'confidence': confidence,
        'keywords': found_keywords[:5],
        'original_text': user_text
    }

def detect_sentiment(user_text):
    """Detect sentiment (positive, negative, neutral)"""
    positive_words = ['good', 'great', 'profit', 'win', 'up', 'bullish', 'strong']
    negative_words = ['bad', 'loss', 'lose', 'down', 'bearish', 'weak', 'crash']
    
    user_lower = user_text.lower()
    
    pos_count = sum(1 for word in positive_words if word in user_lower)
    neg_count = sum(1 for word in negative_words if word in user_lower)
    
    if pos_count > neg_count:
        return "positive"
    elif neg_count > pos_count:
        return "negative"
    else:
        return "neutral"

def extract_entities(user_text):
    """Extract trading entities (symbols, numbers, etc.)"""
    entities = {
        'symbols': re.findall(r'\b[A-Z]{3,6}\b', user_text),
        'numbers': re.findall(r'\d+\.?\d*', user_text),
        'percentages': re.findall(r'(\d+\.?\d*)%', user_text)
    }
    return entities