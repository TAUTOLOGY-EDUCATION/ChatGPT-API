# OpenAI API Guide

## **Contents**

- [Generate API Key](#generate-api-key)
- [Monitoring API Usage](#monitoring-api-usage)
- [Rate Limits](#rate-limits)
- [Pricing](#pricing)

## **Generate API Key**

To generate an API key for OpenAI, follow these steps:

1. Visit the [OpenAI API Keys page](https://platform.openai.com/account/api-keys).
2. If you haven't already, create an account and sign in.
3. Click on "Create a new API key".
4. Label your key and then click on "Create".

**Note:** Keep your API key secure. Never share it and avoid exposing it in public repositories or client-side code.

## **Monitoring API Usage**

Monitor your API usage to keep track of your consumption and avoid exceeding rate limits:

1. Visit the [OpenAI usage page](https://platform.openai.com/account/usage).
2. Here, see the number of requests made, the tokens used, and other usage details.

## **Rate Limits**

Rate limits depend on your OpenAI plan:

- Free trial users: 20 RPM, 40,000 TPM
- Pay-as-you-go (first 48 hours): 60 RPM, 60,000 TPM
- Pay-as-you-go (after 48 hours): 3500 RPM, 90,000 TPM

*RPM: Requests per minute
*TPM: Tokens per minute

Find more details about rate limits on the [OpenAI rate limits page](https://platform.openai.com/account/rate-limits) and in the [rate limits guide](https://platform.openai.com/docs/guides/rate-limits/overview).

Exceeding these limits will result in a `429 Too Many Requests` error.

## **Pricing**

The pricing for different models of ChatGPT is as follows:

| Model       | Context Size | Prompt Price  | Completion Price |
| ----------- | ------------ | ------------  | --------------   |
| GPT-4       | 8K          | $0.03 / 1K tokens  | $0.06 / 1K tokens   |
| GPT-4       | 32K         | $0.06 / 1K tokens  | $0.12 / 1K tokens   |
| gpt-3.5-turbo | N/A      | $0.002 / 1K tokens | N/A             |
| Ada         | N/A         | $0.0004 / 1K tokens | N/A            |
| Babbage     | N/A         | $0.0005 / 1K tokens | N/A            |
| Curie       | N/A         | $0.0020 / 1K tokens | N/A            |
| Davinci     | N/A         | $0.0200 / 1K tokens | N/A            |

Please visit OpenAI's [pricing page](https://openai.com/pricing) for the most accurate and up-to-date information.

To estimate the number of tokens in a text string, you can use the [OpenAI token counter](https://platform.openai.com/tokenizer).