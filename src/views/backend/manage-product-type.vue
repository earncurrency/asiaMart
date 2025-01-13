<script setup>
import backend_navbar from "@/components/backend/navbar.vue";
import Modal from "@/components/backend/modal.vue";
import axios from "axios";
import { fas } from "@fortawesome/free-solid-svg-icons";
</script>

<template class="">
  <backend_navbar @showFormTable="showFormTable" />
  <Modal ref="modal" @showFormTable="showFormTable" />

  <div class="p-4 lg:pr-24 lg:pl-24 pt-6 sm:ml-64">
    <div
      class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-14"
    >
      <div class="mt-2 mb-2">
        <div class="lg:p-4 w-full rounded-md text-gray-600">
          <div v-if="formTable">
            <!-- title -->
            <div class="flex justify-between items-center mb-2">
              <p class="text-3xl font-semibold">หมวดหมู่สินค้า</p>
              <button
                @click="showFormAdd"
                class="block py-2 px-6 bg-green-500 hover:bg-green-600 text-white rounded-md transition"
              >
                <i class="fa-solid fa-plus"></i>
              </button>
            </div>

            <!-- sort -->
            <div class="lg:flex lg:justify-between mb-4 mt-4 items-center">
              <!-- ช่องค้นหา -->
              <div class="bg-white lg:justify-start">
                <div class="relative mt-1">
                  <div
                    class="absolute inset-y-0 rtl:inset-r-0 start-0 flex items-center ps-3 pointer-events-none"
                  >
                    <svg
                      class="w-4 h-4 text-gray-500"
                      aria-hidden="true"
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 20 20"
                    >
                      <path
                        stroke="currentColor"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
                      />
                    </svg>
                  </div>
                  <input
                    type="text"
                    class="block ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-full lg:w-80 bg-white focus:border-gray-300 h-full py-2.5"
                    placeholder="ค้นหา"
                  />
                </div>
              </div>

              <div class="flex gap-2 justify-center pt-4 lg:pt-0">
                <!-- เลือกสถานะ-->
                <div class="relative">
                  <!-- ปุ่มเลือกสถานะ-->
                  <button
                    class="border border-gray-300 bg-gray-50 font-medium rounded-lg text-sm px-16 py-2.5 text-center inline-flex items-center h-full"
                    type="button"
                    @click="dropdownStatus"
                  >
                    <span class="mr-2">
                      <span>ทั้งหมด</span>
                    </span>
                    <i class="fa-solid fa-angle-down"></i>
                  </button>
                  <!-- เมนูสถานะ -->
                  <div
                    v-show="DropdownStatusOpen"
                    ref="statusMenu"
                    class="z-50 absolute right-0 mt-2 text-base list-none w-full bg-white divide-y divide-gray-100 rounded-lg shadow border border-gray-300"
                  >
                    <ul class="py-2">
                      <li>
                        <a
                          href="#"
                          @click="DropdownStatus('')"
                          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          >ทั้งหมด</a
                        >
                      </li>
                      <li>
                        <a
                          href="#"
                          @click="DropdownStatus(0)"
                          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          >เเสดง</a
                        >
                      </li>
                      <li>
                        <a
                          href="#"
                          @click="DropdownStatus(1)"
                          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          >ไม่เเสดง</a
                        >
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- เลือกขนาดเเถวในตาราง -->
                <div class="relative">
                  <!-- ปุ่มเลือกขนาดเเถวในตาราง -->
                  <button
                    class="border border-gray-300 bg-gray-50 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center h-full"
                    type="button"
                    @click="togglePageSize"
                  >
                    <span class="mr-2">10</span
                    ><i class="fa-solid fa-angle-down"></i>
                  </button>
                  <!-- เมนูขนาดเเถวในตาราง -->
                  <div
                    v-show="pageSizeOpen"
                    ref="pageSizeMenu"
                    class="z-50 absolute right-0 mt-2 text-base list-none w-full bg-white divide-y divide-gray-100 rounded-lg shadow border border-gray-300"
                  >
                    <ul class="py-2">
                      <li>
                        <a
                          href="#"
                          @click="DropdownPageSize(10)"
                          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          >10</a
                        >
                      </li>
                      <li>
                        <a
                          href="#"
                          @click="DropdownPageSize(20)"
                          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          >20</a
                        >
                      </li>
                      <li>
                        <a
                          href="#"
                          @click="DropdownPageSize(50)"
                          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          >50</a
                        >
                      </li>
                      <li>
                        <a
                          href="#"
                          @click="DropdownPageSize(100)"
                          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          >100</a
                        >
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>

            <!-- ตาราง -->
            <div
              class="relative overflow-x-auto rounded-lg border border-gray-200"
            >
              <table
                class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400"
              >
                <thead
                  class="text-sm text-gray-100 uppercase bg-gray-800 dark:bg-gray-700 dark:text-gray-400"
                >
                  <tr>
                    <th scope="col" class="px-6 py-4 whitespace-nowrap">
                      ชื่อ
                    </th>
                    <th scope="col" class="px-6 py-4 whitespace-nowrap">
                      สถานะ
                    </th>
                    <th scope="col" class="px-6 py-4 whitespace-nowrap"></th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="(product_type, index) in product_types"
                    :key="index"
                    @click="showFormEdit(product_type.id)"
                    class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 cursor-pointer hover:bg-gray-100 transition"
                  >
                    <th
                      scope="row"
                      class="px-6 py-4 font-medium whitespace-nowrap"
                    >
                      <span class="font-semibold">{{ product_type.name }}</span>
                    </th>
                    <td class="px-6 py-4 whitespace-nowrap">
                      <span
                        v-if="product_type.status === 'active'"
                        class="font-semibold text-green-500 p-1 bg-green-100 rounded-md"
                      >
                        แสดง
                      </span>
                      <span
                        v-else
                        class="font-semibold text-red-500 p-1 bg-red-100 rounded-md"
                      >
                        ไม่แสดง
                      </span>
                    </td>
                    <td class="px-6 py-4">
                      <button
                        @click.stop="btnDelete"
                        class="bg-red-500 text-white px-4 py-2 rounded-md"
                      >
                        <i class="fa-solid fa-trash-can"></i>
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <div v-if="formAdd">
            <!-- title -->
            <div class="flex gap-2 items-center mb-2">
              <p class="text-3xl font-semibold">เพิ่มหมวดหมู่สินค้า</p>
            </div>
            <div class="md:flex w-full gap-2 mb-2 pt-1 mt-4">
              <div class="flex gap-2 w-full lg:w-1/2">
                <div class="w-full">
                  <input
                    type="text"
                    v-model="type.name"
                    ref="inputNameProductType"
                    :class="{
                      'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                      'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                        !type.name,
                    }"
                    placeholder="ใส่ชื่อหมวดหมู่สินค้า"
                    required
                  />
                </div>
              </div>

              <div class="flex gap-2 justify-center mt-4 md:mt-0">
                <button
                  @click="btnAdd"
                  class="text-white bg-blue-500 border border-blue-500 font-medium rounded-lg text-sm px-3 py-2.5 text-center inline-flex items-center h-full"
                >
                  ยืนยัน
                </button>
                <button
                  @click="showFormTable"
                  class="text-black bg-gray-200 border border-gray-400 font-medium rounded-lg text-sm px-3 py-2.5 text-center inline-flex items-center h-full"
                >
                  ยกเลิก
                </button>
              </div>
            </div>
          </div>

          <div v-if="formEdit">
            <!-- title -->
            <div class="flex justify-between items-center mb-2">
              <p class="text-3xl font-semibold">เเก้ไขหมวดหมู่สินค้า</p>
              <button
                @click.stop="btnDelete"
                class="bg-red-500 text-white px-4 py-1.5 rounded-md"
              >
                <i class="fa-solid fa-trash-can"></i>
              </button>
            </div>

            <div class="md:flex w-full gap-2 mb-2 pt-1 mt-4">
              <div class="flex gap-2 w-full lg:w-1/2">
                <div class="w-full">
                  <input
                    type="text"
                    v-model="product_type.name"
                    ref="inputNameProductType"
                    :class="{
                      'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                      'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                        !product_type.name,
                    }"
                    placeholder="ใส่ชื่อหมวดหมู่สินค้า"
                    required
                  />
                </div>
                <div class="lg:w-1/2 w-full">
                  <select
                    v-model="product_type.status"
                    ref="inputStatusProduct"
                    :class="{
                      'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                      'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                        !product_type.status,
                    }"
                    required
                  >
                    <option value="" disabled selected>สถานะ</option>
                    <option value="active">เเสดง</option>
                    <option value="inactive">ไม่เเสดง</option>
                  </select>
                </div>
              </div>

              <div class="flex gap-2 justify-center mt-4 md:mt-0">
                <button
                  @click="btnEdit"
                  class="text-white bg-blue-500 border border-blue-500 font-medium rounded-lg text-sm px-3 py-2.5 text-center inline-flex items-center h-full"
                >
                  ยืนยัน
                </button>
                <button
                  @click="showFormTable"
                  class="text-black bg-gray-200 border border-gray-400 font-medium rounded-lg text-sm px-3 py-2.5 text-center inline-flex items-center h-full"
                >
                  ยกเลิก
                </button>
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
      apiUrl: "http://127.0.0.1:8000/",

      product_types: [],

      product_type: {
        id: "",
        name: "",
        status: "",
      },

      isFocus: false,

      formTable: true,
      formAdd: false,
      formEdit: false,

      DropdownStatusOpen: false,
      pageSizeOpen: false,
    };
  },
  mounted() {
    this.getListProductTypes();

    document.addEventListener("click", this.closeDropdownStatus);
    document.addEventListener("click", this.closeDropdown);
  },
  methods: {
    // เพิ่มหมวดหมู่สินค้า
    showFormAdd() {
      this.formTable = false;
      this.formAdd = true;
      this.formEdit = false;

      this.type.name = "";
      this.type.status = "";
    },

    showFormTable() {
      this.formTable = true;
      this.formAdd = false;
      this.formEdit = false;

      this.getListProductTypes();
    },

    //เเสดงข้อมูลประเภทสินค้าบนตาราง
    async getListProductTypes() {
      await axios
        .get(`${this.apiUrl}product_type`)
        .then((response) => {
          const data = response.data;
          this.product_types = data.rows;
          console.log(this.product_types);
        })
        .catch((error) => {
          console.error("There was an error fetching the data:", error);
        });
    },

    async showFormEdit(productTypeId) {
      // เปิดฟอร์มแก้ไข
      this.formTable = false;
      this.formAdd = false;
      this.formEdit = true;

      // Set loading state to true
      this.loading = true;

      try {
        // เรียก API เพื่อดึงข้อมูลสินค้าที่ระบุ
        const response = await axios.get(
          `${this.apiUrl}product_type/${productTypeId}`
        );

        // ตรวจสอบว่าข้อมูลของสินค้าได้รับมาอย่างถูกต้อง
        if (response.status === 200) {
          const product_type = response.data.row;

          if (product_type) {
            this.product_type.id = productTypeId;
            this.product_type.name = product_type.name;
            this.product_type.status = product_type.status;

            // แสดงข้อมูลสินค้าใน console
            console.log("Product Data:", product_type);
          } else {
            alert("ไม่พบข้อมูลประเภทสินค้าที่ต้องการแก้ไข");
          }
        } else {
          alert(`Failed to fetch product type: ${response.statusText}`);
        }
      } catch (error) {
        console.error(
          `Error fetching product type ${productTypeId} from ${this.apiUrl}product_type/${productTypeId}:`,
          error.response?.data?.detail || error.message
        );
        this.$refs.modal.showAlertModal({
          swlIcon: "error",
          swlTitle: "ล้มเหลว",
          swlText: "เกิดข้อผิดพลาด",
        });
      } finally {
        // Set loading state to false
        this.loading = false;
      }
    },

    btnAdd() {
      if (!this.type.name) {
        this.isFocus = true;
        this.$refs.inputNameProductType.focus();
      } else {
        this.$refs.modal.showAlertModal({
          swlIcon: "success",
          swlTitle: "สำเร็จ",
          swlText: "เพิ่มหมวดหมู่สินค้าสำเร็จ!",
        });
      }
    },
    btnEdit() {
      if (!this.type.name) {
        this.isFocus = true;
        this.$refs.inputNameProductType.focus();
      } else {
        this.$refs.modal.showAlertModal({
          swlIcon: "success",
          swlTitle: "สำเร็จ",
          swlText: "เเก้ไขชื่อหมวดหมู่สินค้าสำเร็จ!",
        });
      }
    },
    btnDelete() {
      this.$refs.modal.showDeleteModal({
        swlIcon: "warning",
        swlTitle: "เเจ้งเตือน",
        swlText: "คุณต้องการลบหมวดหมู่สินค้านี้หรือไม่!",
      });
    },

    DropdownStatus(statusName) {
      this.pageSizeOpen = false;
    },
    dropdownStatus(event) {
      // ป้องกันการคลิกบนปุ่มที่ทำให้ event ไปถึง listener ของ document
      event.stopPropagation();
      this.DropdownStatusOpen = !this.DropdownStatusOpen;
    },
    closeDropdownStatus(event) {
      // ตรวจสอบว่าคลิกภายนอกปุ่มและ dropdown หรือไม่
      const dropdown = this.$refs.statusMenu;
      if (dropdown && !dropdown.contains(event.target)) {
        this.DropdownStatusOpen = false;
      }
    },

    DropdownPageSize(size) {
      this.pageSizeOpen = false;
    },
    togglePageSize(event) {
      // ป้องกันการคลิกบนปุ่มที่ทำให้ event ไปถึง listener ของ document
      event.stopPropagation();
      this.pageSizeOpen = !this.pageSizeOpen;
    },
    closeDropdown(event) {
      // ตรวจสอบว่าคลิกภายนอกปุ่มและ dropdown หรือไม่
      const dropdown = this.$refs.pageSizeMenu;
      if (dropdown && !dropdown.contains(event.target)) {
        this.pageSizeOpen = false;
      }
    },
  },
};
</script>
