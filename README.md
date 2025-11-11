# Mini ATM System

A Python-based mini ATM system that simulates basic banking operations with user authentication, transaction management, and admin functionality.

## Features

### 🔐 Authentication System
- Username and PIN-based login
- Maximum 3 PIN attempts before account lock
- Pre-configured user database

### 💰 Banking Operations
- **Balance Inquiry**: Check current account balance
- **Cash Deposit**: Add funds to account
- **Cash Withdrawal**: Withdraw money with daily limits
- **Transaction History**: View all past transactions
- **PIN Change**: Update account PIN (admin feature)

### ⚡ Security Features
- Daily withdrawal limit (₹20,000)
- Input validation
- Secure logout option
- Separate admin mode

### 👨‍💼 Admin Mode
- Access all user accounts and data
- Modify admin PIN
- System-wide oversight

## User Accounts

Pre-configured demo accounts:

| Username | PIN | Balance |
|----------|-----|---------|
| Suryam | 202004 | ₹50,000 |
| Shrutika | 182005 | ₹1,00,000 |
| Kaiser | 123456 | ₹15,000 |
| Mahesh Dalle | 343434 | ₹1,00,000 |
| Mukesh | 901256 | ₹40,000 |

**Admin Access:**
- Username: `Admin`
- PIN: `606060`

## Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/mini-atm-system.git
   cd mini-atm-system
