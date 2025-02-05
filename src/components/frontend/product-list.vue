<script setup>
import { useRoute } from "vue-router";

import axios from "axios";
import pagination from "@/components/backend/paging.vue";
</script>

<template>
  <div
    v-if="products.length === 0"
    class="text-center mt-24 mb-8 text-xl text-gray-600"
  >
    ไม่มีสินค้าในหมวดหมู่นี้เเสดงอยู่
  </div>
  <div
    v-else
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
  <pagination
    :pageSize="dataPaging.rows"
    :totalList="totalList"
    @reloadData="reloadData"
  />
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

      dataPaging: {
        pageNumber: 0,
        rows: 4,
        totalPage: 0,
        status: "",
      },
      totalList: [],
    };
  },
  mounted() {
    this.getListProduct();
  },
  watch: {
    categoryId(newCategoryId) {
      this.getListProduct(newCategoryId);
    },

  },
  methods: {
    async getListProduct() {
      await axios
        .get(`${this.apiUrl}products/cat/`, {
          params: {
            category_id: this.categoryId,
            limit: this.dataPaging.rows,
            offset: this.dataPaging.pageNumber,
          },
        })
        .then((response) => {
          const data = response.data;
          this.products = data.rows;
          this.totalList = data.total;

          console.log("totalList", this.totalList);
          console.log(this.products);
        })
        .catch((error) => {
          console.error("There was an error fetching the data:", error);
        });
    },
    reloadData(pageNo) {
      this.dataPaging.pageNumber = pageNo;

      this.getListProduct();

      console.log("pageNo", pageNo);
    },

    pageSize(row) {
      this.dataPaging.pageNumber = 0;
      this.dataPaging.rows = row;
      this.getListProduct();
      this.pageSizeOpen = false;

      console.log("row", row);
    },
  },
};
</script>
