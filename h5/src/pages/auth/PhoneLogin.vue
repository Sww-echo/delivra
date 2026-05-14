<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const auth = useAuthStore()
const phone = ref('13800000000')
const password = ref('123456')
const agreed = ref(true)
const showCountryCode = ref(false)

function login() {
  auth.login()
  showToast('登录成功')
  router.push('/home')
}
</script>

<template>
  <main class="login-page">
    <section class="top-view">
      <button class="language" type="button" @click="showToast('语言切换待接入')">
        <span>简体中文</span>
        <van-icon name="arrow-down" />
      </button>
      <div class="hero-text">
        <h1>Hello</h1>
        <p>欢迎来到Delivra</p>
      </div>
    </section>

    <section class="content-view">
      <h2>注册或登录</h2>
      <p class="subtitle">请选择您喜欢的方式登录</p>

      <van-form class="login-form" @submit="login">
        <van-field model-value="+86 中国" readonly is-link @click="showCountryCode = true" />
        <van-field v-model="phone" name="phone" placeholder="请输入手机号" clearable />
        <van-field v-model="password" name="password" type="password" placeholder="请输入用户密码" clearable />
        <button class="login-button" type="submit">登录</button>
      </van-form>

      <div class="login-links">
        <button type="button" @click="router.push('/auth/register/phone')">还没有账号？立即注册。</button>
        <button type="button" @click="router.push('/auth/forgot/phone')">忘记密码</button>
      </div>

      <div class="switch-row">
        <button type="button" class="switch-item">
          <span class="switch-icon active"><van-icon name="phone-o" /></span>
          <em>手机号</em>
        </button>
        <button type="button" class="switch-item" @click="router.push('/auth/login/email')">
          <span class="switch-icon muted"><van-icon name="envelop-o" /></span>
          <em>邮箱</em>
        </button>
      </div>

      <div class="divider-title">
        <i />
        <span>其他登录方式</span>
        <i />
      </div>

      <div class="oauth-row">
        <button type="button" @click="router.push('/auth/oauth/google')"><span>G</span><em>Google</em></button>
        <button type="button" @click="router.push('/auth/oauth/facebook')"><span>f</span><em>Facebook</em></button>
        <button type="button" @click="router.push('/auth/oauth/line')"><span>L</span><em>Line</em></button>
      </div>

      <label class="agreement">
        <van-checkbox v-model="agreed" icon-size="20px" />
        <span>我已阅读并同意</span>
        <button type="button" @click="router.push('/static/agreement')">《用户协议》</button>
        <span>和</span>
        <button type="button" @click="router.push('/static/privacy')">《隐私政策》</button>
      </label>
    </section>

    <van-action-sheet :show="showCountryCode" :actions="[{ name: '+86 中国' }, { name: '+1 美国' }, { name: '+81 日本' }]" @update:show="showCountryCode = $event" @select="showCountryCode = false" />
  </main>
</template>

<style scoped lang="scss">
.login-page {
  min-height: 100vh;
  overflow: hidden;
  background: #fff;
  color: #000;
}

.top-view {
  position: relative;
  height: 192px;
  background: var(--app-primary);
}

.language {
  position: absolute;
  top: 14px;
  right: 20px;
  display: flex;
  gap: 3px;
  align-items: center;
  border: 0;
  background: transparent;
  padding: 0;
  color: #fff;
  font-size: 13px;
  line-height: 18px;
}

.hero-text {
  position: absolute;
  top: 76px;
  left: 31px;

  h1 {
    margin: 0;
    color: #fff;
    font-size: 29px;
    font-weight: 700;
    line-height: 35px;
  }

  p {
    margin: 0;
    color: #fff;
    font-size: 15px;
    font-weight: 700;
    line-height: 20px;
  }
}

.content-view {
  position: relative;
  margin-top: -22px;
  min-height: calc(100vh - 170px);
  border-radius: 17px 17px 0 0;
  background: #fff;
  padding-top: 11px;

  h2 {
    margin: 0 0 0 26px;
    color: #000;
    font-size: 19px;
    font-weight: 500;
    line-height: 25px;
  }
}

.subtitle {
  margin: 0 0 0 26px;
  color: #bbb8b8;
  font-size: 12px;
  line-height: 16px;
}

.login-form {
  margin-top: 12px;

  :deep(.van-cell) {
    width: auto;
    height: 46px;
    margin: 0 26px;
    border-radius: 4px;
    background: #f2f2f2;
    padding: 12px 17px;
  }

  :deep(.van-cell + .van-cell) {
    margin-top: 21px;
  }

  :deep(.van-field__control) {
    color: #111827;
    font-size: 15px;
    line-height: 21px;
  }

  :deep(.van-field__control::placeholder) {
    color: #000;
  }
}

.login-button {
  display: block;
  width: calc(100% - 51px);
  height: 43px;
  margin: 21px 25.5px 0;
  border: 0;
  border-radius: 4px;
  background: var(--app-primary);
  color: #fff;
  font-size: 15px;
}

.login-links {
  display: flex;
  justify-content: space-between;
  padding: 16px 26px 0;

  button {
    border: 0;
    background: transparent;
    padding: 0;
    font-size: 15px;
    line-height: 20px;
  }

  button:first-child {
    color: #ff6b35;
  }

  button:last-child {
    color: #6b7280;
  }
}

.switch-row {
  display: flex;
  justify-content: center;
  gap: 58px;
  margin-top: 23px;
}

.switch-item,
.oauth-row button {
  display: grid;
  justify-items: center;
  border: 0;
  background: transparent;
  padding: 0;
  color: #4b5563;

  em {
    margin-top: 9px;
    font-size: 13px;
    font-style: normal;
    line-height: 16px;
  }
}

.switch-icon,
.oauth-row span {
  display: grid;
  place-items: center;
  width: 45px;
  height: 45px;
  border-radius: 50%;
  color: #fff;
  font-size: 22px;
}

.switch-icon.muted,
.oauth-row span {
  background: #d1d5db;
}

.switch-icon.active {
  background: var(--app-primary);
}

.divider-title {
  display: flex;
  align-items: center;
  gap: 17px;
  margin-top: 14px;
  padding: 0 65px;

  i {
    height: 1px;
    flex: 1;
    background: #e5e7eb;
  }

  span {
    color: #6b7280;
    font-size: 13px;
    line-height: 17px;
  }
}

.oauth-row {
  display: flex;
  justify-content: space-between;
  margin-top: 15px;
  padding: 0 64px;

  span {
    color: #fff;
    font-weight: 700;
  }
}

.agreement {
  display: flex;
  align-items: center;
  justify-content: center;
  color: #6b7280;
  font-size: 13px;
  line-height: 20px;

  :deep(.van-checkbox) {
    margin-right: 0;
  }

  :deep(.van-checkbox__icon--checked .van-icon) {
    border-color: var(--app-primary);
    background: var(--app-primary);
  }

  button {
    border: 0;
    background: transparent;
    padding: 0;
    color: var(--app-primary);
    font-size: 13px;
  }
}

.agreement {
  margin-top: 42px;
}
</style>
