<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { showToast } from 'vant'
import AppPage from '@/components/layout/AppPage.vue'

const router = useRouter()
const keyword = ref('')

type FeedProduct = {
  id: string
  name: string
  image: string
  price: string
  routeId: 'p1' | 'p2' | 'p3'
}

const categories = [
  { name: 'Foods', icon: '/delivra/categories/food.png', to: '/products' },
  { name: 'Milk Tea', icon: '/delivra/categories/drink.png', to: '/products' },
  { name: 'Coffee', icon: '/delivra/categories/coffee.png', to: '/products' },
  { name: 'Hot Pot/BBQ', icon: '/delivra/products/hotpot.jpeg', to: '/products' },
  { name: 'Stores', icon: '/delivra/logo.png', to: '/merchant/m1' },
  { name: 'Flowers', icon: '/delivra/categories/food.png', to: '/products' },
  { name: 'Watches Bags', icon: '/delivra/categories/drink.png', to: '/products' },
  { name: 'Personal Care', icon: '/delivra/categories/coffee.png', to: '/products' },
  { name: 'Medicine', icon: '/delivra/products/drinks.jpeg', to: '/products' },
  { name: 'Hotels', icon: '/delivra/products/hotel.jpeg', to: '/hotels' },
]

const merchantFeeds: Array<{
  id: string
  name: string
  logo: string
  rating: string
  sold: number
  products: FeedProduct[]
}> = [
  {
    id: 'm1',
    name: 'Starbucks',
    logo: '/delivra/home-merchants/starbucks.jpeg',
    rating: '4.9',
    sold: 2784,
    products: [
      { id: 'p1', name: 'Iced Brown Sugar Oatmilk', image: '/delivra/home-products/starbucks-1.jpeg', price: '57.46', routeId: 'p1' },
      { id: 'p2', name: 'Strawberry Açai', image: '/delivra/home-products/starbucks-2.jpeg', price: '51.20', routeId: 'p2' },
      { id: 'p3', name: 'Iced Matcha Latte', image: '/delivra/home-products/starbucks-3.jpeg', price: '51.20', routeId: 'p3' },
      { id: 'p4', name: 'Iced Lavender Cream', image: '/delivra/products/drinks.jpeg', price: '52.77', routeId: 'p2' },
    ],
  },
  {
    id: 'm2',
    name: 'Costa Coffee',
    logo: '/delivra/home-merchants/costa.jpeg',
    rating: '4.9',
    sold: 2311,
    products: [
      { id: 'p5', name: 'Salted Caramel Frappe', image: '/delivra/home-products/costa-1.jpeg', price: '56.51', routeId: 'p1' },
      { id: 'p6', name: 'Americano', image: '/delivra/home-products/costa-2.jpeg', price: '40.19', routeId: 'p1' },
      { id: 'p7', name: 'Latte', image: '/delivra/home-products/costa-3.jpeg', price: '46.51', routeId: 'p1' },
      { id: 'p8', name: 'Cheese & Tomato Toastie', image: '/delivra/products/coffee.jpeg', price: '58.00', routeId: 'p1' },
    ],
  },
  {
    id: 'm3',
    name: 'Taco Bell',
    logo: '/delivra/home-merchants/taco.jpeg',
    rating: '4.9',
    sold: 2115,
    products: [
      { id: 'p9', name: 'Soft Taco', image: '/delivra/home-products/taco-1.jpeg', price: '18.97', routeId: 'p3' },
      { id: 'p10', name: 'Crunchwrap Supreme', image: '/delivra/home-products/taco-2.jpeg', price: '63.78', routeId: 'p3' },
      { id: 'p11', name: 'Chicken Quesadilla', image: '/delivra/home-products/taco-3.jpeg', price: '65.76', routeId: 'p3' },
      { id: 'p12', name: 'MTN DEW Baja Blast', image: '/delivra/products/hotpot.jpeg', price: '39.98', routeId: 'p2' },
    ],
  },
  {
    id: 'm4',
    name: 'KFC',
    logo: '/delivra/home-merchants/kfc.jpeg',
    rating: '4.9',
    sold: 1992,
    products: [
      { id: 'p13', name: 'Chicken Burger', image: '/delivra/home-products/kfc-1.jpeg', price: '42.80', routeId: 'p3' },
      { id: 'p14', name: 'Popcorn Chicken', image: '/delivra/home-products/kfc-2.jpeg', price: '36.50', routeId: 'p3' },
      { id: 'p15', name: 'Fries Combo', image: '/delivra/home-products/kfc-3.jpeg', price: '29.90', routeId: 'p3' },
      { id: 'p16', name: 'Pepsi Set', image: '/delivra/products/drinks.jpeg', price: '31.20', routeId: 'p2' },
    ],
  },
]

function search() {
  router.push({ path: '/search', query: { q: keyword.value } })
}
</script>

<template>
  <AppPage title="首页" :show-back="false" class="home-page">
    <section class="home-header">
      <div class="home-header__top">
        <button class="location" type="button" @click="showToast('定位待接入')">
          <van-icon name="location" />
          <span>Unknow Address</span>
        </button>
        <button class="country" type="button" @click="router.push('/country')">
          <span class="flag">🇨🇳</span>
          <span>China</span>
          <van-icon name="arrow-down" />
        </button>
      </div>
      <van-search v-model="keyword" placeholder="搜索商家、商品名称" shape="round" @search="search" />
    </section>

    <main class="home-content">
      <section class="category-grid">
        <button v-for="category in categories" :key="category.name" type="button" @click="router.push(category.to)">
          <img :src="category.icon" :alt="category.name" />
          <span>{{ category.name }}</span>
        </button>
      </section>

      <section class="merchant-feed">
        <article v-for="merchant in merchantFeeds" :key="merchant.id" class="merchant-feed__card" @click="router.push(`/merchant/${merchant.id}`)">
          <header class="merchant-feed__head">
            <img :src="merchant.logo" :alt="merchant.name" />
            <div>
              <h3>{{ merchant.name }}</h3>
              <p><van-icon name="star" /> <span>{{ merchant.rating }}</span><em>已售{{ merchant.sold }}</em></p>
            </div>
          </header>
          <div class="product-strip">
            <button v-for="product in merchant.products" :key="product.id" type="button" @click.stop="router.push(`/product/${product.routeId}`)">
              <img :src="product.image" :alt="product.name" />
              <strong>{{ product.name }}</strong>
              <span>￥{{ product.price }}</span>
            </button>
          </div>
        </article>
      </section>
    </main>
  </AppPage>
</template>

<style scoped lang="scss">
:deep(.van-nav-bar) {
  display: none;
}

:deep(.app-page__body) {
  padding: 0;
}

.home-page {
  background: #fff;
}

.home-header {
  position: sticky;
  top: 0;
  z-index: 5;
  background: var(--app-primary);
  padding: 12px 24px 15px;
}

.home-header__top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 13px;
  color: #fff;
}

.location,
.country {
  display: flex;
  align-items: center;
  border: 0;
  background: transparent;
  padding: 0;
  color: #fff;
  font-weight: 700;
}

.location {
  gap: 8px;
  min-width: 0;
  font-size: 17px;

  span {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .van-icon {
    flex: none;
    font-size: 20px;
  }
}

.country {
  gap: 5px;
  flex: none;
  font-size: 14px;
}

.flag {
  display: grid;
  place-items: center;
  width: 34px;
  height: 22px;
  background: #ef3f31;
  font-size: 13px;
  line-height: 1;
}

:deep(.van-search) {
  padding: 0;
}

:deep(.van-search__content) {
  height: 42px;
  border: 0;
  border-radius: 4px;
  box-shadow: none;
}

:deep(.van-field__control) {
  color: #111827;
  font-size: 15px;
  font-weight: 500;
}

:deep(.van-field__control::placeholder) {
  color: #9ca3af;
}

:deep(.van-search__field) {
  align-items: center;
}

:deep(.van-icon-search) {
  color: #9ca3af;
  font-size: 20px;
}

.home-content {
  padding: 10px 16px 84px;
  background: #f7f7f7;
}

.category-grid {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  gap: 11px 4px;
  border-radius: 13px;
  background: #fff;
  padding: 11px 10px 12px;
}

.category-grid button {
  display: grid;
  min-width: 0;
  justify-items: center;
  border: 0;
  background: transparent;
  padding: 0;
  color: #111;
  font-size: 11px;
  line-height: 1.18;
  text-align: center;
}

.category-grid img {
  display: block;
  width: 36px;
  height: 36px;
  margin: 0 auto 6px;
  border-radius: 50%;
  object-fit: cover;
}

.category-grid span {
  display: -webkit-box;
  width: 54px;
  min-height: 26px;
  overflow: hidden;
  overflow-wrap: anywhere;
  word-break: break-word;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
}

.merchant-feed {
  display: grid;
  gap: 11px;
  margin-top: 11px;
}

.merchant-feed__card {
  overflow: hidden;
  border-radius: 13px;
  background: #fff;
  padding: 12px 0 11px;
  box-shadow: 0 2px 5px rgb(0 0 0 / 7%);
}

.merchant-feed__head {
  display: flex;
  gap: 11px;
  align-items: center;
  padding: 0 16px 10px;

  > img {
    width: 46px;
    height: 46px;
    flex: none;
    border-radius: 50%;
    object-fit: cover;
  }

  div {
    min-width: 0;
  }

  h3 {
    margin: 0 0 6px;
    color: #111;
    font-size: 17px;
    line-height: 1;
  }

  p {
    display: flex;
    gap: 5px;
    align-items: center;
    margin: 0;
    color: var(--app-primary);
    font-size: 12px;
    line-height: 1;
  }

  em {
    color: #6b7280;
    font-style: normal;
  }
}

.product-strip {
  display: grid;
  grid-auto-columns: 86px;
  grid-auto-flow: column;
  gap: 10px;
  overflow-x: auto;
  padding: 0 16px 1px;
  scrollbar-width: none;

  &::-webkit-scrollbar {
    display: none;
  }

  button {
    border: 0;
    background: transparent;
    padding: 0;
    text-align: left;
  }

  img {
    display: block;
    width: 86px;
    height: 68px;
    border-radius: 8px;
    background: #17382d;
    object-fit: cover;
  }

  strong {
    display: -webkit-box;
    min-height: 32px;
    margin-top: 6px;
    overflow: hidden;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
    color: #111;
    font-size: 13px;
    font-weight: 500;
    line-height: 1.2;
  }

  span {
    display: block;
    margin-top: 3px;
    color: var(--app-primary);
    font-size: 13px;
    font-weight: 600;
    line-height: 1;
  }
}
</style>
