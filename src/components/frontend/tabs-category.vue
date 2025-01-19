<script setup>

import axios from "axios";
</script>
<template>
  <ul
    class="flex flex-wrap justify-center text-md font-medium text-center mt-4 lg:mt-0 text-gray-500 dark:text-gray-400"
  >
    <li v-for="(category, index) in categorys" :key="index" class="me-2">
      <RouterLink :to="`/category/${category.id}`">
        <a
          href="#"
          class="inline-block px-4 py-3 rounded-lg hover:text-gray-900 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-white"
          >{{ category.name }}</a
        >
      </RouterLink>
    </li>
  </ul>
</template>

<script>
export default {
  data() {
    return {
        apiUrl: "http://127.0.0.1:8000/",

        categorys: {
            id: "",
            name: "",
        },

    };
  },
  mounted() {
    this.getListCategory();

  },
  methods: {
    
    async getListCategory() {
      this.categoryStatus = "active";

      await axios
        .get(`${this.apiUrl}category/`, {
          params: { category_status: this.categoryStatus },
        })
        .then((response) => {
          const data = response.data;
          this.categorys = data.rows;
          console.log(this.categorys);
        })
        .catch((error) => {
          console.error("There was an error fetching the data:", error); // แสดงข้อผิดพลาด
        });
    },
  },
};
</script>
