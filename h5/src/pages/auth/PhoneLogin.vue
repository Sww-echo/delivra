<script setup lang="ts">
import AppPage from '@/components/layout/AppPage.vue'
</script>

<template>
  <AppPage title="手机号登录" :show-back="true">
    <div class="app-card">
      <h2>手机号登录</h2>
      <p class="app-muted">页面占位，后续子任务补充完整交互。</p>
    </div>
    <van-cell-group inset class="placeholder-list">
      <van-cell title="登录 -> 首页" />
      <van-cell title="邮箱 -> 邮箱登录页" />
      <van-cell title="国家/区号 -> 国家区号选择控件" />
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
