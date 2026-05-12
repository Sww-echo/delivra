from pathlib import Path

root = Path('h5/src')
pages = {
    'auth/EmailLogin.vue': ('邮箱登录', ['登录 -> 首页', '手机号 -> 手机号登录页', 'Google/Facebook/Line -> 第三方登录占位', '语言 -> 语言选择控件', '立即注册 -> 手机号注册页', '忘记密码 -> 手机号忘记密码页']),
    'auth/PhoneLogin.vue': ('手机号登录', ['登录 -> 首页', '邮箱 -> 邮箱登录页', '国家/区号 -> 国家区号选择控件']),
    'auth/PhoneRegister.vue': ('手机号注册', ['注册 -> 完成手机账号注册', '邮箱 -> 邮箱注册页']),
    'auth/EmailRegister.vue': ('邮箱注册', ['注册 -> 完成邮箱账号注册', '手机号 -> 手机号注册页']),
    'auth/PhoneForgot.vue': ('手机号忘记密码', ['修改密码 -> 完成手机账号密码修改', '邮箱 -> 邮箱忘记密码页']),
    'auth/EmailForgot.vue': ('邮箱忘记密码', ['修改密码 -> 完成邮箱账号密码修改', '手机号 -> 手机号忘记密码页']),
    'auth/OAuthPlaceholder.vue': ('第三方登录', ['Google / Facebook / Line 登录占位页']),
    'home/HomePage.vue': ('首页', ['商品、酒店、机票快捷入口', '精选推荐 -> 商家详情', '地址、国家、搜索入口']),
    'home/SearchResults.vue': ('搜索结果', ['展示首页搜索结果占位']),
    'home/ChooseCountry.vue': ('选择国家', ['国家切换页面占位']),
    'product/ProductList.vue': ('商品列表', ['商品列表 -> 商家详情', '排序、筛选、搜索']),
    'product/MerchantDetail.vue': ('商家详情', ['联系商家、点菜/评价 Tab、菜单目录、加购、购物车、去结算']),
    'product/ProductDetail.vue': ('商品详情', ['加购、购物车、去结算、查看更多评价']),
    'product/CommentList.vue': ('评价列表', ['评价筛选与列表占位']),
    'order/CheckoutPage.vue': ('确认订单', ['地址、提交订单、返回']),
    'order/OrderDetail.vue': ('订单详情', ['状态、复制订单号、联系商家、修改地址、支付、代付、取消']),
    'order/OrderList.vue': ('我的订单', ['状态筛选、订单卡片、支付凭证、发货详情、评价入口']),
    'order/ReviewPage.vue': ('评价', ['评分、添加图片、提交评价']),
    'hotel/HotelList.vue': ('酒店列表', ['酒店列表、排序、搜索、地址']),
    'hotel/HotelDetail.vue': ('酒店详情', ['拨打电话、日期、房型预订、立即预订']),
    'hotel/HotelBooking.vue': ('酒店预订', ['日期选择、提交订单']),
    'hotel/HotelOrderDetail.vue': ('酒店订单详情', ['订单状态、酒店卡片、支付、代付、取消']),
    'message/MessageList.vue': ('消息列表', ['消息卡片、聊天背景设置']),
    'message/ChatPage.vue': ('聊天页', ['聊天功能弹窗、发送消息、设置']),
    'message/ChatSettings.vue': ('聊天背景设置', ['聊天背景设置占位']),
    'user/UserCenter.vue': ('我的', ['个人信息、充值、提现、订单、记录、客服、收款、地址、密码、代理、帮助、退出']),
    'user/ProfilePage.vue': ('个人信息', ['头像、性别、生日、换绑账号、密码、实名、国家、删除账号']),
    'user/ChangeAccount.vue': ('换绑账号', ['手机/邮箱注册切换、手机号/邮箱换绑']),
    'user/RechargePage.vue': ('充值', ['确认充值、充值记录']),
    'user/WithdrawPage.vue': ('提现', ['全部提现、确认提现、提现记录']),
    'user/RecordsPage.vue': ('记录列表', ['充值/提现/交易/评价记录筛选与复制']),
    'user/PaymentInfo.vue': ('收款信息', ['删除、修改、添加收款']),
    'user/EditPayment.vue': ('修改/添加银行卡', ['类型弹窗、提交']),
    'user/AddressPage.vue': ('我的地址', ['地址管理占位']),
    'user/ChangePassword.vue': ('修改密码', ['修改密码表单占位']),
    'user/ChangeWithdrawPassword.vue': ('修改提现密码', ['修改提现密码表单占位']),
    'user/RealInfo.vue': ('实名信息', ['修改实名信息表单占位']),
    'agent/AgentDashboard.vue': ('代理', ['快速创建订单、代付订单列表、冻结金额']),
    'agent/QuickCreateOrder.vue': ('快速创建订单', ['套餐选择、生成套餐弹窗']),
    'agent/PayOrderList.vue': ('代付订单列表', ['筛选、查看详情、复制订单号']),
    'agent/FrozenAmounts.vue': ('冻结金额明细', ['查看详情、复制代付链接、复制订单号、复制代付ID']),
    'static/StaticPage.vue': ('静态页面', ['帮助中心、公司资质、产品/服务介绍、退款政策、用户协议、隐私政策']),
}

no_back = {'home/HomePage.vue', 'order/OrderList.vue', 'message/MessageList.vue', 'user/UserCenter.vue'}
for file, (title, items) in pages.items():
    path = root / 'pages' / file
    path.parent.mkdir(parents=True, exist_ok=True)
    list_items = '\n'.join(f'      <van-cell title="{item}" />' for item in items)
    show_back = 'false' if file in no_back else 'true'
    path.write_text(f'''<script setup lang="ts">
import AppPage from '@/components/layout/AppPage.vue'
</script>

<template>
  <AppPage title="{title}" :show-back="{show_back}">
    <div class="app-card">
      <h2>{title}</h2>
      <p class="app-muted">页面占位，后续子任务补充完整交互。</p>
    </div>
    <van-cell-group inset class="placeholder-list">
{list_items}
    </van-cell-group>
  </AppPage>
</template>

<style scoped lang="scss">
h2 {{
  margin: 0 0 8px;
  font-size: 20px;
}}

.placeholder-list {{
  margin-top: 12px;
}}
</style>
''', encoding='utf-8')

router = '''import type { RouteRecordRaw } from 'vue-router'
import { createRouter, createWebHistory } from 'vue-router'

const tabMeta = { tabbar: true }

export const routes: RouteRecordRaw[] = [
  { path: '/', redirect: '/auth/login/email' },
  { path: '/auth/login/email', name: 'email-login', component: () => import('@/pages/auth/EmailLogin.vue') },
  { path: '/auth/login/phone', name: 'phone-login', component: () => import('@/pages/auth/PhoneLogin.vue') },
  { path: '/auth/register/phone', name: 'phone-register', component: () => import('@/pages/auth/PhoneRegister.vue') },
  { path: '/auth/register/email', name: 'email-register', component: () => import('@/pages/auth/EmailRegister.vue') },
  { path: '/auth/forgot/phone', name: 'phone-forgot', component: () => import('@/pages/auth/PhoneForgot.vue') },
  { path: '/auth/forgot/email', name: 'email-forgot', component: () => import('@/pages/auth/EmailForgot.vue') },
  { path: '/auth/oauth/:provider', name: 'oauth', component: () => import('@/pages/auth/OAuthPlaceholder.vue') },
  { path: '/home', name: 'home', component: () => import('@/pages/home/HomePage.vue'), meta: tabMeta },
  { path: '/search', name: 'search', component: () => import('@/pages/home/SearchResults.vue') },
  { path: '/country', name: 'country', component: () => import('@/pages/home/ChooseCountry.vue') },
  { path: '/products', name: 'products', component: () => import('@/pages/product/ProductList.vue') },
  { path: '/merchant/:id', name: 'merchant', component: () => import('@/pages/product/MerchantDetail.vue') },
  { path: '/product/:id', name: 'product-detail', component: () => import('@/pages/product/ProductDetail.vue') },
  { path: '/comments', name: 'comments', component: () => import('@/pages/product/CommentList.vue') },
  { path: '/checkout', name: 'checkout', component: () => import('@/pages/order/CheckoutPage.vue') },
  { path: '/order/:id', name: 'order-detail', component: () => import('@/pages/order/OrderDetail.vue') },
  { path: '/orders', name: 'orders', component: () => import('@/pages/order/OrderList.vue'), meta: tabMeta },
  { path: '/review/:id?', name: 'review', component: () => import('@/pages/order/ReviewPage.vue') },
  { path: '/hotels', name: 'hotels', component: () => import('@/pages/hotel/HotelList.vue') },
  { path: '/hotel/:id', name: 'hotel-detail', component: () => import('@/pages/hotel/HotelDetail.vue') },
  { path: '/hotel-booking/:id', name: 'hotel-booking', component: () => import('@/pages/hotel/HotelBooking.vue') },
  { path: '/hotel-order/:id', name: 'hotel-order', component: () => import('@/pages/hotel/HotelOrderDetail.vue') },
  { path: '/messages', name: 'messages', component: () => import('@/pages/message/MessageList.vue'), meta: tabMeta },
  { path: '/chat/:id?', name: 'chat', component: () => import('@/pages/message/ChatPage.vue') },
  { path: '/chat-settings', name: 'chat-settings', component: () => import('@/pages/message/ChatSettings.vue') },
  { path: '/user', name: 'user', component: () => import('@/pages/user/UserCenter.vue'), meta: tabMeta },
  { path: '/user/profile', name: 'profile', component: () => import('@/pages/user/ProfilePage.vue') },
  { path: '/user/change-account', name: 'change-account', component: () => import('@/pages/user/ChangeAccount.vue') },
  { path: '/user/recharge', name: 'recharge', component: () => import('@/pages/user/RechargePage.vue') },
  { path: '/user/withdraw', name: 'withdraw', component: () => import('@/pages/user/WithdrawPage.vue') },
  { path: '/user/records/:type', name: 'records', component: () => import('@/pages/user/RecordsPage.vue') },
  { path: '/user/payment', name: 'payment', component: () => import('@/pages/user/PaymentInfo.vue') },
  { path: '/user/payment/edit/:id?', name: 'edit-payment', component: () => import('@/pages/user/EditPayment.vue') },
  { path: '/user/address', name: 'address', component: () => import('@/pages/user/AddressPage.vue') },
  { path: '/user/change-password', name: 'change-password', component: () => import('@/pages/user/ChangePassword.vue') },
  { path: '/user/change-withdraw-password', name: 'change-withdraw-password', component: () => import('@/pages/user/ChangeWithdrawPassword.vue') },
  { path: '/user/real-info', name: 'real-info', component: () => import('@/pages/user/RealInfo.vue') },
  { path: '/agent', name: 'agent', component: () => import('@/pages/agent/AgentDashboard.vue') },
  { path: '/agent/quick-create-order', name: 'agent-quick-create-order', component: () => import('@/pages/agent/QuickCreateOrder.vue') },
  { path: '/agent/pay-orders', name: 'agent-pay-orders', component: () => import('@/pages/agent/PayOrderList.vue') },
  { path: '/agent/frozen-amounts', name: 'agent-frozen-amounts', component: () => import('@/pages/agent/FrozenAmounts.vue') },
  { path: '/static/:type', name: 'static', component: () => import('@/pages/static/StaticPage.vue') },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})
'''
(root / 'router/index.ts').write_text(router, encoding='utf-8')
