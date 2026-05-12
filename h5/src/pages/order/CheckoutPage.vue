<script setup lang="ts">
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import SectionCard from '@/components/common/SectionCard.vue'
import AppPage from '@/components/layout/AppPage.vue'
import { useCartStore } from '@/stores/cart'

const router = useRouter()
const cart = useCartStore()

function submitOrder() {
  showToast('订单提交成功')
  router.push('/order/D202605120001')
}
</script>

<template>
  <AppPage title="确认订单">
    <SectionCard title="收货地址">
      <van-cell title="中心商圈 88 号" label="Delivra 用户 13800000000" is-link @click="router.push('/user/address')" />
    </SectionCard>
    <SectionCard title="商品明细">
      <van-cell v-for="item in cart.items" :key="item.product.id" :title="item.product.name" :label="`x${item.quantity}`" :value="`¥${item.product.price}`" />
      <van-empty v-if="!cart.items.length" description="购物车为空，将提交示例订单" />
    </SectionCard>
    <van-submit-bar :price="(cart.totalAmount || 40) * 100" button-text="提交订单" @submit="submitOrder" />
  </AppPage>
</template>
