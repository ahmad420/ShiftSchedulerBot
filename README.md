# Shift Scheduler Bot

A Telegram bot for managing and scheduling weekly shifts for IT teams. The bot supports multiple languages (English, Arabic, and Hebrew) and provides role-based access control.

## Features

### User Roles
- **Admin**
  - Full system access
  - Can manage all users and their roles
  - Can override any shift assignments
  - Access to all reports and analytics
  - Can configure system settings

- **Department Manager**
  - Can view and manage shifts for their department
  - Can approve shift swap requests
  - Can assign shifts to employees
  - Access to department-specific reports
  - Can manage employees in their department

- **Shift Manager**
  - Can create and modify shift schedules
  - Can approve shift swap requests
  - Can assign shifts to employees
  - Access to shift-related reports
  - Cannot modify user roles

- **Employee**
  - Can view their own shifts
  - Can request shift swaps
  - Can view department schedule
  - Can set preferences
  - Can request time off

### Commands
- `/start` - Start the bot and set language preference
- `/help` - Show available commands
- `/myshift` - Show user's shifts
- `/schedule` - Show shift schedule
- `/swap` - Request shift swap
- `/create_shift` - Create new shift (supervisors only)
- `/assign_shift` - Assign shift to user (supervisors only)
- `/approve_swap` - Approve swap request (supervisors only)
- `/manage_users` - Manage users (supervisors only)

## Tech Stack
- Python 3.8+
- python-telegram-bot 20.x
- SQLAlchemy (ORM)
- SQLite (with migration to PostgreSQL in future)
- APScheduler (for task scheduling)
- Redis (for caching and rate limiting)

## Project Structure
```
shift_scheduler_bot/
│
├── bot/                # Bot logic and command handlers
│   ├── commands/       # Command handlers
│   ├── handlers/       # Message and callback handlers
│   ├── keyboards/      # Keyboard layouts
│   └── main.py        # Bot entry point
│
├── db/                 # Database models and utilities
│   ├── models/        # Database models
│   └── base.py        # Database base configuration
│
├── utils/              # Helper functions
│   ├── scheduler.py   # Shift scheduling logic
│   └── translations.py # Multi-language support
│
├── tests/              # Unit tests
│   ├── test_db.py     # Database tests
│   └── test_bot.py    # Bot tests
│
├── requirements.txt    # Project dependencies
├── README.md          # Project documentation
└── .gitignore
```

## Development Progress

### Completed Steps
1. ✅ Project Setup
   - Created project structure
   - Set up development environment
   - Created requirements.txt
   - Created .gitignore

2. ✅ Database Design
   - Created User model with role-based access
   - Created Department model
   - Created Shift model
   - Created ShiftAssignment model
   - Created SwapRequest model
   - Created UserPreference model

3. ✅ Core Bot Development
   - Set up basic bot structure
   - Implemented multi-language support
   - Created keyboard layouts
   - Implemented message handlers
   - Implemented callback handlers
   - Added error handling

### Next Steps
1. 🔄 Database Implementation
   - Set up database connection
   - Create database migrations
   - Implement database utilities
   - Write database tests

2. 🔄 Command Implementation
   - Implement basic commands
   - Implement admin commands
   - Add command tests
   - Add command documentation

3. 🔄 Shift Scheduling Logic
   - Implement shift assignment
   - Add preference handling
   - Add conflict resolution
   - Add notification system

## Setup Instructions
1. Clone the repository
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Create `.env` file with required variables
5. Run the bot: `python bot/main.py`

## Environment Variables
- `TELEGRAM_BOT_TOKEN` - Your Telegram bot token
- `DATABASE_URL` - Database connection URL
- `REDIS_URL` - Redis connection URL (optional)

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License
MIT License
