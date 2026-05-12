import type { AgentOrder, PaymentAccount, User } from '@/types/domain'

export const currentUser: User = {
  id: 'u1',
  nickname: 'Delivra 用户',
  avatar: 'https://fastly.jsdelivr.net/npm/@vant/assets/cat.jpeg',
  phone: '+86 13800000000',
  email: 'user@example.com',
  country: '中国',
  language: '简体中文',
  balance: 1288.5,
}

export const paymentAccounts: PaymentAccount[] = [
  { id: 'bank1', type: '银行卡', accountName: 'Delivra 用户', accountNo: '**** **** **** 8888', bankName: '示例银行' },
]

export const agentOrders: AgentOrder[] = [
  { id: 'ao1', status: 'pending', productName: '代付商品套餐 A', amount: 199, payLink: 'https://pay.example/ao1', proxyId: 'proxy-1001' },
  { id: 'ao2', status: 'paid', productName: '代付商品套餐 B', amount: 299, payLink: 'https://pay.example/ao2', proxyId: 'proxy-1002' },
]
