# Multiwallet Gas Rescue Bot

## 🌐 English Description

This Python bot is designed to automatically rescue native tokens (used for gas) from multiple compromised wallets across various EVM-compatible blockchains.
It continuously scans wallet balances and, if enough native token exists to cover the gas fee, transfers the remainder to a safe wallet.

### Supported Chains
- Ethereum
- BNB Smart Chain (BSC)
- Arbitrum
- Optimism
- Base
- Polygon
- Fantom
- Gravity
- Sonic
- Soneium
- Zora

### Features
- Monitors multiple wallets simultaneously
- Works on all major EVM networks
- Sends any remaining native token to a safe wallet
- Logs all transactions and errors
- Uses a gas fee buffer to prevent overshooting

### Setup Instructions
1. Install Python dependencies:
   ```bash
   pip install web3
   ```
2. Edit the `wallets` list in the script with your compromised wallets and safe destination addresses.
3. Run the bot:
   ```bash
   python main.py
   ```

---

## 🌐 توضیح فارسی

این بات پایتون برای نجات دادن مقادیر گَس (توکن بومی) از چندین کیف پول هک‌شده طراحی شده است.
اسکریپت به صورت خودکار موجودی کیف‌پول‌ها را در شبکه‌های بلاک‌چینی مختلف بررسی کرده و در صورت کافی بودن برای پرداخت کارمزد، موجودی را به یک کیف‌پول امن منتقل می‌کند.

### شبکه‌های پشتیبانی‌شده
- اتریوم
- زنجیره BNB (BSC)
- آربیتروم
- آپتیمیسم
- بیس (Base)
- پالیگان
- فانتوم
- گراویتی
- سونیک
- سونیوم
- زورا

### امکانات
- پشتیبانی از چندین والت همزمان
- سازگار با شبکه‌های EVM
- انتقال خودکار گَس به والت امن
- ثبت لاگ تراکنش و خطاها
- جلوگیری از خطای کارمزد با بافر

### نحوه استفاده
1. نصب وابستگی‌ها:
   ```bash
   pip install web3
   ```
2. لیست `wallets` را در کد با کلید خصوصی و آدرس والت‌ها پر کنید.
3. اجرای برنامه:
   ```bash
   python main.py
   ```

---

