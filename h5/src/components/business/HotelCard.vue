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
    <van-image class="hotel-card__cover" :src="hotel.cover" radius="10" fit="cover" />
    <div class="hotel-card__body">
      <h3>{{ hotel.name }}</h3>
      <p>{{ hotel.address }}</p>
      <span>¥{{ hotel.rooms[0]?.price || 0 }} 起</span>
    </div>
  </div>
</template>

<style scoped lang="scss">
.hotel-card {
  display: flex;
  gap: 10px;
  border-radius: 12px;
  background: #fff;
  padding: 12px;
}

.hotel-card__cover {
  width: 92px;
  height: 72px;
  flex: none;
}

.hotel-card__body {
  flex: 1;

  h3 {
    margin: 0 0 6px;
    font-size: 16px;
  }

  p {
    margin: 0 0 8px;
    color: var(--app-muted);
    font-size: 13px;
  }

  span {
    color: #ee0a24;
    font-weight: 600;
  }
}
</style>
