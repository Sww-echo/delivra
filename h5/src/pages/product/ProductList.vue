<script setup lang="ts">
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import ProductCard from '@/components/business/ProductCard.vue'
import FilterBar from '@/components/common/FilterBar.vue'
import AppPage from '@/components/layout/AppPage.vue'
import { products } from '@/data/mockProducts'
import { useCartStore } from '@/stores/cart'

const router = useRouter()
const cart = useCartStore()
const keyword = ref('')
const filteredProducts = computed(() => products.filter((item) => item.name.includes(keyword.value)))
</script>

<template>
  <AppPage title="商品列表">
    <van-search v-model="keyword" placeholder="搜索商品" shape="round" />
    <FilterBar @sort="showToast('已按销量排序')" @filter="showToast('价格筛选待选择')" />
    <div class="card-list">
      <ProductCard v-for="product in filteredProducts" :key="product.id" :product="product" @click="router.push(`/merchant/${product.merchantId}`)" @add="cart.add" />
    </div>
  </AppPage>
</template>

<style scoped lang="scss">
.card-list { display: grid; gap: 10px; }
</style>
