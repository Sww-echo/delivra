<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'

const router = useRouter()
const phone = ref('')
const password = ref('')
const showCountryCode = ref(false)
</script>

<template>
  <AppPage title="手机号忘记密码">
    <van-form @submit="showToast('密码修改成功')">
      <van-field label="国家/区号" model-value="+86" readonly is-link @click="showCountryCode = true" />
      <van-field v-model="phone" label="手机号" placeholder="请输入手机号" />
      <van-field v-model="password" label="新密码" type="password" placeholder="请输入新密码" />
      <van-button block round type="primary" native-type="submit">修改密码</van-button>
    </van-form>
    <van-cell-group inset class="page-links">
      <van-cell title="邮箱找回" is-link @click="router.push('/auth/forgot/email')" />
    </van-cell-group>
    <van-action-sheet v-model:show="showCountryCode" :actions="[{ name: '+86 中国' }, { name: '+1 美国' }]" @select="showCountryCode = false" />
  </AppPage>
</template>

<style scoped lang="scss">
.page-links { margin-top: 12px; }
</style>
