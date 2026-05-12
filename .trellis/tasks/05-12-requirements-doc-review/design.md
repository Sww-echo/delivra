# H5 Frontend Technical Design

## 1. Goal

Build a new mobile H5 frontend from scratch based on `页面需求.docx`, using Vue 3 + Vite + Vant. The project should provide a maintainable page-flow application with mobile-first UI, route-based navigation, reusable page primitives, mockable data, and clear boundaries for future API integration.

## 2. Scope

### In scope

- Create a new Vue 3 H5 source project under the `h5/` subdirectory in this repository.
- Implement the app shell, mobile viewport behavior, routing, bottom tab navigation, and shared layout components.
- Cover the page groups from the requirements document:
  - Auth: login, register, forgot password, protocol/privacy, third-party login placeholder pages.
  - Home/business: home, product list, merchant detail, product detail, cart popup, order confirmation, order detail.
  - Hotel: hotel list, hotel detail, booking, hotel order detail.
  - Orders: order list, order detail entry behavior, review page, order-related popups.
  - Messages: message list, chat page, chat settings.
  - Mine/account: profile, recharge, withdraw, records, payment info, address, account binding, password/real-name pages, proxy/agent pages, static help pages.
- Implement documented interactions as front-end behavior: route navigation, tabs, popups, pickers, filters, copy actions, submit success feedback.
- Use local mock data and UI state until backend APIs are confirmed.

### Out of scope for initial implementation

- Real backend integration.
- Real payment, third-party OAuth, SMS/email verification, upload, phone call, map/address SDK integration.
- Editing built files under `delivra.top/`.
- Pixel-perfect reproduction of unknown visual design details not present in the docx.

## 3. Technology Decisions

- Framework: Vue 3 with Composition API.
- Build tool: Vite.
- Language: TypeScript.
- UI library: Vant 4.
- Router: Vue Router 4.
- State: Pinia for cross-page app state that is genuinely shared, such as auth mock state, cart, selected country/language, and current user.
- Styling: mobile-first SCSS/CSS modules or scoped SCSS in Vue SFCs; global design tokens for colors, spacing, radius, shadows.
- Tests/checks: TypeScript check, build verification, and minimal route/component smoke tests if test tooling is added.

## 4. Architecture

### Suggested directory structure

```text
src/
  app/
    App.vue
    main.ts
    router.ts
  assets/
  components/
    common/
    layout/
    business/
  data/
    mockAuth.ts
    mockHome.ts
    mockProducts.ts
    mockOrders.ts
    mockMessages.ts
    mockUser.ts
  pages/
    auth/
    home/
    product/
    hotel/
    order/
    message/
    user/
    agent/
    static/
  stores/
    auth.ts
    cart.ts
    app.ts
    user.ts
  styles/
    variables.scss
    global.scss
  types/
    domain.ts
  utils/
    navigation.ts
    feedback.ts
```

### Layer boundaries

- `pages/`: route-level screens only. Pages compose Vant and shared components, handle page-specific UI state, and call stores/mock data.
- `components/common/`: generic reusable UI wrappers, such as app page shell, section cards, empty states, copy rows, filter bars.
- `components/business/`: reusable domain widgets, such as product cards, merchant cards, order cards, hotel cards, cart popup, status tabs.
- `stores/`: shared state only. Avoid putting one-page temporary state in Pinia.
- `data/`: mock data shaped like future API responses so backend integration can replace data access later.
- `utils/`: small framework-agnostic helpers for navigation labels, copy feedback, formatting, and route builders.

## 5. Routing Design

Use route names and nested feature prefixes so docx page flows are easy to map.

### Main tab routes

- `/home` — 首页
- `/orders` — 我的订单
- `/messages` — 消息列表
- `/user` — 我的

### Auth routes

- `/auth/login/email`
- `/auth/login/phone`
- `/auth/register/phone`
- `/auth/register/email`
- `/auth/forgot/phone`
- `/auth/forgot/email`
- `/auth/oauth/google`
- `/auth/oauth/facebook`
- `/auth/oauth/line`

### Business routes

- `/products`
- `/merchant/:id`
- `/product/:id`
- `/checkout`
- `/order/:id`
- `/hotels`
- `/hotel/:id`
- `/hotel-booking/:id`
- `/hotel-order/:id`

### Account and support routes

- `/user/profile`
- `/user/recharge`
- `/user/withdraw`
- `/user/records/:type`
- `/user/payment`
- `/user/payment/edit/:id?`
- `/user/address`
- `/user/change-account`
- `/user/change-password`
- `/user/change-withdraw-password`
- `/user/real-info`
- `/agent`
- `/agent/quick-create-order`
- `/agent/pay-orders`
- `/agent/frozen-amounts`
- `/static/:type`

## 6. UI and Interaction Patterns

- Page shell: every non-tab page uses a consistent top nav with back behavior.
- Bottom tabs: Vant Tabbar for Home / Orders / Messages / User.
- Forms: Vant Form, Field, Button, Picker, Popup, DatePicker, Radio/Checkbox where needed.
- Lists: reusable list/card components; future infinite scroll can be added later.
- Popups: Vant Popup/Dialog/ActionSheet for language, country code, filters, cart, payment confirmation, share link, delete account confirmation.
- Feedback: Vant Toast/Notify for copy, submit success, placeholder interactions.
- Search/filter: maintain local filter state first; API query integration can replace it later.

## 7. Data Model Draft

Use simple mock domain types:

- `User`: id, nickname, avatar, phone, email, country, language, balance.
- `Merchant`: id, name, cover, rating, tags, address, products, comments.
- `Product`: id, merchantId, name, image, price, category, sales, description.
- `CartItem`: product, quantity.
- `Order`: id, type, status, merchant/hotel info, items, amount, address, createdAt.
- `Hotel`: id, name, cover, phone, address, rooms.
- `MessageThread`: id, title, avatar, lastMessage, unread, messages.
- `PaymentAccount`: id, type, accountName, accountNo, bankName.
- `AgentOrder`: id, status, productName, amount, payLink, proxyId.

## 8. Compatibility and Mobile Constraints

- Target mobile H5 browsers first.
- Use `viewport-fit=cover`, responsive width, and max-width container if desktop browser opens H5.
- Prefer CSS units and layout that adapt to 360–430px common mobile widths.
- Avoid browser APIs that require special permissions unless feature is explicitly mocked.
- Clipboard copy should use `navigator.clipboard` with fallback only if needed during implementation.

## 9. Risks and Mitigations

- Large page count: use route/page scaffolding plus reusable components to avoid duplicated layout code.
- Missing visual details: use a consistent mobile design system rather than guessing exact art direction.
- Missing backend contracts: keep mock data in one layer and avoid hardcoding data deep inside pages.
- Interaction ambiguity: implement documented navigation/popups first; mark unsupported real-world actions as mock feedback.
- Built artifact temptation: do not edit `delivra.top/`; only inspect if needed for naming/reference.

## 10. Rollout Shape

Recommended MVP rollout:

1. Project scaffold and design system foundation.
2. Route map and page skeletons for all docx pages.
3. Core flows: auth → home → product/merchant → cart → checkout → order detail.
4. Secondary flows: hotels, messages, user center, agent, static pages.
5. Final verification against `requirements_extracted.txt`.
