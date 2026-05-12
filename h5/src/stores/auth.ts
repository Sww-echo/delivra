import { ref } from 'vue'
import { defineStore } from 'pinia'
import type { User } from '@/types/domain'
import { currentUser } from '@/data/mockUser'

export const useAuthStore = defineStore('auth', () => {
  const user = ref<User | null>(currentUser)
  const isLoggedIn = ref(true)

  function login() {
    user.value = currentUser
    isLoggedIn.value = true
  }

  function logout() {
    user.value = null
    isLoggedIn.value = false
  }

  return { user, isLoggedIn, login, logout }
})
