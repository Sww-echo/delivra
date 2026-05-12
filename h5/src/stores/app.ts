import { defineStore } from 'pinia'

export const useAppStore = defineStore('app', {
  state: () => ({
    language: '简体中文',
    country: '中国',
  }),
})
