<script setup lang="ts">
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'
</script>

<template>
  <AppPage title="我的地址">
    <van-address-list
      :list="[{ id: '1', name: 'Delivra 用户', tel: '13800000000', address: '中心商圈 88 号', isDefault: true }]"
      default-tag-text="默认"
      @add="showToast('新增地址待接入')"
      @edit="showToast('编辑地址待接入')"
    />
  </AppPage>
</template>
