<script setup>
import frontend_navbar from "../../components/frontend/navbar.vue";
import axios from "axios";
</script>

<template>
  <frontend_navbar />
  <div class="flex justify-center pt-24 p-4">
    <div
      class="w-full lg:w-2/4 max-w-screen-2xl lg:p-12 lg:border border-gray-200 rounded-lg mb-16 lg:mb-4 bg-white z-40"
    >
      <div>
        <!-- content -->
        <div
          class="mt-4 mb-2 bg-gray-100 p-8 rounded-md flex lg:justify-center gap-4 lg:gap-8 items-center lg:flex-row flex-col text-center lg:text-left"
        >
          <img
            src="../../assets/image/system/cathothead.jpg"
            alt=""
            class="h-28 w-28 lg:h-40 lg:w-40 rounded-full bg-gray-300 object-cover ring-4 ring-gray-300 shadow-md mx-auto lg:mx-0"
          />

          <div class="text-gray-600 text-md">
            <p class="text-2xl lg:text-3xl font-semibold">{{ fullname }}</p>
            <div class="lg:flex gap-4 mt-2">
              <div class="flex gap-2 justify-center lg:justify-start">
                <p class="font-semibold">รหัสพนักงาน :</p>
                <p>{{ member_id }}</p>
              </div>
            </div>
            <div class="lg:flex gap-4 mb-2">
              <div class="flex gap-2 justify-center lg:justify-start">
                <p class="font-semibold">เบอร์มือถือ :</p>
                <p>0xx xxx xxxx</p>
              </div>
              <!-- <div class="flex gap-2 justify-center lg:justify-start">
                <p class="font-semibold">ไลน์ :</p>
                <p>kornwsn04</p>
              </div> -->
            </div>
            <button
              class="p-2 pr-4 pl-4 rounded-lg bg-red-600 text-white mt-2 hover:bg-red-500 transition"
            >
              ออกจากระบบ
            </button>
          </div>
        </div>

        <div class="flex justify-end">
          <RouterLink to="/history">
            <button
              class="p-2 pr-4 pl-4 bg-gray-300 rounded-md text-md text-gray-600 hover:bg-gray-200 transition"
            >
              <i class="fa-solid fa-clock-rotate-left"></i> ประวัติคำสั่งซื้อ
            </button>
          </RouterLink>
        </div>

        <div class="mt-2 mb-2">
          <div class="p-4 w-ful rounded-md text-gray-600">
            <p class="mb-4 text-md">
              <i class="fa-solid fa-box"></i> ติดตามสถานะสินค้า
            </p>

            <div v-if="orders.length > 0">
              <RouterLink
                v-for="(order, index) in orders"
                :key="index"
                :to="`/order-detail/${order.id}`"
              >
                <div
                  class="w-full h-auto bg-gray-50 rounded-md p-4 shadow-md text-md cursor-pointer mb-4"
                >
                  <div class="flex gap-2">
                    <p>วันที่</p>
                    <p class="font-semibold">{{ order.order_date }}</p>
                  </div>

                  <div
                    class="flex items-center gap-4 border p-2 lg:p-4 rounded-md mt-3 mb-3"
                  >
                    <img
                      v-if="order.status === 'new'"
                      :src="`${baseUrl}/src/assets/image/system/product.png`"
                      alt=""
                      class="h-12 w-12 lg:h-16 lg:w-16 object-cover"
                    />
                    <img
                      v-else-if="order.status === 'pending'"
                      :src="`${baseUrl}/src/assets/image/system/checklist.png`"
                      alt=""
                      class="h-12 w-12 lg:h-16 lg:w-16 object-cover"
                    />
                    <img
                      v-else-if="order.status === 'delivery'"
                      :src="`${baseUrl}/src/assets/image/system/delivery-man.png`"
                      alt=""
                      class="h-12 w-12 lg:h-16 lg:w-16 object-cover"
                    />
                    <img
                      v-else
                      :src="`${baseUrl}/src/assets/image/system/warning.png`"
                      alt=""
                      class="h-12 w-12 lg:h-16 lg:w-16 object-cover"
                    />
                    <div>
                      <div class="flex gap-2 mt-1">
                        <p class="">เลขที่ :</p>
                        <p class="font-semibold">{{ order.code }}</p>
                      </div>

                      <div class="flex gap-2 mt-1">
                        <p class="">สถานะ :</p>
                        <p class="font-semibold" v-if="order.status === 'new'">
                          รอรับออเดอร์
                        </p>
                        <p
                          class="font-semibold"
                          v-else-if="order.status === 'pending'"
                        >
                          กำลังเตรียมสินค้า
                        </p>
                        <p
                          class="font-semibold"
                          v-else-if="order.status === 'delivery'"
                        >
                          กำลังจัดส่ง
                        </p>
                        <p
                          class="font-semibold"
                          v-else-if="order.status === 'success'"
                        >
                          สำเร็จ
                        </p>
                        <p class="font-semibold" v-else>ไม่พบสถานะ</p>
                      </div>
                    </div>
                  </div>

                  <div class="lg:flex lg:justify-end gap-4">
                    <div class="flex gap-2">
                      <p>จำนวนสินค้า :</p>
                      <p class="">{{ order.length }} ชิ้น</p>
                    </div>
                    <div class="flex gap-2 text-orange-500">
                      <p>ราคารวม :</p>
                      <p class="font-semibold">{{ order.total }} บาท</p>
                    </div>
                  </div>
                </div>
              </RouterLink>
            </div>

            <div
              v-else
              class="w-full h-auto bg-gray-50 rounded-md p-4 shadow-md text-md cursor-pointer mb-4"
            >
              <div
                class="flex items-center justify-center gap-4 border p-2 lg:p-4 rounded-md mt-3 mb-3"
              >
                <img
                  src="../../assets/image/system/shopping-basket.png"
                  alt=""
                  class="h-10 w-10 lg:h-14 lg:w-14 object-cover"
                />
                <p class="font-semibold text-md lg:text-2xl">
                  ไม่มีรายการสั่งซื้อ
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      baseUrl: __BASE_URL__,
      apiUrl: "http://127.0.0.1:8000/",

      orders: [],
      order: {
        id: "",
        code: "",
        order_date: "",
        member_id: "",
        member_name: "",
        member_phone: "",
        address: "",
        total: "",
        status: "",
        length: "",
        details: "",
        info: "",
        products: [],
      },

      order_status: "",
      fullname: "",
      member_id: "",
    };
  },
  mounted() {
    this.setdata();
    this.getListOrder();
  },

  methods: {
    setdata() {
      let storedHash = localStorage.getItem("hash");
      const firstNumber = storedHash.split("-")[0];
      this.member_id = firstNumber;

      let storedFullname = localStorage.getItem("fullname");
      this.fullname = storedFullname;
    },

    async getListOrder() {
      this.setdata();
      this.orders_status = "pending";

      await axios
        .get(`${this.apiUrl}orders/`, {
          params: {
            member_id: this.member_id,
            orders_status: this.orders_status,
          },
        })
        .then((response) => {
          const data = response.data;
          this.orders = data.rows;
          console.log(this.orders);
        })
        .catch((error) => {
          console.error("There was an error fetching the data:", error);
        });
    },
  },
};
</script>
