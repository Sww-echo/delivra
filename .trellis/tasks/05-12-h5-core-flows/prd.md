# H5 auth home product order flows

## Goal

Implement the first core usable H5 flows: auth/onboarding, home, product/merchant browsing, cart, checkout, and order detail using mock data and documented interactions.

## Requirements

- Implement email/phone login, register, forgot password pages.
- Implement language and country/area code popup behavior.
- Implement third-party login placeholder pages for Google, Facebook, and Line.
- Implement home page entries: product, hotel, flight placeholder, recommendations, address, country, search.
- Implement product list with sort/filter/search local behavior.
- Implement merchant detail with menu/evaluate tabs, category switching, add to cart, cart popup, checkout navigation.
- Implement product detail with add to cart, cart popup, checkout, more comments, and back behavior.
- Implement checkout page and order detail page with status, copy, contact merchant, address change, payment confirmation, share popup, and cancel order behavior.

## Acceptance Criteria

- [ ] A user can navigate from login to home.
- [ ] A user can browse home recommendations into merchant/product pages.
- [ ] A user can add products to cart and open the cart popup.
- [ ] A user can navigate to checkout and then order detail.
- [ ] Documented core popups/actions show visible front-end feedback.

## Notes

- Parent task: `.trellis/tasks/05-12-requirements-doc-review`.
- Real auth/payment/OAuth/API behavior remains out of scope.
