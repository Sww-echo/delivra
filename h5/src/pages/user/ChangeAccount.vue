<script setup lang="ts">
import { ref } from 'vue'
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'

const registerType = ref('phone')
const bindType = ref('phone')
</script>

<template>
  <AppPage title="换绑账号">
    <van-tabs v-model:active="registerType">
      <van-tab title="手机注册" name="phone" />
      <van-tab title="邮箱注册" name="email" />
    </van-tabs>
    <van-tabs v-model:active="bindType" class="bind-tabs">
      <van-tab title="手机号" name="phone" />
      <van-tab title="邮箱" name="email" />
    </van-tabs>
    <van-form @submit="showToast('换绑账号成功')">
      <van-field label="账号" :placeholder="bindType === 'phone' ? '请输入手机号' : '请输入邮箱'" />
      <van-field label="验证码" placeholder="请输入验证码" />
      <van-button block round type="primary" native-type="submit">换绑账号</van-button>
    </van-form>
  </AppPage>
</template>

<style scoped lang="scss">
.bind-tabs { margin: 12px 0; }
</style>
