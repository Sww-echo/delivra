# H5 scaffold and routing

## Goal

Create a new Vue 3 + Vite + TypeScript + Vant H5 project under `h5/`, establish the app shell, route table, mobile layout, and placeholder pages needed for the full requirements document.

## Requirements

- Create the H5 source project in `h5/`.
- Configure Vue 3, Vite, TypeScript, Vue Router, Vant, and Pinia.
- Add mobile viewport/global style foundation.
- Implement app entry, router, tabbar layout, and reusable page shell with back navigation.
- Define routes for auth, home, products, hotels, orders, messages, user center, agent, and static pages.
- Create placeholder pages for every route so documented navigation targets exist.
- Do not modify `delivra.top/` build artifacts.

## Acceptance Criteria

- [ ] `h5/` contains the new editable H5 source project.
- [ ] The project installs, starts, and builds successfully.
- [ ] Main tab routes exist: home, orders, messages, user.
- [ ] Non-tab route placeholders exist for all page groups in `design.md`.
- [ ] Basic navigation between placeholders works in browser.

## Notes

- Parent task: `.trellis/tasks/05-12-requirements-doc-review`.
- Source location decision: `h5/` subdirectory.
- This task must complete before feature-module implementation tasks.
