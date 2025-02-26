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
              <p class="text-3xl font-semibold">รายการลูกค้า</p>
            </div>

            <!-- sort -->
            <div class="lg:flex lg:justify-between mb-4 mt-4 items-center">
              <!-- ช่องค้นหา -->
              <div class="flex items-center w-1/4">
                <label for="voice-search" class="sr-only">Search</label>

                <div class="relative w-full">
                  <div
                    class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none"
                  >
                    <i class="fa-solid fa-magnifying-glass"></i>
                  </div>
                  <input
                    type="text"
                    v-model="searchText"
                    @input="searchMember"
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full pl-10 pr-10 p-2.5 focus:border-gray-300"
                    placeholder="ค้นหา..."
                  />

                  <button
                    @click="xmark"
                    class="absolute inset-y-0 end-0 flex items-center ps-3 p-3 pointer"
                  >
                    <i class="fa-solid fa-xmark"></i>
                  </button>
                </div>
              </div>

              <div class="flex gap-2 justify-center pt-4 lg:pt-0">
                <!-- เลือกสถานะ-->
                <div class="relative">
                  <!-- ปุ่มเลือกสถานะ-->
                  <button
                    class="border border-gray-300 bg-gray-50 font-medium rounded-lg text-sm px-16 p-2.5 text-center inline-flex items-center h-full"
                    type="button"
                    @click="clickDropdownStatus"
                  >
                    <span class="mr-2">
                      <span>สถานะ : {{ DropdownStatusName }}</span>
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
                          @click="DropdownStatus('active', 'เเสดง')"
                          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          >เเสดง</a
                        >
                      </li>
                      <li>
                        <a
                          href="#"
                          @click="DropdownStatus('inactive', 'ไม่เเสดง')"
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
                    class="border border-gray-300 bg-gray-50 font-medium rounded-lg text-sm px-5 p-2.5 text-center inline-flex items-center h-full"
                    type="button"
                    @click="togglePageSize"
                  >
                    <span class="mr-2">{{ dataPaging.rows }}</span
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
                          @click="pageSize(3)"
                          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          >3</a
                        >
                      </li>
                      <li>
                        <a
                          href="#"
                          @click="pageSize(5)"
                          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          >5</a
                        >
                      </li>
                      <li>
                        <a
                          href="#"
                          @click="pageSize(10)"
                          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          >10</a
                        >
                      </li>
                      <li>
                        <a
                          href="#"
                          @click="pageSize(20)"
                          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          >20</a
                        >
                      </li>
                      <li>
                        <a
                          href="#"
                          @click="pageSize(50)"
                          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          >50</a
                        >
                      </li>
                      <li>
                        <a
                          href="#"
                          @click="pageSize(100)"
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
                    <th scope="col" class="px-6 py-4 whitespace-nowrap">รูป</th>
                    <th scope="col" class="px-6 py-4 whitespace-nowrap">
                      รหัส
                    </th>
                    <th scope="col" class="px-6 py-4 whitespace-nowrap">
                      ชื่อ
                    </th>
                    <th scope="col" class="px-6 py-4 whitespace-nowrap">
                      เบอร์
                    </th>
                    <th scope="col" class="px-6 py-4 whitespace-nowrap">
                      สถานะ
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="(member, index) in members"
                    :key="index"
                    @click="showFormEdit(member.id)"
                    class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 cursor-pointer hover:bg-gray-100 transition"
                  >
                    <th scope="row" class="px-6 py-4">
                      <div class="w-20 h-20">
                        <img
                          class="w-full h-full rounded-full object-cover ring-4 ring-gray-300 shadow-md"
                          src="../../assets/image/system/cathothead.jpg"
                        />
                      </div>
                    </th>

                    <td class="px-6 py-4 whitespace-nowrap font-semibold">
                      {{ member.code }}
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                      {{ member.name }}
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                      {{ member.phone }}
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                      <span
                        v-if="member.status === 'active'"
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
                  </tr>
                </tbody>
              </table>
              <pagination
                ref="paginationRef"
                :pageSize="dataPaging.rows"
                :totalList="totalList"
                @reloadData="reloadData"
              />
            </div>
          </div>

          <div v-if="formEdit">
            <!-- title -->
            <div class="flex justify-between items-center mb-2">
              <p class="text-3xl font-semibold">ข้อมูลลูกค้า</p>
            </div>

            <div class="flex justify-center w-full">
              <div class="w-28 h-28 lg:w-44 lg:h-44 mt-4 mb-2">
                <img
                  class="w-full h-full rounded-full object-cover ring-4 ring-gray-300 shadow-md"
                  src="../../assets/image/system/cathothead.jpg"
                />
              </div>
            </div>

            <div class="md:flex w-full gap-2 mb-2 pt-1 mt-4">
              <div class="flex gap-2 w-full">
                <div class="lg:w-1/2 w-full">
                  <input
                    type="text"
                    v-model="member.code"
                    ref="inputCodeMember"
                    :class="{
                      'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                      'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                        !member.code,
                    }"
                    placeholder="รหัส"
                  />
                </div>

                <div class="lg:w-1/2 w-full">
                  <input
                    type="text"
                    v-model="member.name"
                    ref="inputNameMember"
                    :class="{
                      'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                      'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                        !member.name,
                    }"
                    placeholder="ชื่อลูกค้า"
                  />
                </div>
              </div>

              <div class="flex gap-2 w-full pt-1 mt-4 lg:pt-0 lg:mt-0">
                <div class="lg:w-1/2 w-full">
                  <input
                    type="text"
                    v-model="member.phone"
                    ref="inputPhoneMember"
                    :class="{
                      'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                      'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                        !member.phone,
                    }"
                    placeholder="เบอร์"
                  />
                </div>

                <div class="lg:w-1/2 w-full">
                  <select
                    v-model="member.status"
                    ref="inputStatusMember"
                    :class="{
                      'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-200 h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                      'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                        !member.status,
                    }"
                  >
                    <option value="" disabled>สถานะ</option>
                    <option value="active">เเสดง</option>
                    <option value="inactive">ไม่เเสดง</option>
                  </select>
                </div>
              </div>
            </div>

            <div
              class="flex gap-2 items-center mb-4 mt-8 text-2xl font-semibold"
            >
              <span class="">ยอดรวมคำสั่งซื้อทั้งหมด :</span>
              <span class="text-orange-500">600บาท</span>
            </div>

            <hr class="my-2 text-gray-600" />

            <div class="flex gap-2 justify-center mt-4 md:mt-4">
              <button
                @click="btnEdit"
                class="text-white bg-blue-500 border border-blue-500 font-medium rounded-lg text-sm px-3 p-2.5 text-center inline-flex items-center h-full"
              >
                ยืนยัน
              </button>
              <button
                @click="showFormTable"
                class="text-black bg-gray-200 border border-gray-400 font-medium rounded-lg text-sm px-3 p-2.5 text-center inline-flex items-center h-full"
              >
                ยกเลิก
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import backend_navbar from "@/components/backend/navbar.vue";
import Modal from "@/components/backend/modal.vue";
import pagination from "@/components/backend/paging.vue";
export default {
  components: { backend_navbar, Modal, pagination },
  data() {
    return {
      apiUrl: __API_URL__,
      searchText: "",
      members: [],
      memberId: "",
      memberStatus: "",
      member: {
        code: "",
        name: "",
        phone: "",
        status: "",
      },

      dataPaging: {
        pageNumber: 1,
        rows: 5,
        totalPage: 0,
        status: "",
      },
      totalList: [],

      isFocus: false,
      formTable: true,
      formAdd: false,
      formEdit: false,

      DropdownStatusName: "ทั้งหมด",
      DropdownStatusOpen: false,
      pageSizeOpen: false,
    };
  },
  mounted() {
    this.checkAuth();
    document.addEventListener("click", this.closeDropdownStatus);
    document.addEventListener("click", this.closeDropdown);
  },

  methods: {
    checkAuth() {
      const adminRole = localStorage.getItem("admin_role");

      if (adminRole !== "admin") {
        this.$router.push("/backend/login");
      } else {
        this.getListMember();
      }
    },
    showFormTable() {
      this.formTable = true;
      this.formAdd = false;
      this.formEdit = false;
      this.dataPaging.pageNumber = 1;
      this.getListMember();
    },

    //เเสดงข้อมูลสมาชิกบนตาราง
    async getListMember() {
      await axios
        .get(`${this.apiUrl}members/`, {
          params: {
            limit: this.dataPaging.rows,
            page: this.dataPaging.pageNumber,
            q: this.searchText,
            status: this.memberStatus,
          },
        })
        .then((response) => {
          const data = response.data;
          this.members = data.rows;
          this.totalList = data.total;
          console.log(this.members);
        })
        .catch((error) => {
          console.error("There was an error fetching the data:", error);
        });
    },
    reloadData(pageNo) {
      this.dataPaging.pageNumber = pageNo;
      this.getListMember();

      console.log("pageNo", pageNo);
    },
    pageSize(row) {
      // ตรวจสอบว่าค่า row ใหม่ไม่เท่ากับค่าเดิม
      if (this.dataPaging.rows !== row) {
        this.dataPaging.pageNumber = 1;
        this.dataPaging.rows = row;
        this.getListMember();
        this.pageSizeOpen = false;
      }
    },
    searchMember() {
      this.dataPaging.pageNumber = 1;
      this.getListMember();
      this.$refs.paginationRef.resetPage();
    },
    xmark() {
      this.searchText = "";
      this.dataPaging.pageNumber = 1;
      this.getListMember();
      this.$refs.paginationRef.resetPage();
    },

    async showFormEdit(memberId) {
      // เปิดฟอร์มแก้ไข
      this.formTable = false;
      this.formAdd = false;
      this.formEdit = true;

      // รีเซ็ตค่าเริ่มต้นในฟอร์ม
      this.member.code = "";
      this.member.name = "";
      this.member.phone = "";
      this.member.status = "";

      try {
        // เรียก API เพื่อดึงข้อมูลสมาชิกที่ระบุ
        const response = await axios.get(`${this.apiUrl}members/${memberId}`);

        if (response.status === 200) {
          const member = response.data.row;

          if (member) {
            this.memberId = memberId;
            this.member.code = member.code;
            this.member.name = member.name;
            this.member.phone = member.phone;
            this.member.status = member.status;
          } else {
            alert("ไม่พบข้อมูลสมาชิกที่ต้องการแก้ไข");
          }
        }
      } catch (error) {
        console.error("เกิดข้อผิดพลาดในการดึงข้อมูลสมาชิก:", error);
        alert(
          "เกิดข้อผิดพลาด: " + (error.response?.data?.detail || error.message)
        );
      }
    },

    async btnEdit() {
      if (!this.member.code) {
        this.isFocus = true;
        this.$refs.inputCodeMember.focus();
      } else if (!this.member.name) {
        this.isFocus = true;
        this.$refs.inputNameMember.focus();
      } else if (!this.member.phone) {
        this.isFocus = true;
        this.$refs.inputPhoneMember.focus();
      } else if (!this.member.status) {
        this.isFocus = true;
        this.$refs.inputStatusMember.focus();
      } else {
        try {
          const dataMember = {
            code: this.member.code,
            name: this.member.name,
            phone: this.member.phone,
            status: this.member.status,
          };

          // เรียก API เพื่ออัปเดตข้อมูลสมาชิก
          const response = await axios.put(
            `${this.apiUrl}members/${this.memberId}`,
            dataMember
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
            swlTitle: "ล้มเหลว",
            swlText: "เกิดข้อผิดพลาดในการอัปเดตข้อมูล",
          });
        }
      }
    },

    ///// {{ DropdownStatus }} /////
    DropdownStatus(status, name) {
      this.memberStatus = status;
      this.dataPaging.pageNumber = 1;
      this.getListMember();
      this.DropdownStatusName = name;
      if (status === "" || name === "") {
        this.DropdownStatusName = "ทั้งหมด";
      }
      this.DropdownStatusOpen = false;
      this.$refs.paginationRef.resetPage();
    },
    clickDropdownStatus(event) {
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
