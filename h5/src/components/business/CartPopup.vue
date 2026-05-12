<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { useCartStore } from '@/stores/cart'

const visible = defineModel<boolean>({ required: true })
const emit = defineEmits<{
  checkout: []
}>()

const cart = useCartStore()
const { items, count, totalAmount } = storeToRefs(cart)
</script>

<template>
  <van-popup v-model:show="visible" round position="bottom" safe-area-inset-bottom>
    <section class="cart-popup">
      <header>
        <strong>购物车</strong>
        <van-button size="mini" plain @click="cart.clear()">清空</van-button>
      </header>
      <van-empty v-if="!items.length" description="购物车为空" />
      <van-cell v-for="item in items" :key="item.product.id" :title="item.product.name" :value="`¥${item.product.price}`">
        <template #label>
          <van-stepper :model-value="item.quantity" min="0" @plus="cart.add(item.product)" @minus="cart.decrease(item.product.id)" />
        </template>
      </van-cell>
      <footer>
        <span>共 {{ count }} 件，¥{{ totalAmount.toFixed(2) }}</span>
        <van-button type="primary" round :disabled="!items.length" @click="emit('checkout')">去结算</van-button>
      </footer>
    </section>
  </van-popup>
</template>

<style scoped lang="scss">
.cart-popup {
  padding: 16px;
}

header,
footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

footer {
  margin-top: 12px;
}
</style>
