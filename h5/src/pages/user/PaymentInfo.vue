<script setup lang="ts">
import AppPage from '@/components/layout/AppPage.vue'
</script>

<template>
  <AppPage title="收款信息" :show-back="true">
    <div class="app-card">
      <h2>收款信息</h2>
      <p class="app-muted">页面占位，后续子任务补充完整交互。</p>
    </div>
    <van-cell-group inset class="placeholder-list">
      <van-cell title="删除、修改、添加收款" />
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
