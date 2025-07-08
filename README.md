

# 🧠 AI-Based Loan Recommendation Agent

A smart, explainable, and extensible loan assessment agent built using **Azure OpenAI**, designed to automate and streamline credit decisioning for **corporates and businesses**.

---

## 📌 Overview

This project enables automated evaluation of business loan applications based on structured financial and credit-related data. The AI agent reads company profiles, credit bureau summaries, and compliance reports, and generates:

✅ A loan recommendation (`Approved`, `Conditional Approval`, or `Rejected`)  
📝 A reason for the decision  
🛠️ Actionable suggestions (if applicable)  
📄 Alternative loan product options (only when risk permits)

> 🤖 This AI is designed to work like a **virtual credit officer** — quick, unbiased, and deeply analytical.

---

## 🛠️ Tech Stack

- **Azure OpenAI Service** (GPT-35 Turbo / GPT-4 model via Azure)
- `openai` SDK (Azure variant)
- Python 3.11+
- JSON-based structured input
- Optional: FastAPI / Azure Blob Storage integration

---

## 📥 Input Format

The AI takes in a JSON object like this:

```json
{
  "company_profile": {
    "name": "Finovate Solutions",
    "industry": "Fintech",
    "location": "Mumbai",
    "revenue": 120000000,
    "net_income": 30000000,
    "total_assets": 80000000,
    "liabilities": 20000000
  },
  "bureau_summary": {
    "existing_loans": 1,
    "past_defaults": 0,
    "recent_enquiries": 2,
    "credit_utilization": 35
  },
  "credit_score": 780,
  "compliance_reports": {
    "gst_filings": "Up to date",
    "tax_filings": "Filed on time",
    "legal_flags": []
  }
}
````

---

## 📤 Output Format

The agent returns a human-readable loan decision:

```text
Recommendation: Conditional Approval  
Reason: High liabilities and recent defaults  
Suggestions: Reduce liabilities below 1.5x net income and file overdue tax returns  
Alternative Loan Options:
- Secured Working Capital Loan
- Invoice Discounting with customer purchase orders
```

> If the company is **too risky**, alternative options will not be recommended.

---

## 💡 Use Cases

* 🔍 SME & Corporate Credit Evaluation
* 🏦 Loan Origination Systems (LOS)
* 📱 Embedded Finance & FinTech Apps
* 🧾 Automated Compliance & Risk Scoring
* 🤖 Credit Bots for Customer Portals

---

## 🧠 AI Decisioning Logic

The model evaluates:

* Revenue, Net Income, Total Assets
* Liabilities & Debt-to-Income Ratio
* Credit Score & Utilization
* Past Defaults & Enquiries
* Tax, GST, and Legal Compliance

It returns:

* ✅ `Approved`: If metrics are healthy
* ⚠️ `Conditional Approval`: If borderline
* ❌ `Rejected`: If risk is too high
  → with options **only if safe** to lend differently

---

## 🔧 Running the Agent

```bash
pip install openai
```

In `loan_recommendation_agent.py`, set the following:

```python
endpoint = "https://<your-resource-name>.openai.azure.com/"
deployment = "gpt-35-turbo"
subscription_key = "<your-azure-api-key>"
```

Then:

```bash
python loan_recommendation_agent.py
```

---

## 🔐 Security & Privacy

Ensure:

* Financial data is encrypted in transit
* API keys are stored securely (e.g., Key Vault or `.env`)
* No sensitive data is logged

---

## 🧩 Roadmap

* [x] JSON-based reasoning
* [x] Suggestions for unapproved cases
* [x] Alternative loan recommendations
* [ ] Credit score simulation
* [ ] Integration with PDF extractors
* [ ] FastAPI backend + Azure App Service
* [ ] React-based frontend demo

---

## 🤝 Contributing

Pull requests welcome! If you're a data scientist, financial analyst, or backend dev — feel free to fork and build.

---




