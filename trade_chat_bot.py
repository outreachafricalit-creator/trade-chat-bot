import telebot
import logging
import os
from dotenv import load_dotenv
from trade_chat_brain import analyze_intent
from trade_chat_responses import get_response
from trade_chat_config import *

# Load environment
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

# Initialize bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('trade_chat.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# User tracking for context
user_context = {}

def get_user_context(user_id):
    """Get or create user context"""
    if user_id not in user_context:
        user_context[user_id] = {
            'last_topic': None,
            'message_count': 0,
            'keywords': []
        }
    return user_context[user_id]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Handle /start command"""
    user_id = message.from_user.id
    user_name = message.from_user.first_name or "Trader"
    
    logger.info(f"User {user_id} started the bot")
    
    welcome_text = f"""🚀 **WELCOME TO TRADE CHAT BOT** 🚀

Hey {user_name}! 👋

I'm your **professional trading assistant & mentor**. I'm here to help you master:

📊 **Technical Analysis** - Support, resistance, candlesticks, trends, breakouts
💰 **Risk Management** - Stop loss, position sizing, risk/reward ratios
🧠 **Trading Psychology** - Discipline, patience, emotional control
🌍 **Market Analysis** - Forex, Crypto, Bitcoin, market sessions
🎯 **Trading Strategies** - Scalping, swing, day trading & more

**I can answer ANY trading question**, and I'll respond like a real trader with experience.

Try asking me:
• "What is support and resistance?"
• "How do I manage risk?"
• "Explain candlestick patterns"
• "Is Bitcoin going up?"
• "How do I control emotions?"

**Let's start your trading journey!** 📈

Just ask me anything about trading... 🎯"""
    
    bot.reply_to(message, welcome_text, parse_mode='Markdown')

@bot.message_handler(commands=['help'])
def send_help(message):
    """Handle /help command"""
    help_text = """🆘 **HELP & GUIDANCE**

I can help you with:

📚 **LEARNING TOPICS:**
• Technical Analysis (TA, chart patterns, indicators)
• Risk Management (stop loss, position sizing, R:R)
• Trading Psychology (discipline, emotions, FOMO)
• Market Structure (support, resistance, trends)
• Trading Strategies (scalping, swing, day trading)
• Cryptocurrency & Forex
• Market News & Impact
• Common Mistakes & Recovery

💡 **HOW TO ASK:**
• Be specific: "What is a breakout?" works better than just "breakout"
• Ask follow-ups: I learn from your questions
• Be conversational: Talk naturally!

🎯 **AVAILABLE COMMANDS:**
/start - Welcome message
/help - This help message
/menu - Show menu options

**Pro Tip:** Just type any trading question and I'll respond intelligently! 🚀"""
    
    bot.reply_to(message, help_text, parse_mode='Markdown')

@bot.message_handler(commands=['menu'])
def send_menu(message):
    """Handle /menu command"""
    menu_text = """📋 **TRADING EDUCATION MENU**

Select a topic or ask me anything:

**📊 TECHNICAL ANALYSIS**
• Support & Resistance
• Breakouts & Fakeouts
• Candlestick Patterns
• Trends & Consolidation
• Chart Patterns

**💰 RISK MANAGEMENT**
• Stop Loss Placement
• Position Sizing
• Risk/Reward Ratios
• Capital Preservation
• Drawdown Management

**🧠 PSYCHOLOGY**
• Discipline & Patience
• Emotional Control
• FOMO & Revenge Trading
• Fear & Greed
• Confidence Building

**🌍 MARKET KNOWLEDGE**
• Forex Trading
• Cryptocurrency
• Bitcoin & Ethereum
• Market Sessions
• Volatility & News

**🎯 TRADING STRATEGIES**
• Scalping
• Swing Trading
• Day Trading
• Position Trading
• Support/Resistance Strategy

Just type your question or topic! 🎯"""
    
    bot.reply_to(message, menu_text, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """Handle all messages - Main response logic"""
    user_id = message.from_user.id
    user_text = message.text.strip()
    
    logger.info(f"User {user_id}: {user_text}")
    
    # Get user context
    context = get_user_context(user_id)
    context['message_count'] += 1
    
    # Analyze intent
    intent_data = analyze_intent(user_text)
    category = intent_data['category']
    confidence = intent_data['confidence']
    keywords = intent_data['keywords']
    
    # Update context
    context['last_topic'] = category
    context['keywords'] = keywords
    
    # Get response
    response = get_response(user_text, category, confidence, context)
    
    # Log the interaction
    logger.info(f"Category: {category}, Confidence: {confidence:.2f}")
    
    # Send response
    try:
        bot.reply_to(message, response, parse_mode='Markdown', disable_web_page_preview=True)
    except Exception as e:
        logger.error(f"Error sending message: {e}")
        fallback = "🤔 Let me think about that... It's related to trading though! Try asking more specifically. 📈"
        bot.reply_to(message, fallback)

def main():
    """Main function"""
    print("""
    ╔════════════════════════════════════════════════════════╗
    ║                                                        ║
    ║   🚀 TRADE CHAT BOT IS RUNNING... 🚀                 ║
    ║                                                        ║
    ║   ==================================================  ║
    ║   🤖 Trading Education Assistant Active              ║
    ║   📊 Ready to help with any trading questions         ║
    ║   ==================================================  ║
    ║                                                        ║
    ║   Press Ctrl+C to stop the bot                        ║
    ║                                                        ║
    ╚════════════════════════════════════════════════════════╝
    """)
    
    logger.info("Bot started successfully")
    
    try:
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        logger.error(f"Bot error: {e}")
    finally:
        logger.info("Bot stopped")

if __name__ == "__main__":
    main()