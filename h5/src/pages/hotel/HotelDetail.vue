<script setup lang="ts">
import { computed, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { showToast } from 'vant'
import SectionCard from '@/components/common/SectionCard.vue'
import AppPage from '@/components/layout/AppPage.vue'
import { hotels } from '@/data/mockHotels'

const route = useRoute()
const router = useRouter()
const activeDate = ref('今天')
const hotel = computed(() => hotels.find((item) => item.id === route.params.id) || hotels[0])
const lowestRoom = computed(() => hotel.value.rooms.slice().sort((a, b) => a.price - b.price)[0])
</script>

<template>
  <AppPage :title="hotel.name">
    <van-image :src="hotel.cover" width="100%" height="180" fit="cover" />
    <SectionCard :title="hotel.name" :extra="`评分 ${hotel.rating}`">
      <p class="app-muted">{{ hotel.address }}</p>
      <van-button size="small" icon="phone-o" @click="showToast(`拨打 ${hotel.phone}`)">拨打电话</van-button>
    </SectionCard>
    <SectionCard title="选择日期">
      <van-tabs v-model:active="activeDate" shrink>
        <van-tab title="今天" name="今天" />
        <van-tab title="明天" name="明天" />
        <van-tab title="后天" name="后天" />
      </van-tabs>
    </SectionCard>
    <SectionCard title="房型">
      <van-cell v-for="room in hotel.rooms" :key="room.id" :title="room.name" :label="`${room.breakfast} · 剩余 ${room.remaining} 间`" :value="`¥${room.price}`">
        <template #right-icon>
          <van-button size="small" type="primary" @click="router.push(`/hotel-booking/${room.id}`)">预订</van-button>
        </template>
      </van-cell>
      <van-button block round type="danger" @click="router.push(`/hotel-booking/${lowestRoom.id}`)">立即预订</van-button>
    </SectionCard>
  </AppPage>
</template>
