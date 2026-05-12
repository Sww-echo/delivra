<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const auth = useAuthStore()
const email = ref('user@example.com')
const password = ref('123456')
const showLanguage = ref(false)

function login() {
  auth.login()
  showToast('登录成功')
  router.push('/home')
}
</script>

<template>
  <AppPage title="邮箱登录" :show-back="false">
    <van-form class="auth-form" @submit="login">
      <van-field v-model="email" name="email" label="邮箱" placeholder="请输入邮箱" />
      <van-field v-model="password" name="password" label="密码" type="password" placeholder="请输入密码" />
      <van-button block round type="primary" native-type="submit">登录</van-button>
    </van-form>
    <van-grid :column-num="3" class="auth-grid">
      <van-grid-item text="Google" @click="router.push('/auth/oauth/google')" />
      <van-grid-item text="Facebook" @click="router.push('/auth/oauth/facebook')" />
      <van-grid-item text="Line" @click="router.push('/auth/oauth/line')" />
    </van-grid>
    <van-cell-group inset>
      <van-cell title="手机号登录" is-link @click="router.push('/auth/login/phone')" />
      <van-cell title="立即注册" is-link @click="router.push('/auth/register/phone')" />
      <van-cell title="忘记密码" is-link @click="router.push('/auth/forgot/phone')" />
      <van-cell title="语言" is-link @click="showLanguage = true" />
      <van-cell title="用户协议" is-link @click="router.push('/static/agreement')" />
      <van-cell title="隐私政策" is-link @click="router.push('/static/privacy')" />
    </van-cell-group>
    <van-action-sheet v-model:show="showLanguage" :actions="[{ name: '简体中文' }, { name: 'English' }]" @select="showLanguage = false" />
  </AppPage>
</template>

<style scoped lang="scss">
.auth-form,
.auth-grid { margin-bottom: 12px; }
</style>
