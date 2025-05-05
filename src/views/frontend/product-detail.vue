<template>
  <frontend_navbar :cartsLength="cartsLength" />
  <Modal ref="modal" " />

  <div class="flex justify-center pt-24 p-4">
    <div
      class="w-full max-w-screen-2xl lg:p-12 lg:border border-gray-200 rounded-lg mb-16 lg:mb-4 bg-white z-40"
    >
      <div>
        <!-- Title -->
        <!-- เปุ่มนี้เสดงเมื่อจอเล็ก -->

        <div
          class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 gap-4 lg:gap-8"
        >
          <div>
            <!-- รูปใหญ่ด้านบนที่จะแสดงภาพที่เลือก -->
            <div v-if="!selectedImage" class="lg:h-96 h-60 w-full cursor-pointer">
            <img
              class="h-full w-full object-contain rounded-md"
              :src="`${imageUrl}/src/assets/image/system/product.png`"
            />
          </div>
            <div  v-else class="lg:h-96 h-60 w-full cursor-pointer">
              <img
                :src="selectedImage"
                alt="Selected Food"
                class="h-full w-full object-contain rounded-md"
              />
            </div>

            <!-- กริดของภาพ -->
            <div class="grid grid-cols-4 gap-2 lg:gap-4 pt-2 lg:pt-4">
              <div
                v-for="(image, imageIndex) in product.images"
                class="w-full lg:h-28 h-20 cursor-pointer"
                @click="
                  selectImage(
                    `${imageUrl}/api/uploads/${Math.ceil(product.id / 100)}/${
                      image.path
                    }`
                  )
                "
              >
                <img
                  :src="`${imageUrl}/api/uploads/${Math.ceil(
                    product.id / 100
                  )}/${image.path}`"
                  alt="image 1"
                  class="h-full w-full object-contain rounded-md"
                />
              </div>
            </div>
          </div>

          <div class="p-8 bg-gray-100 rounded-md text-gray-600">
            <p class="text-2xl lg:text-3xl font-semibold mb-2">
              {{ product.name }}
            </p>
            <p class="text-md">
              {{ product.detail }}
            </p>
            <div
              class="flex gap-4 items-center mt-8 justify-center lg:justify-start"
            >
              <p class="text-2xl font-semibold">ราคา</p>
              <p class="text-2xl font-semibold text-orange-500">
                {{ product.price }} บาท
              </p>
            </div>
            <div
              class="flex gap-4 items-center mt-4 justify-center lg:justify-start"
            >
              <div class="flex items-center">
                <!-- ปุ่มลดจำนวน -->
                <button
                  class="bg-gray-300 text-gray-600 hover:bg-gray-200 p-2 pr-3 pl-3 focus:outline-none transition rounded-l-md"
                  @click="decrementQuantity"
                  :disabled="qty <= 1"
                >
                  -
                </button>

                <!-- ช่องกรอกจำนวนสินค้า -->
                <input
                  type="text"
                  class="w-14 text-center border-none focus:outline-none p-2 pr-3 pl-3"
                  v-model.number="qty"
                  min="1"
                />

                <!-- ปุ่มเพิ่มจำนวน -->
                <button
                  class="bg-gray-300 text-gray-600 hover:bg-gray-200 p-2 pr-3 pl-3 focus:outline-none transition rounded-r-md"
                  @click="incrementQuantity"
                >
                  +
                </button>
              </div>
            </div>

            <div class="flex justify-center lg:justify-start">
              <button
                @click="addToCart(product)"
                class="p-2 pr-4 pl-4 rounded-lg bg-gray-800 text-white mt-6 hover:bg-gray-600 transition"
              >
                <i class="fa-solid fa-cart-plus text-md"></i> เพิ่มลงตระกร้า
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { parse } from "vue/compiler-sfc";
import frontend_navbar from "../../components/frontend/navbar.vue";
import Modal from "@/components/frontend/modal.vue";
import axios from "axios";
export default {
  components: { frontend_navbar, Modal },
  props: {
    productId: {
      required: true,
    },
  },

  data() {
    return {
      apiUrl: __API_URL__,
      baseUrl: __BASE_URL__,
      imageUrl: __IMAGE_URL__,
      product: {
        id: "",
        code: "",
        name: "",
        cost: "",
        price: "",
        category_id: "",
        status: "",
        detail: "",
        images: [],
      },

      member: {
        id: "",
        code: "",
      },

      member_id: "",
      qty: 1,
      cartsLength: 0,

      // กำหนดภาพเริ่มต้นที่จะแสดง
      selectedImage: "",
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
        this.getProduct();
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
          })
          .catch((error) => {
            console.error("There was an error fetching the data:", error);
          });
      }
    },
    async getProduct() {
      try {
        const response = await axios.get(
          `${this.apiUrl}products/${this.productId}`
        );
        this.product = response.data.row;

        if (this.product.images[0]) {
          this.selectedImage = `${this.imageUrl}/api/uploads/${Math.ceil(
            this.productId / 100
          )}/${this.product.images[0].path}`;
        }
        //console.log("this.selectedImage",this.selectedImage);
      } catch (error) {
        console.error("Error fetching product:", error);
      }
    },
    // ฟังก์ชันในการเปลี่ยนภาพเมื่อคลิก
    selectImage(imageUrl) {
      this.selectedImage = imageUrl;
    },
    addToCart(product) {
      if (!this.member.id) {
        this.$refs.modal.showAlertModal({
          swlIcon: "warning",
          swlTitle: "กรุณาเข้าสู่ระบบ",
          swlText: "กรุณาเข้าสู่ระบบก่อนที่จะเพื่มลงตระกร้า",
        });
        return;
      }

      // ดึงข้อมูลที่มีอยู่ใน localStorage มาเก็บไว้ในตัวแปร carts (array)
      let carts = JSON.parse(localStorage.getItem("carts")) || [];

      // ตรวจสอบว่าสินค้าที่ต้องการเพิ่มมีอยู่ใน carts อยู่แล้วหรือไม่
      let existingItem = carts.find(
        (item) => item.id === product.id && item.member_id === this.member.id
      );

      if (existingItem) {
        // หากมีอยู่แล้วให้เพิ่ม quantity ของสินค้านี้
        existingItem.qty += parseFloat(this.qty);
      } else {
        // หากยังไม่มีให้เพิ่มรายการสินค้าใหม่
        // console.log("=========================");
        // console.log(this.product);
        // console.log("=========================");

        carts.push({
          member_id: this.member.id,
          id: product.id,
          name: product.name,
          price: product.price,
          qty: parseFloat(this.qty),
          image:
            this.product.images.length > 0 ? this.product.images[0].path : "",
        });
      }
      // บันทึก carts กลับไปยัง localStorage
      localStorage.setItem("carts", JSON.stringify(carts));
      (this.cartsLength = carts.length),
        this.$swal.fire({
          title: "สำเร็จ",
          text: "เพิ่มสินค้าเข้าสู่ตะกร้าเรียบร้อยแล้ว",
          icon: "success",
          confirmButtonText: "ยืนยัน",
          customClass: {
            confirmButton:
              "bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400",
          },
        });

      // แสดงข้อมูลใน localStorage ที่บันทึกอยู่ในคอนโซล
      // console.log("ตะกร้าสินค้า:", carts);
      // console.log("รายการ:", carts.length);
    },
    decrementQuantity() {
      if (this.qty > 1) {
        this.qty--;
      }
    },
    incrementQuantity() {
      this.qty++;
    },
  },
};
</script>
