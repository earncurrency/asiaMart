<script setup>
import axios from "axios";
</script>

<template>
  <div class="grid grid-cols-1 lg:grid-cols-4 gap-4">
    <div class="w-full rounded-md shadow-md">
      <div
        class="p-4 flex justify-between items-center bg-gray-800 text-white rounded-t-md"
      >
        <div>
          <p class="text-2xl font-semibold">{{ productTotal }}</p>
          <p class="text-md">จำนวนสินค้า</p>
        </div>
        <div
          class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500"
        >
          <i class="fa-solid fa-boxes-packing"></i>
        </div>
      </div>
      <RouterLink to="/backend/manage-product">
        <div
          class="flex justify-between items-center p-2 bg-gray-100 text-sm text-blue-500 cursor-pointer rounded-b-md"
        >
          <p>ดูทั้งหมด</p>
          <i class="fa-solid fa-circle-arrow-right"></i>
        </div>
      </RouterLink>
    </div>
    <div class="w-full rounded-md shadow-md">
      <div
        class="p-4 flex justify-between items-center bg-gray-800 text-white rounded-t-md"
      >
        <div>
          <p class="text-2xl font-semibold">{{ memberTotal }}</p>
          <p class="text-md">จำนวนลูกค้า</p>
        </div>
        <div
          class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500"
        >
          <i class="fa-solid fa-users"></i>
        </div>
      </div>
      <RouterLink to="/backend/manage-member">
        <div
          class="flex justify-between items-center p-2 bg-gray-100 text-sm text-blue-500 cursor-pointer rounded-b-md"
        >
          <p>ดูทั้งหมด</p>
          <i class="fa-solid fa-circle-arrow-right"></i>
        </div>
      </RouterLink>
    </div>
    <div class="w-full rounded-md shadow-md">
      <div
        class="p-4 flex justify-between items-center bg-gray-800 text-white rounded-t-md"
      >
        <div>
          <p class="text-2xl font-semibold">{{ orderTotal }}</p>
          <p class="text-md">จำนวนคำสั่งซื้อ</p>
        </div>
        <div
          class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500"
        >
          <i class="fa-solid fa-list-check"></i>
        </div>
      </div>
      <RouterLink to="/backend/manage-order">
        <div
          class="flex justify-between items-center p-2 bg-gray-100 text-sm text-blue-500 cursor-pointer rounded-b-md"
        >
          <p>ดูทั้งหมด</p>
          <i class="fa-solid fa-circle-arrow-right"></i>
        </div>
      </RouterLink>
    </div>
    <div class="w-full rounded-md shadow-md">
      <div
        class="p-4 flex justify-between items-center bg-gray-800 text-white rounded-t-md"
      >
        <div>
          <p class="text-2xl font-semibold">{{ total_sales }}</p>
          <p class="text-md">ยอดขาย</p>
        </div>
        <div
          class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500"
        >
          <i class="fa-solid fa-baht-sign"></i>
        </div>
      </div>
      <div
        class="flex justify-between items-center p-2 bg-gray-100 text-sm text-blue-500 cursor-pointer rounded-b-md"
      >
        <p>ดูทั้งหมด</p>
        <i class="fa-solid fa-circle-arrow-right"></i>
      </div>
    </div>
  </div>
</template>

<script>
export default {

  data() {
    return {
      apiUrl: "http://127.0.0.1:8000/",

      productTotal: "",
      memberTotal: "",
      orderTotal: "",
      total_sales: "",

    };
  },
  mounted() {
    this.getTotal();
  },
  methods: {

    async getTotal() {
      await axios
        .get(`${this.apiUrl}dashboard/total/`)
        .then((response) => {
          const data = response.data;
          console.log("data", response.data);

          this.productTotal = data.product;
          this.memberTotal = data.member;
          this.orderTotal= data.order;
          this.total_sales = data.total_sales;
        })
        .catch((error) => {
          console.error("There was an error fetching the data:", error);
        });
    },

  },
};
</script>