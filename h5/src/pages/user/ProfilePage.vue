<script setup lang="ts">
import { showToast } from 'vant'
import { useRouter } from 'vue-router'
import AppPage from '@/components/layout/AppPage.vue'
import { showConfirmDialog } from '@/utils/feedback'

const router = useRouter()
</script>

<template>
  <AppPage title="个人信息">
    <van-cell-group inset>
      <van-cell title="头像" is-link @click="showToast('打开相册')" />
      <van-cell title="性别" value="男" is-link @click="showToast('性别选择控件')" />
      <van-cell title="生日" value="1990-01-01" is-link @click="showToast('日期选择控件')" />
      <van-cell title="换绑账号" is-link @click="router.push('/user/change-account')" />
      <van-cell title="修改密码" is-link @click="router.push('/user/change-password')" />
      <van-cell title="修改提现密码" is-link @click="router.push('/user/change-withdraw-password')" />
      <van-cell title="修改实名信息" is-link @click="router.push('/user/real-info')" />
      <van-cell title="切换国家" is-link @click="router.push('/country')" />
      <van-cell title="删除账号" is-link @click="showConfirmDialog('确认删除账号？', '删除账号')" />
    </van-cell-group>
  </AppPage>
</template>
