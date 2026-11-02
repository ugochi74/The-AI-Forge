# APIs & Keys

Course lesson: [APIs & Keys](https://aiengineeringfromscratch.com/lesson?path=phases/00-setup-and-tooling/04-apis-and-keys)

## Goal

Learn how an application authenticates to an AI API, sends a request, receives
a response, and diagnoses common errors.

## Request parts

1. Endpoint: where the request is sent.
2. API key: identifies and authorizes the account.
3. Request body: contains the model and message.
4. Response: contains generated content and usage metadata.

Anthropic's Messages endpoint is `POST /v1/messages`. The SDK and raw HTTP
examples are in `code/first_api_call.py`.

## Key handling

- Keep real keys in environment variables or a local `.env` file.
- Add `.env` to the repository-root `.gitignore` before creating one.
- Never put a real key in source code, commits, screenshots, or chat.
- The sample sends real API requests when a valid key is available; do not run
  it until you are ready to use your provider account.

## Lesson deliverable

Use `outputs/prompt-api-troubleshooter.md` to diagnose authentication,
permission, rate-limit, request, server, and network errors.
