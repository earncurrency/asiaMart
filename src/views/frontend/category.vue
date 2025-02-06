<script setup>
import { useRoute } from "vue-router";
import frontend_navbar from "../../components/frontend/navbar.vue";
import productList from "../../components/frontend/product-list.vue";
import tabsCategory from "../../components/frontend/tabs-category.vue";
</script>

<template>
  <frontend_navbar />

  <div class="flex justify-center pt-24 p-4">
    <div
      class="w-full max-w-screen-2xl lg:p-12 lg:border border-gray-200 rounded-lg mb-16 lg:mb-4 bg-white z-40"
    >
      <div>

        
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
  data() {
    return {};
  },
  methods: {},
};
</script>
