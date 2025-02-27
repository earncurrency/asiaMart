<template>
  <frontend_navbar />

  <div class="flex justify-center pt-24 p-4">
    <div
      class="w-full max-w-screen-2xl lg:p-12 lg:border border-gray-200 rounded-lg mb-16 lg:mb-4 bg-white z-40"
    >
      <div>
        <div class="flex justify-center">
          <p class="text-3xl font-semibold mt-8 mb-4 lg:mb-16">
            ผลลัพธ์สำหรับ "{{ searchQuery }}"
          </p>
        </div>
        <!-- content -->
        <productList :searchQuery="searchQuery"/>
      </div>
    </div>
  </div>
</template>

<script>
import frontend_navbar from "../../components/frontend/navbar.vue";
import productList from "../../components/frontend/product-list.vue";
export default {
  components: { frontend_navbar, productList },
  props: {
    searchQuery : {
      type: String,
      required: true,
    },
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
