<script setup lang="ts">
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import HotelCard from '@/components/business/HotelCard.vue'
import FilterBar from '@/components/common/FilterBar.vue'
import AppPage from '@/components/layout/AppPage.vue'
import { hotels } from '@/data/mockHotels'

const router = useRouter()
const keyword = ref('')
const list = computed(() => hotels.filter((item) => item.name.includes(keyword.value)))
</script>

<template>
  <AppPage title="酒店列表">
    <van-search v-model="keyword" placeholder="搜索酒店" shape="round" />
    <FilterBar sort-label="排序" filter-label="地址" @sort="showToast('已按推荐排序')" @filter="router.push('/user/address')" />
    <div class="card-list">
      <HotelCard v-for="hotel in list" :key="hotel.id" :hotel="hotel" @click="router.push(`/hotel/${hotel.id}`)" />
    </div>
  </AppPage>
</template>

<style scoped lang="scss">
.card-list { display: grid; gap: 10px; }
</style>
