import type { MessageThread } from '@/types/domain'

export const messageThreads: MessageThread[] = [
  {
    id: 't1',
    title: 'Delivra 优选餐厅',
    avatar: 'https://fastly.jsdelivr.net/npm/@vant/assets/cat.jpeg',
    lastMessage: '您好，订单已收到。',
    unread: 2,
    messages: [
      { id: 'msg1', sender: 'merchant', content: '您好，订单已收到。', createdAt: '10:20' },
      { id: 'msg2', sender: 'me', content: '请尽快配送，谢谢。', createdAt: '10:21' },
    ],
  },
]
