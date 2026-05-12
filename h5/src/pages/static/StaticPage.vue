<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import StaticContent from '@/components/common/StaticContent.vue'
import AppPage from '@/components/layout/AppPage.vue'

const route = useRoute()
const type = computed(() => String(route.params.type || 'help'))
</script>

<template>
  <AppPage title="静态页面" :show-back="true">
    <div class="app-card">
      <StaticContent :type="type" />
    </div>
  </AppPage>
</template>
