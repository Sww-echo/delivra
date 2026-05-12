<script setup lang="ts">
import { useRouter } from 'vue-router'
import AppPage from '@/components/layout/AppPage.vue'
import { useUserStore } from '@/stores/user'
import { showConfirmDialog } from '@/utils/feedback'

const router = useRouter()
const user = useUserStore()
</script>

<template>
  <AppPage title="收款信息">
    <van-cell-group inset>
      <van-cell v-for="account in user.accounts" :key="account.id" :title="account.bankName" :label="`${account.accountName} ${account.accountNo}`">
        <template #right-icon>
          <div class="actions">
            <van-button size="mini" @click.stop="router.push(`/user/payment/edit/${account.id}`)">修改</van-button>
            <van-button size="mini" type="danger" @click.stop="showConfirmDialog('确认删除收款信息？', '删除')">删除</van-button>
          </div>
        </template>
      </van-cell>
    </van-cell-group>
    <van-button block round type="primary" class="add-button" @click="router.push('/user/payment/edit')">添加收款</van-button>
  </AppPage>
</template>

<style scoped lang="scss">
.actions { display: flex; gap: 6px; }
.add-button { margin-top: 12px; }
</style>
