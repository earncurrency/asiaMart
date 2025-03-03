<template>
  <frontend_navbar :cartsLength="cartsLength" />
  <Modal ref="modal" @clearLocalStorage="clearLocalStorage" />

  <div class="flex justify-center pt-24">
    <div
      class="w-full max-w-screen-2xl lg:p-12 lg:border border-gray-200 rounded-lg lg:mb-4 bg-white z-40"
    >
      <div>
        <!-- content -->

        <div class="mt-2 mb-2">
          <div class="w-full rounded-md text-gray-600">
            <p class="mb-6 text-3xl font-semibold pt-4 pr-8 pl-8">
              ยืนยันรายการสินค้า
            </p>

            <div class="lg:flex lg:gap-8 w-full">
              <div
                class="lg:w-3/4 w-full z-40 pr-8 pl-8 pt-2 lg:h-auto h-[calc(100vh-480px)] overflow-y-auto no-scrollbar"
              >
                <!--ข้อมูลลูกค้า-->
                <div class="mb-8">
                  <p class="mb-2 text-xl font-semibold">ข้อมูลลูกค้า</p>
                  <div
                    class="p-4 text-md text-gray-600 rounded-lg bg-gray-50 shadow-md"
                  >
                    <div class="mb-5">
                      <label
                        class="block text-md font-medium text-gray-900 mb-3"
                        >ชื่อผู้รับสินค้า</label
                      >
                      <input
                        v-model="member.name"
                        type="text"
                        class="bg-gray-50 border border-gray-300 text-orange-500 text-md rounded-lg focus:border-gray-300 block w-full p-2"
                        value=""
                        disabled
                      />
                    </div>
                    <div class="mb-5">
                      <div class="flex justify-between mb-2 items-center">
                        <label class="block text-md font-medium text-gray-900"
                          >เบอร์โทรศัพท์</label
                        >
                        <button
                          @click="changePhone"
                          class="py-1 px-2 shadow-md rounded-md bg-gray-800 text-white"
                        >
                          <i class="fa-regular fa-pen-to-square"></i>
                          เเก้ไขเบอร์
                        </button>
                      </div>
                      <input
                        v-if="inputNowPhone"
                        v-model="member.phone"
                        type="text"
                        class="bg-gray-50 border border-gray-300 text-orange-500 text-md rounded-lg focus:border-gray-300 block w-full p-2"
                        value=""
                        disabled
                      />
                      <input
                        v-show="inputNewPhone"
                        v-model="newPhone"
                        ref="inputNewPhone"
                        type="text"
                        :class="{
                          'bg-white border border-gray-300 text-orange-500 text-md rounded-lg focus:border-gray-300 block w-full p-2 focus': true,
                          'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                            !newPhone,
                        }"
                        value=""
                      />
                      <div v-show="boxBtn" class="flex justify-end mt-2 gap-1">
                        <button
                          @click="saveNewPhone"
                          class="py-1 px-2 rounded-md bg-orange-500 text-white"
                        >
                          บันทึก
                        </button>
                        <button
                          @click="cancelChangePhone"
                          class="py-1 px-2 rounded-md bg-white text-gray-500 ring-1 ring-gray-300"
                        >
                          ยกเลิก
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
                <!--ที่อยู่จัดส่ง-->
                <div class="mb-8">
                  <p class="mb-2 text-xl font-semibold">ที่อยู่จัดส่ง</p>
                  <div
                    class="p-4 lg:flex gap-6 text-md text-gray-600 rounded-lg bg-gray-50 shadow-md"
                  >
                    <label class="flex items-center space-x-2 cursor-pointer">
                      <input
                        type="radio"
                        name="deliveryOption"
                        value="Asia Mart"
                        v-model="deliveryOption"
                        class="h-4 w-4 text-gray-600 border-gray-300 focus:ring-gray-500 cursor-pointer"
                      />
                      <span class="text-gray-700">รับที่ Asia Mart</span>
                    </label>
                    <label
                      class="flex items-center space-x-2 pt-4 lg:pt-0 cursor-pointer"
                    >
                      <input
                        type="radio"
                        name="deliveryOption"
                        value="สาขาบางมด"
                        v-model="deliveryOption"
                        class="h-4 w-4 text-gray-600 border-gray-300 focus:ring-gray-500 cursor-pointer"
                      />
                      <span class="text-gray-700">สาขาบางมด</span>
                    </label>
                    <label
                      class="flex items-center space-x-2 pt-4 lg:pt-0 cursor-pointer"
                    >
                      <input
                        type="radio"
                        name="deliveryOption"
                        value="สาขาบ้านเเพ้ว"
                        v-model="deliveryOption"
                        class="h-4 w-4 text-gray-600 border-gray-300 focus:ring-gray-500"
                      />
                      <span class="text-gray-700">สาขาบ้านเเพ้ว</span>
                    </label>
                    <label
                      class="flex items-center space-x-2 pt-4 lg:pt-0 cursor-pointer"
                    >
                      <input
                        type="radio"
                        name="deliveryOption"
                        value="สาขามหาชัย"
                        v-model="deliveryOption"
                        class="h-4 w-4 text-gray-600 border-gray-300 focus:ring-gray-500"
                      />
                      <span class="text-gray-700">สาขามหาชัย</span>
                    </label>
                  </div>
                </div>
                <!--รายการสินค้า-->
                <div class="mb-8">
                  <p class="mb-2 text-xl font-semibold">รายการสินค้า</p>
                  <div
                    class="bg-gray-50 shadow-md p-4 rounded-md grid grid-rows-auto gap-4"
                  >
                    <!-- สินค้า -->

                    <div
                      v-if="carts.length === 0"
                      class="w-full h-auto rounded-md text-md cursor-pointer border bg-gray-50"
                    >
                      <div class="flex gap-4 lg:gap-6 p-2 lg:p-4 rounded-md">
                        <div class="w-full">
                          <div class="flex items-center justify-center">
                            <h1 class="text-center">ไม่มีสินค้าในตระกร้า</h1>
                          </div>
                        </div>
                      </div>
                    </div>

                    <div v-for="(item, index) in carts" :key="index">
                      <div
                        class="w-full h-auto rounded-md text-md cursor-pointer border bg-gray-50"
                      >
                        <div class="flex gap-4 lg:gap-6 p-2 lg:p-4 rounded-md">
                          <div class="h-20 w-48 object-cover rounded-md">
                            <img
                              :src="`${imageUrl}/api/uploads/${Math.ceil(
                                item.id / 100
                              )}/${item.image}`"
                              alt=""
                              class="w-full h-full object-cover rounded-md"
                            />
                          </div>
                          <div class="w-full">
                            <div class="flex justify-between">
                              <p class="text-mb mb-1 lg:mb-2">
                                {{ item.name }}
                              </p>
                              <p
                                class="font-semibold text-mb text-orange-500 mb-2 lg:mb-3"
                              >
                                {{ item.price }} บาท
                              </p>
                            </div>
                            <div class="flex justify-end">
                              <p class="text-mb mb-2 lg:mb-3">
                                จำนวน X{{ item.qty }}
                              </p>
                            </div>
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
                <p class="text-xl font-semibold text-gray-600">
                  สรุปคำสั่งซื้อ
                </p>

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

                <button
                  @click="confirmOrder()"
                  class="bg-gray-800 text-white p-2 w-full rounded-md"
                >
                  สั่งซื้อ
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
      deliveryOption: "",
      carts: [],
      cartsLength: 0,

      member: {
        id: "",
        code: "",
        name: "",
        phone: "",
      },
      order: {
        code: "",
      },

      // isFocus: false,

      newPhone: "",
      inputNowPhone: true,
      inputNewPhone: false,
      boxBtn: false,
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
        this.getMember();
      }
    },
    setdata() {
      //ข้อมูลจาก hash
      let storedHash = localStorage.getItem("hash");

      //รหัสพนักงาน
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
            this.member.name = data.row.name;
            this.member.phone = data.row.phone;

            if (!this.member.phone) {
              this.inputNowPhone = false;
              this.inputNewPhone = true;
              this.boxBtn = true;
            } else {
              this.inputNowPhone = true;
              this.inputNewPhone = false;
            }

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

    changePhone() {
      this.inputNowPhone = false;
      this.inputNewPhone = true;
      this.boxBtn = true;
      this.$nextTick(() => {
        this.$refs.inputNewPhone.focus();
      });
      return;
    },

    async saveNewPhone() {
      if (!this.newPhone) {
        this.$refs.inputNewPhone.focus();
      } else {
        try {
          const dataMember = {
            phone: this.newPhone,
          };

          const response = await axios.put(
            `${this.apiUrl}members/code/${this.member.code}`,
            dataMember
          );
          if (response.status === 200) {
            this.getMember();
            this.inputNowPhone = true;
            this.inputNewPhone = false;
            this.boxBtn = false;
          }
        } catch (error) {
          console.error("เกิดข้อผิดพลาดในการบันทึกเบอร์โทรศัพท์ใหม่:", error);
          this.$refs.modal.showAlertModal({
            swlIcon: "error",
            swlTitle: "เกิดข้อผิดพลาด",
            swlText: "ไม่สามารถบันทึกได้",
          });
        }
      }
    },

    cancelChangePhone() {
      this.newPhone = "";
      this.inputNowPhone = true;
      this.inputNewPhone = false;
      this.boxBtn = false;
    },

    async confirmOrder() {
      if (!this.member.id) {
        this.$refs.modal.showAlertModal({
          swlIcon: "warning",
          swlTitle: "กรุณาเข้าสู่ระบบ",
          swlText: "กรุณาเข้าสู่ระบบก่อนที่จะทำการสั่งซื้อ",
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
      if (!this.member.phone) {
        this.inputNowPhone = false;
        this.inputNewPhone = true;
        this.boxBtn = true;
        this.$refs.inputNewPhone.focus();
        return;
      }
      if (!this.deliveryOption) {
        this.$refs.modal.showAlertModal({
          swlIcon: "warning",
          swlTitle: "ไม่พบที่อยู่ในการจัดส่ง",
          swlText: "กรุณาเลือกที่อยู่ในการจัดส่ง",
        });
        return;
      }
      try {
        this.generateRandomCode();

        const order = {
          code: this.order.code,
          member_id: this.member.id,
          member_name: this.member.name,
          member_phone: this.member.phone,
          address: this.deliveryOption,
          total: this.totalAmount,
          status: "new",
          length: this.carts.length,
        };

        const orderDetails = this.carts.map((item) => ({
          product_id: item.id,
          product_name: item.name,
          product_price: item.price,
          qty: item.qty,
        }));

        const orderResponse = await axios.post(`${this.apiUrl}orders/`, {
          order: order,
          orderDetails: orderDetails,
        });

        if (orderResponse.status === 200) {
          this.$refs.modal.showSuccessModal({
            swlIcon: "success",
            swlTitle: "ทำรายการสั่งซื้อสำเร็จ",
            swlText: "",
          });
        }
      } catch (error) {
        this.$refs.modal.showAlertModal({
          swlIcon: "warning",
          swlTitle: "เกิดข้อผิดพลาด",
          swlText: error,
        });
      }
    },

    clearLocalStorage() {
      // ดึงข้อมูลจาก localStorage
      let carts = localStorage.getItem("carts");
      this.carts = JSON.parse(carts) || [];

      // กรองออก item ที่ member_id ใน carts ตรงกับ this.member.id
      this.carts = this.carts.filter(
        (item) => !(item.member_id === this.member.id) // ลบ item ที่ตรงกับเงื่อนไข
      );

      // ลบข้อมูลทั้งหมดใน localStorage
      localStorage.removeItem("carts");

      // อัพเดท localStorage ด้วยข้อมูลใหม่ที่กรองแล้ว
      localStorage.setItem("carts", JSON.stringify(this.carts));
      this.cartsLength = this.carts.length;
    },

    generateRandomCode() {
      const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
      const randomChars1 = Array.from(
        { length: 2 },
        () => characters[Math.floor(Math.random() * characters.length)]
      );
      const randomChars2 = Array.from(
        { length: 1 },
        () => characters[Math.floor(Math.random() * characters.length)]
      );
      const randomDigits = Math.floor(10 + Math.random() * 90);
      const currentDate = new Date()
        .toISOString()
        .slice(0, 10)
        .replace(/-/g, "");

      const code =
        randomChars1.join("") +
        this.member.id.toString() +
        currentDate +
        randomDigits.toString() +
        randomChars2.join("");

      this.order.code = code;
      console.log(code);
    },
  },
};
</script>
