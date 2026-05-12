<script setup lang="ts">
const titles: Record<string, string> = {
  help: '帮助中心',
  qualification: '公司资质',
  intro: '产品/服务介绍',
  refund: '退款政策',
  agreement: '用户协议',
  privacy: '隐私政策',
}

defineProps<{
  type: string
}>()
</script>

<template>
  <article class="static-content">
    <h2>{{ titles[type] || '静态页面' }}</h2>
    <p>这里展示 {{ titles[type] || type }} 的静态内容占位，后续可替换为接口或富文本内容。</p>
  </article>
</template>

<style scoped lang="scss">
.static-content {
  line-height: 1.7;

  h2 {
    margin: 0 0 12px;
    font-size: 20px;
  }

  p {
    margin: 0;
    color: var(--app-muted);
  }
}
</style>
