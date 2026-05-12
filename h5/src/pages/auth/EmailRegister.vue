<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'

const router = useRouter()
const email = ref('')
const code = ref('')
const password = ref('')
</script>

<template>
  <AppPage title="邮箱注册">
    <van-form @submit="showToast('注册成功')">
      <van-field v-model="email" label="邮箱" placeholder="请输入邮箱" />
      <van-field v-model="code" label="验证码" placeholder="请输入验证码" />
      <van-field v-model="password" label="密码" type="password" placeholder="请设置密码" />
      <van-button block round type="primary" native-type="submit">注册</van-button>
    </van-form>
    <van-cell-group inset class="page-links">
      <van-cell title="手机号注册" is-link @click="router.push('/auth/register/phone')" />
      <van-cell title="用户协议" is-link @click="router.push('/static/agreement')" />
      <van-cell title="隐私政策" is-link @click="router.push('/static/privacy')" />
    </van-cell-group>
  </AppPage>
</template>

<style scoped lang="scss">
.page-links { margin-top: 12px; }
</style>
