
class AltnoisiDashboardPage {
  constructor(page) {
    this.page = page;
    this.pageTitle = page.locator('header .menu-item.active a:has-text("Dashboard")');
    this.welcomeMessage = page.locator('div.bg-blue-50.text-blue-500:has-text("successfully logged in")');
    
    this.logoutButton = page.locator('header a.btn.button:has-text("Logout")');
  }

//   async verifySuccessfulLogin() {
//     try {
//       await this.page.waitForURL(/dashboard/, { timeout: 10000 });
//       await expect(this.dashboardMenu).toBeVisible();
//       await expect(this.successMessage).toBeVisible();
//       await expect(this.logoutButton).toBeVisible();
//       return true;
//     } catch (error) {
//       console.error('Dashboard verification failed:', error);
//       return false;
//     }
//   }
// }

  async isDisplayed() {
    try {
      await this.page.waitForURL(/dashboard/, { timeout: 10000 });
      
      const elementsVisible = await Promise.all([
        this.pageTitle.isVisible(),
        this.logoutButton.isVisible()
      ]);
      
      return elementsVisible.every(visible => visible);
    } catch (error) {
      console.error('Dashboard verification failed:', error);
      return false;
    }
  }
}

module.exports = AltnoisiDashboardPage;