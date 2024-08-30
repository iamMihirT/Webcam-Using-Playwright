import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('https://www.banffjaspercollection.com/plan-your-trip/webcams/#/0');
  await page.getByRole('heading', { name: 'Banff Gondola Webcam' }).click();
  await page.frameLocator('strips iframe >> nth=0').locator('#svg-go-app path').click();
  const page1Promise = page.waitForEvent('popup');
  const downloadPromise = page.waitForEvent('download');
  await page.frameLocator('strips iframe >> nth=0').getByRole('button', { name: 'Download' }).click();
  const page1 = await page1Promise;
  const download = await downloadPromise;
  await page.frameLocator('strips iframe >> nth=0').locator('#archives-prev-button').click();
  await page.frameLocator('strips iframe >> nth=0').locator('#svg-go-app path').click();
  await page.frameLocator('strips iframe >> nth=0').getByRole('button', { name: 'Download' }).click();
  await page2.goto(':');
});await page2.goto(':');