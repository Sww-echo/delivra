<script setup lang="ts">
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'
</script>

<template>
  <AppPage title="实名信息">
    <van-form @submit="showToast('实名信息已提交')">
      <van-field label="真实姓名" placeholder="请输入真实姓名" />
      <van-field label="证件号码" placeholder="请输入证件号码" />
      <van-button block round type="primary" native-type="submit">提交实名信息</van-button>
    </van-form>
  </AppPage>
</template>
