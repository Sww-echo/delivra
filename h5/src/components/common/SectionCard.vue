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
  border-radius: 12px;
  background: #fff;
  padding: 14px;
  box-shadow: 0 6px 18px rgb(31 41 51 / 6%);
}

.section-card + .section-card {
  margin-top: 12px;
}

.section-card__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;

  h3 {
    margin: 0;
    font-size: 16px;
  }

  span {
    color: var(--app-muted);
    font-size: 13px;
  }
}
</style>
