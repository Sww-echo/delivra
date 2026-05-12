<script setup lang="ts">
import AppPage from '@/components/layout/AppPage.vue'
import { agentOrders } from '@/data/mockUser'
import { copyText } from '@/utils/feedback'
</script>

<template>
  <AppPage title="冻结金额明细">
    <van-cell-group inset>
      <van-cell v-for="order in agentOrders" :key="order.id" :title="order.productName" :label="`冻结金额 ¥${order.amount}`" is-link to="/product/p1">
        <template #right-icon>
          <div class="actions">
            <van-button size="mini" @click.stop="copyText(order.payLink, '代付链接已复制')">链接</van-button>
            <van-button size="mini" @click.stop="copyText(order.id, '订单号已复制')">单号</van-button>
            <van-button size="mini" @click.stop="copyText(order.proxyId, '代付ID已复制')">ID</van-button>
          </div>
        </template>
      </van-cell>
    </van-cell-group>
  </AppPage>
</template>

<style scoped lang="scss">
.actions { display: flex; gap: 4px; }
</style>
