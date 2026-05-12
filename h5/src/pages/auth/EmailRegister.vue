<script setup lang="ts">
import AppPage from '@/components/layout/AppPage.vue'
</script>

<template>
  <AppPage title="邮箱注册" :show-back="true">
    <div class="app-card">
      <h2>邮箱注册</h2>
      <p class="app-muted">页面占位，后续子任务补充完整交互。</p>
    </div>
    <van-cell-group inset class="placeholder-list">
      <van-cell title="注册 -> 完成邮箱账号注册" />
      <van-cell title="手机号 -> 手机号注册页" />
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
