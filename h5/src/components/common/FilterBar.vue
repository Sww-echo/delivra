<script setup lang="ts">
defineProps<{
  sortLabel?: string
  filterLabel?: string
}>()

const emit = defineEmits<{
  sort: []
  filter: []
}>()
</script>

<template>
  <div class="filter-bar">
    <van-button size="small" round icon="sort" @click="emit('sort')">{{ sortLabel || '排序' }}</van-button>
    <van-button size="small" round icon="filter-o" @click="emit('filter')">{{ filterLabel || '筛选' }}</van-button>
    <slot />
  </div>
</template>

<style scoped lang="scss">
.filter-bar {
  display: flex;
  gap: 8px;
  align-items: center;
  padding: 8px 0;
}
</style>
