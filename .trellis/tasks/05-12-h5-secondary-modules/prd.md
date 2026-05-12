# H5 hotel order message user agent modules

## Goal

Implement the remaining H5 modules from the requirements document after the scaffold and core flows exist: hotel booking, order center, messages, user center/account settings, agent flows, and static pages.

## Requirements

- Implement hotel list, hotel detail, hotel booking, and hotel order detail flows.
- Implement order list with status filters, order card navigation, payment proof popup, delivery detail popup, and review entry.
- Implement review page with rating, image picker placeholder, submit feedback, and back behavior.
- Implement message list, chat page, chat action popup, send message local behavior, and chat settings placeholder.
- Implement user center menu and related pages: profile, recharge, withdraw, records, payment info, address, password pages, real-info, account binding, country/language actions, delete confirmation.
- Implement agent dashboard, quick-create-order page, package-generation popup, pay order list, frozen amount list, and copy actions.
- Implement static help/protocol/policy pages.

## Acceptance Criteria

- [ ] Hotel flow is navigable through list, detail, booking, and order detail pages.
- [ ] Order center supports status switching and required popups.
- [ ] Message list and chat page support local message sending behavior.
- [ ] User center menu entries route to implemented or explicit placeholder pages.
- [ ] Agent pages support documented navigation, filters, popups, and copy feedback.
- [ ] Static pages render by route type.

## Notes

- Parent task: `.trellis/tasks/05-12-requirements-doc-review`.
- Depends on shared components/mock data and core app shell.
