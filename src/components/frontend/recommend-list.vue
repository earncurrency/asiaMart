<template>
  <div class="relative">
    <div class="overflow-hidden">
      <div class="flex transition-transform duration-300 ease-in-out" :style="{ transform: `translateX(-${currentIndex * (100 / visibleItems)}%)` }">
        <div v-for="(product, index) in products" :key="index" class="w-1/4 flex-shrink-0 p-2">
          <div class="bg-white rounded-lg shadow-lg overflow-hidden">
            <img :src="product.image" :alt="product.name" class="w-full h-48 object-cover">
            <div class="p-4">
              <h3 class="font-semibold text-lg">{{ product.name }}</h3>
              <p class="text-gray-600">{{ product.description }}</p>
              <p class="text-gray-900 font-bold">{{ product.price }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <button @click="prev" class="absolute left-0 top-1/2 transform -translate-y-1/2 bg-gray-800 text-white p-2 rounded-full">
      &lt;
    </button>
    <button @click="next" class="absolute right-0 top-1/2 transform -translate-y-1/2 bg-gray-800 text-white p-2 rounded-full">
      &gt;
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentIndex: 0,
      visibleItems: 4, // จำนวนสินค้าที่แสดงในหนึ่งหน้า
      products: [
        {
          name: 'Product 1',
          description: 'Description for product 1',
          price: '$100',
          image: 'https://via.placeholder.com/300'
        },
        {
          name: 'Product 2',
          description: 'Description for product 2',
          price: '$200',
          image: 'https://via.placeholder.com/300'
        },
        {
          name: 'Product 3',
          description: 'Description for product 3',
          price: '$300',
          image: 'https://via.placeholder.com/300'
        },
        {
          name: 'Product 4',
          description: 'Description for product 4',
          price: '$400',
          image: 'https://via.placeholder.com/300'
        },
        {
          name: 'Product 5',
          description: 'Description for product 5',
          price: '$500',
          image: 'https://via.placeholder.com/300'
        },
        {
          name: 'Product 6',
          description: 'Description for product 6',
          price: '$600',
          image: 'https://via.placeholder.com/300'
        },
        {
          name: 'Product 7',
          description: 'Description for product 7',
          price: '$700',
          image: 'https://via.placeholder.com/300'
        },
        {
          name: 'Product 8',
          description: 'Description for product 8',
          price: '$800',
          image: 'https://via.placeholder.com/300'
        }
      ]
    };
  },
  methods: {
    prev() {
      this.currentIndex = Math.max(this.currentIndex - 1, 0);
    },
    next() {
      this.currentIndex = Math.min(this.currentIndex + 1, this.products.length - this.visibleItems);
    }
  }
};
</script>

<style scoped>
/* คุณสามารถเพิ่มสไตล์เพิ่มเติมได้ที่นี่ */
</style>