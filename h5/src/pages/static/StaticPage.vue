<script setup lang="ts">
import AppPage from '@/components/layout/AppPage.vue'
</script>

<template>
  <AppPage title="静态页面" :show-back="true">
    <div class="app-card">
      <h2>静态页面</h2>
      <p class="app-muted">页面占位，后续子任务补充完整交互。</p>
    </div>
    <van-cell-group inset class="placeholder-list">
      <van-cell title="帮助中心、公司资质、产品/服务介绍、退款政策、用户协议、隐私政策" />
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
