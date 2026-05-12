# Research: H5 Mobile App Technology Stack

- **Query**: Research suitable technology stacks for building a mobile H5 app from scratch based on a large page-flow requirements doc. Compare 2-4 options such as Vue 3 + Vite + Vant, React + Vite + Ant Design Mobile, uni-app H5, and plain custom CSS. Consider Chinese/mobile H5 ecosystem, routing, mobile components, form/popup support, development speed, maintainability, and fit for this repo with no existing source.
- **Scope**: mixed
- **Date**: 2026-05-12

## Findings

### Files Found

| File Path | Description |
|---|---|
| `.trellis/spec/frontend/index.md` | Frontend guideline index; currently a template with status "To fill" for directory structure, components, hooks, state, quality, and type safety. |
| `.trellis/spec/frontend/directory-structure.md` | Frontend directory structure guide; currently placeholder content only. |
| `.trellis/spec/frontend/component-guidelines.md` | Component guideline document; currently placeholder content only. |
| `.trellis/spec/frontend/state-management.md` | State management guide; currently placeholder content only. |
| `delivra.top/delivra.top/assets/index-BUg3a9VG.js` | Built/minified existing H5 bundle artifact; contains Vue copyright markers and `vue-router v4.4.4` banner. |
| `delivra.top/delivra.top/assets/uni-app.es.D4Qqltdf.js` | Built uni-app runtime artifact. |
| `delivra.top/delivra.top/assets/uni-popup.OYh3Izn_.js` | Built uni-popup component artifact. |
| `delivra.top/delivra.top/assets/uni-popup-dialog.CH6hGMUw.js` | Built uni-popup dialog artifact. |
| `delivra.top/delivra.top/assets/uni-badge.EenAhifE.js` | Built uni-badge component artifact. |
| `delivra.top/delivra.top/assets/uni-icons.BhbChskQ.js` | Built uni-icons component artifact. |
| `delivra.top/delivra.top/assets/uni-rate.DJJquYW_.js` | Built uni-rate component artifact. |
| `delivra.top/delivra.top/assets/z-paging.D6NpLHz5.js` | Built z-paging artifact, commonly used in Chinese mobile list/pagination flows. |
| `delivra.top/delivra.top/assets/pages-*.js` | 29 built page chunks, indicating the checked-in artifact resembles a multi-page mobile flow rather than source code. |

No `package.json` files were found under the repository root, and package context reports a single repo with no packages configured.

### Code Patterns

- The repository currently has no editable frontend source tree detected by `package.json` discovery; it contains built artifacts under `delivra.top/` and placeholder Trellis frontend specs.
- Existing artifact evidence points to Vue/uni-app-style output:
  - `delivra.top/delivra.top/assets/index-BUg3a9VG.js:9` and `:15` include Vue copyright banners.
  - `delivra.top/delivra.top/assets/index-BUg3a9VG.js:21` includes `vue-router v4.4.4`.
  - `delivra.top/delivra.top/assets/uni-app.es.D4Qqltdf.js` exists as a built uni-app runtime artifact.
  - `delivra.top/delivra.top/assets/uni-popup*.js`, `uni-badge*.js`, `uni-icons*.js`, and `uni-rate*.js` indicate use of uni UI-style components in the artifact.
- Existing page-flow artifact names include common mobile H5 product/order/account screens: `pages-home-home`, `pages-merchant-merchant`, `pages-product_detail-product_detail`, `pages-order_list-order_list`, `pages-user-user`, `pages-user_address-user_address`, `pages-user_payment-user_payment`, `pages-agent_*`, etc.

### Stack Comparison

| Option | Chinese/mobile H5 ecosystem | Routing fit | Components/forms/popups | Development speed | Maintainability | Fit for this repo |
|---|---|---|---|---|---|---|
| Vue 3 + Vite + Vant | Strong fit. Vant is a Vue mobile UI library widely used in Chinese H5 projects. | Vue Router is mature for page-flow H5; existing artifact already shows `vue-router v4.4.4`. | Vant covers form controls, field validation patterns, dialogs, popups, action sheets, pickers, tabs, lists, pull refresh, etc. | Fast for a page-flow requirements doc because many mobile primitives are prebuilt and Vite scaffolding is minimal. | High if source is organized by pages/features; Vue SFCs are concise for visual page implementation. | Strong fit: no existing source means this can be started cleanly, while the checked-in artifacts suggest Vue familiarity/compatibility. |
| React + Vite + Ant Design Mobile | Strong general ecosystem; Ant Design Mobile is a mature React mobile component library with Chinese ecosystem roots. | React Router is mature, but no React evidence exists in this repo. | Ant Design Mobile covers forms, dialogs, popups, selectors, tabs, lists, infinite scroll, etc. | Fast if the team prefers React; otherwise slightly more setup/boilerplate than Vue for template-heavy mobile pages. | High in React teams; TypeScript patterns are strong. | Viable from scratch, but less aligned with existing artifact evidence than Vue/uni-app. |
| uni-app H5 | Very strong in Chinese cross-platform/mobile ecosystem; supports H5 plus mini-program/app targets. Existing artifacts include uni-app runtime and uni components. | uni-app page routing is convention/config driven and matches multi-page app flows; H5 output can also integrate Vue under the hood. | uni UI plus third-party components cover popups, badges, icons, forms, paging; existing artifact includes `uni-popup`, `uni-badge`, `uni-icons`, `uni-rate`, and `z-paging`. | Fast for mobile page-flow CRUD/list/order apps, especially if cross-platform deployment is desired. | Medium to high: maintainability is good when staying within uni-app conventions, but framework-specific APIs can be less portable than plain Vue + Vite. | Strong fit if the target is H5 now and possible mini-program/app later; strongest match to checked-in artifact names. |
| Plain custom CSS + vanilla JS or minimal framework | Universal and dependency-light, but no specialized Chinese mobile H5 component ecosystem. | Manual routing or lightweight router required; large page-flow requirements make this more work. | Forms/popups/lists/pickers/loading/toasts must be custom-built or assembled from small libraries. | Slow for large mobile page-flow docs because common mobile interactions are repeated manually. | Lower for a large app unless strict internal conventions are established early. | Possible because there is no existing source, but least supported by current artifact evidence and component needs. |

### External References

- [Vite docs](https://vite.dev) — npm metadata reports `vite` version `8.0.12`, described as "Native-ESM powered web dev build tool"; relevant as the build/scaffold layer for Vue or React H5.
- [Vant GitHub/readme](https://github.com/vant-ui/vant#readme) — npm metadata reports `vant` version `4.9.24`, described as "Mobile UI Components built on Vue"; relevant for Vue mobile forms, popups, lists, and H5 UI.
- [Ant Design Mobile GitHub/readme](https://github.com/ant-design/ant-design-mobile#readme) — npm metadata reports `antd-mobile` version `5.42.3`; relevant for React mobile forms, popups, selectors, lists, and dialogs.
- [uni-app GitHub/readme](https://github.com/dcloudio/uni-app#readme) — npm metadata for `@dcloudio/vite-plugin-uni` points to the uni-app repository; relevant for H5 output and possible multi-end Chinese mobile delivery.

### Related Specs

- `.trellis/spec/frontend/index.md` — frontend documentation index; states frontend docs are currently "To fill".
- `.trellis/spec/frontend/directory-structure.md` — intended place for source layout conventions; currently no project-specific frontend structure documented.
- `.trellis/spec/frontend/component-guidelines.md` — intended place for component conventions; currently no project-specific UI/component conventions documented.
- `.trellis/spec/frontend/state-management.md` — intended place for state conventions; currently no project-specific state approach documented.

## Caveats / Not Found

- No editable app source or `package.json` was found, so internal evidence comes from built/minified artifacts and Trellis placeholder specs only.
- The existing `delivra.top/` artifacts indicate Vue/uni-app-related output, but built files do not prove the desired future stack unless the original source/tooling is recovered.
- External package details were checked through npm metadata available from the local environment; this research did not inspect full online documentation pages beyond package metadata URLs.
