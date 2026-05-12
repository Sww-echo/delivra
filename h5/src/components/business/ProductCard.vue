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
    :title="product.name"
    :desc="product.description"
    :thumb="product.image"
    :price="product.price"
    :tag="product.category"
    @click="emit('click', product)"
  >
    <template #footer>
      <van-button size="mini" type="primary" @click.stop="emit('add', product)">+</van-button>
    </template>
  </van-card>
</template>
