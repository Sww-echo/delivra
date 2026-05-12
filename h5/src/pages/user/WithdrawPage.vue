<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'
import { currentUser } from '@/data/mockUser'

const router = useRouter()
const amount = ref('')
</script>

<template>
  <AppPage title="提现">
    <van-field v-model="amount" label="提现金额" type="number" placeholder="请输入金额" />
    <van-button block plain type="primary" @click="amount = String(currentUser.balance)">全部提现</van-button>
    <van-button block round type="primary" @click="showToast('提现申请已提交')">确认提现</van-button>
    <van-cell-group inset class="link-list">
      <van-cell title="提现记录" is-link @click="router.push('/user/records/withdraw')" />
    </van-cell-group>
  </AppPage>
</template>

<style scoped lang="scss">
.link-list { margin-top: 12px; }
</style>
