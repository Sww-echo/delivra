<script setup lang="ts">
import type { Hotel } from '@/types/domain'

defineProps<{
  hotel: Hotel
}>()

const emit = defineEmits<{
  click: [Hotel]
}>()
</script>

<template>
  <div class="hotel-card" @click="emit('click', hotel)">
    <van-image class="hotel-card__cover" :src="hotel.cover" radius="12" fit="cover" />
    <div class="hotel-card__body">
      <h3>{{ hotel.name }}</h3>
      <p>{{ hotel.address }}</p>
      <div class="hotel-card__meta">
        <van-rate :model-value="hotel.rating" readonly allow-half size="12" color="#ff9500" void-color="#e5e7eb" />
        <span>¥{{ hotel.rooms[0]?.price || 0 }} 起</span>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.hotel-card {
  display: flex;
  gap: 10px;
  border: 1px solid var(--app-border);
  border-radius: var(--app-radius-lg);
  background: #fff;
  padding: 10px;
  box-shadow: var(--app-shadow);
}

.hotel-card__cover {
  width: 94px;
  height: 74px;
  flex: none;
  overflow: hidden;
  background: var(--app-primary-soft);
}

.hotel-card__body {
  flex: 1;
  min-width: 0;

  h3 {
    margin: 0 0 6px;
    color: var(--app-text);
    font-size: 16px;
  }

  p {
    margin: 0 0 8px;
    color: var(--app-muted);
    font-size: 13px;
    line-height: 1.4;
  }
}

.hotel-card__meta {
  display: flex;
  align-items: center;
  justify-content: space-between;

  span {
    color: var(--app-primary);
    font-weight: 700;
  }
}
</style>
