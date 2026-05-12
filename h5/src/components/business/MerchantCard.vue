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
    <van-image class="merchant-card__cover" :src="merchant.cover" radius="10" fit="cover" />
    <div class="merchant-card__body">
      <h3>{{ merchant.name }}</h3>
      <p>{{ merchant.address }}</p>
      <div class="merchant-card__tags">
        <van-tag v-for="tag in merchant.tags" :key="tag" plain type="primary">{{ tag }}</van-tag>
      </div>
    </div>
    <van-rate :model-value="merchant.rating" readonly allow-half size="12" />
  </div>
</template>

<style scoped lang="scss">
.merchant-card {
  display: flex;
  gap: 10px;
  border-radius: 12px;
  background: #fff;
  padding: 12px;
}

.merchant-card__cover {
  width: 76px;
  height: 76px;
  flex: none;
}

.merchant-card__body {
  flex: 1;
  min-width: 0;

  h3 {
    margin: 0 0 6px;
    font-size: 16px;
  }

  p {
    margin: 0 0 8px;
    color: var(--app-muted);
    font-size: 13px;
  }
}

.merchant-card__tags {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
}
</style>
