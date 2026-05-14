# Component Guidelines

> How components are built in this project.

---

## Overview

<!--
Document your project's component conventions here.

Questions to answer:
- What component patterns do you use?
- How are props defined?
- How do you handle composition?
- What accessibility standards apply?
-->

(To be filled by the team)

---

## Component Structure

<!-- Standard structure of a component file -->

(To be filled by the team)

---

## Props Conventions

<!-- How props should be defined and typed -->

(To be filled by the team)

---

## Styling Patterns

### Convention: H5 theme tokens

**What**: Shared H5 visual tokens and conservative Vant overrides live in `h5/src/styles/global.scss`.

**Why**: Keeping brand colors, radius, shadows, and Vant primary styling in one file prevents blue/orange drift across pages and components.

**Example**:
```scss
:root {
  --app-primary: #ff6b00;
  --app-bg: #f9fafb;
  --app-card-bg: #ffffff;
  --app-border: #eef0f3;
}
```

Use component-scoped styles for layout-specific polish, but read the global tokens before adding hard-coded colors.

### Convention: Compiled assets are visual references only

**What**: `delivra.top/` is compiled uni-app output. Use its CSS chunks for visual tokens and layout hints, not as source code to copy directly.

**Why**: Compiled selectors contain generated `data-v-*` scopes and minified structure that do not map cleanly to the Vue/Vant H5 source.

**Correct**:
```scss
.card {
  border-radius: var(--app-radius-lg);
  box-shadow: var(--app-shadow);
}
```

**Wrong**:
```scss
.container .userInfo[data-v-20f33b5a] {
  /* copied directly from compiled output */
}
```

---

## Accessibility

<!-- A11y requirements and patterns -->

(To be filled by the team)

---

## Common Mistakes

<!-- Component-related mistakes your team has made -->

(To be filled by the team)
