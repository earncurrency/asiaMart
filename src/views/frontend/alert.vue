<script setup>
import frontend_navbar from "../../components/frontend/navbar.vue";
</script>
<template>
  <frontend_navbar />
  <div class="flex justify-center pt-24 p-4">
    <div
      class="w-full lg:w-2/4 max-w-screen-2xl lg:p-12 lg:border border-gray-200 rounded-lg mb-16 lg:mb-4 bg-white z-40"
    >
      <div>
        <!-- content -->

        <div class="mt-2 mb-2">
          <div class="p-4 w-full rounded-md text-gray-600">
            <p class="mb-6 text-3xl font-semibold">เเจ้งเตือน</p>

            <RouterLink to="/order-detail">
              <div
                class="p-4 mb-4 text-md text-gray-600 rounded-lg bg-gray-50 cursor-pointer relative shadow-md"
                role="alert"
              >
                <span class="font-semibold block lg:inline"
                  >เลขที่
                  <span class="text-orange-500">78945623</span> อยู่ในสถานะ
                  'จัดเตรียมสินค้า'</span
                >
                <span class="block lg:inline">
                  วันที่ 2024/12/06 เวลา 09:31
                </span>

                <span
                  class="hidden lg:block absolute right-3 top-1/2 transform -translate-y-1/2"
                >
                  <i class="fa-solid fa-angle-right"></i>
                </span>
              </div>
            </RouterLink>

            <div
              class="p-4 mb-4 text-md text-gray-600 rounded-lg bg-gray-50 cursor-pointer relative shadow-md text-center"
              role="alert"
            >
              <span class="font-semibold block lg:inline mx-auto"
                >ไม่มีการแจ้งเตือน</span
              >
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
