# H5 shared components and mock data

## Goal

Build the reusable UI primitives, domain widgets, mock data, types, and stores needed to implement the H5 page flows consistently without duplicating layout and state logic.

## Requirements

- Add shared layout/common components such as AppPage, SectionCard, StatusTabs, FilterBar, and EmptyState.
- Add business components such as ProductCard, MerchantCard, OrderCard, HotelCard, CartPopup, and StaticPage.
- Define domain types for user, merchant, product, cart, order, hotel, message, payment account, and agent order.
- Add mock data modules shaped for future API replacement.
- Add Pinia stores for app preferences, user/auth mock state, and cart.
- Use Vant feedback patterns for copy, submit success, dialogs, and popups.

## Acceptance Criteria

- [ ] Shared components are reusable across at least two feature modules.
- [ ] Mock data is centralized under the H5 source tree rather than embedded deeply in pages.
- [ ] Cart state works across product-related pages.
- [ ] Static page rendering can support help, qualification, intro, refund policy, agreement, and privacy pages.
- [ ] Components follow the architecture in parent `design.md`.

## Notes

- Parent task: `.trellis/tasks/05-12-requirements-doc-review`.
- Depends on scaffold/routing being available.
