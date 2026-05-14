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
        <div>
          <strong>购物车</strong>
          <span>共 {{ count }} 件</span>
        </div>
        <van-button size="mini" plain @click="cart.clear()">清空</van-button>
      </header>
      <van-empty v-if="!items.length" description="购物车为空" />
      <van-cell v-for="item in items" :key="item.product.id" :title="item.product.name" :value="`¥${item.product.price}`">
        <template #icon>
          <van-image class="cart-popup__thumb" :src="item.product.image" radius="8" fit="cover" />
        </template>
        <template #label>
          <van-stepper :model-value="item.quantity" min="0" @plus="cart.add(item.product)" @minus="cart.decrease(item.product.id)" />
        </template>
      </van-cell>
      <footer>
        <span>¥{{ totalAmount.toFixed(2) }}</span>
        <van-button type="primary" round :disabled="!items.length" @click="emit('checkout')">去结算</van-button>
      </footer>
    </section>
  </van-popup>
</template>

<style scoped lang="scss">
.cart-popup {
  padding: 16px;
  background: linear-gradient(180deg, var(--app-primary-soft) 0%, #fff 82px);
}

header,
footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

header {
  margin-bottom: 8px;

  div {
    display: grid;
    gap: 2px;
  }

  strong {
    color: var(--app-text);
    font-size: 17px;
  }

  span {
    color: var(--app-muted);
    font-size: 12px;
  }
}

.cart-popup__thumb {
  width: 44px;
  height: 44px;
  margin-right: 10px;
  overflow: hidden;
}

:deep(.van-cell) {
  margin-top: 8px;
  border: 1px solid var(--app-border);
  border-radius: 12px;
  box-shadow: var(--app-shadow);
}

footer {
  margin-top: 12px;

  span {
    color: var(--app-primary);
    font-size: 20px;
    font-weight: 800;
  }
}
</style>
