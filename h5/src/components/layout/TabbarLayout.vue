<script setup lang="ts">
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const active = computed({
  get: () => String(route.name ?? 'home'),
  set: (name: string) => router.push({ name }),
})
</script>

<template>
  <main class="tabbar-layout">
    <div class="tabbar-layout__content">
      <slot />
    </div>
    <van-tabbar v-model="active" route safe-area-inset-bottom>
      <van-tabbar-item name="home" to="/home" icon="home-o">首页</van-tabbar-item>
      <van-tabbar-item name="orders" to="/orders" icon="orders-o">订单</van-tabbar-item>
      <van-tabbar-item name="messages" to="/messages" icon="chat-o">消息</van-tabbar-item>
      <van-tabbar-item name="user" to="/user" icon="user-o">我的</van-tabbar-item>
    </van-tabbar>
  </main>
</template>

<style scoped lang="scss">
.tabbar-layout {
  min-height: 100vh;
  background: var(--app-bg);
}

.tabbar-layout__content {
  min-height: calc(100vh - 50px - env(safe-area-inset-bottom));
  padding-bottom: calc(66px + env(safe-area-inset-bottom));
}
</style>
