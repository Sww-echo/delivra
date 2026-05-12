<script setup lang="ts">
import { useRouter } from 'vue-router'
import AppPage from '@/components/layout/AppPage.vue'
import { messageThreads } from '@/data/mockMessages'

const router = useRouter()
</script>

<template>
  <AppPage title="消息列表" :show-back="false">
    <van-cell-group inset>
      <van-cell v-for="thread in messageThreads" :key="thread.id" :title="thread.title" :label="thread.lastMessage" is-link @click="router.push(`/chat/${thread.id}`)">
        <template #icon>
          <van-image :src="thread.avatar" width="40" height="40" round class="thread-avatar" />
        </template>
        <template #right-icon>
          <van-badge :content="thread.unread" />
        </template>
      </van-cell>
      <van-cell title="聊天背景设置" is-link @click="router.push('/chat-settings')" />
    </van-cell-group>
  </AppPage>
</template>

<style scoped lang="scss">
.thread-avatar { margin-right: 10px; }
</style>
