<script setup lang="ts">
import { computed, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { showToast } from 'vant'
import CartPopup from '@/components/business/CartPopup.vue'
import ProductCard from '@/components/business/ProductCard.vue'
import AppPage from '@/components/layout/AppPage.vue'
import { merchants } from '@/data/mockProducts'
import { useCartStore } from '@/stores/cart'

const route = useRoute()
const router = useRouter()
const cart = useCartStore()
const activeTab = ref('menu')
const showCart = ref(false)
const merchant = computed(() => merchants.find((item) => item.id === route.params.id) || merchants[0])
const categories = computed(() => [...new Set(merchant.value.products.map((item) => item.category))])
const activeCategory = ref('')
const visibleProducts = computed(() => merchant.value.products.filter((item) => !activeCategory.value || item.category === activeCategory.value))
</script>

<template>
  <AppPage :title="merchant.name">
    <div class="app-card merchant-hero">
      <van-image :src="merchant.cover" width="72" height="72" radius="12" />
      <div>
        <h2>{{ merchant.name }}</h2>
        <p class="app-muted">{{ merchant.address }}</p>
        <van-button size="small" icon="chat-o" @click="router.push('/chat/' + merchant.id)">联系商家</van-button>
      </div>
    </div>
    <van-tabs v-model:active="activeTab">
      <van-tab title="点菜" name="menu">
        <van-tabs v-model:active="activeCategory" class="category-tabs" shrink>
          <van-tab title="全部" name="" />
          <van-tab v-for="category in categories" :key="category" :title="category" :name="category" />
        </van-tabs>
        <ProductCard v-for="product in visibleProducts" :key="product.id" :product="product" @click="router.push(`/product/${product.id}`)" @add="cart.add" />
      </van-tab>
      <van-tab title="评价" name="comments">
        <van-cell v-for="comment in merchant.comments" :key="comment" :title="comment" />
        <van-button block @click="showToast('评价筛选待接入')">筛选</van-button>
      </van-tab>
    </van-tabs>
    <van-submit-bar :price="cart.totalAmount * 100" button-text="去结算" @submit="router.push('/checkout')">
      <van-button size="small" round @click="showCart = true">购物车 {{ cart.count }}</van-button>
    </van-submit-bar>
    <CartPopup v-model="showCart" @checkout="router.push('/checkout')" />
  </AppPage>
</template>

<style scoped lang="scss">
.merchant-hero { display: flex; gap: 12px; margin-bottom: 12px; }
h2 { margin: 0 0 4px; font-size: 18px; }
.category-tabs { margin-bottom: 8px; }
</style>
