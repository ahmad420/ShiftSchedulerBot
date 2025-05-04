"""
Translation support for multiple languages.
"""
from enum import Enum
from typing import Dict


class Language(Enum):
    """Supported languages."""
    ENGLISH = "en"
    ARABIC = "ar"
    HEBREW = "he"


# Translations for each language
TRANSLATIONS = {
    Language.ENGLISH: {
        # Main menu
        "my_shifts": "📋 My Shifts",
        "shift_schedule": "📅 Shift Schedule",
        "request_swap": "🔄 Request Swap",
        "create_shift": "➕ Create Shift",
        "manage_users": "👥 Manage Users",
        
        # Shift types
        "morning": "Morning",
        "evening": "Evening",
        "night": "Night",
        
        # Messages
        "welcome": "Hello {name}! I am the Shift Scheduler Bot.\nUse /help to see available commands.",
        "no_shifts": "No shifts assigned to you.",
        "no_schedule": "No shift schedule available.",
        "swap_request": "To request a shift swap, please select the shift you want to swap.\nUse /myshift to view your shifts.",
        "error": "Sorry, an error occurred while processing your request. Please try again later.",
        
        # Help text
        "help_text": """
Available commands:
/start - Start the bot
/help - Show this message
/myshift - Show my shifts
/schedule - Show shift schedule
/swap - Request shift swap

Supervisor commands:
/create_shift - Create new shift
/assign_shift - Assign shift to user
/approve_swap - Approve swap request
/manage_users - Manage users
"""
    },
    
    Language.ARABIC: {
        # Main menu
        "my_shifts": "📋 وردياتي",
        "shift_schedule": "📅 جدول الورديات",
        "request_swap": "🔄 طلب تبديل وردية",
        "create_shift": "➕ إنشاء وردية",
        "manage_users": "👥 إدارة المستخدمين",
        
        # Shift types
        "morning": "صباحي",
        "evening": "مسائي",
        "night": "ليلي",
        
        # Messages
        "welcome": "مرحباً {name}! أنا بوت جدولة الورديات.\nاستخدم /help لمعرفة الأوامر المتاحة.",
        "no_shifts": "لا توجد ورديات مسجلة لك.",
        "no_schedule": "لا يوجد جدول ورديات متاح.",
        "swap_request": "لطلب تبديل وردية، يرجى تحديد الوردية التي تريد تبديلها.\nاستخدم الأمر /myshift لرؤية وردياتك.",
        "error": "عذراً، حدث خطأ أثناء معالجة طلبك. يرجى المحاولة مرة أخرى لاحقاً.",
        
        # Help text
        "help_text": """
الأوامر المتاحة:
/start - بدء البوت
/help - عرض هذه الرسالة
/myshift - عرض وردياتي
/schedule - عرض جدول الورديات
/swap - طلب تبديل وردية

أوامر المشرفين:
/create_shift - إنشاء وردية جديدة
/assign_shift - تعيين وردية لمستخدم
/approve_swap - الموافقة على طلب تبديل
/manage_users - إدارة المستخدمين
"""
    },
    
    Language.HEBREW: {
        # Main menu
        "my_shifts": "📋 המשמרות שלי",
        "shift_schedule": "📅 לוח משמרות",
        "request_swap": "🔄 בקשה להחלפת משמרת",
        "create_shift": "➕ יצירת משמרת",
        "manage_users": "👥 ניהול משתמשים",
        
        # Shift types
        "morning": "בוקר",
        "evening": "ערב",
        "night": "לילה",
        
        # Messages
        "welcome": "שלום {name}! אני בוט לוח המשמרות.\nהשתמש ב-/help כדי לראות את הפקודות הזמינות.",
        "no_shifts": "אין משמרות מוקצות לך.",
        "no_schedule": "אין לוח משמרות זמין.",
        "swap_request": "כדי לבקש החלפת משמרת, אנא בחר את המשמרת שברצונך להחליף.\nהשתמש ב-/myshift כדי לראות את המשמרות שלך.",
        "error": "מצטער, אירעה שגיאה בעיבוד הבקשה שלך. אנא נסה שוב מאוחר יותר.",
        
        # Help text
        "help_text": """
פקודות זמינות:
/start - התחל את הבוט
/help - הצג הודעה זו
/myshift - הצג את המשמרות שלי
/schedule - הצג לוח משמרות
/swap - בקש החלפת משמרת

פקודות מנהל:
/create_shift - צור משמרת חדשה
/assign_shift - הקצה משמרת למשתמש
/approve_swap - אשר בקשת החלפה
/manage_users - נהל משתמשים
"""
    }
}


def get_translation(key: str, language: Language, **kwargs) -> str:
    """
    Get translation for a given key in the specified language.
    """
    translation = TRANSLATIONS[language].get(key, key)
    return translation.format(**kwargs) if kwargs else translation 