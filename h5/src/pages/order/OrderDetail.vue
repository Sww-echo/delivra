<script setup lang="ts">
import AppPage from '@/components/layout/AppPage.vue'
</script>

<template>
  <AppPage title="订单详情" :show-back="true">
    <div class="app-card">
      <h2>订单详情</h2>
      <p class="app-muted">页面占位，后续子任务补充完整交互。</p>
    </div>
    <van-cell-group inset class="placeholder-list">
      <van-cell title="状态、复制订单号、联系商家、修改地址、支付、代付、取消" />
    </van-cell-group>
  </AppPage>
</template>

<style scoped lang="scss">
h2 {
  margin: 0 0 8px;
  font-size: 20px;
}

.placeholder-list {
  margin-top: 12px;
}
</style>
