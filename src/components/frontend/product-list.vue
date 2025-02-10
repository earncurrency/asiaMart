<script setup>
import { useRoute } from "vue-router";

import axios from "axios";
import pagination from "@/components/backend/paging.vue";
</script>

<template>
  <div class="lg:flex items-center justify-between font-medium p-4 lg:p-0">
    <!-- ปุ่มนี้จะแสดงเมื่อจอใหญ่ -->
    <div class="flex items-center max-w-xl lg:w-1/3">
      <label for="voice-search" class="sr-only">Search</label>

      <div class="relative w-full">
        <div
          class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none"
        >
          <i class="fa-solid fa-magnifying-glass"></i>
        </div>
        <input
          type="text"
          v-model="searchText"
          @input="getListProduct"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full pl-10 pr-10 p-2.5 focus:border-gray-300"
          placeholder="ค้นหา..."
        />

        <button @click="xmark"
          class="absolute inset-y-0 end-0 flex items-center ps-3 p-3 pointer"
        >
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>
    </div>

    <!-- tabs Category-->
    <ul
      class="flex flex-wrap justify-center text-md font-medium text-center mt-4 lg:mt-0 text-gray-500 dark:text-gray-400"
    >
      <li v-for="(category, index) in categorys" :key="index" class="me-2">
        <RouterLink
          :to="`/category/${category.id}/${category.name}`"
          @click="clickCategory(category.id)"
        >
          <a
            href="#"
            class="inline-block px-4 py-3 rounded-lg hover:text-gray-900 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-white"
            >{{ category.name }}</a
          >
        </RouterLink>

        <!-- <a
          @click="clickCategory(category.id)"
          href="#"
          class="inline-block px-4 py-3 rounded-lg hover:text-gray-900 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-white"
          >{{ category.name }}</a
        > -->
      </li>
    </ul>
  </div>

  <hr class="my-2 text-gray-600" />

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
              class="w-full h-full object-cover rounded-t-lg lg:rounded-lg p-1 cursor-pointer"
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
  <div v-if="products.length === 0" class=""></div>
  <div v-else class="">
    <pagination
      :pageSize="dataPaging.rows"
      :totalList="totalList"
      :currentNum="currentNum"
      @reloadData="reloadData"
    />
  </div>
</template>

<script>
export default {
  props: {
    categoryId: {
      type: String,
      required: false,
    },
    categoryName: {
      type: String,
      required: false,
    },
  },
  data() {
    return {
      baseUrl: __BASE_URL__,
      apiUrl: __API_URL__,
      products: [],
      searchText:"",
      categorys: {
        id: "",
        name: "",
      },
      dataPaging: {
        pageNumber: 1,
        rows: 4,
        totalPage: 0,
        status: "",
      },
      totalList: [],
      currentNum: 1,
    };
  },
  mounted() {
    this.getListProduct();
    this.getListCategory();
  },
  watch: {
    categoryId(newCategoryId) {
      this.getListProduct(newCategoryId);
    },
  },
  methods: {
    async getListProduct() {

      this.page = (this.dataPaging.pageNumber * this.dataPaging.rows) - this.dataPaging.rows;
      
      await axios

        .get(`${this.apiUrl}products/cat/`, {
          params: {
            category_id: this.categoryId,
            limit: this.dataPaging.rows,
            // offset: this.dataPaging.pageNumber,
            page: this.page,
            q: this.searchText,
          },
        })
        .then((response) => {
          const data = response.data;
          this.products = data.rows;
          this.totalList = data.total;

          // console.log("totalList", this.totalList);
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

    async getListCategory() {
      this.categoryStatus = "active";

      await axios
        .get(`${this.apiUrl}category/`, {
          params: { category_status: this.categoryStatus },
        })
        .then((response) => {
          const data = response.data;
          this.categorys = data.rows;
          console.log("categorys", this.categorys);
        })
        .catch((error) => {
          console.error("There was an error fetching the data:", error); // แสดงข้อผิดพลาด
        });
    },
    clickCategory(id) {
      // this.$router.push(`/category/${categoryId}`);
      this.dataPaging.pageNumber = 1;
      this.currentNum = id;

      console.log("currentNum", this.currentNum);
    },
    xmark(){
      this.searchText = "";
      this.getListProduct();
    },
  },
};
</script>
