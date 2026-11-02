---
name: prompt-api-troubleshooter
description: Diagnose common AI API errors involving authentication, rate limits, timeouts, and request formats.
phase: 0
lesson: 4
---

When troubleshooting an API request, inspect the status code and error type.
Do not print, paste, or log the API key.

| Error | Common cause | First check |
|---|---|---|
| 401 Unauthorized | Key missing or invalid | Check whether the environment variable is set without displaying its value. |
| 403 Forbidden | Key or account lacks permission | Check provider access, endpoint, and model permissions. |
| 429 Too Many Requests | Rate limit exceeded | Wait, then retry with backoff. |
| 400 Bad Request | Invalid request body or model ID | Compare required fields and model ID with the provider's current API docs. |
| 500, 502, or 503 | Provider-side failure | Retry later with a delay. |
| Timeout | Slow response or network interruption | Retry with a suitable timeout or use streaming when appropriate. |
| Connection error | Wrong endpoint or network issue | Check the endpoint URL and network connection. |

## Safe diagnostic steps

1. Check whether `ANTHROPIC_API_KEY` is set without printing its value:

   ```python
   import os
   print("ANTHROPIC_API_KEY is set:", bool(os.environ.get("ANTHROPIC_API_KEY")))
   ```

2. Confirm the key is kept out of source control with `git check-ignore -v .env`.
3. Check the endpoint, model ID, request body, and provider's current docs.
4. For a controlled authentication exercise, use a fake key and inspect the error response. Never use or share a real key for this test.
