import { computed, ref } from 'vue'
import { defineStore } from 'pinia'
import type { CartItem, Product } from '@/types/domain'

export const useCartStore = defineStore('cart', () => {
  const items = ref<CartItem[]>([])

  const count = computed(() => items.value.reduce((total, item) => total + item.quantity, 0))
  const totalAmount = computed(() => items.value.reduce((total, item) => total + item.product.price * item.quantity, 0))

  function add(product: Product) {
    const existing = items.value.find((item) => item.product.id === product.id)
    if (existing) {
      existing.quantity += 1
      return
    }
    items.value.push({ product, quantity: 1 })
  }

  function decrease(productId: string) {
    const existing = items.value.find((item) => item.product.id === productId)
    if (!existing) return
    existing.quantity -= 1
    if (existing.quantity <= 0) {
      items.value = items.value.filter((item) => item.product.id !== productId)
    }
  }

  function clear() {
    items.value = []
  }

  return { items, count, totalAmount, add, decrease, clear }
})
