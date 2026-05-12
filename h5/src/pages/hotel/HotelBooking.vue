<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import SectionCard from '@/components/common/SectionCard.vue'
import AppPage from '@/components/layout/AppPage.vue'

const router = useRouter()
const date = ref('2026-05-12')
const showDatePicker = ref(false)
</script>

<template>
  <AppPage title="酒店预订">
    <SectionCard title="预订信息">
      <van-cell title="日期" :value="date" is-link @click="showDatePicker = true" />
      <van-field label="入住人" model-value="Delivra 用户" readonly />
      <van-field label="联系电话" model-value="13800000000" readonly />
    </SectionCard>
    <van-button block round type="primary" @click="showToast('酒店订单提交成功'); router.push('/hotel-order/H202605120001')">提交订单</van-button>
    <van-popup v-model:show="showDatePicker" round position="bottom">
      <van-date-picker title="选择日期" @confirm="({ selectedValues }) => { date = selectedValues.join('-'); showDatePicker = false }" @cancel="showDatePicker = false" />
    </van-popup>
  </AppPage>
</template>
