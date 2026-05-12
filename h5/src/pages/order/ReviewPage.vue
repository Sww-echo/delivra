<script setup lang="ts">
import { ref } from 'vue'
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'

const rate = ref(5)
</script>

<template>
  <AppPage title="评价">
    <div class="app-card review-card">
      <span>评分</span>
      <van-rate v-model="rate" />
      <van-uploader :after-read="() => showToast('图片已选择')" />
      <van-field rows="4" autosize type="textarea" placeholder="请输入评价内容" />
      <van-button block round type="primary" @click="showToast('评价提交成功')">提交评价</van-button>
    </div>
  </AppPage>
</template>

<style scoped lang="scss">
.review-card { display: grid; gap: 12px; }
</style>
