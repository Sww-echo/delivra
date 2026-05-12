<script setup lang="ts">
import { ref } from 'vue'
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'

const showPackage = ref(false)
const priceRange = ref('100-300')
</script>

<template>
  <AppPage title="快速创建订单">
    <van-cell-group inset>
      <van-cell title="套餐" value="选择套餐类型" is-link @click="showPackage = true" />
    </van-cell-group>
    <van-popup v-model:show="showPackage" round position="bottom">
      <div class="package-popup">
        <van-field v-model="priceRange" label="价格区间" placeholder="请输入价格区间" />
        <van-button block plain type="primary" @click="priceRange = '200-500'">充值</van-button>
        <van-button block round type="primary" @click="showToast('套餐生成成功'); showPackage = false">确认</van-button>
      </div>
    </van-popup>
  </AppPage>
</template>

<style scoped lang="scss">
.package-popup { display: grid; gap: 12px; padding: 16px; }
</style>
