<script setup lang="ts">
import { ref } from 'vue'
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'

const color = ref('默认背景')
</script>

<template>
  <AppPage title="聊天背景设置">
    <van-radio-group v-model="color">
      <van-cell-group inset>
        <van-cell title="默认背景" clickable @click="color = '默认背景'"><template #right-icon><van-radio name="默认背景" /></template></van-cell>
        <van-cell title="浅蓝背景" clickable @click="color = '浅蓝背景'"><template #right-icon><van-radio name="浅蓝背景" /></template></van-cell>
        <van-cell title="自定义图片" clickable @click="showToast('打开相册占位')"><template #right-icon><van-radio name="自定义图片" /></template></van-cell>
      </van-cell-group>
    </van-radio-group>
  </AppPage>
</template>
