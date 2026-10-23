# QRShield

A QR code security system that checks QR codes **before** you open the link or pay.

> CSAI 490 – Senior Project
> Advisor: Dr. Nashwa Abdelbaki
> Team: Zeyad Hendawy, Omar Kareem, Khaled Fayoumy, Fahd Rashdan

## The problem

Users can't tell whether a QR code leads to a safe website or whether a payment QR has been tampered with. This leaves them open to phishing and financial theft.

## What QRShield does

1. **Classify** – is the code a payment, a website link, or something else?
2. **Read payment data** – extract merchant, account and amount (e.g. InstaPay, wallets) into one common format.
3. **Check links** – follow redirects, flag look-alike bank/wallet domains, check blocklists.
4. **Merchant memory** – warn when a familiar shop's QR suddenly points to a different account.

The result is a green / yellow / red verdict with a plain explanation in Arabic and English.

*Optional:* Verified Merchant Mode using signed QR codes.

> We reduce risk; we can't prove a well-made fake is fake from the code alone.

## Project structure

```
qrshield/
├── docs/      # presentation, notes, Gantt chart, risk log
├── src/       # source code
├── data/      # datasets (not committed if large)
└── README.md
```

## Getting started

```bash
git clone <repo-url>
cd qrshield
```

Setup instructions will be added as development progresses.

## Status

🚧 In early development – environment and repository setup complete.
