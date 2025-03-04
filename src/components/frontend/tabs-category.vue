<script setup>
import axios from "axios";
</script>
<template>
  <div
    class="title-content lg:flex items-center justify-between font-medium mt-4 gap-4 p-4 lg:p-0"
  >
    <div class="flex items-center max-w-xl lg:w-1/3">
      <!-- <label for="voice-search" class="sr-only">Search</label> -->

      <div class="relative w-full">
        <input
          type="text"
          v-model="searchText"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full pl-3 pr-12 p-2.5 focus:border-gray-300"
          placeholder="ค้นหา..."
        />
        <button
          @click="searchBtn"
          class="absolute inset-y-0 end-0 flex items-center ps-3 p-3 pointer text-white bg-gray-800 rounded-lg"
        >
          <i class="fa-solid fa-search"></i>
        </button>
      </div>
    </div>
    <div class="lg:flex justify-center">
      <ul
        class="flex flex-wrap justify-center text-md font-medium text-center mt-4 lg:mt-0 text-gray-500 dark:text-gray-400"
      >
        <RouterLink :to="`/category/0/ทั้งหมด`" @click="clickCate('')">
          <a
            href="#"
            class="inline-block px-4 py-3 rounded-lg hover:text-gray-900 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-white"
            >ทั้งหมด</a
          >
        </RouterLink>
        <li v-for="(category, index) in categorys" :key="index" class="me-2">
          <RouterLink
            :to="`/category/${category.id}/${category.name}`"
            @click="clickCate(category.id)"
          >
            <a
              href="#"
              class="inline-block px-4 py-3 rounded-lg hover:text-gray-900 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-white"
              >{{ category.name }}</a
            >
          </RouterLink>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      apiUrl: __API_URL__,
      searchText: "",
      categorys: [],
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
          // console.log(this.categorys);
        })
        .catch((error) => {
          console.error("There was an error fetching the data:", error); // แสดงข้อผิดพลาด
        });
    },
    searchBtn() {
      if (this.searchText !== "") {
        this.$router.push(`/search/${this.searchText}`);
      }
    },
    clickCate(catId) {
      this.$emit("clickCategory", catId);
    },
  },
};
</script>
