<script setup lang="ts">
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import OrderCard from '@/components/business/OrderCard.vue'
import StatusTabs from '@/components/common/StatusTabs.vue'
import AppPage from '@/components/layout/AppPage.vue'
import { orders } from '@/data/mockOrders'
import { copyText } from '@/utils/feedback'

const router = useRouter()
const active = ref('all')
const options = [
  { label: '全部', value: 'all' },
  { label: '待支付', value: 'pending' },
  { label: '已支付', value: 'paid' },
  { label: '已完成', value: 'completed' },
]
const list = computed(() => active.value === 'all' ? orders : orders.filter((item) => item.status === active.value))
</script>

<template>
  <AppPage title="我的订单" :show-back="false">
    <StatusTabs v-model="active" :options="options" />
    <div class="card-list">
      <OrderCard v-for="order in list" :key="order.id" :order="order" @click="router.push(`/order/${order.id}`)" @copy="copyText(order.id, '订单号已复制')" />
    </div>
    <van-cell-group inset class="action-list">
      <van-cell title="支付凭证" is-link @click="showToast('支付凭证弹窗')" />
      <van-cell title="发货详情" is-link @click="showToast('发货详情弹窗')" />
      <van-cell title="去评价" is-link @click="router.push('/review/D202605120001')" />
    </van-cell-group>
  </AppPage>
</template>

<style scoped lang="scss">
.card-list { display: grid; gap: 10px; padding: 12px 0; }
.action-list { margin-top: 12px; }
</style>
