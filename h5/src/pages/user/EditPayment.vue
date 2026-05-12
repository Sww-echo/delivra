<script setup lang="ts">
import { ref } from 'vue'
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'

const type = ref('银行卡')
const showType = ref(false)
</script>

<template>
  <AppPage title="修改/添加银行卡">
    <van-form @submit="showToast('银行卡信息已保存')">
      <van-field v-model="type" label="类型" readonly is-link @click="showType = true" />
      <van-field label="开户人" placeholder="请输入开户人" />
      <van-field label="银行卡号" placeholder="请输入银行卡号" />
      <van-field label="开户行" placeholder="请输入开户行" />
      <van-button block round type="primary" native-type="submit">修改/添加银行账户</van-button>
    </van-form>
    <van-action-sheet v-model:show="showType" :actions="[{ name: '银行卡' }, { name: '电子钱包' }]" @select="(action) => { type = action.name; showType = false }" />
  </AppPage>
</template>
