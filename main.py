from playwright.sync_api import sync_playwright, expect


def test1():
    with sync_playwright() as s:
        for browser_type in [s.chromium]:
            browser = browser_type.launch()
            page = browser.new_page()
            page.goto('https://github.com/DamirDyanov?tab=repositories')
            page.get_by_role("link", name="first_test").click()
            page.get_by_role("link", name='Issues').click()

            page.locator("//a[@id='issue_2_link']").click()
            locator = page.locator("//div[@class='js-issues-results js-socket-channel js-updatable-content']")
            expect(locator).to_be_visible()
            page.screenshot(path=f'example-{browser_type.name}.png')
            browser.close()
