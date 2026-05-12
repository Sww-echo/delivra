<script setup lang="ts">
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { showToast } from 'vant'
import OrderCard from '@/components/business/OrderCard.vue'
import SectionCard from '@/components/common/SectionCard.vue'
import AppPage from '@/components/layout/AppPage.vue'
import { orders } from '@/data/mockOrders'
import { copyText, showConfirmDialog } from '@/utils/feedback'

const route = useRoute()
const router = useRouter()
const order = computed(() => orders.find((item) => item.id === route.params.id) || orders[0])

function confirmPayment() {
  void showConfirmDialog(`确认支付 ¥${order.value.amount}？`, '确认金额')
}

function cancelOrder() {
  void showConfirmDialog('确认取消当前订单？', '取消订单')
}
</script>

<template>
  <AppPage title="订单详情">
    <OrderCard :order="order" @copy="copyText(order.id, '订单号已复制')" />
    <SectionCard title="订单操作">
      <van-cell title="商家信息" is-link @click="router.push('/merchant/m1')" />
      <van-cell title="联系商家" is-link @click="router.push('/chat/m1')" />
      <van-cell title="修改收货地址" is-link @click="router.push('/user/address')" />
      <van-cell title="支付订单" is-link @click="confirmPayment" />
      <van-cell title="找人代付" is-link @click="showToast('代付链接弹窗待生成')" />
      <van-cell title="取消订单" is-link @click="cancelOrder" />
    </SectionCard>
  </AppPage>
</template>
