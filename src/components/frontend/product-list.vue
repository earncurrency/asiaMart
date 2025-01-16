<script setup>
import { useRoute } from "vue-router";
import axios from "axios";
</script>

<template>
  <div
    class="grid grid-cols-2 sm:grid-cols-2 md:grid-cols-4 gap-4 lg:gap-8 mt-8"
  >
    <div v-for="product in products" :key="product.id">
      <RouterLink :to="`/product-detail/${product.id}`">
        <div
          class="bg-white rounded-lg shadow-lg lg:shadow-none lg:border lg:p-2"
        >
          <div class="h-48 lg:h-72">
            <img
              :src="`${baseUrl}/api/uploads/${Math.ceil(product.id / 100)}/${
                product.images[0]
              }`"
              alt="Card 1"
              class="w-full h-full object-cover rounded-t-lg lg:rounded-lg cursor-pointer"
            />
          </div>
          <div class="p-2 pt-4">
            <h3
              class="text-md font-semibold text-gray-600 overflow-hidden text-ellipsis whitespace-nowrap"
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
</template>

<script>
export default {
  props: {
    categoryId: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      baseUrl: __BASE_URL__,
      apiUrl: "http://127.0.0.1:8000/",
      products: [],
    };
  },
  mounted() {
    this.getListProduct();
  },
  watch: {
    categoryId(newCategoryId) {
      this.getListProduct(newCategoryId);
    }
  },
  methods: {
    async getListProduct() {
      await axios
        .get(
          `${this.apiUrl}products/get_products_by_category_id/${this.categoryId}`
        )
        .then((response) => {
          const data = response.data;
          this.products = data.rows;
          console.log(this.products);
        })
        .catch((error) => {
          console.error("There was an error fetching the data:", error);
        });
    },
  },
};
</script>
