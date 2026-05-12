<script setup lang="ts">
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import AppPage from '@/components/layout/AppPage.vue'

const route = useRoute()
const router = useRouter()
const provider = computed(() => String(route.params.provider || '第三方'))
</script>

<template>
  <AppPage :title="`${provider} 登录`">
    <div class="app-card oauth-card">
      <h2>{{ provider }} 登录页</h2>
      <p class="app-muted">第三方登录暂以占位方式展示。</p>
      <van-button block round type="primary" @click="router.push('/home')">模拟登录成功</van-button>
    </div>
  </AppPage>
</template>

<style scoped lang="scss">
.oauth-card { display: grid; gap: 12px; }
h2 { margin: 0; }
</style>
