<script setup>
    import frontend_navbar from '../../components/frontend/navbar.vue';
</script>

<template>
    <frontend_navbar />
    <div class="flex justify-center pt-24 p-4 ">
        <div
            class="w-full lg:w-2/4 max-w-screen-2xl lg:p-12 lg:border border-gray-200 rounded-lg mb-16 lg:mb-4 bg-white z-40">
            <div>

                <!-- content -->

                <div class="mt-2 mb-2">
                    <div class="p-4 w-full rounded-md text-gray-600">
                        <p class="mb-6 text-3xl font-semibold">ประวัติคำสั่งซื้อ</p>

                        <RouterLink to="/order-detail">
                            <div class="w-full h-auto bg-gray-50 rounded-md p-4 shadow-md text-md cursor-pointer mb-4">
                                <div class="flex gap-2">
                                    <p>วันที่</p>
                                    <p class="font-semibold">2024/12/06</p>
                                    <p>เวลา</p>
                                    <p class="font-semibold">09:31</p>
                                </div>

                                <div class="flex items-center gap-4 border p-2 lg:p-4 rounded-md mt-3 mb-3">
                                    <div class="text-green-500 text-5xl">
                                        <i class="fa-solid fa-circle-check"></i>
                                    </div>
                                    <div>
                                        <div class="flex gap-2 mt-1">
                                            <p class="">เลขที่ : </p>
                                            <p class="font-semibold">78945623</p>
                                        </div>

                                        <div class="flex gap-2 mt-1">
                                            <p class="">สถานะ : </p>
                                            <p class="font-semibold">รับสินค้าเเล้ว</p>
                                        </div>
                                    </div>
                                </div>

                                <div class="lg:flex lg:justify-end gap-4 ">
                                    <div class="flex gap-2">
                                        <p>จำนวนสินค้า : </p>
                                        <p class="">4 ชิ้น</p>
                                    </div>
                                    <div class="flex gap-2 text-orange-500">
                                        <p>ราคารวม : </p>
                                        <p class="font-semibold ">121.00 บาท</p>
                                    </div>

                                </div>
                            </div>
                        </RouterLink>


                        <div class="w-full h-auto bg-gray-50 rounded-md p-4 shadow-md text-md cursor-pointer mb-4">

                            <div class="flex items-center justify-center gap-4 border p-2 lg:p-4 rounded-md mt-3 mb-3">
                                <img src="../../assets/image/system/shopping-basket.png" alt=""
                                    class="h-10 w-10 lg:h-14 lg:w-14 object-cover">
                                <p class="font-semibold text-md lg:text-2xl">ไม่มีประวัติคำสั่งซื้อ</p>
                            </div>

                        </div>

                    </div>
                </div>


            </div>

        </div>
    </div>
</template>