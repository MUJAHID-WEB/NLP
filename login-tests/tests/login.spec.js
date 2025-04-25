
const { test, expect } = require('@playwright/test');
const AltnoisiLoginPage = require('../pages/LoginPage');
const AltnoisiDashboardPage = require('../pages/DashboardPage');

test.describe('Altnoisi Login Tests', () => {
  const testCredentials = {
    valid: {
      username: 'shopper@altnoisi.com',
      password: 'Hb2CxpUMLNd02OHNVY'
    },
    invalid: {
      username: 'shopper@altnoisi.com',
      password: 'wrongpassword'
    }
  };

  let loginPage;
  let dashboardPage;

  test.beforeEach(async ({ page }) => {
    loginPage = new AltnoisiLoginPage(page);
    dashboardPage = new AltnoisiDashboardPage(page);
    await loginPage.navigate();
  });

  test('Successful login redirects to dashboard', async ({ page }) => {
    await loginPage.login(
      testCredentials.valid.username,
      testCredentials.valid.password
    );
    
    const dashboardVisible = await dashboardPage.isDisplayed();
    expect(dashboardVisible).toBeTruthy();
    
    await expect(dashboardPage.pageTitle).toBeVisible();
    await expect(dashboardPage.logoutButton).toBeVisible();
    
    await page.screenshot({ path: 'dashboard.png', fullPage: true });
  });

  test('Failed login shows error message', async () => {
    await loginPage.login(
      testCredentials.invalid.username,
      testCredentials.invalid.password
    );
    
    await expect(loginPage.errorMessage).toBeVisible();
    const errorText = await loginPage.getErrorMessage();
    expect(errorText).toContain('Incorrect email or password');

    await expect(loginPage.page).toHaveURL(/login/);
  });

  test('Login with empty fields shows validation errors', async () => {
    await loginPage.loginButton.click();
    
    // Verify HTML5 validation
    const usernameValid = await loginPage.usernameField.evaluate(
      (el) => el.checkValidity()
    );
    const passwordValid = await loginPage.passwordField.evaluate(
      (el) => el.checkValidity()
    );
    
    expect(usernameValid).toBeFalsy();
    expect(passwordValid).toBeFalsy();
  });

  test('Remember me functionality', async ({ context }) => {

    await expect(loginPage.rememberMeCheckbox).toBeVisible();
    
    await loginPage.checkRememberMe();
    
    await expect(loginPage.rememberMeCheckbox).toBeChecked();
    
    await loginPage.login(
      testCredentials.valid.username,
      testCredentials.valid.password
    );
    
    await dashboardPage.isDisplayed();
    
    const cookies = await context.cookies();
    console.log('Cookies:', cookies);
  });

  test('Forgot password link works', async () => {
    await loginPage.forgotPasswordLink.click();
    await expect(loginPage.page).toHaveURL(/recover-password/);
  });
});


////////////////////////

// const { test, expect } = require('@playwright/test');
// const AltnoisiLoginPage = require('../pages/LoginPage');
// const AltnoisiDashboardPage = require('../pages/DashboardPage');

// test.describe('Altnoisi Login Tests', () => {
//   const testCredentials = {
//     valid: { username: 'shopper@altnoisi.com', password: 'Hb2CxpUMLNd02OHNVY' },
//     invalid: { username: 'shopper@altnoisi.com', password: 'wrongpassword' }
//   };

//   let loginPage, dashboardPage;

//   test.beforeEach(async ({ page }) => {
//     loginPage = new AltnoisiLoginPage(page);
//     dashboardPage = new AltnoisiDashboardPage(page);
//     await loginPage.navigate();
//   });

//   test('Successful login redirects to dashboard', async () => {
//     await loginPage.login(testCredentials.valid.username, testCredentials.valid.password);
//     const loginSuccess = await dashboardPage.verifySuccessfulLogin();
//     expect(loginSuccess).toBeTruthy();
//   });

//   test('Failed login shows appropriate error message', async () => {
//     await loginPage.login(testCredentials.invalid.username, testCredentials.invalid.password);
    

//     await expect(loginPage.errorMessage).toBeVisible();
//     const errorText = await loginPage.errorText.textContent();
//     expect(errorText).toMatch(/incorrect email or password/i);
    
//     await expect(loginPage.page).toHaveURL(/login/);
//   });

//   test('Login attempts with empty fields show validation errors', async () => {

//     await loginPage.passwordField.fill('test');
//     await loginPage.loginButton.click();
//     let errors = await loginPage.getFieldErrorMessages();
//     expect(errors.some(e => e.includes('email'))).toBeTruthy();

//     await loginPage.usernameField.fill(testCredentials.valid.username);
//     await loginPage.passwordField.fill('');
//     await loginPage.loginButton.click();
//     errors = await loginPage.getFieldErrorMessages();
//     expect(errors.some(e => e.includes('password'))).toBeTruthy();
//   });

//   test('Remember me functionality persists session', async ({ context }) => {
//     await expect(loginPage.rememberMeCheckbox).toBeVisible();
//     await loginPage.login(testCredentials.valid.username, testCredentials.valid.password, true);
    
//     await dashboardPage.verifySuccessfulLogin();
    
//     const cookies = await context.cookies();
//     const rememberCookie = cookies.find(c => c.name.includes('remember'));
//     expect(rememberCookie).toBeTruthy();
//   });

//   test('Forgot password link redirects properly', async () => {
//     await loginPage.forgotPasswordLink.click();
//     await expect(loginPage.page).toHaveURL(/recover-password/);
//   });
// });