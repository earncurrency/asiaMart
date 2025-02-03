<script setup>
import { useRoute } from "vue-router";
import frontend_navbar from "../../components/frontend/navbar.vue";
import productList from "../../components/frontend/product-list.vue";
import tabsCategory from "../../components/frontend/tabs-category.vue";
</script>

<template>
  <frontend_navbar />

  <div class="flex justify-center lg:pt-24 p-4">
    <div
      class="w-full max-w-screen-2xl lg:p-12 lg:border border-gray-200 rounded-lg mb-16 lg:mb-4 bg-white z-40"
    >
      <div>
        <!-- Title -->
        <!-- ปุ่มนี้จะแสดงเมื่อจอเล็ก -->
        <div class="flex items-center gap-4 lg:hidden">
          <RouterLink to="/">
            <button class="px-2 py-1 bg-gray-800 rounded-md text-white text-sm">
              <i class="fa-solid fa-arrow-left"></i>
            </button>
          </RouterLink>
        </div>

        <div
          class="lg:flex items-center justify-between font-medium p-4 lg:p-0"
        >
          <!-- ปุ่มนี้จะแสดงเมื่อจอใหญ่ -->
          <div class="flex justify-center gap-4">
            <div class="hidden lg:flex items-center gap-4">
              <RouterLink to="/">
                <button
                  class="px-2 py-1 bg-gray-800 rounded-md text-white text-sm"
                >
                  <i class="fa-solid fa-arrow-left"></i>
                </button>
              </RouterLink>
            </div>
            <!-- แสดงชื่อผลิตภัณฑ์ที่ดึงมาจาก URL -->
            <!-- <p class="text-3xl font-semibold">{{ categoryName }}</p> -->
            <!-- แสดงชื่อผลิตภัณฑ์ -->
          </div>

          <!-- tabs menu -->
          <tabsCategory />
        </div>

        <hr class="my-2 text-gray-600" />

        <!-- content -->
        <productList :categoryId="categoryId" />
      </div>
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
};
</script>
