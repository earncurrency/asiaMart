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
            <p class="mb-6 text-3xl font-semibold">ประวัติคำสั่งซื้อ</p>

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
                      :src="`${baseUrl}/assets/image/system/product.png`"
                      alt=""
                      class="h-12 w-12 lg:h-16 lg:w-16 object-cover"
                    />
                    <img
                      v-else-if="order.status === 'pending'"
                      :src="`${baseUrl}/assets/image/system/checklist.png`"
                      alt=""
                      class="h-12 w-12 lg:h-16 lg:w-16 object-cover"
                    />
                    <img
                      v-else-if="order.status === 'delivery'"
                      :src="`${baseUrl}/assets/image/system/delivery-man.png`"
                      alt=""
                      class="h-12 w-12 lg:h-16 lg:w-16 object-cover"
                    />
                    <img
                      v-else-if="order.status === 'success'"
                      :src="`${baseUrl}/assets/image/system/checked.png`"
                      alt=""
                      class="h-12 w-12 lg:h-16 lg:w-16 object-cover"
                    />
                    <img
                      v-else-if="order.status === 'cancel'"
                      :src="`${baseUrl}/assets/image/system/x-button.png`"
                      alt=""
                      class="h-12 w-12 lg:h-16 lg:w-16 object-cover"
                    />
                    <img
                      v-else
                      :src="`${baseUrl}/assets/image/system/warning.png`"
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
                        <p
                          class="font-semibold"
                          v-else-if="order.status === 'cancel'"
                        >
                          ยกเลิก
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
                  ไม่มีประวัติคำสั่งซื้อ
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
import frontend_navbar from "../../components/frontend/navbar.vue";
import axios from "axios";
export default {
  components: { frontend_navbar },
  data() {
    return {
      baseUrl: __BASE_URL__,
      apiUrl: __API_URL__,

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

      member: {
        id: "",
        code: "",
        name: "",
        phone: "",
      },
    };
  },
  mounted() {
    this.checkAuth();
  },

  methods: {
    checkAuth() {
      const storedHash = localStorage.getItem("hash");

      if (!storedHash || storedHash === "") {
        this.$router.push("/login");
      } else {
        this.setdata();
        this.getListOrder();
      }
    },
    setdata() {
      let storedHash = localStorage.getItem("hash");

      const codeNumber = storedHash ? storedHash.split("-")[1] : 0;
      this.member.code = codeNumber;
    },

    async getMember() {
      if (this.member.code) {
        await axios
          .get(`${this.apiUrl}members/code/${this.member.code}`)
          .then((response) => {
            const data = response.data;
            this.member.id = data.row.id;
          })
          .catch((error) => {
            console.error("There was an error fetching the data:", error);
          });
      }
    },
    async getListOrder() {
      // รอให้ getMember ทำงานเสร็จก่อน
      await this.getMember();

      try {
        const response = await axios.get(`${this.apiUrl}orders/`, {
          params: {
            member_id: this.member.id, 
          },
        });
        const data = response.data;
        this.orders = data.rows;
      } catch (error) {
        console.error("There was an error fetching the data:", error);
      }

      console.log(this.orders);
    },
  },
};
</script>
