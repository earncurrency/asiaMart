<template>
  <frontend_navbar :cartsLength="cartsLength" />
  <Modal ref="modal" />

  <div class="flex justify-center pt-24">
    <div
      class="w-full max-w-screen-2xl lg:p-12 lg:border border-gray-200 rounded-lg lg:mb-4 bg-white z-40"
    >
      <div>
        <!-- content -->

        <div class="mt-2 mb-2">
          <div class="w-full rounded-md text-gray-600">
            <p class="mb-6 text-3xl font-semibold pt-4 pr-8 pl-8">ตระกร้า</p>

            <div class="lg:flex lg:gap-8 w-full">
              <div
                class="lg:w-3/4 w-full z-40 pr-8 pl-8 pt-2 lg:h-auto h-[calc(100vh-480px)] overflow-y-auto no-scrollbar"
              >
                <!-- product -->
                <div>
                  <!-- แสดงข้อความเมื่อไม่มีสินค้าในตระกร้า -->
                  <div
                    v-if="carts.length === 0"
                    class="flex flex-col items-center justify-center p-6 border-2 border-dashed border-gray-200 rounded-lg"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-12 w-12 text-gray-400"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"
                      />
                    </svg>
                    <p class="mt-4 text-gray-500 text-lg">
                      ไม่มีสินค้าในตระกร้า
                    </p>
                  </div>

                  <div v-for="(item, index) in carts" :key="index">
                    <div
                      class="relative w-full h-auto bg-gray-50 rounded-md shadow-md text-md mb-4"
                    >
                      <div class="flex gap-4 lg:gap-6 p-2 lg:p-4 rounded-md">
                        <RouterLink :to="`/product-detail/${item.id}`">
                          <div
                            v-if="item.image"
                            class="h-28 w-28 lg:h-32 lg:w-48"
                          >
                            <img
                              :src="`${imageUrl}/api/uploads/${Math.ceil(
                                item.id / 100
                              )}/${item.image}`"
                              alt=""
                              class="w-full h-full object-contain rounded-md"
                            />
                          </div>
                          <div v-else class="h-28 w-28 lg:h-32 lg:w-48">
                            <img
                              class="w-full h-full object-contain rounded-md"
                              :src="`${imageUrl}/src/assets/image/system/product.png`"
                            />
                          </div>
                        </RouterLink>

                        <div class="flex flex-col w-full">
                          <div
                            class="flex justify-between items-center mb-1 lg:mb-2 w-full"
                          >
                            <RouterLink :to="`/product-detail/${item.id}`">
                              <p
                                class="text-mb cursor-pointer overflow-hidden text-ellipsis whitespace-nowrap w-36 lg:w-full"
                              >
                                {{ item.name }}
                              </p>
                            </RouterLink>

                            <button
                              class="absolute -right-2 -top-2 bg-red-500 text-white w-10 h-10 rounded-full justify-center text-md"
                              @click="removeItem(item.id)"
                            >
                              <i class="fa-solid fa-trash-can"></i>
                            </button>
                          </div>
                          <p
                            class="font-semibold text-mb text-orange-500 mb-2 lg:mb-3"
                          >
                            {{ item.price }} บาท
                          </p>
                          <div class="flex items-center bottom-0">
                            <!-- ปุ่มลดจำนวน -->
                            <button
                              class="bg-gray-300 text-gray-600 hover:bg-gray-200 p-2 pr-3 pl-3 focus:outline-none transition rounded-l-md"
                              @click="decrementQuantity(item.id)"
                              :disabled="item.qty <= 1"
                            >
                              -
                            </button>

                            <!-- ช่องกรอกจำนวนสินค้า -->
                            <input
                              @change="inputQuantity(item.id, item.qty)"
                              type="text"
                              class="w-14 text-center border-none focus:outline-none p-2 pr-3 pl-3"
                              v-model.number="item.qty"
                              min="1"
                            />

                            <!-- ปุ่มเพิ่มจำนวน -->
                            <button
                              class="bg-gray-300 text-gray-600 hover:bg-gray-200 p-2 pr-3 pl-3 focus:outline-none transition rounded-r-md"
                              @click="incrementQuantity(item.id)"
                            >
                              +
                            </button>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!--สรุปคำสั่งซื้อ-->
              <div
                class="w-full lg:w-1/4 bg-gray-100 rounded-md lg:rounded-t-md shadow-md p-8 text-md cursor-pointer h-60 z-50"
              >
                <p class="text-xl font-semibold text-gray-600">รวมทั้งหมด</p>

                <hr class="my-2 text-gray-600" />

                <p class="text-mb text-gray-600 mt-4">
                  จำนวน<span class="mr-2 ml-2">{{ carts.length }}</span
                  >รายการ
                </p>

                <div
                  class="flex justify-between text-mb font-semibold text-orange-500"
                >
                  <p class="mb-8">ราคารวม</p>
                  <div class="flex">
                    <span class="">{{ totalAmount }}</span>
                    <span class="ml-2">บาท</span>
                  </div>
                </div>

                <!-- <RouterLink to="/confirm-order">
                  <button class="bg-gray-800 text-white p-2 w-full rounded-md">
                    ยืนยันรายการสินค้า
                  </button>
                </RouterLink> -->
                <button
                  @click="confirmOrder()"
                  class="bg-gray-800 text-white p-2 w-full rounded-md"
                >
                  ยืนยันรายการสินค้า
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* ใช้สำหรับซ่อนแถบเลื่อน */
.no-scrollbar::-webkit-scrollbar {
  display: none;
}

.no-scrollbar {
  -ms-overflow-style: none;
  /* Internet Explorer 10+ */
  scrollbar-width: none;
  /* Firefox */
}
</style>

<script>
import axios from "axios";
import frontend_navbar from "../../components/frontend/navbar.vue";
import Modal from "@/components/frontend/modal.vue";
export default {
  components: { frontend_navbar, Modal },
  data() {
    return {
      apiUrl: __API_URL__,
      baseUrl: __BASE_URL__,
      imageUrl: __IMAGE_URL__,
      carts: [],
      cartsLength: 0,
      member_id: "",
      member: {
        id: "",
        code: "",
      },
    };
  },
  computed: {
    totalAmount() {
      // คำนวณราคารวม
      let total = this.carts.reduce((acc, item) => {
        return acc + item.price * item.qty;
      }, 0);

      return total;
    },
  },
  mounted() {
    this.checkAuth();
  },
  watch: {
    // คอยติดตามการเปลี่ยนแปลงของ carts และอัพเดต cartsLength
    carts(newCarts) {
      this.cartsLength = newCarts.length;
    },
  },
  methods: {
    checkAuth() {
      const storedHash = localStorage.getItem("hash");

      if (!storedHash || storedHash === "") {
        this.$router.push("/login");
      } else {
        this.setdata();
        this.getProductInCart();
      }
    },
    setdata() {
      let storedHash = localStorage.getItem("hash");

      //รหัสพนักงาน
      const codeNumber = storedHash ? storedHash.split("-")[1] : 0;
      this.member.code = codeNumber;
    },
    getProductInCart() {
      if (this.member.code) {
        axios
          .get(`${this.apiUrl}members/code/${this.member.code}`)
          .then((response) => {
            const data = response.data;
            this.member.id = data.row.id;

            //เรียก localStorage carts
            let carts = localStorage.getItem("carts");
            this.carts = JSON.parse(carts) || [];

            // กรองข้อมูลเฉพาะของสมาชิกที่กำลังใช้งาน
            this.carts = this.carts.filter(
              (item) => item.member_id === this.member.id
            );
          })
          .catch((error) => {
            console.error("There was an error fetching the data:", error);
          });
      }
    },

    decrementQuantity(itemId) {
      let carts = localStorage.getItem("carts");
      this.carts = JSON.parse(carts) || [];

      // ค้นหารายการในตะกร้าที่ตรงกับ itemId
      let item = this.carts.find(
        (item) => item.id === itemId && item.member_id === this.member.id
      );

      if (item && item.qty > 1) {
        // ลดจำนวนสินค้า
        item.qty--;

        // อัพเดท localStorage
        localStorage.setItem("carts", JSON.stringify(this.carts));
        // กรองข้อมูลเฉพาะของสมาชิกที่กำลังใช้งาน
        this.carts = this.carts.filter(
          (item) => item.member_id === this.member.id
        );

        // แสดงผลในคอนโซลเพื่อดีบัก
        // console.log(this.carts);
      }
    },

    incrementQuantity(itemId) {
      // ดึงข้อมูลจาก localStorage
      let carts = localStorage.getItem("carts");
      this.carts = JSON.parse(carts) || [];

      // ค้นหารายการในตะกร้าที่ตรงกับ itemId
      let item = this.carts.find(
        (item) => item.id === itemId && item.member_id === this.member.id
      );

      if (item) {
        // เพิ่มจำนวนสินค้า
        item.qty++;

        // อัพเดท localStorage
        localStorage.setItem("carts", JSON.stringify(this.carts));
        // กรองข้อมูลเฉพาะของสมาชิกที่กำลังใช้งาน
        this.carts = this.carts.filter(
          (item) => item.member_id === this.member.id
        );
      }
    },
    inputQuantity(itemId, itemQty) {
      // ดึงข้อมูลจาก localStorage
      let carts = localStorage.getItem("carts");
      this.carts = JSON.parse(carts) || [];

      // ค้นหารายการในตะกร้าที่ตรงกับ itemId
      let item = this.carts.find(
        (item) => item.id === itemId && item.member_id === this.member.id
      );

      if (item) {
        // เพิ่มจำนวนสินค้า
        item.qty = itemQty;

        // อัพเดท localStorage
        localStorage.setItem("carts", JSON.stringify(this.carts));
        // กรองข้อมูลเฉพาะของสมาชิกที่กำลังใช้งาน
        this.carts = this.carts.filter(
          (item) => item.member_id === this.member.id
        );
      }
    },
    removeItem(itemId) {
      // ดึงข้อมูลจาก localStorage
      let carts = localStorage.getItem("carts");
      this.carts = JSON.parse(carts) || [];

      // กรองออก item ที่ตรงกับ itemId และ member_id
      this.carts = this.carts.filter(
        (item) => !(item.id === itemId && item.member_id === this.member.id) // ลบ item ที่ตรงกับเงื่อนไข
      );

      // อัพเดท localStorage ด้วยข้อมูลใหม่ที่กรองแล้ว
      localStorage.setItem("carts", JSON.stringify(this.carts));
      this.cartsLength = this.carts.length;
      // กรองข้อมูลเฉพาะของสมาชิกที่กำลังใช้งาน
      this.carts = this.carts.filter(
        (item) => item.member_id === this.member.id
      );

      console.log("cartsLength:", this.cartsLength);
      console.log("ข้อมูลใน localStorage (ตะกร้าสินค้า):", this.carts);
    },

    confirmOrder() {
      if (!this.member.id) {
        this.$refs.modal.showAlertModal({
          swlIcon: "warning",
          swlTitle: "กรุณาเข้าสู่ระบบ",
          swlText: "กรุณาเข้าสู่ระบบก่อนยืนยันรายการ",
        });
        return;
      }
      if (this.carts.length == 0) {
        this.$refs.modal.showAlertModal({
          swlIcon: "warning",
          swlTitle: "ไม่มีสินค้าในตระกร้า",
          swlText: "กรุณาเพิ่มสินค้าลงในตะกร้าก่อนยืนยันรายการ",
        });
        return;
      }

      this.$router.push("/confirm-order");
      console.log("ข้อมูลใน localStorage (ตะกร้าสินค้า):", this.carts);
    },
  },
};
</script>
