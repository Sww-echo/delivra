<script setup lang="ts">
import { useRouter } from 'vue-router'

withDefaults(
  defineProps<{
    title: string
    showBack?: boolean
  }>(),
  { showBack: true },
)

const router = useRouter()
</script>

<template>
  <section class="app-page">
    <van-nav-bar v-if="showBack" :title="title" left-arrow fixed placeholder @click-left="router.back()" />
    <van-nav-bar v-else :title="title" fixed placeholder />
    <div class="app-page__body">
      <slot />
    </div>
  </section>
</template>

<style scoped lang="scss">
.app-page {
  min-height: 100vh;
  background: var(--app-bg);
}

.app-page__body {
  padding: 12px;
}
</style>
