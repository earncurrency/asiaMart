<template>
  <div class="relative">
    <div class="overflow-hidden">
      <div
        class="flex transition-transform duration-300 ease-in-out"
        :style="{
          transform: `translateX(-${currentIndex * (100 / visibleItems)}%)`,
        }"
      >
        <div
          v-for="(product, index) in products"
          :key="index"
          class="w-1/2 md:w-1/3 lg:w-1/4 flex-shrink-0 p-2"
        >
          <RouterLink :to="`/product-detail/${product.product_id}`">
            <div class="bg-white rounded-lg border overflow-hidden">
              <img
                :src="`${imageUrl}/api/uploads/${Math.ceil(product.id / 100)}/${
                  product.images[0]
                }`"
                class="w-full h-48 p-1 object-contain"
              />
              <div class="p-4">
                <h3
                  class="font-semibold text-gray-600 overflow-hidden text-ellipsis whitespace-nowrap"
                >
                  {{ product.name }}
                </h3>
                <div class="flex justify-between items-center mt-2">
                  <p class="text-xl font-semibold text-orange-500">
                    {{ product.price }} บาท
                  </p>
                  <button
                    class="p-2 rounded-lg ml-4 bg-gray-800 text-white hover:bg-gray-600 transition"
                  >
                    <i class="fa-solid fa-cart-plus text-md"></i>
                  </button>
                </div>
              </div>
            </div>
          </RouterLink>
        </div>
      </div>
    </div>
    <button
      @click="prev"
      class="absolute left-0 top-1/2 transform -translate-y-1/2 bg-gray-800 text-white p-2 rounded-full"
    >
      &lt;
    </button>
    <button
      @click="next"
      class="absolute right-0 top-1/2 transform -translate-y-1/2 bg-gray-800 text-white p-2 rounded-full"
    >
      &gt;
    </button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      apiUrl: __API_URL__,
      imageUrl: __IMAGE_URL__,

      currentIndex: 0,
      visibleItems: 2,
      products: [],

      dataPaging: {
        pageNumber: 1,
        rows: 4,
        totalPage: 0,
        status: "",
      },
    };
  },
  mounted() {
    this.updateVisibleItems();
    window.addEventListener("resize", this.updateVisibleItems);

    this.getListRecommend();
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.updateVisibleItems);
  },
  methods: {
    async getListRecommend() {
      await axios
        .get(`${this.apiUrl}recommends/`)
        .then((response) => {
          const data = response.data;
          this.products = data.rows;
          this.totalList = data.total;

          console.log("recommends", this.products);
        })
        .catch((error) => {
          console.error("There was an error fetching the data:", error);
        });
    },

    prev() {
      this.currentIndex = Math.max(this.currentIndex - 1, 0);
    },
    next() {
      this.currentIndex = Math.min(
        this.currentIndex + 1,
        this.products.length - this.visibleItems
      );
    },
    updateVisibleItems() {
      if (window.innerWidth < 768) {
        this.visibleItems = 2; // หน้าจอเล็ก (โทรศัพท์มือถือ) แสดง 2 สินค้า
      } else if (window.innerWidth < 1024) {
        this.visibleItems = 3; // หน้าจอขนาดกลาง (แท็บเล็ต) แสดง 3 สินค้า
      } else {
        this.visibleItems = 4; // หน้าจอขนาดใหญ่ (เดสก์ท็อป) แสดง 4 สินค้า
      }
    },
  },
};
</script>

<style scoped>
/* คุณสามารถเพิ่มสไตล์เพิ่มเติมได้ที่นี่ */
</style>
