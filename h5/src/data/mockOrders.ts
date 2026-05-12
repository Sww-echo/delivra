import type { Order } from '@/types/domain'
import { products } from './mockProducts'

export const orders: Order[] = [
  {
    id: 'D202605120001',
    type: 'product',
    status: 'pending',
    title: 'Delivra 优选餐厅订单',
    amount: 40,
    merchantName: 'Delivra 优选餐厅',
    address: '中心商圈 88 号',
    createdAt: '2026-05-12 10:30',
    items: [{ product: products[0], quantity: 1 }, { product: products[1], quantity: 1 }],
  },
  {
    id: 'H202605120001',
    type: 'hotel',
    status: 'paid',
    title: 'Delivra 城市酒店订单',
    amount: 388,
    hotelName: 'Delivra 城市酒店',
    createdAt: '2026-05-12 11:00',
    items: [],
  },
]
