
class AltnoisiLoginPage {
  constructor(page) {
    this.page = page;
    this.usernameField = page.locator('#username');
    this.passwordField = page.locator('#password');
    this.loginButton = page.locator('button[type="submit"]');
    
    this.rememberMeCheckbox = page.locator('input[name="rememberme"]');
    
    this.forgotPasswordLink = page.locator('text=I forgot my password');
    
    // this.errorMessage = page.locator('div.bg-red-50.text-red-500');
    // this.errorText = page.locator('div.bg-red-50.text-red-500 span:last-child');
    this.errorMessage = page.locator('.notice.bg-red-50');
    this.errorText = page.locator('.notice.bg-red-50 span:has-text("Incorrect email or password")');
    
    this.fieldErrors = page.locator('.form-input-wrapper .error-message');
  }

  async navigate() {
    await this.page.goto('https://altnoisi.com/en/login');
    await this.page.waitForLoadState('networkidle');
  }

  async login(username, password) {
    await this.usernameField.fill(username);
    await this.passwordField.fill(password);
    await this.loginButton.click();
  }
//   async login(username, password, rememberMe = false) {
//     await this.usernameField.fill(username);
//     await this.passwordField.fill(password);
//     if (rememberMe) await this.rememberMeCheckbox.check();
//     await this.loginButton.click();
//   }

//   async getFieldErrorMessages() {
//     const errors = [];
//     for (const error of await this.fieldErrors.all()) {
//       errors.push(await error.textContent());
//     }
//     return errors;
//   }
// }

  async checkRememberMe() {
    await this.rememberMeCheckbox.check();
  }

  async getErrorMessage() {
    await this.errorMessage.waitFor({ state: 'visible', timeout: 5000 });
    return await this.errorText.textContent();
  }
}

module.exports = AltnoisiLoginPage;