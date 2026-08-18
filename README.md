# 💼 B2B Intent Lead Intelligence & Contact Finder Actor

Enrich company firmographics, detect buying intent signals (funding, hiring surge, CRM migrations), and extract verified decision-maker emails with LinkedIn profile URLs.

## 🚀 Usage & Input Parameters

| Field | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `company_name` | string | Target company name | `Apex Cloud Systems` |
| `domain` | string | Company domain | `apexcloud.io` |
| `intent_signal` | string | Buying intent trigger | `Series A Funded $10M` |
| `target_title` | string | Executive title | `VP of Engineering` |

## 📤 Output Format

```json
{
  "company_name": "Apex Cloud Systems",
  "domain": "apexcloud.io",
  "estimated_headcount": "50-250 employees",
  "intent_score": 94,
  "intent_signals_detected": ["Series A Funded $10M", "Hiring AI Engineers"],
  "decision_maker": {
    "name": "Alex Mercer",
    "title": "VP of Engineering",
    "verified_email": "alex.mercer@apexcloud.io",
    "linkedin_url": "https://linkedin.com/in/alexmercer-apexcloud"
  },
  "verified_status": "✅ Verified (SMTP Socket Passed)"
}
```
