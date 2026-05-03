import re
from trade_chat_keywords import KEYWORDS_DATABASE

class TradeAnalysisEngine:
    """Advanced trading conversation engine"""
    
    def __init__(self):
        self.scenario_patterns = self._build_patterns()
    
    def _build_patterns(self):
        """Build regex patterns for scenarios"""
        return {
            "loss": r'\b(loss|lost|losing|down|dropped|went down)\b',
            "profit": r'\b(profit|win|winning|up|made|gained)\b',
            "entry": r'\b(enter|entry|buy|sell|long|short|position)\b',
            "exit": r'\b(exit|take profit|close|liquidate|stop out)\b',
            "risk": r'\b(risk|leverage|margin|drawdown|ruin)\b',
            "technical": r'\b(support|resistance|breakout|trend|pattern)\b',
        }
    
    def detect_scenario(self, user_text):
        """Detect user's trading scenario"""
        user_lower = user_text.lower()
        detected = {}
        
        for scenario, pattern in self.scenario_patterns.items():
            if re.search(pattern, user_lower):
                detected[scenario] = True
        
        return detected
    
    def generate_scenario_response(self, scenario, user_text):
        """Generate response based on detected scenario"""
        
        if scenario == "loss":
            return self._response_loss(user_text)
        elif scenario == "profit":
            return self._response_profit(user_text)
        elif scenario == "risk":
            return self._response_risk(user_text)
        else:
            return None
    
    def _response_loss(self, user_text):
        """Response for loss scenarios"""
        responses = [
            "Losses happen to EVERY trader, even pros. The key is learning. What happened? What will you do differently next time? 📊",
            "This is actually good - losses teach you more than wins! Review the trade calmly. Was it a bad setup or bad execution? 🔍",
            "Don't revenge trade! Take a break, analyze what went wrong, and come back with a clear head. 💭",
        ]
        import random
        return random.choice(responses)
    
    def _response_profit(self, user_text):
        """Response for profit scenarios"""
        responses = [
            "Awesome! Did you follow your plan? If yes, repeat that setup. Consistency beats luck! 🎯",
            "Great win! Now here's the tricky part: DON'T get overconfident. Stick to your risk management! 👑",
            "Profits are awesome, but compound them! Don't spend them - reinvest and let them grow! 💰",
        ]
        import random
        return random.choice(responses)
    
    def _response_risk(self, user_text):
        """Response for risk scenarios"""
        responses = [
            "Risk management is EVERYTHING. A bad trade with good risk > good trade with bad risk. Always manage risk first! 🛡️",
            "Leverage is a double-edged sword. It magnifies wins AND losses. Start small, learn, then grow! ⚖️",
            "Your biggest enemy isn't the market - it's your account blowing up. Protect capital above all else! 💪",
        ]
        import random
        return random.choice(responses)

# Create engine instance
engine = TradeAnalysisEngine()

def process_with_engine(user_text, category):
    """Process message with advanced engine"""
    scenarios = engine.detect_scenario(user_text)
    
    if scenarios:
        for scenario in scenarios:
            response = engine.generate_scenario_response(scenario, user_text)
            if response:
                return response
    
    return None