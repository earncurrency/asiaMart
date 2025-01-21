<script setup>
import frontend_navbar from "../../components/frontend/navbar.vue";
import axios from "axios";
</script>

<template>
  <frontend_navbar />

  <div class="flex justify-center pt-24 p-4">
    <div
      class="w-full max-w-screen-2xl lg:p-12 lg:border border-gray-200 rounded-lg mb-16 lg:mb-4 bg-white z-40"
    >
      <div>
        <!-- Title -->
        <!-- เปุ่มนี้เสดงเมื่อจอเล็ก -->
        <div class="flex items-center gap-4 lg:hidden">
          <RouterLink to="/">
            <button class="px-2 py-1 bg-gray-800 rounded-md text-white text-sm">
              <i class="fa-solid fa-arrow-left"></i>
            </button>
          </RouterLink>
          <!-- <p class="text-xl">อาหาร</p> -->
        </div>
        <div
          class="lg:flex items-center justify-between font-medium p-2 lg:p-0"
        >
          <!-- เปุ่มนี้เสดงเมื่อจอใหญ่ -->
          <div class="flex justify-center gap-4">
            <div class="hidden lg:flex items-center gap-4">
              <RouterLink :to="`/category/${product.category_id}`">
                <button
                  class="px-2 py-1 bg-gray-800 rounded-md text-white text-sm hover:bg-gray-600 transition"
                >
                  <i class="fa-solid fa-arrow-left"></i>
                </button>
              </RouterLink>
              <!-- <p class="text-xl">อาหาร</p> -->
            </div>
            <!-- <p class="text-xl">กลับ</p> -->
          </div>
        </div>

        <hr class="my-2 text-gray-600" />

        <div
          class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 gap-4 lg:gap-8 mt-8"
        >
          <div>
            <!-- รูปใหญ่ด้านบนที่จะแสดงภาพที่เลือก -->
            <div class="lg:h-96 h-60 w-full cursor-pointer">
              <img
                :src="selectedImage"
                alt="Selected Food"
                class="h-full w-full object-cover rounded-md"
              />
            </div>

            <!-- กริดของภาพ -->
            <div class="grid grid-cols-4 gap-2 lg:gap-4 pt-2 lg:pt-4">
              <div
                v-for="(image, imageIndex) in product.images"
                class="w-full lg:h-28 h-20 cursor-pointer"
                @click="
                  selectImage(
                    `${baseUrl}/api/uploads/${Math.ceil(product.id / 100)}/${
                      image.path
                    }`
                  )
                "
              >
                <img
                  :src="`${baseUrl}/api/uploads/${Math.ceil(
                    product.id / 100
                  )}/${image.path}`"
                  alt="image 1"
                  class="h-full w-full object-cover rounded-md"
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
                >
                  -
                </button>

                <!-- ช่องกรอกจำนวนสินค้า -->
                <input
                  type="text"
                  class="w-14 text-center border-none focus:outline-none p-2 pr-3 pl-3"
                  v-model="quantity"
                />

                <!-- ปุ่มเพิ่มจำนวน -->
                <button
                  class="bg-gray-300 text-gray-600 hover:bg-gray-200 p-2 pr-3 pl-3 focus:outline-none transition rounded-r-md"
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
export default {
  props: {
    productId: {
      required: true,
    },
  },
  data() {
    return {
      apiUrl: "http://127.0.0.1:8000/",
      baseUrl: __BASE_URL__,
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
      quantity: "1",

      // กำหนดภาพเริ่มต้นที่จะแสดง
      selectedImage: "",
    };
  },
  mounted() {
    this.getProduct();
  },

  methods: {
    // ฟังก์ชันในการเปลี่ยนภาพเมื่อคลิก
    selectImage(imageUrl) {
      this.selectedImage = imageUrl;
    },

    async getProduct() {
      try {
        const response = await axios.get(
          `${this.apiUrl}products/${this.productId}`
        );
        this.product = response.data.row;
        console.log(this.product);

        this.selectedImage = `${this.baseUrl}/api/uploads/${Math.ceil(
          this.productId / 100
        )}/${this.product.images[0].path}`;
      } catch (error) {
        console.error("Error fetching product:", error);
      }
    },
    addToCart(product) {
      // ดึงข้อมูลที่มีอยู่ใน localStorage มาเก็บไว้ในตัวแปร carts (array)
      let carts = JSON.parse(localStorage.getItem("carts")) || [];

      // ตรวจสอบว่าสินค้าที่ต้องการเพิ่มมีอยู่ใน carts อยู่แล้วหรือไม่
      let existingItem = carts.find((item) => item.id === product.id);

      if (existingItem) {
        // หากมีอยู่แล้วให้เพิ่ม quantity ของสินค้านี้
        existingItem.quantity += this.quantity;
      } else {
        // หากยังไม่มีให้เพิ่มรายการสินค้าใหม่
        carts.push({
          id: product.id,
          name: product.name,
          price: product.price,
          quantity: this.quantity 
        });
      }

      // บันทึก carts กลับไปยัง localStorage
      localStorage.setItem("carts", JSON.stringify(carts));

      // แสดงข้อความแจ้งเตือนว่าเพิ่มสินค้าลงในตะกร้าเรียบร้อยแล้ว
      this.$swal
        .fire({
          title: "สำเร็จ",
          text: "เพิ่มสินค้าเข้าสู่ตะกร้าเรียบร้อยแล้ว",
          icon: "success",
          confirmButtonText: "ยืนยัน",
          customClass: {
            confirmButton:
              "bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400",
          },
        })
        .then((result) => {
          if (result.isConfirmed) {
            // ทำอะไรต่อไปหลังจากกดยืนยัน (ถ้ามี)
          }
        });

      // แสดงข้อมูลใน localStorage ที่บันทึกอยู่ในคอนโซล
      console.log("ข้อมูลใน localStorage (ตะกร้าสินค้า):", carts);
    },
  },
};
</script>
