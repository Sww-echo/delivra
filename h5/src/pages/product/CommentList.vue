<script setup lang="ts">
import { ref } from 'vue'
import AppPage from '@/components/layout/AppPage.vue'

const active = ref('all')
</script>

<template>
  <AppPage title="评价列表">
    <van-tabs v-model:active="active">
      <van-tab title="全部" name="all" />
      <van-tab title="好评" name="good" />
      <van-tab title="有图" name="image" />
    </van-tabs>
    <van-cell title="包装完整，配送很快" label="用户 A" />
    <van-cell title="味道不错，下次还会购买" label="用户 B" />
  </AppPage>
</template>
