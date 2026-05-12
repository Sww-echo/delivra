<script setup lang="ts">
import { ref } from 'vue'
import StatusTabs from '@/components/common/StatusTabs.vue'
import AppPage from '@/components/layout/AppPage.vue'
import { copyText } from '@/utils/feedback'

const active = ref('all')
const options = [{ label: '全部', value: 'all' }, { label: '充值', value: 'recharge' }, { label: '提现', value: 'withdraw' }, { label: '交易', value: 'trade' }]
</script>

<template>
  <AppPage title="记录列表">
    <StatusTabs v-model="active" :options="options" />
    <van-cell-group inset class="record-list">
      <van-cell title="记录 ID：REC202605120001" label="金额 ¥100.00" value="复制" is-link @click="copyText('REC202605120001', 'ID 已复制')" />
      <van-cell title="记录 ID：REC202605120002" label="金额 ¥68.00" value="复制" is-link @click="copyText('REC202605120002', 'ID 已复制')" />
    </van-cell-group>
  </AppPage>
</template>

<style scoped lang="scss">
.record-list { margin-top: 12px; }
</style>
