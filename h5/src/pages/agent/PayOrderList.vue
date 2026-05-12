<script setup lang="ts">
import { ref } from 'vue'
import StatusTabs from '@/components/common/StatusTabs.vue'
import AppPage from '@/components/layout/AppPage.vue'
import { agentOrders } from '@/data/mockUser'
import { copyText } from '@/utils/feedback'

const active = ref('all')
const options = [{ label: '全部', value: 'all' }, { label: '待支付', value: 'pending' }, { label: '已支付', value: 'paid' }]
</script>

<template>
  <AppPage title="代付订单列表">
    <StatusTabs v-model="active" :options="options" />
    <van-cell-group inset class="order-list">
      <van-cell v-for="order in agentOrders" :key="order.id" :title="order.productName" :label="`金额 ¥${order.amount}`" is-link to="/product/p1">
        <template #right-icon>
          <van-button size="mini" @click.stop="copyText(order.id, '订单号已复制')">复制</van-button>
        </template>
      </van-cell>
    </van-cell-group>
  </AppPage>
</template>

<style scoped lang="scss">
.order-list { margin-top: 12px; }
</style>
