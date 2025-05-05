<template>
  <!-- tabsCategory -->
  <tabsCategory v-if="!isHomePage" @clickCategory="clickCategory" />

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
          <div
            v-if="product.images.length > 0 && product.images[0]"
            class="h-48 lg:h-72"
          >
            <img
              :src="`${imageUrl}/api/uploads/${Math.ceil(product.id / 100)}/${
                product.images[0]
              }`"
              alt="Card 1"
              class="w-full h-full object-cover rounded-t-lg lg:rounded-lg p-1 cursor-pointer"
            />
          </div>
          <div v-else class="h-48 lg:h-72">
            <img
              class="w-full h-full object-cover rounded-t-lg lg:rounded-lg p-1 cursor-pointer"
              :src="`${imageUrl}/src/assets/image/system/product.png`"
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
  <!-- <div v-if="products.length === 0" class=""></div> -->
  <div class="">
    <pagination
      v-if="!isHomePage"
      ref="paginationRef"
      :pageSize="dataPaging.rows"
      :totalList="totalList"
      @reloadData="reloadData"
    />
  </div>
</template>

<script>
import { useRoute } from "vue-router";
import axios from "axios";
import tabsCategory from "@/components/frontend/tabs-category.vue";
import pagination from "@/components/backend/paging.vue";

export default {
  components: {
    tabsCategory,
    pagination,
  },
  props: {
    categoryId: {
      type: String,
      required: false,
    },
    categoryName: {
      type: String,
      required: false,
    },
    searchQuery: {
      type: String,
      required: false,
    },
  },
  data() {
    return {
      baseUrl: __BASE_URL__,
      apiUrl: __API_URL__,
      imageUrl: __IMAGE_URL__,
      products: [],
      categorys: {
        id: "",
        name: "",
      },
      dataPaging: {
        pageNumber: 1,
        rows: 8,
        totalPage: 0,
        status: "",
      },
      totalList: [],

      category_id: this.categoryId === "0" ? "" : this.categoryId || "",
    };
  },
  computed: {
    // เช็คว่าเป็นหน้า Home หรือไม่
    isHomePage() {
      return this.$route.name === "home";
    },
  },
  mounted() {
    this.searchText = this.searchQuery || "";

    this.getListProduct();
    this.getListCategory();
  },
  watch: {
    categoryId(newCategoryId) {
      // ตรวจสอบว่า newCategoryId เป็น "0" หรือไม่
      this.category_id = newCategoryId === "0" ? "" : newCategoryId;
      this.dataPaging.pageNumber = 1;
      this.getListProduct();
    },
    searchQuery(newSearchText) {
      this.searchText = newSearchText;
      this.getListProduct();

    },
  },
  methods: {
    async getListProduct() {
      await axios

        .get(`${this.apiUrl}products/cat/`, {
          params: {
            category_id: this.category_id,
            limit: this.dataPaging.rows,
            page: this.dataPaging.pageNumber,
            q: this.searchText,
          },
        })
        .then((response) => {
          const data = response.data;
          this.products = data.rows;
          this.totalList = data.total;

          // console.log("totalList", this.totalList);
          // console.log(this.products);
        })
        .catch((error) => {
          console.error("There was an error fetching the data:", error);
        });
    },
    reloadData(pageNo) {
      this.dataPaging.pageNumber = pageNo;

      this.getListProduct();

      // console.log("pageNo", pageNo);
    },

    xmark() {
      this.searchText = "";
      this.dataPaging.pageNumber = 1;
      this.getListProduct();
      this.$refs.paginationRef.resetPage();
    },

    async getListCategory() {
      // this.categoryStatus = "active";

      await axios
        .get(`${this.apiUrl}category/`)
        .then((response) => {
          const data = response.data;
          this.categorys = data.rows;
          // console.log("categorys", this.categorys);
        })
        .catch((error) => {
          console.error("There was an error fetching the data:", error); // แสดงข้อผิดพลาด
        });
    },
    clickCategory(catId) {
      this.dataPaging.pageNumber = 1;
      this.category_id = catId;
      this.getListProduct();
      this.$refs.paginationRef.resetPage();
    },
  },
};
</script>
