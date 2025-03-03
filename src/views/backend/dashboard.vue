<script setup>
import axios from "axios";
import backend_navbar from "@/components/backend/navbar.vue";
import dashboard_card from "@/components/backend/dashboard/card.vue";
import dashboard_chart from "@/components/backend/dashboard/chart.vue";
</script>

<template>
  <backend_navbar />
  <div class="p-4 lg:pr-24 lg:pl-24 pt-6 sm:ml-64">
    ๅ
    <div
      class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-14"
    >
      <div class="lg:p-4 mt-2 mb-2">
        <div class="w-full rounded-md text-gray-600">
          <!-- title -->
          <div class="flex gap-2 items-center mb-2">
            <p class="text-3xl font-semibold">หน้าเเรก</p>
          </div>

          <div class="w-full gap-2 mb-2 pt-1 mt-4">
            <!-- grid card -->
            <dashboard_card />

            <!-- grid chart -->
            <div class="p-4 flex justify-start gap-4 items-center mt-8">
              <p class="text-2xl font-semibold">กราฟแสดงยอดขายรายเดือน</p>
            </div>
            <dashboard_chart />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  mounted() {
    this.checkAuth();
  },
  methods: {
    checkAuth() {
      const adminRole = localStorage.getItem("admin_role");

      if (adminRole !== "admin") {
        this.$router.push("/backend/login");
      } else {
      }
    },
  },
};
</script>
