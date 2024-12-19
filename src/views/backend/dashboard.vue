<script setup>
import backend_navbar from '@/components/backend/navbar.vue';
import VueApexCharts from "vue3-apexcharts";
</script>

<template>

    <backend_navbar />

    <div class="p-4 lg:pr-64 lg:pl-64 pt-6 sm:ml-64">
        <div class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-14">

            <div class="p-4 mt-2 mb-2">
                <div class="w-full rounded-md text-gray-600">
                    <!-- title -->
                    <div class="flex gap-2 items-center mb-2">
                        <p class="text-3xl font-semibold">หน้าเเรก</p>
                    </div>

                    <div class="w-full gap-2 mb-2 pt-1 mt-4">

                        <!-- grid data -->
                        <div class="grid grid-cols-1 lg:grid-cols-4 gap-4 ">
                            <div class="w-full rounded-md shadow-md">
                                <div class="p-4 flex justify-between items-center">
                                    <div>
                                        <p class="text-2xl font-semibold">4</p>
                                        <p class="text-md">จำนวนรายการสินค้า</p>
                                    </div>
                                    <div
                                        class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500">
                                        <i class="fa-solid fa-boxes-packing"></i>
                                    </div>
                                </div>
                                <div
                                    class="flex justify-between items-center p-2 bg-gray-100 text-sm text-blue-500 cursor-pointer">
                                    <p>ดูทั้งหมด</p>
                                    <i class="fa-solid fa-circle-arrow-right"></i>
                                </div>
                            </div>
                            <div class="w-full rounded-md shadow-md">
                                <div class="p-4 flex justify-between items-center">
                                    <div>
                                        <p class="text-2xl font-semibold">3</p>
                                        <p class="text-md">จำนวนรายการลูกค้า</p>
                                    </div>
                                    <div
                                        class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500">
                                        <i class="fa-solid fa-boxes-packing"></i>
                                    </div>
                                </div>
                                <div
                                    class="flex justify-between items-center p-2 bg-gray-100 text-sm text-blue-500 cursor-pointer">
                                    <p>ดูทั้งหมด</p>
                                    <i class="fa-solid fa-circle-arrow-right"></i>
                                </div>
                            </div>
                            <div class="w-full rounded-md shadow-md">
                                <div class="p-4 flex justify-between items-center">
                                    <div>
                                        <p class="text-2xl font-semibold">1</p>
                                        <p class="text-md">จำนวนรายการคำสั่งซื้อ</p>
                                    </div>
                                    <div
                                        class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500">
                                        <i class="fa-solid fa-boxes-packing"></i>
                                    </div>
                                </div>
                                <div
                                    class="flex justify-between items-center p-2 bg-gray-100 text-sm text-blue-500 cursor-pointer">
                                    <p>ดูทั้งหมด</p>
                                    <i class="fa-solid fa-circle-arrow-right"></i>
                                </div>
                            </div>
                            <div class="w-full rounded-md shadow-md">
                                <div class="p-4 flex justify-between items-center">
                                    <div>
                                        <p class="text-2xl font-semibold">20</p>
                                        <p class="text-md">กำไร</p>
                                    </div>
                                    <div
                                        class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500">
                                        <i class="fa-solid fa-boxes-packing"></i>
                                    </div>
                                </div>
                                <div
                                    class="flex justify-between items-center p-2 bg-gray-100 text-sm text-blue-500 cursor-pointer">
                                    <p>ดูทั้งหมด</p>
                                    <i class="fa-solid fa-circle-arrow-right"></i>
                                </div>
                            </div>
                        </div>

                        <div class="grid grid-cols-1 lg:grid-cols-4 gap-4 lg:mt-4">
                            <div class="w-full rounded-md shadow-md lg:col-span-3">
                                <div class="p-4 flex justify-start gap-4 items-center">
                                    <div
                                        class="h-12 w-12 rounded-md bg-gray-100 flex items-center justify-center text-blue-500">
                                        <i class="fa-solid fa-chart-simple"></i>
                                    </div>
                                    <p class="text-2xl font-semibold">กราฟเเสดงกำไรรายเดือน</p>
                                </div>

                                <apexcharts type="line" :options="chartOptions" :series="chartSeries" />
                            </div>
                            <div class="w-full rounded-md shadow-md lg:col-span-1">
                                <div class="">data</div>
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
            chartOptions: {
                chart: {
                    id: "vuechart-example",
                },
                xaxis: {
                    categories: ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน",
                        "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"],
                },
            },
            chartSeries: [
                {
                    name: "Sales",
                    data: [300, 248, 350, 450, 249, 160],
                },
            ],
        };
    },
};
</script>