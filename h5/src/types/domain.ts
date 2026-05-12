export type OrderStatus = 'pending' | 'paid' | 'shipping' | 'completed' | 'cancelled'
export type OrderType = 'product' | 'hotel' | 'agent'

export interface User {
  id: string
  nickname: string
  avatar: string
  phone: string
  email: string
  country: string
  language: string
  balance: number
}

export interface Product {
  id: string
  merchantId: string
  name: string
  image: string
  price: number
  category: string
  sales: number
  description: string
}

export interface Merchant {
  id: string
  name: string
  cover: string
  rating: number
  tags: string[]
  address: string
  products: Product[]
  comments: string[]
}

export interface CartItem {
  product: Product
  quantity: number
}

export interface Order {
  id: string
  type: OrderType
  status: OrderStatus
  title: string
  amount: number
  merchantName?: string
  hotelName?: string
  address?: string
  createdAt: string
  items: CartItem[]
}

export interface HotelRoom {
  id: string
  name: string
  price: number
  breakfast: string
  remaining: number
}

export interface Hotel {
  id: string
  name: string
  cover: string
  phone: string
  address: string
  rating: number
  rooms: HotelRoom[]
}

export interface Message {
  id: string
  sender: 'me' | 'merchant' | 'system'
  content: string
  createdAt: string
}

export interface MessageThread {
  id: string
  title: string
  avatar: string
  lastMessage: string
  unread: number
  messages: Message[]
}

export interface PaymentAccount {
  id: string
  type: string
  accountName: string
  accountNo: string
  bankName: string
}

export interface AgentOrder {
  id: string
  status: OrderStatus
  productName: string
  amount: number
  payLink: string
  proxyId: string
}
