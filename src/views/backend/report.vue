<template class="">
  <backend_navbar />

  <div class="p-4 lg:pr-24 lg:pl-24 pt-6 sm:ml-64">
    <div
      class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-14"
    >
      <div class="mt-2 mb-2">
        <div class="lg:p-4 w-full rounded-md text-gray-600">
          <!-- title -->
          <p class="mb-6 text-3xl font-semibold">ยอดขาย</p>

          <!-- content -->

          <!-- sort -->
          <div class="lg:flex lg:justify-start items-center mb-6">
            <!-- ช่องค้นหา -->

            <div class="flex gap-2 justify-center pt-4">
              <!-- เลือกขนาดเเถวในตาราง -->
              <div class="relative">
                <!-- ปุ่มเลือกขนาดเเถวในตาราง -->
                <button
                  class="border border-gray-300 bg-gray-50 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center h-full"
                  type="button"
                  @click="togglePageSize"
                >
                  <span class="mr-2">{{ DropdownMonthYearsName }}</span
                  ><i class="fa-solid fa-angle-down"></i>
                </button>
                <!-- เมนูขนาดเเถวในตาราง -->
                <div
                  v-show="pageSizeOpen"
                  ref="pageSizeMenu"
                  class="z-50 absolute right-0 mt-2 text-base list-none w-full bg-white divide-y divide-gray-100 rounded-lg shadow border border-gray-300"
                >
                  <ul class="py-2">
                    <li v-for="monthYear in monthYears">
                      <a
                        href="#"
                        @click="DropdownMonthYear(monthYear)"
                        class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                        >{{ monthYear }}</a
                      >
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

          <!-- grid chart -->
          <div class="p-4 flex justify-start gap-4 items-center">
            <p class="text-2xl font-semibold">กราฟแสดงยอดขาย {{ DropdownMonthYearsName }}</p>
          </div>
          <report_chart :monthYear="monthYear" />

          <!-- ตาราง -->
          <!-- <div class="p-4 flex justify-start gap-4 items-center mt-8">
            <p class="text-2xl font-semibold">รายการสินค้าที่ขายได้เดือนนี้</p>
          </div> -->
          <!-- <div
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
                  <th scope="col" class="px-6 py-4 whitespace-nowrap">รหัส</th>
                  <th scope="col" class="px-6 py-4 whitespace-nowrap">ชื่อ</th>
                  <th scope="col" class="px-6 py-4 whitespace-nowrap">
                    ราคาทุน
                  </th>
                  <th scope="col" class="px-6 py-4 whitespace-nowrap">
                    ราคาขาย
                  </th>
                  <th scope="col" class="px-6 py-4 whitespace-nowrap">
                    จำนวนที่ขายได้
                  </th>
                  <th scope="col" class="px-6 py-4 whitespace-nowrap">กำไร</th>
                </tr>
              </thead>
              <tbody>
                <tr
                  class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 cursor-pointer hover:bg-gray-100 transition"
                >
                  <th scope="row" class="px-6 py-4">
                    <div class="w-24 h-14 lg:w-36 lg:h-24">
                      <img
                        class="w-full h-full rounded-md object-cover ring-4 ring-gray-300 shadow-md"
                        src="../../assets/image/product/food1.jpg"
                      />
                    </div>
                  </th>
                  <td class="px-6 py-4 whitespace-nowrap font-semibold">
                    78945623
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">สินค้าทดสอบ 01</td>
                  <td class="px-6 py-4 whitespace-nowrap">145</td>
                  <td class="px-6 py-4 whitespace-nowrap">150</td>
                  <td class="px-6 py-4 whitespace-nowrap">1</td>
                  <td
                    class="px-6 py-4 whitespace-nowrap font-semibold text-green-500"
                  >
                    5
                  </td>
                </tr>
              </tbody>
            </table>
          </div> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import report_chart from "@/components/backend/report/chart.vue";
import backend_navbar from "@/components/backend/navbar.vue";
export default {
  components: { report_chart, backend_navbar },
  data() {
    return {
      apiUrl: __API_URL__,

      DropdownMonthYearsName: "ทั้งหมด",
      monthYears: [],
      monthYear: "",

      DropdownStatusOpen: false,
      pageSizeOpen: false,
    };
  },
  mounted() {
    this.getMonthYear();
    document.addEventListener("click", this.closeDropdownStatus);
    document.addEventListener("click", this.closeDropdown);
  },

  methods: {
    getMonthYear() {
      axios
        .get(`${this.apiUrl}dashboard/chart/`)
        .then((response) => {
          const data = response.data.rows;

          this.monthYears = data.map((item) => item.month_year);

          console.log("เดือนที่เลือก", this.monthYear);
          console.log("getMonthYear", this.monthYears);
        })
        .catch((error) => {
          console.error("There was an error fetching the data:", error);
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

    DropdownMonthYear(montYear) {
      this.monthYear = montYear;
      this.getMonthYear();

      this.DropdownMonthYearsName = montYear;
      if (montYear === "") {
        this.DropdownCategoryName = "ทั้งหมด";
      }

      this.pageSizeOpen = false;
      console.log(this.monthYear);
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
