<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'

const router = useRouter()
const email = ref('')
const password = ref('')
</script>

<template>
  <AppPage title="邮箱忘记密码">
    <van-form @submit="showToast('密码修改成功')">
      <van-field v-model="email" label="邮箱" placeholder="请输入邮箱" />
      <van-field v-model="password" label="新密码" type="password" placeholder="请输入新密码" />
      <van-button block round type="primary" native-type="submit">修改密码</van-button>
    </van-form>
    <van-cell-group inset class="page-links">
      <van-cell title="手机号找回" is-link @click="router.push('/auth/forgot/phone')" />
    </van-cell-group>
  </AppPage>
</template>

<style scoped lang="scss">
.page-links { margin-top: 12px; }
</style>
