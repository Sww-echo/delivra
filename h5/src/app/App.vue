<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import TabbarLayout from '@/components/layout/TabbarLayout.vue'

const route = useRoute()
const usesTabbar = computed(() => Boolean(route.meta.tabbar))
</script>

<template>
  <TabbarLayout v-if="usesTabbar">
    <RouterView />
  </TabbarLayout>
  <RouterView v-else />
</template>
