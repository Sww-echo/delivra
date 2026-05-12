<script setup lang="ts">
defineProps<{
  options: Array<{ label: string; value: string }>
}>()

const model = defineModel<string>({ required: true })
</script>

<template>
  <van-tabs v-model:active="model" shrink sticky>
    <van-tab v-for="option in options" :key="option.value" :name="option.value" :title="option.label" />
  </van-tabs>
</template>
