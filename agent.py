from openai import AzureOpenAI

# Azure OpenAI config
endpoint = "https://aihub0012034742062.openai.azure.com/"
deployment = "gpt-35-turbo"
api_version = "2024-12-01-preview"
subscription_key = "EY3z5eTUiFnr2s63t2aohykHWhhavdObJFKI9svE0EONuGAsJz9XJQQJ99BFACHYHv6XJ3w3AAAAACOGXAew"  # Replace with your actual Azure OpenAI key

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

# System prompt (the core logic of the agent)

system_prompt = """
You are a financial loan recommendation expert.

You will receive structured JSON input with:
- Company profile
- Bureau summary
- Credit score
- Compliance reports

Return one of the following:
- Recommendation: <Approved / Conditional Approval / Rejected>
- If not Approved:
    - Reason: <Clear explanation>
    - Suggestions: <Ways to improve loan eligibility>

Additionally:
- If Suggestions are given and the applicant is **unable to make changes**, recommend **alternative loan options** that fit their current risk profile (e.g., secured working capital, invoice-based loans).
- Only offer such alternatives if risk is **not severe**.
- If the company is **too risky**, state: "No safe alternative loan options available."

Output format:
Recommendation: ...
Reason: ...
Suggestions: ...
Alternative Loan Options: ...

Only include 'Reason', 'Suggestions', and 'Alternative Loan Options' if the recommendation is NOT "Approved".
Keep answers clear and based strictly on data from the input JSON.
"""



def generate_loan_recommendation(user_input_json: dict) -> str:
    # Create user prompt from JSON input
    import json
    user_prompt = f"Input JSON:\n{json.dumps(user_input_json, indent=2)}"

    # Send to Azure OpenAI
    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=1024,
        temperature=0.7,
        top_p=1.0
    )

    return response.choices[0].message.content
if __name__ == "__main__":
    sample_input = {
        "company_profile": {
            "name": "GreenBuild Infra Pvt Ltd",
            "industry": "Construction",
            "location": "Hyderabad",
            "revenue": 90000000,
            "net_income": 4000000,
            "total_assets": 30000000,
            "liabilities": 25000000
        },
        "bureau_summary": {
            "existing_loans": 3,
            "past_defaults": 1,
            "recent_enquiries": 4,
            "credit_utilization": 78
        },
        "credit_score": 660,
        "compliance_reports": {
            "gst_filings": "Up to date",
            "tax_filings": "Delayed for FY 2022-23",
            "legal_flags": ["Pending GST hearing"]
        }
    }

    result = generate_loan_recommendation(sample_input)
    print(result)
