<script setup lang="ts">
import { computed, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import CartPopup from '@/components/business/CartPopup.vue'
import AppPage from '@/components/layout/AppPage.vue'
import { products } from '@/data/mockProducts'
import { useCartStore } from '@/stores/cart'

const route = useRoute()
const router = useRouter()
const cart = useCartStore()
const showCart = ref(false)
const product = computed(() => products.find((item) => item.id === route.params.id) || products[0])
</script>

<template>
  <AppPage :title="product.name">
    <van-image :src="product.image" width="100%" height="220" fit="cover" />
    <div class="app-card detail-card">
      <h2>{{ product.name }}</h2>
      <p class="price">¥{{ product.price }}</p>
      <p class="app-muted">{{ product.description }}</p>
      <van-button block plain type="primary" @click="router.push('/comments')">查看更多评价</van-button>
    </div>
    <van-action-bar>
      <van-action-bar-icon icon="cart-o" :badge="cart.count || undefined" text="购物车" @click="showCart = true" />
      <van-action-bar-button color="var(--app-primary)" text="加入购物车" @click="cart.add(product)" />
      <van-action-bar-button color="linear-gradient(135deg, #ff9500, var(--app-primary))" text="去结算" @click="router.push('/checkout')" />
    </van-action-bar>
    <CartPopup v-model="showCart" @checkout="router.push('/checkout')" />
  </AppPage>
</template>

<style scoped lang="scss">
.detail-card { margin-top: 12px; }
h2 { margin: 0 0 8px; }
.price { color: var(--app-primary); font-size: 22px; font-weight: 700; }
</style>
