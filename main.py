"""
B2B Intent Lead Intelligence Apify Actor
Wrapper calling Micro-SaaS AI Agent Suite API (POST /enrich-lead)
"""

import os
import requests
from apify import Actor

async def main():
    async with Actor:
        actor_input = await Actor.get_input() or {}
        company_name = actor_input.get("company_name", "Apex Cloud Systems")
        domain = actor_input.get("domain", "apexcloud.io")
        intent_signal = actor_input.get("intent_signal", "Series A Funded $10M")
        target_title = actor_input.get("target_title", "VP of Engineering")

        Actor.log.info(f"Enriching B2B Lead for {company_name} ({domain}) with signal: {intent_signal}")

        api_url = "https://microsaas-agent-api.vercel.app/enrich-lead"
        payload = {
            "company_name": company_name,
            "domain": domain,
            "intent_signal": intent_signal,
            "target_title": target_title
        }

        response = requests.post(api_url, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()

        await Actor.push_data(data)
        Actor.log.info("Successfully pushed enriched B2B lead to Apify dataset!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
