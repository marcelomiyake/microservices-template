import { expect, test } from '@playwright/test'

test('renders the real Kind service response', async ({ page }) => {
  await page.goto('/')
  await expect(page.getByRole('heading', { name: 'Start your proof of concept' })).toBeVisible()
  await expect(page.getByText('Your Rust and Vue PoC is running.')).toBeVisible()
})
