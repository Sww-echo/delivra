<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'

const router = useRouter()
const amount = ref('100')
</script>

<template>
  <AppPage title="充值">
    <van-field v-model="amount" label="充值金额" type="number" placeholder="请输入金额" />
    <van-button block round type="primary" @click="showToast('充值成功')">确认充值</van-button>
    <van-cell-group inset class="link-list">
      <van-cell title="充值记录" is-link @click="router.push('/user/records/recharge')" />
    </van-cell-group>
  </AppPage>
</template>

<style scoped lang="scss">
.link-list { margin-top: 12px; }
</style>
