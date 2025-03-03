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
  </div>
</template>

<script>
import axios from "axios";

export default {
  components: {
    apexcharts: VueApexCharts,
  },
  props: {
    monthYear: {
      required: false,
      default: "",
    },
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
  watch: {
    monthYear(newMonthYear) {
      this.getDataChart();
    },
  },
  methods: {
    getDataChart() {

      // if (!this.monthYear) return;

      axios
        .get(`${this.apiUrl}report/chart/`, {
          params: {
            month_year: this.monthYear,
          },
        })
        .then((response) => {
          const data = response.data.rows;

          // แยกข้อมูลเดือนและยอดขาย
          const categories = data.map((item) => item.day_month_year);
          const seriesData = data.map((item) => item.total_sum);

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
