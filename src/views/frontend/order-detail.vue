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
            <p class="mb-6 text-3xl font-semibold">รายละเอียดคำสั่งซื้อ</p>

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
                  v-if="order.status === 'pending'"
                  :src="`${baseUrl}/assets/image/system/checklist.png`"
                  alt=""
                  class="h-12 w-12 lg:h-16 lg:w-16 object-cover"
                />
                <img
                  v-if="order.status === 'delivery'"
                  :src="`${baseUrl}/assets/image/system/delivery-man.png`"
                  alt=""
                  class="h-12 w-12 lg:h-16 lg:w-16 object-cover"
                />
                <img
                  v-if="order.status === 'success'"
                  :src="`${baseUrl}/assets/image/system/checked.png`"
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
                    <p class="font-semibold" v-if="order.status === 'pending'">
                      กำลังเตรียมสินค้า
                    </p>
                    <p class="font-semibold" v-if="order.status === 'delivery'">
                      กำลังจัดส่ง
                    </p>
                    <p class="font-semibold" v-if="order.status === 'success'">
                      สำเร็จ
                    </p>
                  </div>
                </div>
              </div>
            </div>

            <!--ข้อมูลลูกค้า-->
            <div class="mb-8">
              <div
                class="p-4 text-md text-gray-600 rounded-lg bg-gray-50 shadow-md"
              >
                <div class="mb-5">
                  <label class="block text-md font-medium text-gray-900 mb-3"
                    >รหัสพนักงาน</label
                  >
                  <input
                    v-model="order.member_code"
                    type="text"
                    class="bg-gray-50 border border-gray-300 text-orange-500 text-md rounded-lg focus:border-gray-300 block w-full p-2"
                    disabled
                  />
                </div>
                <div class="mb-5">
                  <label class="block text-md font-medium text-gray-900 mb-3"
                    >ชื่อผู้รับสินค้า</label
                  >
                  <input
                    v-model="order.member_name"
                    type="text"
                    class="bg-gray-50 border border-gray-300 text-orange-500 text-md rounded-lg focus:border-gray-300 block w-full p-2"
                    disabled
                  />
                </div>
                <div class="mb-5">
                  <label class="block text-md font-medium text-gray-900 mb-2"
                    >เบอร์โทร</label
                  >
                  <input
                    v-model="order.member_phone"
                    type="text"
                    class="bg-gray-50 border border-gray-300 text-orange-500 text-md rounded-lg focus:border-gray-300 block w-full p-2"
                    disabled
                  />
                </div>
                <div class="mb-5">
                  <span class="text-gray-700">ที่อยู่ในการจัดส่ง</span>
                  <label class="flex items-center space-x-2 mt-4">
                    <input
                      checked
                      type="radio"
                      name="deliveryOption"
                      value="0"
                      class="h-4 w-4 text-gray-600 border-gray-300 focus:ring-gray-500 cursor-pointer"
                    />
                    <span class="text-gray-700">{{ order.address }}</span>
                  </label>
                </div>
              </div>
            </div>

            <div class="mb-8">
              <p class="mb-2 text-xl font-semibold">รายการสินค้า</p>
              <div
                class="bg-gray-50 shadow-md p-4 rounded-md grid grid-rows-auto gap-4"
              >
                <!-- สินค้า -->
                <div
                  v-for="(product, index) in order.products"
                  :key="index"
                  class="flex items-center p-4 border border-gray-200 rounded-lg cursor-pointer"
                >
                  <!-- รูปภาพสินค้า -->
                  <div
                    class="flex-shrink-0 w-24 h-24 rounded-lg overflow-hidden"
                  >
                    <img
                      v-if="product.images.path"
                      :src="`${imageUrl}/api/uploads/${Math.ceil(
                        product.id / 100
                      )}/${product.images.path}`"
                      alt="Product Image Preview"
                      class="w-full h-full object-cover"
                    />
                    <img
                      v-else
                      :src="`${imageUrl}/src/assets/image/system/product.png`"
                      alt="Default Product Image"
                      class="w-full h-full object-cover"
                    />
                  </div>

                  <!-- รายละเอียดสินค้า -->
                  <div class="ml-4 flex-1">
                    <p
                      class="text-lg font-medium text-gray-800 overflow-hidden text-ellipsis whitespace-nowrap w-36 lg:w-full"
                    >
                      {{ product.product_name }}
                    </p>
                    <div class="flex justify-between">
                      <p class="text-lg font-semibold text-orange-500">
                        {{ product.product_price }} บาท
                      </p>
                      <p class="text-gray-600">จำนวน X{{ product.qty }}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!--สรุปคำสั่งซื้อ-->
            <p class="mb-2 text-xl font-semibold">สรุปคำสั่งซื้อ</p>
            <div
              class="w-full bg-gray-50 rounded-md lg:rounded-t-md shadow-md p-4 text-md cursor-pointer"
            >
              <p class="text-mb text-gray-600 mt-2">
                จำนวน<span class="mr-2 ml-2">{{ order.length }}</span
                >รายการ
              </p>

              <div
                class="flex justify-between text-mb font-semibold text-orange-500 text-2xl"
              >
                <p class="mb-2">ยอดชำระ</p>
                <div class="flex">
                  <span class="">{{ order.total }}</span>
                  <span class="ml-2">บาท</span>
                </div>
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
  props: {
    orderId: {
      required: true,
    },
  },
  data() {
    return {
      baseUrl: __BASE_URL__,
      apiUrl: __API_URL__,
      imageUrl: __IMAGE_URL__,
      order: {
        id: "",
        code: "",
        order_date: "",
        member_id: "",
        member_code: "",
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
        this.getOrder();
      }
    },
    async getOrder() {
      try {
        const response = await axios.get(
          `${this.apiUrl}orders/${this.orderId}`
        );
        this.order = response.data.row;
        console.log(this.order);
      } catch (error) {
        console.error("Error fetching product:", error);
      }
    },
  },
};
</script>
