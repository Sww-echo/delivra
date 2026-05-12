<script setup lang="ts">
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import SectionCard from '@/components/common/SectionCard.vue'
import AppPage from '@/components/layout/AppPage.vue'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const auth = useAuthStore()
const menu = [
  ['我的订单', '/orders'], ['交易记录', '/user/records/transaction'], ['我的评价', '/user/records/review'], ['联系客服', '/chat/service'],
  ['收款信息', '/user/payment'], ['收货地址', '/user/address'], ['修改提现密码', '/user/change-withdraw-password'], ['修改密码', '/user/change-password'],
  ['代理', '/agent'], ['帮助中心', '/static/help'], ['公司资质', '/static/qualification'], ['产品/服务介绍', '/static/intro'], ['退款政策', '/static/refund'],
]
</script>

<template>
  <AppPage title="我的" :show-back="false">
    <SectionCard>
      <van-cell :title="auth.user?.nickname" :label="`余额 ¥${auth.user?.balance}`" is-link @click="router.push('/user/profile')">
        <template #icon><van-image :src="auth.user?.avatar" width="48" height="48" round class="avatar" /></template>
      </van-cell>
      <van-grid :column-num="2">
        <van-grid-item text="充值" icon="gold-coin-o" @click="router.push('/user/recharge')" />
        <van-grid-item text="提现" icon="balance-o" @click="router.push('/user/withdraw')" />
      </van-grid>
    </SectionCard>
    <van-cell-group inset class="menu-list">
      <van-cell v-for="item in menu" :key="item[0]" :title="item[0]" is-link @click="router.push(item[1])" />
      <van-cell title="切换语言" is-link @click="showToast('语言选择控件')" />
      <van-cell title="退出登录" is-link @click="auth.logout(); router.push('/auth/login/email')" />
    </van-cell-group>
  </AppPage>
</template>

<style scoped lang="scss">
.avatar { margin-right: 10px; }
.menu-list { margin-top: 12px; }
</style>
