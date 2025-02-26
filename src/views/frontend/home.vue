<template>
  <frontend_navbar />

  <imageBanner />

  <div class="flex justify-center pt-18 p-4">
    <div
      class="w-full max-w-screen-2xl lg:p-12 lg:border border-gray-200 rounded-lg mb-16 lg:mb-4 bg-white z-40"
    >
      <div>
        <!-- Title -->
        <div
          class="title-content lg:flex items-center justify-between font-medium mt-4 gap-4 p-4 lg:p-0"
        >
          <div class="flex items-center max-w-xl lg:w-1/3">
            <!-- <label for="voice-search" class="sr-only">Search</label> -->

            <div class="relative w-full">
              <div
                class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none"
              >
                <i class="fa-solid fa-magnifying-glass"></i>
              </div>
              <input
                type="text"
                v-model="searchText"
                @input="searchProduct"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full pl-10 pr-10 p-2.5 focus:border-gray-300"
                placeholder="ค้นหา..."
              />

              <button
                @click="xmark"
                class="absolute inset-y-0 end-0 flex items-center ps-3 p-3 pointer"
              >
                <i class="fa-solid fa-xmark"></i>
              </button>
            </div>
          </div>
          <div class="lg:flex justify-center">
            <tabsCategory />
          </div>
        </div>

        <hr class="my-2 text-gray-600" />

        <!-- <div class="flex justify-center">
          <p class="text-3xl font-semibold mt-8 mb-2">โปรโมชั่น</p>
        </div>

        <promotion /> -->

        <div class="flex justify-center">
          <p class="text-3xl font-semibold mt-8 mb-4 lg:mb-16">สินค้าเเนะนำ</p>
        </div>

        <recommendList />

        <!-- <div class="flex justify-center">
          <p class="text-3xl font-semibold mt-8 mb-4 lg:mb-16">รายการสินค้า</p>
        </div>

        <productList /> -->
      </div>
    </div>
  </div>
</template>

<script>
import frontend_navbar from "@/components/frontend/navbar.vue";
import imageBanner from "@/components/frontend/image-banner.vue";
import productList from "@/components/frontend/product-list.vue";
import recommendList from "@/components/frontend/recommend-list.vue";
import promotion from "@/components/frontend/promotion.vue";
import tabsCategory from "@/components/frontend/tabs-category.vue";
export default {
  components: {
    frontend_navbar,
    imageBanner,
    productList,
    promotion,
    recommendList,
    tabsCategory,
  },
  data() {
    return {
      searchText: "",
    };
  },
  mounted() {
    this.checkAuth();
  },

  methods: {
    checkAuth() {
      const storedHash = localStorage.getItem("hash");

      if (!storedHash || storedHash === "") {
        this.$router.push("/login");
      }
    },
  },
};
</script>
