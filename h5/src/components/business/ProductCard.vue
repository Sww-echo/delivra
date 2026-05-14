<script setup lang="ts">
import type { Product } from '@/types/domain'

defineProps<{
  product: Product
}>()

const emit = defineEmits<{
  click: [Product]
  add: [Product]
}>()
</script>

<template>
  <van-card
    class="product-card"
    :title="product.name"
    :desc="product.description"
    :thumb="product.image"
    :price="product.price"
    :tag="product.category"
    @click="emit('click', product)"
  >
    <template #tags>
      <span class="product-card__sales">已售 {{ product.sales }}</span>
    </template>
    <template #footer>
      <van-button class="product-card__add" size="mini" type="primary" round @click.stop="emit('add', product)">+</van-button>
    </template>
  </van-card>
</template>

<style scoped lang="scss">
.product-card {
  margin: 0;
  padding: 10px;

  :deep(.van-card__thumb) {
    width: 88px;
    height: 88px;
    overflow: hidden;
    border-radius: 12px;
  }

  :deep(.van-card__title) {
    color: var(--app-text);
    font-size: 15px;
    font-weight: 700;
  }

  :deep(.van-card__desc) {
    color: var(--app-muted);
    line-height: 1.45;
  }

  :deep(.van-card__price) {
    color: var(--app-primary);
    font-weight: 700;
  }
}

.product-card__sales {
  color: var(--app-muted);
  font-size: 12px;
}

.product-card__add {
  min-width: 28px;
  height: 28px;
  padding: 0;
  font-size: 18px;
  line-height: 1;
}
</style>
