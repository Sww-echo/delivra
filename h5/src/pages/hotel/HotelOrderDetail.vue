<script setup lang="ts">
import { showToast } from 'vant'
import SectionCard from '@/components/common/SectionCard.vue'
import AppPage from '@/components/layout/AppPage.vue'
import { showConfirmDialog } from '@/utils/feedback'
</script>

<template>
  <AppPage title="酒店订单详情">
    <SectionCard title="订单状态" extra="已支付">
      <van-cell title="Delivra 城市酒店" label="高级大床房 · 2026-05-12" is-link to="/hotel/h1" />
    </SectionCard>
    <SectionCard title="订单操作">
      <van-cell title="支付订单" is-link @click="showConfirmDialog('确认支付酒店订单？', '确认金额')" />
      <van-cell title="找人代付" is-link @click="showToast('代付链接弹窗待生成')" />
      <van-cell title="取消订单" is-link @click="showConfirmDialog('确认取消酒店订单？', '取消订单')" />
    </SectionCard>
  </AppPage>
</template>
