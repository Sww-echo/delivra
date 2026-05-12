<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const auth = useAuthStore()
const phone = ref('13800000000')
const password = ref('123456')
const showCountryCode = ref(false)

function login() {
  auth.login()
  showToast('登录成功')
  router.push('/home')
}
</script>

<template>
  <AppPage title="手机号登录" :show-back="false">
    <van-form class="auth-form" @submit="login">
      <van-field label="国家/区号" model-value="+86" readonly is-link @click="showCountryCode = true" />
      <van-field v-model="phone" name="phone" label="手机号" placeholder="请输入手机号" />
      <van-field v-model="password" name="password" label="密码" type="password" placeholder="请输入密码" />
      <van-button block round type="primary" native-type="submit">登录</van-button>
    </van-form>
    <van-cell-group inset>
      <van-cell title="邮箱登录" is-link @click="router.push('/auth/login/email')" />
      <van-cell title="立即注册" is-link @click="router.push('/auth/register/phone')" />
      <van-cell title="忘记密码" is-link @click="router.push('/auth/forgot/phone')" />
      <van-cell title="用户协议" is-link @click="router.push('/static/agreement')" />
      <van-cell title="隐私政策" is-link @click="router.push('/static/privacy')" />
    </van-cell-group>
    <van-action-sheet v-model:show="showCountryCode" :actions="[{ name: '+86 中国' }, { name: '+1 美国' }, { name: '+81 日本' }]" @select="showCountryCode = false" />
  </AppPage>
</template>

<style scoped lang="scss">
.auth-form { margin-bottom: 12px; }
</style>
