# OpenAI API Guide

## Contents

- [Generate API Key](#generate-api-key)
- [Monitoring API Usage](#monitoring-api-usage)
- [Rate Limits](#rate-limits)
- [Pricing](#pricing)

## Generate API Key

To generate an API key for OpenAI, you need to follow these steps:

1. Visit the OpenAI website and navigate to the dashboard.
2. If you haven't already, create an account and sign in.
3. Navigate to the API Keys section.
4. Click on "Create a new API key".
5. Label your key and then click on "Create".

Note: Remember to keep your API key secure. Never share your API key and avoid exposing it in public repositories or client-side code.

## Monitoring API Usage

Monitoring your API usage is essential to keep track of your consumption and avoid exceeding rate limits. Here is how you can monitor your API usage:

1. Visit the OpenAI dashboard.
2. Navigate to the API usage section.
3. Here you can see the number of requests made, the tokens used, and other usage details.

## Rate Limits

Rate limits depend on your OpenAI plan:

- Free trial users: 20 RPM, 40,000 TPM
- Pay-as-you-go (first 48 hours): 60 RPM, 60,000 TPM
- Pay-as-you-go (after 48 hours): 3500 RPM, 90,000 TPM

*RPM: Requests per minute
*TPM: Tokens per minute

If you exceed these limits, you will receive a `429 Too Many Requests` error.

## Pricing

OpenAI's pricing details can be found on their [pricing page](https://openai.com/pricing). Charges are typically based on the number of tokens processed (input and output). There is also a monthly cost for usage above the free tier.

Remember, always consult the official OpenAI documentation for the most accurate and up-to-date information.
