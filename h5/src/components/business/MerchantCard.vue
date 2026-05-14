<script setup lang="ts">
import type { Merchant } from '@/types/domain'

defineProps<{
  merchant: Merchant
}>()

const emit = defineEmits<{
  click: [Merchant]
}>()
</script>

<template>
  <div class="merchant-card" @click="emit('click', merchant)">
    <van-image class="merchant-card__cover" :src="merchant.cover" radius="12" fit="cover" />
    <div class="merchant-card__body">
      <div class="merchant-card__title-row">
        <h3>{{ merchant.name }}</h3>
        <van-rate :model-value="merchant.rating" readonly allow-half size="12" color="#ff9500" void-color="#e5e7eb" />
      </div>
      <p>{{ merchant.address }}</p>
      <div class="merchant-card__tags">
        <van-tag v-for="tag in merchant.tags" :key="tag" plain type="primary">{{ tag }}</van-tag>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.merchant-card {
  display: flex;
  gap: 10px;
  border: 1px solid var(--app-border);
  border-radius: var(--app-radius-lg);
  background: #fff;
  padding: 10px;
  box-shadow: var(--app-shadow);
}

.merchant-card__cover {
  width: 78px;
  height: 78px;
  flex: none;
  overflow: hidden;
  background: var(--app-primary-soft);
}

.merchant-card__body {
  flex: 1;
  min-width: 0;
}

.merchant-card__title-row {
  display: flex;
  gap: 8px;
  align-items: flex-start;
  justify-content: space-between;

  h3 {
    margin: 0 0 6px;
    color: var(--app-text);
    font-size: 16px;
    line-height: 1.25;
  }
}

p {
  margin: 0 0 8px;
  color: var(--app-muted);
  font-size: 13px;
  line-height: 1.4;
}

.merchant-card__tags {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
}
</style>
