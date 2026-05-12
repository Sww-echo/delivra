<script setup lang="ts">
import { useRouter } from 'vue-router'
import AppPage from '@/components/layout/AppPage.vue'

const router = useRouter()
</script>

<template>
  <AppPage title="代理">
    <van-grid :column-num="1">
      <van-grid-item icon="add-o" text="快速创建订单" @click="router.push('/agent/quick-create-order')" />
      <van-grid-item icon="orders-o" text="代付订单列表" @click="router.push('/agent/pay-orders')" />
      <van-grid-item icon="balance-list-o" text="冻结金额" @click="router.push('/agent/frozen-amounts')" />
    </van-grid>
  </AppPage>
</template>
