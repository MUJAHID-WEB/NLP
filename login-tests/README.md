# Login Page Automated Tests

This repository contains automated tests for a login page using Playwright.

## Setup

1. Clone the repository: `git clone https://github.com/your-username/login-tests.git`
2. Install dependencies: `npm install`
3. Run tests: `npx playwright test`
4. To show report: `npx playwright show-report`
5. Run tests with HTML report: `npx playwright test --reporter=html`

## Branching Strategy

- `main`: Contains all merged test scenarios
- `successful-login`: Tests for valid credentials
- `failed-login`: Tests for invalid credentials
- `empty-fields`: Tests for empty form submission
- `error-messages`: Tests for validation messages

Each feature was developed in its own branch and merged to main after review.

## Test Approach

Tests follow the Page Object Model pattern for better maintainability. 
Playwright was chosen for its excellent cross-browser support and built-in assertions.


## Automation Strategy (250 words)
The automation strategy focuses on comprehensive validation of the login functionality while maintaining test reliability and readability. Using Playwright provides several advantages including automatic waiting for elements, built-in assertions, and cross-browser support.

The Page Object Model (POM) pattern was implemented to separate test logic from page structure, making tests more maintainable as the UI evolves. Each page has its own class containing element selectors and interaction methods.

For test scenarios, we cover both happy paths (successful login) and edge cases (empty fields, invalid formats). Assertions verify both UI changes (error messages) and application state (URL changes after login). Network delay handling is built into Playwright's auto-waiting functionality.

Test data is externalized in a JSON file, allowing easy updates without modifying test code. This also enables data-driven testing if we want to expand test cases later.

The branching strategy follows Git best practices, with each test scenario developed in isolation and merged after review. This keeps the commit history clean and makes it easy to track changes to specific test cases.

Error handling is implemented at multiple levels - Playwright's built-in retries for flaky tests, explicit assertions for business logic validation, and proper test isolation with beforeEach hooks. This creates a robust test suite that provides reliable feedback on the login functionality.