import { ref } from 'vue'
import { defineStore } from 'pinia'
import type { PaymentAccount } from '@/types/domain'
import { paymentAccounts } from '@/data/mockUser'

export const useUserStore = defineStore('user', () => {
  const accounts = ref<PaymentAccount[]>([...paymentAccounts])

  function removeAccount(id: string) {
    accounts.value = accounts.value.filter((item) => item.id !== id)
  }

  return { accounts, removeAccount }
})
