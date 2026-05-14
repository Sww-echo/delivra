<script setup lang="ts">
import type { Order } from '@/types/domain'

defineProps<{
  order: Order
}>()

const emit = defineEmits<{
  click: [Order]
  copy: [Order]
}>()

const statusText: Record<Order['status'], string> = {
  pending: '待支付',
  paid: '已支付',
  shipping: '配送中',
  completed: '已完成',
  cancelled: '已取消',
}
</script>

<template>
  <section class="order-card" @click="emit('click', order)">
    <div class="order-card__header">
      <strong>{{ order.title }}</strong>
      <van-tag type="primary">{{ statusText[order.status] }}</van-tag>
    </div>
    <p>订单号：{{ order.id }}</p>
    <p>金额：<span>¥{{ order.amount.toFixed(2) }}</span></p>
    <van-button size="mini" plain type="primary" @click.stop="emit('copy', order)">复制</van-button>
  </section>
</template>

<style scoped lang="scss">
.order-card {
  border: 1px solid var(--app-border);
  border-radius: var(--app-radius-lg);
  background: #fff;
  padding: 12px;
  box-shadow: var(--app-shadow);
}

.order-card__header {
  display: flex;
  align-items: center;
  justify-content: space-between;

  strong {
    color: var(--app-text);
    font-size: 15px;
  }
}

p {
  margin: 8px 0 0;
  color: var(--app-muted);
  font-size: 13px;

  span {
    color: var(--app-primary);
    font-weight: 700;
  }
}

.van-button {
  margin-top: 10px;
}
</style>
