<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import MerchantCard from '@/components/business/MerchantCard.vue'
import SectionCard from '@/components/common/SectionCard.vue'
import AppPage from '@/components/layout/AppPage.vue'
import { merchants } from '@/data/mockProducts'

const router = useRouter()
const keyword = ref('')

function search() {
  router.push({ path: '/search', query: { q: keyword.value } })
}
</script>

<template>
  <AppPage title="首页" :show-back="false">
    <van-search v-model="keyword" placeholder="搜索商品/商家" shape="round" @search="search" />
    <van-grid :column-num="4" class="quick-grid">
      <van-grid-item icon="shop-o" text="商品" @click="router.push('/products')" />
      <van-grid-item icon="hotel-o" text="酒店" @click="router.push('/hotels')" />
      <van-grid-item icon="logistics" text="机票" @click="showToast('机票预订待接入')" />
      <van-grid-item icon="location-o" text="地址" @click="router.push('/user/address')" />
    </van-grid>
    <SectionCard title="当前位置" extra="切换国家">
      <van-cell title="中国 / 中心商圈" is-link @click="router.push('/country')" />
    </SectionCard>
    <SectionCard title="精选推荐">
      <div class="card-list">
        <MerchantCard v-for="merchant in merchants" :key="merchant.id" :merchant="merchant" @click="router.push(`/merchant/${merchant.id}`)" />
      </div>
    </SectionCard>
  </AppPage>
</template>

<style scoped lang="scss">
.quick-grid { margin-bottom: 12px; }
.card-list { display: grid; gap: 10px; }
</style>
