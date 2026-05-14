import type { Hotel } from '@/types/domain'

export const hotels: Hotel[] = [
  {
    id: 'h1',
    name: 'Delivra 城市酒店',
    cover: '/delivra/products/hotel.jpeg',
    phone: '+86 010-88888888',
    address: '城市中心 100 号',
    rating: 4.7,
    rooms: [
      { id: 'r1', name: '高级大床房', price: 388, breakfast: '含早', remaining: 5 },
      { id: 'r2', name: '商务双床房', price: 468, breakfast: '双早', remaining: 3 },
    ],
  },
  {
    id: 'h2',
    name: '海景度假酒店',
    cover: '/delivra/products/drinks.jpeg',
    phone: '+86 020-66666666',
    address: '海滨大道 66 号',
    rating: 4.9,
    rooms: [{ id: 'r3', name: '海景套房', price: 688, breakfast: '含早', remaining: 2 }],
  },
]
