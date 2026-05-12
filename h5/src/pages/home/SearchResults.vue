<script setup lang="ts">
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import ProductCard from '@/components/business/ProductCard.vue'
import AppPage from '@/components/layout/AppPage.vue'
import { products } from '@/data/mockProducts'
import { useCartStore } from '@/stores/cart'

const route = useRoute()
const router = useRouter()
const cart = useCartStore()
const keyword = computed(() => String(route.query.q || ''))
const results = computed(() => products.filter((item) => !keyword.value || item.name.includes(keyword.value)))
</script>

<template>
  <AppPage title="搜索结果">
    <van-cell :title="`关键词：${keyword || '全部'}`" />
    <ProductCard v-for="product in results" :key="product.id" :product="product" @click="router.push(`/product/${product.id}`)" @add="cart.add" />
  </AppPage>
</template>
