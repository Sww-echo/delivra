<script setup lang="ts">
withDefaults(
  defineProps<{
    description?: string
  }>(),
  { description: '暂无数据' },
)
</script>

<template>
  <van-empty :description="description" />
</template>
