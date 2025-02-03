<script setup>
import backend_navbar from "@/components/backend/navbar.vue";
import VueApexCharts from "vue3-apexcharts";
import axios from "axios";
import { data } from "autoprefixer";
</script>

<template>
  <backend_navbar />
  <div class="p-4 lg:pr-24 lg:pl-24 pt-6 sm:ml-64">
    <div
      class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-14"
    >
      <div class="lg:p-4 mt-2 mb-2">
        <div class="w-full rounded-md text-gray-600">
          <!-- title -->
          <div class="flex gap-2 items-center mb-2">
            <p class="text-3xl font-semibold">หน้าเเรก</p>
          </div>

          <div class="w-full gap-2 mb-2 pt-1 mt-4">
            <!-- grid data -->
            <div class="grid grid-cols-1 lg:grid-cols-4 gap-4">
              <div class="w-full rounded-md shadow-md">
                <div
                  class="p-4 flex justify-between items-center bg-gray-800 text-white rounded-t-md"
                >
                  <div>
                    <p class="text-2xl font-semibold">{{ productTotal }}</p>
                    <p class="text-md">จำนวนสินค้า</p>
                  </div>
                  <div
                    class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500"
                  >
                    <i class="fa-solid fa-boxes-packing"></i>
                  </div>
                </div>
                <RouterLink to="/backend/manage-product">
                  <div
                    class="flex justify-between items-center p-2 bg-gray-100 text-sm text-blue-500 cursor-pointer rounded-b-md"
                  >
                    <p>ดูทั้งหมด</p>
                    <i class="fa-solid fa-circle-arrow-right"></i>
                  </div>
                </RouterLink>
              </div>
              <div class="w-full rounded-md shadow-md">
                <div
                  class="p-4 flex justify-between items-center bg-gray-800 text-white rounded-t-md"
                >
                  <div>
                    <p class="text-2xl font-semibold">{{ memberTotal }}</p>
                    <p class="text-md">จำนวนลูกค้า</p>
                  </div>
                  <div
                    class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500"
                  >
                    <i class="fa-solid fa-users"></i>
                  </div>
                </div>
                <RouterLink to="/backend/manage-member">
                  <div
                    class="flex justify-between items-center p-2 bg-gray-100 text-sm text-blue-500 cursor-pointer rounded-b-md"
                  >
                    <p>ดูทั้งหมด</p>
                    <i class="fa-solid fa-circle-arrow-right"></i>
                  </div>
                </RouterLink>
              </div>
              <div class="w-full rounded-md shadow-md">
                <div
                  class="p-4 flex justify-between items-center bg-gray-800 text-white rounded-t-md"
                >
                  <div>
                    <p class="text-2xl font-semibold">{{ orderTotal }}</p>
                    <p class="text-md">จำนวนคำสั่งซื้อ</p>
                  </div>
                  <div
                    class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500"
                  >
                    <i class="fa-solid fa-list-check"></i>
                  </div>
                </div>
                <RouterLink to="/backend/manage-order">
                  <div
                    class="flex justify-between items-center p-2 bg-gray-100 text-sm text-blue-500 cursor-pointer rounded-b-md"
                  >
                    <p>ดูทั้งหมด</p>
                    <i class="fa-solid fa-circle-arrow-right"></i>
                  </div>
                </RouterLink>
              </div>
              <div class="w-full rounded-md shadow-md">
                <div
                  class="p-4 flex justify-between items-center bg-gray-800 text-white rounded-t-md"
                >
                  <div>
                    <p class="text-2xl font-semibold">{{ allToTalSum }}</p>
                    <p class="text-md">ยอดขาย</p>
                  </div>
                  <div
                    class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500"
                  >
                    <i class="fa-solid fa-baht-sign"></i>
                  </div>
                </div>
                <div
                  class="flex justify-between items-center p-2 bg-gray-100 text-sm text-blue-500 cursor-pointer rounded-b-md"
                >
                  <p>ดูทั้งหมด</p>
                  <i class="fa-solid fa-circle-arrow-right"></i>
                </div>
              </div>
            </div>

            <!-- grid chart -->
            <div class="grid grid-cols-1 lg:grid-cols gap-4 mt-8">
              <!-- กราฟแสดงกำไรรายเดือนต่อปี -->
              <div class="w-full rounded-md shadow-md lg:col-span-3">
                <div class="p-4 flex justify-start gap-4 items-center">
                  <div
                    class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500"
                  >
                    <i class="fa-solid fa-chart-simple"></i>
                  </div>
                  <p class="text-2xl font-semibold">
                    กราฟแสดงยอดขายรายเดือนต่อปี
                  </p>
                </div>

                <!-- กราฟเส้น -->
                <apexcharts
                  height="450"
                  type="line"
                  :options="lineChartOptions"
                  :series="lineChartSeries"
                />
              </div>

              <!-- <div class="w-full flex flex-col lg:flex-col gap-4">

                <div class="w-full rounded-md shadow-md">
                  <div class="p-4 flex justify-start gap-4 items-center">
                    <div
                      class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500"
                    >
                      <i class="fa-solid fa-arrow-up-short-wide"></i>
                    </div>
                    <p class="text-2xl font-semibold">
                      หมวดหมู่สินค้าที่ขายได้
                    </p>
                  </div>
                  <apexcharts
                    type="donut"
                    :options="donutChartOptions"
                    :series="donutChartSeries"
                  />
                </div>

                <div class="w-full rounded-md shadow-md">
                  <div class="p-4 flex justify-start gap-4 items-center">
                    <div
                      class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500"
                    >
                      <i class="fa-solid fa-location-dot"></i>
                    </div>
                    <p class="text-2xl font-semibold">สถานที่จัดส่ง</p>
                  </div>
                  <apexcharts
                    type="donut"
                    :options="locationChartOptions"
                    :series="locationChartSeries"
                  />
                </div>
              </div> -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  components: {
    apexcharts: VueApexCharts,
  },
  data() {
    return {
      apiUrl: "http://127.0.0.1:8000/",

      productTotal: "",
      memberTotal: "",
      orderTotal: "",
      allToTalSum:"",

      lineChartOptions: {
        dataLabels: {
          enabled: true,
        },
        xaxis: {
          categories: [],
        },
      },
      lineChartSeries: [
        {
          name: "ยอดขาย",
          data: [],
        },
      ],

      donutChartOptions: {
        chart: {
          id: "vuechart-donut-example",
          type: "donut",
        },
        labels: ["อาหาร", "เครื่องดื่ม", "ของทานเล่น", "ของใช้ทั่วไป"],
        plotOptions: {
          donut: {
            size: "10%",
          },
        },
      },
      donutChartSeries: [5, 8, 21, 2],

      locationChartOptions: {
        chart: {
          id: "vuechart-donut-example",
          type: "donut",
        },
        labels: ["รับที่ AsiaMart", "บางมด", "บ้านเเพ้ว", "มหาชัย"],
        plotOptions: {
          donut: {
            size: "10%",
          },
        },
      },
      locationChartSeries: [5, 22, 38, 5],
    };
  },
  mounted() {
    this.checkAuth();
  },
  methods: {
    checkAuth() {
      const adminRole = localStorage.getItem("admin_role");

      if (adminRole !== "admin") {
        this.$router.push("/backend/login");
      } else {
        this.getDataChart();
        this.getTotalProduct();
        this.getTotalMember();
        this.getTotalOrder();
      }
    },

    getDataChart() {
      axios
        .get(`${this.apiUrl}orders/chart/`)
        .then((response) => {
          const data = response.data.rows;

          // แยกข้อมูลเดือนและยอดขาย
          const categories = data.map((item) => item.month_year); // ดึงเดือน/ปี
          const seriesData = data.map((item) => item.total_sum); // ดึงยอดขาย

          // อัพเดตค่าใน lineChartOptions และ lineChartSeries
          this.lineChartOptions = {
            xaxis: {
              categories: categories, // ตั้งค่า categories
            },
          };
          this.lineChartSeries = [
            {
              name: "ยอดขาย",
              data: seriesData, // ตั้งค่า data
            },
          ];

          this.allToTalSum = response.data.all_total_sum;

          // console.log(
          //   "Chart data updated:",
          //   this.lineChartOptions,
          //   this.lineChartSeries
          // );
        })
        .catch((error) => {
          console.error("There was an error fetching the data:", error);
        });
    },

    async getTotalProduct() {
      await axios
        .get(`${this.apiUrl}products/`)
        .then((response) => {
          const data = response.data;
          this.productTotal = data.total;
          // console.log("productTotal", this.productTotal);
        })
        .catch((error) => {
          console.error("There was an error fetching the data:", error);
        });
    },

    async getTotalMember() {
      await axios
        .get(`${this.apiUrl}members/`)
        .then((response) => {
          const data = response.data;
          this.memberTotal = data.total;
          // console.log("memberTotal", this.memberTotal);
        })
        .catch((error) => {
          console.error("There was an error fetching the data:", error);
        });
    },

    async getTotalOrder() {
      await axios
        .get(`${this.apiUrl}orders/`)
        .then((response) => {
          const data = response.data;
          this.orderTotal = data.total;
          // console.log("orderTotal", this.orderTotal);
        })
        .catch((error) => {
          console.error("There was an error fetching the data:", error);
        });
    },
  },
};
</script>
