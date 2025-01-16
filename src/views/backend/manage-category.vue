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
                    v-for="(category, index) in categorys"
                    :key="index"
                    @click="showFormEdit(category.id)"
                    class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 cursor-pointer hover:bg-gray-100 transition"
                  >
                    <th
                      scope="row"
                      class="px-6 py-4 font-medium whitespace-nowrap"
                    >
                      <span class="font-semibold">{{ category.name }}</span>
                    </th>
                    <td class="px-6 py-4 whitespace-nowrap">
                      <span
                        v-if="category.status === 'active'"
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
                        @click.stop="btnDelete(category.id)"
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
                    v-model="category.name"
                    ref="inputNameProductType"
                    :class="{
                      'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                      'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                        !category.name,
                    }"
                    placeholder="ใส่ชื่อหมวดหมู่สินค้า"
                    required
                  />
                </div>
                <div class="lg:w-1/2 w-full">
                  <select
                    v-model="category.status"
                    ref="inputStatusProductType"
                    :class="{
                      'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                      'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                        !category.status,
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
                @click.stop="btnDelete(category.id)"
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
                    v-model="category.name"
                    ref="inputNameProductType"
                    :class="{
                      'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                      'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                        !category.name,
                    }"
                    placeholder="ใส่ชื่อหมวดหมู่สินค้า"
                    required
                  />
                </div>
                <div class="lg:w-1/2 w-full">
                  <select
                    v-model="category.status"
                    ref="inputStatusProductType"
                    :class="{
                      'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                      'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                        !category.status,
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

      categorys: [],

      category: {
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
    this.getListCategory();

    document.addEventListener("click", this.closeDropdownStatus);
    document.addEventListener("click", this.closeDropdown);
  },
  methods: {
    // เพิ่มหมวดหมู่สินค้า
    showFormAdd() {
      this.formTable = false;
      this.formAdd = true;
      this.formEdit = false;

      this.category.name = "";
      this.category.status = "";
    },

    showFormTable() {
      this.formTable = true;
      this.formAdd = false;
      this.formEdit = false;

      this.getListCategory();
    },

    //เเสดงข้อมูลประเภทสินค้าบนตาราง
    async getListCategory() {
      await axios
        .get(`${this.apiUrl}category/get_category_not_remove`)
        .then((response) => {
          const data = response.data;
          this.categorys = data.rows;
          console.log(this.categorys);
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
          `${this.apiUrl}category/get_category/${productTypeId}`
        );

        // ตรวจสอบว่าข้อมูลของสินค้าได้รับมาอย่างถูกต้อง
        if (response.status === 200) {
          const category = response.data.row;

          if (category) {
            this.category.id = productTypeId;
            this.category.name = category.name;
            this.category.status = category.status;

            // แสดงข้อมูลสินค้าใน console
            console.log("Product Data:", category);
          } else {
            alert("ไม่พบข้อมูลประเภทสินค้าที่ต้องการแก้ไข");
          }
        } else {
          alert(`Failed to fetch product type: ${response.statusText}`);
        }
      } catch (error) {
        console.error(
          `Error fetching product type ${productTypeId} from ${this.apiUrl}category/${productTypeId}:`,
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

    async btnAdd() {
      if (!this.category.name) {
        this.isFocus = true;
        this.$refs.inputNameProductType.focus();
      } else if (!this.category.status) {
        this.isFocus = true;
        this.$refs.inputStatusProductType.focus();
      } else {
        try {
          const dataProductType = {
            name: this.category.name,
            status: this.category.status,
          };

          const response = await axios.post(
            `${this.apiUrl}category/add_category`,
            dataProductType
          );

          if (response.status === 200) {
            this.$refs.modal.showAlertModal({
              swlIcon: "success",
              swlTitle: "สำเร็จ",
              swlText: response.data.message,
            });
          }
        } catch (error) {
          this.$refs.modal.showAlertModal({
            swlIcon: "error",
            swlTitle: "เกิดข้อผิดพลาด",
            swlText: error,
          });
        }
      }
    },

    async btnEdit() {
      if (!this.category.name) {
        this.isFocus = true;
        this.$refs.inputNameProductType.focus();
      } else {
        try {
          const dataProductType = {
            name: this.category.name,
            status: this.category.status,
          };

          const response = await axios.put(
            `${this.apiUrl}category/update_category/${this.category.id}`,
            dataProductType
          );

          if (response.status === 200) {
            this.$refs.modal.showAlertModal({
              swlIcon: "success",
              swlTitle: "สำเร็จ",
              swlText: response.data.message,
            });
          }
        } catch (error) {
          this.$refs.modal.showAlertModal({
            swlIcon: "error",
            swlTitle: "เกิดข้อผิดพลาด",
            swlText: error,
          });
        }
      }
    },

    btnDelete(productTypeId) {
      console.log(productTypeId)
      // เรียกใช้งาน modal เพื่อแสดงคำเตือน
      this.$refs.modal.showDeleteModal({
        swlIcon: "warning",
        swlTitle: "แจ้งเตือน",
        swlText: "คุณต้องการลบประเภทสินค้านี้หรือไม่!",
        onConfirm: () => {
          // เมื่อผู้ใช้กด "ยืนยัน" ใน modal
          axios
            .put(`${this.apiUrl}category/remove_category/${productTypeId}`)
            .then((response) => {
              // แสดงข้อความว่า "ลบสำเร็จ"
              this.$swal
                .fire({
                  title: "ลบสำเร็จ",
                  icon: "success",
                  confirmButtonText: "ยืนยัน",
                  customClass: {
                    confirmButton:
                      "bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400",
                  },
                })
                .then(() => {
                  // เมื่อกดปุ่ม "ยืนยัน" ใน swal ที่สอง
                  this.showFormTable();
                });
            })
            .catch((error) => {
              console.error("Error updating product status:", error);
              this.$swal.fire({
                title: "เกิดข้อผิดพลาด",
                text: "ไม่สามารถอัปเดตสถานะสินค้าได้",
                icon: "error",
                confirmButtonText: "ยืนยัน",
                customClass: {
                  confirmButton:
                    "bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400",
                },
              });
            });
        },
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
