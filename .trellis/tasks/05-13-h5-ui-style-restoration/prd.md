# Restore H5 visual style from built assets

## Goal

Restore the `h5/` mock MVP visual style using reusable references from the compiled `delivra.top/` assets, focusing on a high-impact first pass rather than pixel-perfect reproduction.

## Requirements

- Do not modify `delivra.top/`; treat it as compiled reference output only.
- Copy only a small curated set of image/icon assets into `h5/public/delivra/` for stable Vite serving.
- Change the H5 theme from generic Vant blue to the original orange/gray visual direction found in the compiled assets.
- Replace bottom tabbar generic icons with copied Delivra PNG icons.
- Polish shared cards, business cards, cart popup, home page, and user center with extracted color, radius, spacing, and shadow patterns.
- Replace a curated subset of mock image URLs with local copied Delivra assets.
- Avoid new business logic, backend/API work, or pixel-perfect source reconstruction.

## Acceptance Criteria

- [x] Selected static assets are copied into `h5/public/delivra/` and referenced by stable public paths.
- [x] Global theme tokens and Vant primary styling use the Delivra orange/gray palette.
- [x] Tabbar, shared cards, business cards, home page, user center, and cart popup visibly match the compiled asset direction more closely.
- [x] Mock product/user/category imagery uses selected local Delivra assets where practical.
- [x] `npm run typecheck --prefix h5` passes.
- [x] `npm run build --prefix h5` passes.
- [ ] Key mobile routes are manually reviewed for broken images, overflow, and obvious visual regressions.

## Notes

- Approved approach: copy a small curated asset subset, not the entire compiled tree.
- Visual target tokens come from `.trellis/tasks/05-13-h5-built-style-reference/style-findings.md`.
