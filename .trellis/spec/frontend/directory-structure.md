# Directory Structure

> How frontend code is organized in this project.

---

## Overview

The H5 frontend lives in `h5/` and uses Vue 3 + Vite + Vant. Source code belongs under `h5/src/`; static files that must be served by stable public URLs belong under `h5/public/`.

---

## Directory Layout

```
h5/
├── public/
│   └── delivra/        # curated copied visual assets served as /delivra/...
└── src/
    ├── app/            # Vue app entry and router
    ├── components/     # shared layout, common, and business components
    ├── data/           # mock data and public asset path references
    ├── pages/          # route pages grouped by domain
    ├── stores/         # Pinia stores
    ├── styles/         # global theme tokens and shared overrides
    ├── types/          # domain types
    └── utils/          # frontend utilities
```

---

## Module Organization

<!-- How should new features be organized? -->

(To be filled by the team)

---

## Naming Conventions

<!-- File and folder naming rules -->

(To be filled by the team)

---

## Examples

### Public Delivra visual assets

Copied assets from the compiled `delivra.top/` reference output must be curated and placed under `h5/public/delivra/`. Reference them with stable public URLs such as `/delivra/icons/home.png` or `/delivra/products/coffee.jpeg`.

Do not reference sibling filesystem paths like `../delivra.top/...` from H5 source code; those paths are not stable for Vite builds or deployment.
