<script setup>
import backend_navbar from '@/components/backend/navbar.vue';
import VueApexCharts from "vue3-apexcharts";
</script>

<template>

    <backend_navbar />
    <div class="p-4 lg:pr-24 lg:pl-24 pt-6 sm:ml-64">
        <div class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-14">

            <div class=" lg:p-4 mt-2 mb-2">
                <div class="w-full rounded-md text-gray-600">
                    <!-- title -->
                    <div class="flex gap-2 items-center mb-2">
                        <p class="text-3xl font-semibold">หน้าเเรก</p>
                    </div>

                    <div class="w-full gap-2 mb-2 pt-1 mt-4">

                        <!-- grid data -->
                        <div class="grid grid-cols-1 lg:grid-cols-4 gap-4 ">
                            <div class="w-full rounded-md shadow-md">
                                <div class="p-4 flex justify-between items-center bg-gray-800 text-white rounded-t-md">
                                    <div>
                                        <p class="text-2xl font-semibold">4</p>
                                        <p class="text-md">จำนวนรายการสินค้า</p>
                                    </div>
                                    <div
                                        class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500">
                                        <i class="fa-solid fa-boxes-packing"></i>
                                    </div>
                                </div>
                                <RouterLink to="/backend/manage-product">
                                    <div
                                        class="flex justify-between items-center p-2 bg-gray-100 text-sm text-blue-500 cursor-pointer rounded-b-md">
                                        <p>ดูทั้งหมด</p>
                                        <i class="fa-solid fa-circle-arrow-right"></i>
                                    </div>
                                </RouterLink>
                            </div>
                            <div class="w-full rounded-md shadow-md">
                                <div class="p-4 flex justify-between items-center bg-gray-800 text-white rounded-t-md">
                                    <div>
                                        <p class="text-2xl font-semibold">3</p>
                                        <p class="text-md">จำนวนรายการลูกค้า</p>
                                    </div>
                                    <div
                                        class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500">
                                        <i class="fa-solid fa-users"></i>
                                    </div>
                                </div>
                                <RouterLink to="/backend/manage-member">
                                    <div
                                        class="flex justify-between items-center p-2 bg-gray-100 text-sm text-blue-500 cursor-pointer rounded-b-md">
                                        <p>ดูทั้งหมด</p>
                                        <i class="fa-solid fa-circle-arrow-right"></i>
                                    </div>
                                </RouterLink>
                            </div>
                            <div class="w-full rounded-md shadow-md">
                                <div class="p-4 flex justify-between items-center bg-gray-800 text-white rounded-t-md">
                                    <div>
                                        <p class="text-2xl font-semibold">1</p>
                                        <p class="text-md">จำนวนรายการคำสั่งซื้อ</p>
                                    </div>
                                    <div
                                        class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500">
                                        <i class="fa-solid fa-list-check"></i>
                                    </div>
                                </div>
                                <RouterLink to="/backend/manage-order">
                                    <div
                                        class="flex justify-between items-center p-2 bg-gray-100 text-sm text-blue-500 cursor-pointer rounded-b-md">
                                        <p>ดูทั้งหมด</p>
                                        <i class="fa-solid fa-circle-arrow-right"></i>
                                    </div>
                                </RouterLink>
                            </div>
                            <div class="w-full rounded-md shadow-md">
                                <div class="p-4 flex justify-between items-center bg-gray-800 text-white rounded-t-md">
                                    <div>
                                        <p class="text-2xl font-semibold">20</p>
                                        <p class="text-md">กำไร</p>
                                    </div>
                                    <div
                                        class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500">
                                        <i class="fa-solid fa-baht-sign"></i>
                                    </div>
                                </div>
                                <RouterLink to="/backend/report">
                                    <div
                                        class="flex justify-between items-center p-2 bg-gray-100 text-sm text-blue-500 cursor-pointer rounded-b-md">
                                        <p>ดูทั้งหมด</p>
                                        <i class="fa-solid fa-circle-arrow-right"></i>
                                    </div>
                                </RouterLink>
                            </div>
                        </div>

                        <!-- grid chart -->
                        <div class="grid grid-cols-1 lg:grid-cols-4 gap-4 mt-8">
                            <!-- กราฟแสดงกำไรรายเดือนต่อปี -->
                            <div class="w-full rounded-md shadow-md lg:col-span-3">
                                <div class="p-4 flex justify-start gap-4 items-center">
                                    <div
                                        class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500">
                                        <i class="fa-solid fa-chart-simple"></i>
                                    </div>
                                    <p class="text-2xl font-semibold">กราฟแสดงกำไรรายเดือนต่อปี</p>
                                </div>

                                <!-- กราฟเส้น -->
                                <apexcharts height="450" type="line" :options="lineChartOptions"
                                    :series="lineChartSeries" />
                            </div>



                            <div class="w-full flex flex-col lg:flex-col gap-4">
                                <!-- กราฟหมวดหมู่สินค้า 1 -->
                                <div class="w-full rounded-md shadow-md">
                                    <div class="p-4 flex justify-start gap-4 items-center">
                                        <div
                                            class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500">
                                            <i class="fa-solid fa-arrow-up-short-wide"></i>
                                        </div>
                                        <p class="text-2xl font-semibold">หมวดหมู่สินค้าที่ขายได้</p>
                                    </div>
                                    <apexcharts type="donut" :options="donutChartOptions" :series="donutChartSeries" />
                                </div>

                                <!-- กราฟหมวดหมู่สินค้า 2 -->
                                <div class="w-full rounded-md shadow-md">
                                    <div class="p-4 flex justify-start gap-4 items-center">
                                        <div
                                            class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500">
                                            <i class="fa-solid fa-location-dot"></i>
                                        </div>
                                        <p class="text-2xl font-semibold">สถานที่จัดส่ง</p>
                                    </div>
                                    <apexcharts type="donut" :options="locationChartOptions"
                                        :series="locationChartSeries" />
                                </div>
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
    components: {
        apexcharts: VueApexCharts,
    },
    data() {
        return {
            lineChartOptions: {
                chart: {
                    id: "vuechart-line-example",
                },
                xaxis: {
                    categories: ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน",
                        "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"],
                },
            },
            lineChartSeries: [
                {
                    name: "กำไร",
                    data: [300, 248, 350, 350, 249, 160, 230, 300, 100, 200, 150, 20],
                },
            ],

            donutChartOptions: {
                chart: {
                    id: "vuechart-donut-example",
                    type: "donut",
                },
                labels: ['อาหาร', 'เครื่องดื่ม', 'ของทานเล่น', 'ของใช้ทั่วไป'],
                plotOptions: {
                    donut: {
                        size: '10%',
                    }
                },
            },
            donutChartSeries: [5, 8, 21, 2],

            locationChartOptions: {
                chart: {
                    id: "vuechart-donut-example",
                    type: "donut",
                },
                labels: ['รับที่ AsiaMart', 'บางมด', 'บ้านเเพ้ว', 'มหาชัย'],
                plotOptions: {
                    donut: {
                        size: '10%',
                    }
                },
            },
            locationChartSeries: [5, 22, 38, 5],
        };
    },
};
</script>