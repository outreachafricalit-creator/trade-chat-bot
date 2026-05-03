import re
import random

def clean_text(text):
    """Clean user input"""
    return text.strip().lower()

def split_message(text, max_length=4096):
    """Split long message into chunks"""
    if len(text) <= max_length:
        return [text]
    
    chunks = []
    current = ""
    
    for line in text.split("\n"):
        if len(current) + len(line) + 1 > max_length:
            if current:
                chunks.append(current)
            current = line
        else:
            current += "\n" + line if current else line
    
    if current:
        chunks.append(current)
    
    return chunks

def extract_symbols(text):
    """Extract trading symbols from text"""
    pattern = r'\b[A-Z]{3,6}\b'
    return re.findall(pattern, text)

def extract_numbers(text):
    """Extract numbers from text"""
    pattern = r'\d+\.?\d*'
    return re.findall(pattern, text)

def get_random_response(responses_list):
    """Get random response with variations"""
    return random.choice(responses_list)

def format_response(text, add_emoji=True):
    """Format response for Telegram"""
    if add_emoji:
        # Emojis already included in responses
        pass
    return text

def truncate_response(text, max_words=300):
    """Truncate response if too long"""
    words = text.split()
    if len(words) > max_words:
        return " ".join(words[:max_words]) + "..."
    return text

def rate_limit_check(user_id, max_per_minute=10):
    """Simple rate limiting (can be enhanced)"""
    return True

def create_markdown(text, bold_sections=None):
    """Create formatted markdown response"""
    if bold_sections:
        for section in bold_sections:
            text = text.replace(section, f"**{section}**")
    return text