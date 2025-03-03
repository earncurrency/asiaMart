<script setup>
import axios from "axios";
import VueApexCharts from "vue3-apexcharts";
</script>

<template>
  <div class="grid grid-cols-1 lg:grid-cols gap-4">
    <!-- กราฟแสดงกำไรรายเดือนต่อปี -->
    <div class="w-full rounded-md shadow-md lg:col-span-3">
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
</template>

<script>
export default {
  components: {
    apexcharts: VueApexCharts,
  },
  data() {
    return {
      apiUrl: __API_URL__,

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


    };
  },
  mounted() {
    this.getDataChart();
  },
  methods: {

    getDataChart() {
      axios
        .get(`${this.apiUrl}dashboard/chart/`)
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


        })
        .catch((error) => {
          console.error("There was an error fetching the data:", error);
        });
    },

  },
};
</script>
