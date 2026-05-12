import type { Merchant, Product } from '@/types/domain'

export const products: Product[] = [
  {
    id: 'p1',
    merchantId: 'm1',
    name: '招牌牛肉饭',
    image: 'https://fastly.jsdelivr.net/npm/@vant/assets/cat.jpeg',
    price: 28,
    category: '主食',
    sales: 238,
    description: '热销招牌套餐，适合作为商品详情和购物车演示。',
  },
  {
    id: 'p2',
    merchantId: 'm1',
    name: '柠檬茶',
    image: 'https://fastly.jsdelivr.net/npm/@vant/assets/apple-1.jpeg',
    price: 12,
    category: '饮品',
    sales: 128,
    description: '清爽饮品，配合主食展示分类切换。',
  },
  {
    id: 'p3',
    merchantId: 'm2',
    name: '精选水果礼盒',
    image: 'https://fastly.jsdelivr.net/npm/@vant/assets/apple-2.jpeg',
    price: 68,
    category: '生鲜',
    sales: 56,
    description: '用于商品列表与订单卡片展示的生鲜商品。',
  },
]

export const merchants: Merchant[] = [
  {
    id: 'm1',
    name: 'Delivra 优选餐厅',
    cover: 'https://fastly.jsdelivr.net/npm/@vant/assets/cat.jpeg',
    rating: 4.8,
    tags: ['热销', '配送快', '支持代付'],
    address: '中心商圈 88 号',
    products: products.filter((item) => item.merchantId === 'm1'),
    comments: ['出餐很快', '包装完整', '味道不错'],
  },
  {
    id: 'm2',
    name: '环球生活超市',
    cover: 'https://fastly.jsdelivr.net/npm/@vant/assets/apple-2.jpeg',
    rating: 4.6,
    tags: ['生鲜', '日用品'],
    address: '国际社区 12 号',
    products: products.filter((item) => item.merchantId === 'm2'),
    comments: ['商品新鲜', '价格合理'],
  },
]
