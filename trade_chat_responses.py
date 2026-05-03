import random
from trade_chat_data import RESPONSE_DATABASE, RESPONSE_ADDITIONS
from trade_chat_config import *

def get_response(user_text, category, confidence, context):
    """
    Generate response based on category and confidence
    """
    
    # Select response from category
    if category in RESPONSE_DATABASE:
        responses = RESPONSE_DATABASE[category]
    else:
        responses = RESPONSE_DATABASE.get("general", ["Let's talk trading! 🎯"])
    
    # Get random response for variation
    response = random.choice(responses)
    
    # Add encouragement if confidence is high
    if confidence > 0.85 and random.random() < 0.6:
        response += "\n\n" + random.choice(RESPONSE_ADDITIONS["encouragement"])
    
    # Add warning if needed
    if any(word in user_text.lower() for word in ["risk", "loss", "leverage", "margin"]):
        if random.random() < 0.5:
            response += "\n\n" + random.choice(RESPONSE_ADDITIONS["warnings"])
    
    return response

def get_advanced_response(user_text, category, context):
    """
    Generate more sophisticated response using multiple factors
    """
    user_lower = user_text.lower()
    
    # Detect special cases
    if "bitcoin" in user_lower or "btc" in user_lower:
        category = "crypto"
    elif "eur" in user_lower or "gbp" in user_lower or "jpy" in user_lower:
        category = "forex"
    
    # Get base response
    base_response = get_response(user_text, category, 0.9, context)
    
    # Add pro tips
    if random.random() < 0.4:
        pro_tips = [
            "\n\n💡 **Pro Tip:** Write this down - you'll reference it often!",
            "\n\n🎯 **Pro Tip:** Most traders miss this, but not you!",
            "\n\n📊 **Pro Tip:** This is what separates pros from losing traders!",
        ]
        base_response += random.choice(pro_tips)
    
    return base_response

def generate_contextual_response(user_text, category, context):
    """
    Generate response based on user context/history
    """
    message_count = context.get('message_count', 0)
    last_topic = context.get('last_topic', None)
    
    # Personalization based on message count
    if message_count > 20:
        prefix = "Alright, I can tell you're getting serious! 💪 "
    elif message_count > 10:
        prefix = "You're asking all the right questions! 🎯 "
    else:
        prefix = ""
    
    # Get base response
    base_response = get_response(user_text, category, 0.85, context)
    
    # Add prefix
    if prefix:
        base_response = prefix + base_response
    
    return base_response

def create_teaching_response(user_text, category):
    """
    Create detailed teaching response
    """
    response = get_response(user_text, category, 0.9, {})
    
    # Add structure for clarity
    structured = f"""
{response}

**Key Points to Remember:**
• This is fundamental to becoming profitable
• Practice this concept in your next trades
• Track results to validate understanding

Keep learning! 📚
"""
    
    return structured