<template>
  <frontend_navbar />

  <imageBanner />

  <div class="flex justify-center pt-18 p-4">
    <div
      class="w-full max-w-screen-2xl lg:p-12 lg:border border-gray-200 rounded-lg mb-16 lg:mb-4 bg-white z-40"
    >
      <div>
        <!-- tabsCategory -->
        <tabsCategory />

        <hr class="my-2 text-gray-600" />

        <!-- <div class="flex justify-center">
          <p class="text-3xl font-semibold mt-8 mb-2">โปรโมชั่น</p>
        </div>

        <promotion /> -->

        <div class="flex justify-center">
          <p class="text-3xl font-semibold mt-8 mb-4 lg:mb-16">สินค้าเเนะนำ</p>
        </div>

        <recommendList />

        <div class="flex justify-center">
          <p class="text-3xl font-semibold mt-16 mb-4 lg:mb-16">รายการสินค้า</p>
        </div>

        <productList />

        <div class="flex justify-center mt-8 mb-8">
          <RouterLink :to="`/category/0/ทั้งหมด`">
            <button
              class="p-2 pr-4 pl-4 rounded-lg bg-gray-800 text-white mt-6 hover:bg-gray-600 transition"
            >
              ดูสินค้าเพิ่มเติม
            </button>
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import frontend_navbar from "@/components/frontend/navbar.vue";
import imageBanner from "@/components/frontend/image-banner.vue";
import recommendList from "@/components/frontend/recommend-list.vue";
import productList from "../../components/frontend/product-list.vue";
import promotion from "@/components/frontend/promotion.vue";
import tabsCategory from "@/components/frontend/tabs-category.vue";
export default {
  components: {
    frontend_navbar,
    imageBanner,
    promotion,
    recommendList,
    productList,
    tabsCategory,
  },

  data() {
    return {};
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
