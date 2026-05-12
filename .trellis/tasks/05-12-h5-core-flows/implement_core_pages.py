from pathlib import Path

root = Path('h5/src/pages')
files = {
    'auth/EmailLogin.vue': '''<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const auth = useAuthStore()
const email = ref('user@example.com')
const password = ref('123456')
const showLanguage = ref(false)

function login() {
  auth.login()
  showToast('登录成功')
  router.push('/home')
}
</script>

<template>
  <AppPage title="邮箱登录" :show-back="false">
    <van-form class="auth-form" @submit="login">
      <van-field v-model="email" name="email" label="邮箱" placeholder="请输入邮箱" />
      <van-field v-model="password" name="password" label="密码" type="password" placeholder="请输入密码" />
      <van-button block round type="primary" native-type="submit">登录</van-button>
    </van-form>
    <van-grid :column-num="3" class="auth-grid">
      <van-grid-item text="Google" @click="router.push('/auth/oauth/google')" />
      <van-grid-item text="Facebook" @click="router.push('/auth/oauth/facebook')" />
      <van-grid-item text="Line" @click="router.push('/auth/oauth/line')" />
    </van-grid>
    <van-cell-group inset>
      <van-cell title="手机号登录" is-link @click="router.push('/auth/login/phone')" />
      <van-cell title="立即注册" is-link @click="router.push('/auth/register/phone')" />
      <van-cell title="忘记密码" is-link @click="router.push('/auth/forgot/phone')" />
      <van-cell title="语言" is-link @click="showLanguage = true" />
      <van-cell title="用户协议" is-link @click="router.push('/static/agreement')" />
      <van-cell title="隐私政策" is-link @click="router.push('/static/privacy')" />
    </van-cell-group>
    <van-action-sheet v-model:show="showLanguage" :actions="[{ name: '简体中文' }, { name: 'English' }]" @select="showLanguage = false" />
  </AppPage>
</template>

<style scoped lang="scss">
.auth-form,
.auth-grid { margin-bottom: 12px; }
</style>
''',
    'auth/PhoneLogin.vue': '''<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const auth = useAuthStore()
const phone = ref('13800000000')
const password = ref('123456')
const showCountryCode = ref(false)

function login() {
  auth.login()
  showToast('登录成功')
  router.push('/home')
}
</script>

<template>
  <AppPage title="手机号登录" :show-back="false">
    <van-form class="auth-form" @submit="login">
      <van-field label="国家/区号" model-value="+86" readonly is-link @click="showCountryCode = true" />
      <van-field v-model="phone" name="phone" label="手机号" placeholder="请输入手机号" />
      <van-field v-model="password" name="password" label="密码" type="password" placeholder="请输入密码" />
      <van-button block round type="primary" native-type="submit">登录</van-button>
    </van-form>
    <van-cell-group inset>
      <van-cell title="邮箱登录" is-link @click="router.push('/auth/login/email')" />
      <van-cell title="立即注册" is-link @click="router.push('/auth/register/phone')" />
      <van-cell title="忘记密码" is-link @click="router.push('/auth/forgot/phone')" />
      <van-cell title="用户协议" is-link @click="router.push('/static/agreement')" />
      <van-cell title="隐私政策" is-link @click="router.push('/static/privacy')" />
    </van-cell-group>
    <van-action-sheet v-model:show="showCountryCode" :actions="[{ name: '+86 中国' }, { name: '+1 美国' }, { name: '+81 日本' }]" @select="showCountryCode = false" />
  </AppPage>
</template>

<style scoped lang="scss">
.auth-form { margin-bottom: 12px; }
</style>
''',
    'auth/PhoneRegister.vue': '''<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'

const router = useRouter()
const phone = ref('')
const code = ref('')
const password = ref('')
const showCountryCode = ref(false)
</script>

<template>
  <AppPage title="手机号注册">
    <van-form @submit="showToast('注册成功')">
      <van-field label="国家/区号" model-value="+86" readonly is-link @click="showCountryCode = true" />
      <van-field v-model="phone" label="手机号" placeholder="请输入手机号" />
      <van-field v-model="code" label="验证码" placeholder="请输入验证码" />
      <van-field v-model="password" label="密码" type="password" placeholder="请设置密码" />
      <van-button block round type="primary" native-type="submit">注册</van-button>
    </van-form>
    <van-cell-group inset class="page-links">
      <van-cell title="邮箱注册" is-link @click="router.push('/auth/register/email')" />
      <van-cell title="用户协议" is-link @click="router.push('/static/agreement')" />
      <van-cell title="隐私政策" is-link @click="router.push('/static/privacy')" />
    </van-cell-group>
    <van-action-sheet v-model:show="showCountryCode" :actions="[{ name: '+86 中国' }, { name: '+1 美国' }]" @select="showCountryCode = false" />
  </AppPage>
</template>

<style scoped lang="scss">
.page-links { margin-top: 12px; }
</style>
''',
    'auth/EmailRegister.vue': '''<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'

const router = useRouter()
const email = ref('')
const code = ref('')
const password = ref('')
</script>

<template>
  <AppPage title="邮箱注册">
    <van-form @submit="showToast('注册成功')">
      <van-field v-model="email" label="邮箱" placeholder="请输入邮箱" />
      <van-field v-model="code" label="验证码" placeholder="请输入验证码" />
      <van-field v-model="password" label="密码" type="password" placeholder="请设置密码" />
      <van-button block round type="primary" native-type="submit">注册</van-button>
    </van-form>
    <van-cell-group inset class="page-links">
      <van-cell title="手机号注册" is-link @click="router.push('/auth/register/phone')" />
      <van-cell title="用户协议" is-link @click="router.push('/static/agreement')" />
      <van-cell title="隐私政策" is-link @click="router.push('/static/privacy')" />
    </van-cell-group>
  </AppPage>
</template>

<style scoped lang="scss">
.page-links { margin-top: 12px; }
</style>
''',
    'auth/PhoneForgot.vue': '''<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'

const router = useRouter()
const phone = ref('')
const password = ref('')
const showCountryCode = ref(false)
</script>

<template>
  <AppPage title="手机号忘记密码">
    <van-form @submit="showToast('密码修改成功')">
      <van-field label="国家/区号" model-value="+86" readonly is-link @click="showCountryCode = true" />
      <van-field v-model="phone" label="手机号" placeholder="请输入手机号" />
      <van-field v-model="password" label="新密码" type="password" placeholder="请输入新密码" />
      <van-button block round type="primary" native-type="submit">修改密码</van-button>
    </van-form>
    <van-cell-group inset class="page-links">
      <van-cell title="邮箱找回" is-link @click="router.push('/auth/forgot/email')" />
    </van-cell-group>
    <van-action-sheet v-model:show="showCountryCode" :actions="[{ name: '+86 中国' }, { name: '+1 美国' }]" @select="showCountryCode = false" />
  </AppPage>
</template>

<style scoped lang="scss">
.page-links { margin-top: 12px; }
</style>
''',
    'auth/EmailForgot.vue': '''<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'

const router = useRouter()
const email = ref('')
const password = ref('')
</script>

<template>
  <AppPage title="邮箱忘记密码">
    <van-form @submit="showToast('密码修改成功')">
      <van-field v-model="email" label="邮箱" placeholder="请输入邮箱" />
      <van-field v-model="password" label="新密码" type="password" placeholder="请输入新密码" />
      <van-button block round type="primary" native-type="submit">修改密码</van-button>
    </van-form>
    <van-cell-group inset class="page-links">
      <van-cell title="手机号找回" is-link @click="router.push('/auth/forgot/phone')" />
    </van-cell-group>
  </AppPage>
</template>

<style scoped lang="scss">
.page-links { margin-top: 12px; }
</style>
''',
    'auth/OAuthPlaceholder.vue': '''<script setup lang="ts">
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import AppPage from '@/components/layout/AppPage.vue'

const route = useRoute()
const router = useRouter()
const provider = computed(() => String(route.params.provider || '第三方'))
</script>

<template>
  <AppPage :title="`${provider} 登录`">
    <div class="app-card oauth-card">
      <h2>{{ provider }} 登录页</h2>
      <p class="app-muted">第三方登录暂以占位方式展示。</p>
      <van-button block round type="primary" @click="router.push('/home')">模拟登录成功</van-button>
    </div>
  </AppPage>
</template>

<style scoped lang="scss">
.oauth-card { display: grid; gap: 12px; }
h2 { margin: 0; }
</style>
''',
    'home/HomePage.vue': '''<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import MerchantCard from '@/components/business/MerchantCard.vue'
import SectionCard from '@/components/common/SectionCard.vue'
import AppPage from '@/components/layout/AppPage.vue'
import { merchants } from '@/data/mockProducts'

const router = useRouter()
const keyword = ref('')

function search() {
  router.push({ path: '/search', query: { q: keyword.value } })
}
</script>

<template>
  <AppPage title="首页" :show-back="false">
    <van-search v-model="keyword" placeholder="搜索商品/商家" shape="round" @search="search" />
    <van-grid :column-num="4" class="quick-grid">
      <van-grid-item icon="shop-o" text="商品" @click="router.push('/products')" />
      <van-grid-item icon="hotel-o" text="酒店" @click="router.push('/hotels')" />
      <van-grid-item icon="logistics" text="机票" @click="showToast('机票预订待接入')" />
      <van-grid-item icon="location-o" text="地址" @click="router.push('/user/address')" />
    </van-grid>
    <SectionCard title="当前位置" extra="切换国家">
      <van-cell title="中国 / 中心商圈" is-link @click="router.push('/country')" />
    </SectionCard>
    <SectionCard title="精选推荐">
      <div class="card-list">
        <MerchantCard v-for="merchant in merchants" :key="merchant.id" :merchant="merchant" @click="router.push(`/merchant/${merchant.id}`)" />
      </div>
    </SectionCard>
  </AppPage>
</template>

<style scoped lang="scss">
.quick-grid { margin-bottom: 12px; }
.card-list { display: grid; gap: 10px; }
</style>
''',
    'product/ProductList.vue': '''<script setup lang="ts">
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import ProductCard from '@/components/business/ProductCard.vue'
import FilterBar from '@/components/common/FilterBar.vue'
import AppPage from '@/components/layout/AppPage.vue'
import { products } from '@/data/mockProducts'
import { useCartStore } from '@/stores/cart'

const router = useRouter()
const cart = useCartStore()
const keyword = ref('')
const filteredProducts = computed(() => products.filter((item) => item.name.includes(keyword.value)))
</script>

<template>
  <AppPage title="商品列表">
    <van-search v-model="keyword" placeholder="搜索商品" shape="round" />
    <FilterBar @sort="showToast('已按销量排序')" @filter="showToast('价格筛选待选择')" />
    <div class="card-list">
      <ProductCard v-for="product in filteredProducts" :key="product.id" :product="product" @click="router.push(`/merchant/${product.merchantId}`)" @add="cart.add" />
    </div>
  </AppPage>
</template>

<style scoped lang="scss">
.card-list { display: grid; gap: 10px; }
</style>
''',
    'product/MerchantDetail.vue': '''<script setup lang="ts">
import { computed, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { showToast } from 'vant'
import CartPopup from '@/components/business/CartPopup.vue'
import ProductCard from '@/components/business/ProductCard.vue'
import AppPage from '@/components/layout/AppPage.vue'
import { merchants } from '@/data/mockProducts'
import { useCartStore } from '@/stores/cart'

const route = useRoute()
const router = useRouter()
const cart = useCartStore()
const activeTab = ref('menu')
const showCart = ref(false)
const merchant = computed(() => merchants.find((item) => item.id === route.params.id) || merchants[0])
const categories = computed(() => [...new Set(merchant.value.products.map((item) => item.category))])
const activeCategory = ref('')
const visibleProducts = computed(() => merchant.value.products.filter((item) => !activeCategory.value || item.category === activeCategory.value))
</script>

<template>
  <AppPage :title="merchant.name">
    <div class="app-card merchant-hero">
      <van-image :src="merchant.cover" width="72" height="72" radius="12" />
      <div>
        <h2>{{ merchant.name }}</h2>
        <p class="app-muted">{{ merchant.address }}</p>
        <van-button size="small" icon="chat-o" @click="router.push('/chat/' + merchant.id)">联系商家</van-button>
      </div>
    </div>
    <van-tabs v-model:active="activeTab">
      <van-tab title="点菜" name="menu">
        <van-tabs v-model:active="activeCategory" class="category-tabs" shrink>
          <van-tab title="全部" name="" />
          <van-tab v-for="category in categories" :key="category" :title="category" :name="category" />
        </van-tabs>
        <ProductCard v-for="product in visibleProducts" :key="product.id" :product="product" @click="router.push(`/product/${product.id}`)" @add="cart.add" />
      </van-tab>
      <van-tab title="评价" name="comments">
        <van-cell v-for="comment in merchant.comments" :key="comment" :title="comment" />
        <van-button block @click="showToast('评价筛选待接入')">筛选</van-button>
      </van-tab>
    </van-tabs>
    <van-submit-bar :price="cart.totalAmount * 100" button-text="去结算" @submit="router.push('/checkout')">
      <van-button size="small" round @click="showCart = true">购物车 {{ cart.count }}</van-button>
    </van-submit-bar>
    <CartPopup v-model="showCart" @checkout="router.push('/checkout')" />
  </AppPage>
</template>

<style scoped lang="scss">
.merchant-hero { display: flex; gap: 12px; margin-bottom: 12px; }
h2 { margin: 0 0 4px; font-size: 18px; }
.category-tabs { margin-bottom: 8px; }
</style>
''',
    'product/ProductDetail.vue': '''<script setup lang="ts">
import { computed, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import CartPopup from '@/components/business/CartPopup.vue'
import AppPage from '@/components/layout/AppPage.vue'
import { products } from '@/data/mockProducts'
import { useCartStore } from '@/stores/cart'

const route = useRoute()
const router = useRouter()
const cart = useCartStore()
const showCart = ref(false)
const product = computed(() => products.find((item) => item.id === route.params.id) || products[0])
</script>

<template>
  <AppPage :title="product.name">
    <van-image :src="product.image" width="100%" height="220" fit="cover" />
    <div class="app-card detail-card">
      <h2>{{ product.name }}</h2>
      <p class="price">¥{{ product.price }}</p>
      <p class="app-muted">{{ product.description }}</p>
      <van-button block plain type="primary" @click="router.push('/comments')">查看更多评价</van-button>
    </div>
    <van-action-bar>
      <van-action-bar-icon icon="cart-o" :badge="cart.count || undefined" text="购物车" @click="showCart = true" />
      <van-action-bar-button type="warning" text="加入购物车" @click="cart.add(product)" />
      <van-action-bar-button type="danger" text="去结算" @click="router.push('/checkout')" />
    </van-action-bar>
    <CartPopup v-model="showCart" @checkout="router.push('/checkout')" />
  </AppPage>
</template>

<style scoped lang="scss">
.detail-card { margin-top: 12px; }
h2 { margin: 0 0 8px; }
.price { color: #ee0a24; font-size: 22px; font-weight: 700; }
</style>
''',
    'order/CheckoutPage.vue': '''<script setup lang="ts">
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import SectionCard from '@/components/common/SectionCard.vue'
import AppPage from '@/components/layout/AppPage.vue'
import { useCartStore } from '@/stores/cart'

const router = useRouter()
const cart = useCartStore()

function submitOrder() {
  showToast('订单提交成功')
  router.push('/order/D202605120001')
}
</script>

<template>
  <AppPage title="确认订单">
    <SectionCard title="收货地址">
      <van-cell title="中心商圈 88 号" label="Delivra 用户 13800000000" is-link @click="router.push('/user/address')" />
    </SectionCard>
    <SectionCard title="商品明细">
      <van-cell v-for="item in cart.items" :key="item.product.id" :title="item.product.name" :label="`x${item.quantity}`" :value="`¥${item.product.price}`" />
      <van-empty v-if="!cart.items.length" description="购物车为空，将提交示例订单" />
    </SectionCard>
    <van-submit-bar :price="(cart.totalAmount || 40) * 100" button-text="提交订单" @submit="submitOrder" />
  </AppPage>
</template>
''',
    'order/OrderDetail.vue': '''<script setup lang="ts">
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { showConfirmDialog, showToast } from 'vant'
import OrderCard from '@/components/business/OrderCard.vue'
import SectionCard from '@/components/common/SectionCard.vue'
import AppPage from '@/components/layout/AppPage.vue'
import { orders } from '@/data/mockOrders'
import { copyText } from '@/utils/feedback'

const route = useRoute()
const router = useRouter()
const order = computed(() => orders.find((item) => item.id === route.params.id) || orders[0])
</script>

<template>
  <AppPage title="订单详情">
    <OrderCard :order="order" @click="undefined" @copy="copyText(order.id, '订单号已复制')" />
    <SectionCard title="订单操作">
      <van-cell title="商家信息" is-link @click="router.push('/merchant/m1')" />
      <van-cell title="联系商家" is-link @click="router.push('/chat/m1')" />
      <van-cell title="修改收货地址" is-link @click="router.push('/user/address')" />
      <van-cell title="支付订单" is-link @click="showConfirmDialog({ title: '确认金额', message: `确认支付 ¥${order.amount}？` })" />
      <van-cell title="找人代付" is-link @click="showToast('代付链接弹窗待生成')" />
      <van-cell title="取消订单" is-link @click="showConfirmDialog({ title: '取消订单', message: '确认取消当前订单？' })" />
    </SectionCard>
  </AppPage>
</template>
''',
    'product/CommentList.vue': '''<script setup lang="ts">
import { ref } from 'vue'
import AppPage from '@/components/layout/AppPage.vue'

const active = ref('all')
</script>

<template>
  <AppPage title="评价列表">
    <van-tabs v-model:active="active">
      <van-tab title="全部" name="all" />
      <van-tab title="好评" name="good" />
      <van-tab title="有图" name="image" />
    </van-tabs>
    <van-cell title="包装完整，配送很快" label="用户 A" />
    <van-cell title="味道不错，下次还会购买" label="用户 B" />
  </AppPage>
</template>
''',
    'home/SearchResults.vue': '''<script setup lang="ts">
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import ProductCard from '@/components/business/ProductCard.vue'
import AppPage from '@/components/layout/AppPage.vue'
import { products } from '@/data/mockProducts'
import { useCartStore } from '@/stores/cart'

const route = useRoute()
const router = useRouter()
const cart = useCartStore()
const keyword = computed(() => String(route.query.q || ''))
const results = computed(() => products.filter((item) => !keyword.value || item.name.includes(keyword.value)))
</script>

<template>
  <AppPage title="搜索结果">
    <van-cell :title="`关键词：${keyword || '全部'}`" />
    <ProductCard v-for="product in results" :key="product.id" :product="product" @click="router.push(`/product/${product.id}`)" @add="cart.add" />
  </AppPage>
</template>
'''
}

for name, content in files.items():
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')
