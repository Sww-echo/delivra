<script setup lang="ts">
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const active = computed({
  get: () => String(route.name ?? 'home'),
  set: (name: string) => router.push({ name }),
})

const tabs = [
  { name: 'home', to: '/home', label: '首页', icon: '/delivra/icons/home.png', activeIcon: '/delivra/icons/home-selected.png' },
  { name: 'orders', to: '/orders', label: '订单', icon: '/delivra/icons/order-list.png', activeIcon: '/delivra/icons/order-list-selected.png' },
  { name: 'messages', to: '/messages', label: '消息', icon: '/delivra/icons/msg.png', activeIcon: '/delivra/icons/msg-selected.png' },
  { name: 'user', to: '/user', label: '我的', icon: '/delivra/icons/user.png', activeIcon: '/delivra/icons/user-selected.png' },
]
</script>

<template>
  <main class="tabbar-layout">
    <div class="tabbar-layout__content">
      <slot />
    </div>
    <van-tabbar v-model="active" route safe-area-inset-bottom>
      <van-tabbar-item v-for="tab in tabs" :key="tab.name" :name="tab.name" :to="tab.to">
        <template #icon="props">
          <img class="tabbar-layout__icon" :src="props.active ? tab.activeIcon : tab.icon" :alt="tab.label" />
        </template>
        {{ tab.label }}
      </van-tabbar-item>
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

.tabbar-layout__icon {
  width: 22px;
  height: 22px;
  object-fit: contain;
}
</style>
