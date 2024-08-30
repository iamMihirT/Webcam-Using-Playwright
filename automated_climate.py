import asyncio
import os
from playwright.async_api import async_playwright

async def test_download_webcam_media():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Navigate to the website
        await page.goto('https://www.banffjaspercollection.com/plan-your-trip/webcams/#/0')

        # Click on the 'Banff Gondola Webcam' heading
        await page.get_by_role("heading", name="Banff Gondola Webcam").click()

        try:
            while True:
                # Click on the path element inside the iframe
                frame = page.frame_locator('strips iframe >> nth=0')
                await frame.locator('#svg-go-app path').click()

                # Wait for the popup and download events
                async with page.expect_popup() as popup_info, page.expect_download() as download_info:
                    # Click on the 'Download' button
                    await frame.get_by_role("button", name="Download").click()

                popup_page = await popup_info.value
                download = await download_info.value
                download_path = os.path.join('C:\\Users\\Mihir Trivedi\\Desktop\\webcams\\store_images', download.suggested_filename)
                await download.save_as(download_path)
                print(f"Downloaded: {download_path}")

                # Click on the previous button in the iframe
                await frame.locator('#archives-prev-button').click()

        except KeyboardInterrupt:
            print("Keyboard interruption detected. Stopping the script.")

        # Close the browser
        await browser.close()

# Run the test
async def main():
    await test_download_webcam_media()

asyncio.run(main())