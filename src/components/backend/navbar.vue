<script setup>
import router from "@/router";
import { faL } from "@fortawesome/free-solid-svg-icons";
</script>

<template>
  <!-- navbar -->
  <nav
    class="fixed top-0 z-50 w-full bg-gray-800 border-b border-gray-900 dark:bg-gray-800 dark:border-gray-700"
  >
    <div class="px-3 py-3 lg:px-5 lg:pl-3">
      <div class="flex items-center justify-between">
        <div class="flex items-center justify-start rtl:justify-end">
          <button
            @click="toggleSidebar"
            class="inline-flex items-center p-2 text-xl text-white rounded-lg sm:hidden hover:bg-gray-600"
          >
            <span class="sr-only">Open sidebar</span>
            <i class="fa-solid fa-bars-staggered"></i>
          </button>
          <a href="" class="flex ms-2 md:me-24 gap-2">
            <img src="@/assets/image/asia/icon.png" class="h-10" alt="Logo" />
            <span
              class="self-center text-xl font-semibold sm:text-2xl whitespace-nowrap text-white"
            >
              AsiaMart</span
            >
          </a>
        </div>
        <div class="flex items-center">
          <div class="flex items-center ms-3">
            <div class="relative">
              <button
                type="button"
                @click="toggleIconUser"
                class="flex text-sm bg-gray-200 rounded-full md:me-0 focus:ring-2 focus:ring-gray-200 items-center transition"
              >
                <img
                  class="w-10 h-10 rounded-full object-cover ring-4 ring-gray-300 shadow-md"
                  src="../../assets/image/system/cathothead.jpg"
                  alt="user photo"
                />
                <span class="hidden lg:block mx-2"
                  >{{ admin_name }}
                  <span class="ml-2"
                    ><i class="fa-solid fa-angle-down"></i
                  ></span>
                </span>
              </button>

              <div
                v-if="iconUserOpen"
                ref="iconUserMenu"
                class="absolute lg:w-full right-0 top-12 z-50 my-4 text-base list-none bg-white divide-y divide-gray-100 rounded shadow dark:bg-gray-700 dark:divide-gray-600 cursor-pointer"
              >
                <div class="lg:hidden px-4 py-3 w-full" role="none">
                  <p
                    class="text-md font-semibold text-gray-900 dark:text-white whitespace-nowrap"
                    role="none"
                  >
                    {{ admin_name }}
                  </p>
                  <p
                    class="text-sm font-medium text-gray-900 truncate dark:text-gray-300"
                    role="none"
                  >
                    โปรเเกรมเมอร์
                  </p>
                </div>
                <ul class="py-1" role="none">
                  <li>
                    <a
                      href="#"
                      @click="closeiconUserMenu"
                      class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white"
                      role="menuitem"
                      >โปรไฟล์</a
                    >
                  </li>
                  <li>
                    <a
                      @click="logout()"
                      class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white "
                      role="menuitem"
                      >ออกจากระบบ</a
                    >
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>

  <!-- sidebar -->
  <aside
    v-if="sidebarOpen"
    ref="sidebarMenu"
    class="fixed top-0 left-0 z-40 w-64 h-screen pt-20 bg-gray-800 border-r border-gray-800"
    aria-label="Sidebar"
  >
    <div class="h-full px-3 pb-4 overflow-y-auto bg-gray-800">
      <ul class="space-y-2 font-medium">
        <li>
          <RouterLink to="/backend/dashboard">
            <a
              href="#"
              class="flex items-center p-2 text-white rounded-lg group"
            >
              <div class="text-xl text-white">
                <i class="fa-solid fa-house"></i>
              </div>
              <span class="ms-3">หน้าเเรก</span>
            </a>
          </RouterLink>
        </li>
        <li @click="showFormTable">
          <RouterLink to="/backend/manage-category">
            <a
              href="#"
              class="flex items-center p-2 text-white rounded-lg group"
            >
              <div class="text-xl text-white">
                <i class="fa-solid fa-table-list"></i>
              </div>
              <span class="flex-1 ms-3 whitespace-nowrap">หมวดหมู่สินค้า</span>
            </a>
          </RouterLink>
        </li>
        <li @click="showFormTable">
          <RouterLink to="/backend/manage-product">
            <a
              href="#"
              class="flex items-center p-2 text-white rounded-lg group"
            >
              <div class="text-xl text-white">
                <i class="fa-solid fa-boxes-packing"></i>
              </div>
              <span class="flex-1 ms-3 whitespace-nowrap">รายการสินค้า</span>
            </a>
          </RouterLink>
        </li>
        <li @click="showFormTable">
          <RouterLink to="/backend/manage-recommend-product">
            <a
              href="#"
              class="flex items-center p-2 text-white rounded-lg group"
            >
              <div class="text-xl text-white">
                <i class="fa-regular fa-thumbs-up"></i>
              </div>
              <span class="flex-1 ms-3 whitespace-nowrap">รายการสินค้าเเนะนำ</span>
            </a>
          </RouterLink>
        </li>
        <li @click="showFormTable">
          <RouterLink to="/backend/manage-admin">
            <a
              href="#"
              class="flex items-center p-2 text-white rounded-lg group"
            >
              <div class="text-xl text-white">
                <i class="fa-solid fa-user"></i>
              </div>
              <span class="flex-1 ms-3 whitespace-nowrap">รายการแอดมิน</span>
            </a>
          </RouterLink>
        </li>
        <li @click="showFormTable">
          <RouterLink to="/backend/manage-member">
            <a
              href="#"
              class="flex items-center p-2 text-white rounded-lg group"
            >
              <div class="text-xl text-white">
                <i class="fa-solid fa-users"></i>
              </div>
              <span class="flex-1 ms-3 whitespace-nowrap">รายการลูกค้า</span>
            </a>
          </RouterLink>
        </li>
        <li @click="showFormTable">
          <RouterLink to="/backend/manage-order">
            <a
              href="#"
              class="flex items-center p-2 text-white rounded-lg group"
            >
              <div class="text-xl text-white">
                <i class="fa-solid fa-list-check"></i>
              </div>
              <span class="flex-1 ms-3 whitespace-nowrap"
                >รายการคำสั่งซื้อ</span
              >
            </a>
          </RouterLink>
        </li>
        <li>
          <div href="#" class="flex items-center p-2 text-white rounded-lg">
            <div class="text-xl text-white">
              <i class="fa-solid fa-file-lines"></i>
            </div>
            <span class="flex-1 ms-3 whitespace-nowrap">รายงาน</span>
          </div>

          <a
            href="#"
            class="flex items-center p-2 text-gray-400 rounded-lg group"
          >
            <span class="flex-1 ms-7 whitespace-nowrap">- สินค้าคงคลัง</span>
          </a>

          <a
            href="#"
            class="flex items-center p-2 text-gray-400 rounded-lg group"
          >
            <span class="flex-1 ms-7 whitespace-nowrap">- ยอดขาย</span>
          </a>
        </li>
      </ul>
    </div>
  </aside>
</template>

<script>
export default {
  data() {
    return {
      admin_name: "",
      sidebarOpen: false,
      iconUserOpen: false,
    };
  },
  mounted() {
    document.addEventListener("click", this.closeIconUser);
    // ตรวจสอบขนาดหน้าจอเมื่อหน้าเว็บโหลดเสร็จ และปรับค่า `sidebarOpen`
    this.checkScreenWidth();
    // เพิ่ม event listener เพื่อให้ตรวจจับการปรับขนาดหน้าจอ (resize)
    window.addEventListener("resize", this.checkScreenWidth);

    this.setdata();

  },
  destroyed() {
    // Clean up the event listener
    window.removeEventListener("resize", this.checkScreenWidth);
  },

  emits: ["showFormTable"],

  methods: {
    showFormTable() {
      this.$emit("showFormTable");
    },

    setdata() {

      let admin_name = localStorage.getItem("admin_name");
      this.admin_name = admin_name;

      let admin_role = localStorage.getItem("admin_role");
      this.admin_role = admin_role;

    },

    logout() {
      localStorage.setItem("admin_hash", "");
      localStorage.setItem("admin_name", "");
      localStorage.setItem("admin_role", "");
      this.$router.push("/backend/login");
    },

    checkScreenWidth() {
      // กำหนดค่า `sidebarOpen` ตามขนาดหน้าจอ
      this.sidebarOpen = window.innerWidth >= 1024; // 1024px ใช้เป็นขนาดของหน้าจอใหญ่
    },
    toggleSidebar(event) {
      event.stopPropagation();
      this.sidebarOpen = !this.sidebarOpen;
    },

    closeiconUserMenu() {
      this.iconUserOpen = false;
    },
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
