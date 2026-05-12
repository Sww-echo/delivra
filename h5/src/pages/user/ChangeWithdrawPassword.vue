<script setup lang="ts">
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'
</script>

<template>
  <AppPage title="修改提现密码">
    <van-form @submit="showToast('提现密码修改成功')">
      <van-field label="原提现密码" type="password" placeholder="请输入原提现密码" />
      <van-field label="新提现密码" type="password" placeholder="请输入新提现密码" />
      <van-button block round type="primary" native-type="submit">确认修改</van-button>
    </van-form>
  </AppPage>
</template>
