<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'
import { messageThreads } from '@/data/mockMessages'

const router = useRouter()
const showActions = ref(false)
const input = ref('')
const messages = ref([...messageThreads[0].messages])

function send() {
  if (!input.value.trim()) return
  messages.value.push({ id: String(Date.now()), sender: 'me', content: input.value, createdAt: '刚刚' })
  input.value = ''
}
</script>

<template>
  <AppPage title="聊天页">
    <div class="chat-list">
      <div v-for="message in messages" :key="message.id" class="chat-bubble" :class="message.sender">
        <span>{{ message.content }}</span>
        <small>{{ message.createdAt }}</small>
      </div>
    </div>
    <van-action-bar>
      <van-action-bar-icon icon="plus" text="更多" @click="showActions = true" />
      <van-field v-model="input" placeholder="请输入消息" class="chat-input" />
      <van-action-bar-button type="primary" text="发送" @click="send" />
    </van-action-bar>
    <van-action-sheet v-model:show="showActions" :actions="[{ name: '图片' }, { name: '拍照' }, { name: '设置' }]" @select="(action) => { showActions = false; action.name === '设置' ? router.push('/chat-settings') : showToast(`${action.name}待接入`) }" />
  </AppPage>
</template>

<style scoped lang="scss">
.chat-list { display: grid; gap: 10px; padding-bottom: 70px; }
.chat-bubble { display: grid; gap: 4px; max-width: 78%; border-radius: 12px; background: #fff; padding: 10px; }
.chat-bubble.me { justify-self: end; background: #e8f3ff; }
.chat-bubble small { color: var(--app-muted); }
.chat-input { min-width: 160px; }
</style>
