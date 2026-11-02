# APIs & Keys Verification

Complete these checks during the lesson. Never record a real API key here.

## Safe configuration

- [x] Add `.env` to the repository-root `.gitignore` before storing a key in a `.env` file.
- [x] Confirm `.env` is ignored by Git (`course-repo/.gitignore:31`).
- [x] Confirm the API key was available to the process without printing its value.

## API exercises

- [x] Install and import the Anthropic Python SDK in the course virtual environment (version 2.3.0).
- [ ] Make a successful SDK request and record the response summary, not the key (pending API credits).
- [ ] Make a raw HTTP request and compare its response with the SDK response (pending API credits).
- [x] Identify the status and error type from a request using a fake key (401 `authentication_error`).

## Results

- Provider: Anthropic
- Model ID used: `claude-sonnet-5` (attempted)
- SDK request result: Not completed; HTTP 400 `invalid_request_error` reported insufficient credit balance.
- Raw HTTP result: Pending; script stopped at the SDK error before making the raw HTTP request.
- Fake-key error status/type: HTTP 401 / `authentication_error`.
- Error and fix: API account credit balance is too low. Check Console billing; successful live calls remain pending unless credits are available.
