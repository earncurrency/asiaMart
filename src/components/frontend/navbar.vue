<script setup>
import router from "@/router";
import { RouterLink, RouterView } from "vue-router";
import axios from "axios";
</script>

<template>
  <!-- เมนูด้านบน -->
  <nav
    class="fixed w-full bg-white border-gray-200 dark:bg-gray-900 shadow-md z-50 top-[-1px]"
  >
    <div
      class="max-w-screen-2xl flex flex-wrap items-center justify-between mx-auto p-4"
    >
      <!-- โลโก้ -->
      <RouterLink to="/">
        <a href="" class="flex items-center space-x-3 rtl:space-x-reverse">
          <img src="@/assets/image/asia/icon.png" class="h-10" alt="Logo" />
          <span
            class="self-center text-xl font-semibold sm:text-2xl whitespace-nowrap dark:text-white text-gray-600"
          >
            AsiaMart</span
          >
        </a>
      </RouterLink>

      <div
        class="hidden lg:flex relative flex gap-1 lg:gap-4 justify-center items-center md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse"
      >
        <!-- ปุ่มตระกร้า -->
        <RouterLink to="/cart">
          <button
            class="relative text-gray-600 w-10 h-10 rounded-full object-cover ring-4 ring-gray-300 shadow-md"
          >
            <i class="fa-solid fa-cart-shopping"></i>
            <div
              class="absolute inline-flex items-center justify-center w-6 h-6 text-xs font-bold text-white bg-red-500 border-2 border-white rounded-full top-6 -end-2"
            >
              {{ computedCartsLength }}
            </div>
          </button>
        </RouterLink>

        <!-- ปุ่มกระดิ่ง -->
        <RouterLink to="/alert">
          <button
            class="relative text-gray-600 w-10 h-10 rounded-full object-cover ring-4 ring-gray-300 shadow-md"
          >
            <i class="fa-solid fa-bell"></i>
            <!-- <div
              class="absolute inline-flex items-center justify-center w-6 h-6 text-xs font-bold text-white bg-red-500 border-2 border-white rounded-full top-6 -end-2"
            >
              20
            </div> -->
          </button>
        </RouterLink>

        <!-- ไอคอน โปรไฟล์ -->

        <button
          v-if="fullname"
          type="button"
          @click="toggleIconUser"
          class="flex text-sm bg-gray-200 rounded-full md:me-0 focus:ring-2 focus:ring-gray-200 items-center transition"
        >
          <img
            class="w-10 h-10 rounded-full object-cover ring-4 ring-gray-300 shadow-md"
            src="../../assets/image/system/cathothead.jpg"
            alt="user photo"
          />
          <span class="mx-2"
            >{{ fullname }}
            <span class="ml-2"><i class="fa-solid fa-angle-down"></i></span>
          </span>
        </button>

        <RouterLink v-else="fullname" to="/login">
          <button
            type="button"
            class="flex text-sm bg-gray-200 h-10 rounded-full md:me-0 focus:ring-2 focus:ring-gray-200 items-center transition"
          >
            <span class="mx-6">เข้าสู่ระบบ </span>
          </button>
        </RouterLink>

        <!-- เมนู โปรไฟล์ -->
        <div
          v-if="iconUserOpen"
          ref="iconUserMenu"
          class="absolute right-0 top-12 z-50 w-40 text-base list-none bg-white divide-y divide-gray-100 rounded-lg shadow cursor-pointer border border-gray-300"
        >
          <ul class="py-1">
            <li>
              <RouterLink to="/profile">
                <a
                  @click="closeiconUserMenu"
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                >
                  <span class="mr-2 text-gray-500">
                    <i class="fa-solid fa-user"></i
                  ></span>
                  โปรไฟล์
                </a>
              </RouterLink>
            </li>
            <li>
              <RouterLink to="/profile">
                <a
                  @click="closeiconUserMenu"
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                >
                  <span class="mr-2 text-gray-500">
                    <i class="fa-solid fa-box"></i
                  ></span>
                  ติดตามสินค้า
                </a>
              </RouterLink>
            </li>

            <li>
              <RouterLink to="/history">
                <a
                  @click="closeiconUserMenu"
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                >
                  <span class="mr-2 text-gray-500">
                    <i class="fa-solid fa-clock-rotate-left"></i
                  ></span>
                  ประวัติ
                </a>
              </RouterLink>
            </li>
            <li>
              <a
                @click="logout()"
                class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
              >
                <span class="mr-2 text-red-500">
                  <i class="fa-solid fa-arrow-right-from-bracket"></i
                ></span>
                ออกจากระบบ
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </nav>

  <!-- เมนูด้านล่าง-->
  <div
    class="lg:hidden fixed bottom-0 left-0 z-50 w-full h-16 bg-white border-t border-gray-200"
    >
    <div class="grid h-full max-w-lg grid-cols-4 mx-auto font-medium">
      <RouterLink to="/">
        <button
          type="button"
          class="h-full w-full inline-flex flex-col items-center justify-center px-5 hover:bg-gray-50 text-gray-500"
        >
          <i class="fa-solid fa-house text-xl"></i>
          <span class="mt-1 text-sm text-gray-500 group-hover:text-blue-600"
            >หน้าเเรก</span
          >
        </button>
      </RouterLink>
      <RouterLink to="/cart">
        <button
          type="button"
          class="h-full w-full relative inline-flex flex-col items-center justify-center px-5 hover:bg-gray-50 text-gray-500"
        >
          <i class="fa-solid fa-cart-shopping text-xl"></i>
          <span class="mt-1 text-sm text-gray-500 group-hover:text-blue-600"
            >ตระกร้า</span
          >
          <div
            class="absolute inline-flex items-center justify-center w-6 h-6 text-xs font-bold text-white bg-red-500 border-2 border-white rounded-full -top-0 end-5"
          >
            {{ computedCartsLength }}
          </div>
        </button>
      </RouterLink>
      <RouterLink to="/alert">
        <button
          type="button"
          class="h-full w-full relative inline-flex flex-col items-center justify-center px-5 hover:bg-gray-50 text-gray-500"
        >
          <i class="fa-solid fa-bell text-xl"></i>
          <span class="mt-1 text-sm text-gray-500 group-hover:text-blue-600"
            >เเจ้งเตือน</span
          >
          <!-- <div
            class="absolute inline-flex items-center justify-center w-6 h-6 text-xs font-bold text-white bg-red-500 border-2 border-white rounded-full -top-0 end-5"
          >
            20
          </div> -->
        </button>
      </RouterLink>
      <RouterLink to="/profile">
        <button
          type="button"
          class="h-full w-full inline-flex flex-col items-center justify-center px-5 hover:bg-gray-50 text-gray-500"
        >
          <i class="fa-solid fa-user text-xl"></i>
          <span class="mt-1 text-sm text-gray-500 group-hover:text-blue-600"
            >โปรไฟล์</span
          >
        </button>
      </RouterLink>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    cartsLength: {
      type: Number,
      required: false,
      default: 0,
    },
  },
  data() {
    return {
      apiUrl: __API_URL__,
      fullname: "",
      iconUserOpen: false,
      carts: [],

      member: {
        id: "",
        code: "",
      },
    };
  },
  computed: {
    // คำนวณค่าความยาวของ carts
    computedCartsLength() {
      return this.carts.length;
    },
  },
  mounted() {
    document.addEventListener("click", this.closeIconUser);
    this.setdata();
    this.getProductInCart();
  },
  watch: {
    // ติดตามการเปลี่ยนแปลงของ prop 'cartsLength' ทุกครั้งที่มันเปลี่ยน
    cartsLength(newLength) {
      this.getProductInCart();
    },
  },

  methods: {
    setdata() {
      let storedHash = localStorage.getItem("hash");

      //รหัสพนักงาน
      const codeNumber = storedHash ? storedHash.split("-")[1] : 0;
      this.member.code = codeNumber;

      //ชื่อพนักงาน
      let storedFullname = localStorage.getItem("fullname");
      this.fullname = storedFullname;
    },
    getProductInCart() {
      //ดึง สินค้าใน localStorage carts ที่ id member ตรงกัน
      if (this.member.code) {
        axios
          .get(`${this.apiUrl}members/code/${this.member.code}`)
          .then((response) => {
            const data = response.data;
            this.member.id = data.row.id;

            let carts = localStorage.getItem("carts");
            this.carts = JSON.parse(carts) || [];

            this.carts = this.carts.filter(
              (item) => item.member_id === this.member.id
            );
          })
          .catch((error) => {
            console.error("There was an error fetching the data:", error);
          });
      }
    },

    async logout() {
      localStorage.setItem("hash", "");
      localStorage.setItem("fullname", "");
      this.$router.push("/login");
      this.closeiconUserMenu();
    },
    closeiconUserMenu() {
      this.iconUserOpen = false;
    },
    // dropdown
    toggleIconUser(event) {
      event.stopPropagation();
      this.iconUserOpen = !this.iconUserOpen;
    },
    closeIconUser(event) {
      const dropdown = this.$refs.iconUserMenu;
      if (dropdown && !dropdown.contains(event.target)) {
        this.iconUserOpen = false;
      }
    },
  },
};
</script>
