# Reflection

- **Endpoint, API key, request body, and response:** The endpoint is the URL that receives the request. The API key authenticates and authorizes the caller. The request body contains the model and message data. The response carries the result and usage metadata, or error details if the request fails.
- **Why keep keys out of source code and Git history?** A committed key can be copied and misused, even if the file is later ignored or deleted. Keep keys in environment variables or an ignored local `.env` file; revoke and replace any key that was exposed.
- **What does the SDK handle?** It builds and sends the HTTP request, applies authentication and version headers, and parses the response into convenient objects. Raw HTTP makes the URL, headers, JSON payload, status code, and response body explicit.
- **What to inspect when an API returns an error:** Check the HTTP status and API error type/message, then verify authentication, model access, endpoint, and request fields. In this run, the real-key request returned HTTP 400 `invalid_request_error` because the account balance was too low; the fake-key request returned HTTP 401 `authentication_error`.
