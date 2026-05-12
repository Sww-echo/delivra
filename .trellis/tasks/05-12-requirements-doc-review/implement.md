# H5 Frontend Implementation Plan

## 1. Preconditions

- User has approved Vue 3 + Vite + Vant as the stack.
- Before coding, activate this Trellis task with `task.py start` after reviewing this plan.
- Do not modify `delivra.top/` build artifacts.

## 2. Trellis Subtasks

- `.trellis/tasks/05-12-h5-scaffold-routing` — pending; create `h5/`, scaffold project, routing, app shell, placeholders.
- `.trellis/tasks/05-12-h5-shared-components-mock-data` — pending; shared components, domain types, mock data, stores.
- `.trellis/tasks/05-12-h5-core-flows` — pending; auth, home, product, merchant, cart, checkout, order detail.
- `.trellis/tasks/05-12-h5-secondary-modules` — pending; hotel, order center, messages, user center, agent, static pages.
- `.trellis/tasks/05-12-h5-verification-polish` — pending; coverage check, build/typecheck, browser verification, polish.

## 3. Implementation Phases

### Phase 1 — Project scaffold

- Create a Vite Vue 3 TypeScript project in the `h5/` subdirectory.
- Add dependencies: Vue 3, Vue Router 4, Vant 4, Pinia, TypeScript, Vite.
- Add basic scripts: `dev`, `build`, `preview`, `typecheck` if supported.
- Configure mobile viewport, global styles, app entry, and Vant style imports.
- Verify the app starts and builds.

### Phase 2 — App shell and routing

- Define the route table from the design document.
- Implement `App.vue`, main layout, tabbar layout, and back-nav page shell.
- Add route guards only if needed for mock auth; avoid real auth enforcement until backend exists.
- Create placeholder pages for all required routes so every documented navigation target exists.
- Verify route navigation manually in browser.

### Phase 3 — Shared components and mock data

- Add shared components:
  - `AppPage`
  - `SectionCard`
  - `StatusTabs`
  - `FilterBar`
  - `ProductCard`
  - `MerchantCard`
  - `OrderCard`
  - `HotelCard`
  - `CartPopup`
  - `StaticPage`
- Add mock data files and domain types.
- Add stores for app preferences, cart, user/auth mock state.

### Phase 4 — Auth and onboarding flows

- Implement email/phone login pages.
- Implement phone/email register pages.
- Implement phone/email forgot password pages.
- Implement language and country code popup behavior.
- Implement protocol/privacy/static route navigation.
- Implement third-party login placeholder pages for Google/Facebook/Line.

### Phase 5 — Home, product, cart, and order flow

- Implement home page with bottom navigation, quick entries, search, recommendations, address, and country selection.
- Implement product list with search/filter/sort controls.
- Implement merchant detail with menu/evaluate tabs, category switching, add-to-cart, cart popup, checkout navigation.
- Implement product detail with add-to-cart, cart popup, checkout, more comments, and back navigation.
- Implement checkout page with address entry, submit order, and order detail navigation.
- Implement order detail with status, copy order number, merchant info, contact merchant, change address, payment confirmation, share popup, cancel order.

### Phase 6 — Hotel flow

- Implement hotel list with sorting/search/address/back behavior.
- Implement hotel detail with phone placeholder, date selection, room selection, booking navigation.
- Implement hotel booking with date picker and submit order.
- Implement hotel order detail with status, hotel navigation, payment, share, cancel, and back behavior.

### Phase 7 — Orders and reviews

- Implement order list with status filters and bottom navigation.
- Implement order card navigation to order detail.
- Implement payment proof popup and delivery detail popup.
- Implement review page with rating, image picker placeholder, submit feedback, and back behavior.

### Phase 8 — Messages

- Implement message list with bottom navigation, message card navigation, and settings navigation.
- Implement chat page with plus popup, send message local behavior, settings navigation, and back behavior.
- Implement chat background settings placeholder page.

### Phase 9 — User center and account settings

- Implement user center menu entries and navigation.
- Implement profile page with avatar picker placeholder, gender picker, birthday picker, account binding, password, withdraw password, real-name, country, delete confirmation.
- Implement change account pages for phone/email account binding.
- Implement recharge, withdraw, records, payment account list, add/edit payment account, address page, password pages, real-info page.
- Implement static pages for help center, company qualification, product/service intro, refund policy, user agreement, privacy policy.

### Phase 10 — Agent flow

- Implement agent dashboard.
- Implement quick create order page and package generation popup.
- Implement pay order list and frozen amount list with filters, detail navigation, copy order number, copy pay link, copy proxy ID.

### Phase 11 — Verification and cleanup

- Check every route from the requirements document has a page or explicit placeholder.
- Check every documented click action has one of: route navigation, popup, local state change, copy feedback, submit feedback, or explicit mock placeholder.
- Run build/typecheck.
- Start dev server and manually verify core mobile flows in browser.
- Run Trellis quality check.

## 3. Validation Commands

Expected commands after scaffold exists:

```bash
npm install
npm run build
npm run typecheck
npm run dev
```

If the chosen package manager differs, update this section before implementation.

## 4. Review Gates

- Gate 1: Scaffold builds and dev server opens.
- Gate 2: Route map covers all page groups.
- Gate 3: Core product order flow works end-to-end with mock data.
- Gate 4: Remaining modules are navigable and interactions are represented.
- Gate 5: Final build and manual browser verification pass.

## 5. Rollback Points

- After Phase 1, scaffold can be reverted independently if dependencies or structure are wrong.
- After Phase 2, route design can still be adjusted before deep page work.
- After Phase 5, core data models and shared components should be stabilized before expanding to all secondary modules.

## 6. Open Decisions Before Start

- Whether the first implementation should prioritize full route/page skeleton coverage or deeply polished core flows.
- App source will be created in the `h5/` subdirectory.
- Preferred package manager: npm.
