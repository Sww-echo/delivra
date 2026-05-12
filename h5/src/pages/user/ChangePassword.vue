<script setup lang="ts">
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'
</script>

<template>
  <AppPage title="修改密码">
    <van-form @submit="showToast('密码修改成功')">
      <van-field label="原密码" type="password" placeholder="请输入原密码" />
      <van-field label="新密码" type="password" placeholder="请输入新密码" />
      <van-field label="确认密码" type="password" placeholder="请再次输入" />
      <van-button block round type="primary" native-type="submit">确认修改</van-button>
    </van-form>
  </AppPage>
</template>
