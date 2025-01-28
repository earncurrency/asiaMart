<script setup>
import router from "@/router";
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <!-- เมนูด้านบน -->
  <nav
    class="fixed w-full bg-white border-gray-200 dark:bg-gray-900 shadow-md z-50"
  >
    <div
      class="max-w-screen-2xl flex flex-wrap items-center justify-between mx-auto p-4"
    >
      <!-- โลโก้ -->
      <RouterLink to="/">
        <a
          href=""
          class="hidden lg:flex items-center space-x-3 rtl:space-x-reverse"
        >
          <img src="@/assets/image/asia/icon.png" class="h-10" alt="Logo" />
          <span
            class="self-center text-xl font-semibold sm:text-2xl whitespace-nowrap dark:text-white text-gray-600"
          >
            AsiaMart</span
          >
        </a>
      </RouterLink>
      <RouterLink to="/">
        <a
          href=""
          class="flex lg:hidden items-center space-x-3 rtl:space-x-reverse"
        >
          <img src="../../assets/image/asia/icon.png" class="h-10" alt="Logo" />
        </a>
      </RouterLink>

      <!-- ช้องค้นหา -->
      <div class="flex items-center max-w-xl lg:w-full mx-auto">
        <label for="voice-search" class="sr-only">Search</label>

        <div class="relative w-full">
          <div
            class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none"
          >
            <i class="fa-solid fa-magnifying-glass"></i>
          </div>
          <input
            type="text"
            id="voice-search"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full pl-10 pr-10 p-2.5 focus:border-gray-300"
            placeholder="ค้นหา..."
          />

          <button
            class="absolute inset-y-0 end-0 flex items-center ps-3 p-3 pointer"
          >
            <i class="fa-solid fa-xmark"></i>
          </button>
        </div>
      </div>

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
            <div
              class="absolute inline-flex items-center justify-center w-6 h-6 text-xs font-bold text-white bg-red-500 border-2 border-white rounded-full top-6 -end-2"
            >
              20
            </div>
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
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white"
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
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white"
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
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white"
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
                class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white"
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
          <div
            class="absolute inline-flex items-center justify-center w-6 h-6 text-xs font-bold text-white bg-red-500 border-2 border-white rounded-full -top-0 end-5"
          >
            20
          </div>
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
      fullname: "",
      iconUserOpen: false,
      carts: [],
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
  },
  watch: {
    // ติดตามการเปลี่ยนแปลงของ prop 'cartsLength' ทุกครั้งที่มันเปลี่ยน
    cartsLength(newLength) {
      this.setdata(); // เรียก setdata เมื่อ prop เปลี่ยน
    },
  },

  methods: {
    setdata() {
      let carts = localStorage.getItem("carts");
      this.carts = JSON.parse(carts) || [];

      let storedHash = localStorage.getItem("hash");
      const firstNumber = storedHash.split("-")[0];
      this.member_id = firstNumber;

      let storedFullname = localStorage.getItem("fullname");
      this.fullname = storedFullname;

      // กรองข้อมูลใน carts เฉพาะที่ member_id ตรงกับ this.member_id
      this.carts = this.carts.filter(
        (item) => item.member_id === this.member_id
      );
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
