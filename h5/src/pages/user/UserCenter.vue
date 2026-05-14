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
    <section class="user-hero">
      <van-image :src="auth.user?.avatar" width="58" height="58" round class="avatar" />
      <div>
        <strong>{{ auth.user?.nickname }}</strong>
        <span>{{ auth.user?.country }} · {{ auth.user?.language }}</span>
      </div>
      <button type="button" @click="router.push('/user/profile')">资料</button>
    </section>
    <SectionCard class="wallet-card">
      <div class="wallet-card__balance">
        <span>账户余额</span>
        <strong>¥{{ auth.user?.balance }}</strong>
      </div>
      <van-grid :column-num="2" :border="false">
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
.user-hero {
  display: flex;
  gap: 12px;
  align-items: center;
  margin: -12px -12px 12px;
  padding: 24px 16px 46px;
  background: #ff7a00 url('/delivra/user_bg.png') center / cover no-repeat;
  color: #fff;

  .avatar {
    flex: none;
    border: 2px solid rgb(255 255 255 / 72%);
    overflow: hidden;
  }

  div {
    display: grid;
    flex: 1;
    gap: 4px;
    min-width: 0;
  }

  strong {
    font-size: 19px;
  }

  span {
    font-size: 12px;
    opacity: .86;
  }

  button {
    border: 0;
    border-radius: 999px;
    background: rgb(255 255 255 / 20%);
    padding: 6px 12px;
    color: #fff;
  }
}

.wallet-card {
  margin-top: -38px;
}

.wallet-card__balance {
  display: grid;
  gap: 4px;
  margin-bottom: 8px;
  text-align: center;

  span {
    color: var(--app-muted);
    font-size: 12px;
  }

  strong {
    color: var(--app-primary);
    font-size: 26px;
  }
}

.menu-list {
  margin-top: 12px;
  overflow: hidden;
  border: 1px solid var(--app-border);
  border-radius: var(--app-radius-lg);
  box-shadow: var(--app-shadow);
}
</style>
