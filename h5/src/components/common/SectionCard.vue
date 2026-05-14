<script setup lang="ts">
defineProps<{
  title?: string
  extra?: string
}>()
</script>

<template>
  <section class="section-card">
    <div v-if="title || extra" class="section-card__header">
      <h3 v-if="title">{{ title }}</h3>
      <span v-if="extra">{{ extra }}</span>
    </div>
    <slot />
  </section>
</template>

<style scoped lang="scss">
.section-card {
  border: 1px solid var(--app-border);
  border-radius: var(--app-radius-lg);
  background: #fff;
  padding: 14px;
  box-shadow: var(--app-shadow);
}

.section-card + .section-card {
  margin-top: 12px;
}

.section-card__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;

  h3 {
    position: relative;
    margin: 0;
    padding-left: 10px;
    color: var(--app-text);
    font-size: 16px;
    line-height: 1.2;
  }

  h3::before {
    position: absolute;
    top: 2px;
    bottom: 2px;
    left: 0;
    width: 4px;
    border-radius: 999px;
    background: var(--app-primary);
    content: '';
  }

  span {
    color: var(--app-muted);
    font-size: 13px;
  }
}
</style>
