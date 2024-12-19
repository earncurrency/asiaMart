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


                <div
                    class="mt-4 mb-2 bg-gray-100 p-8 rounded-md flex lg:justify-center gap-4 lg:gap-8 items-center lg:flex-row flex-col text-center lg:text-left ">
                    <img src="../../assets/image/system/cathothead.jpg" alt=""
                        class="h-28 w-28 lg:h-40 lg:w-40 rounded-full bg-gray-300 object-cover ring-4 ring-gray-300 shadow-md mx-auto lg:mx-0">

                    <div class="text-gray-600 text-md">
                        <p class="text-2xl lg:text-3xl font-semibold">เจษฎากร หวานสนิท</p>
                        <div class="lg:flex gap-4 mt-2">
                            <div class="flex gap-2 justify-center lg:justify-start">
                                <p class="font-semibold">รหัสพนักงาน :</p>
                                <p>1670525</p>
                            </div>
                            <div class="flex gap-2 justify-center lg:justify-start">
                                <p class="font-semibold">ตำเเหน่ง :</p>
                                <p>โปรเเกรมเมอร์</p>
                            </div>
                        </div>
                        <div class="lg:flex gap-4 mb-2">
                            <div class="flex gap-2 justify-center lg:justify-start">
                                <p class="font-semibold">เบอร์มือถือ :</p>
                                <p>0xx xxx xxxx</p>
                            </div>
                            <div class="flex gap-2 justify-center lg:justify-start">
                                <p class="font-semibold">ไลน์ :</p>
                                <p>kornwsn04</p>
                            </div>
                        </div>
                        <button class="p-2 pr-4 pl-4 rounded-lg bg-red-600 text-white mt-2 hover:bg-red-500 transition">
                            ออกจากระบบ
                        </button>
                    </div>

                </div>

                <div class="flex justify-end">
                    <RouterLink to="/history">
                        <button
                            class="p-2 pr-4 pl-4 bg-gray-300 rounded-md text-md text-gray-600 hover:bg-gray-200 transition">
                            <i class="fa-solid fa-clock-rotate-left"></i> ประวัติคำสั่งซื้อ</button>
                    </RouterLink>

                </div>

                <div class="mt-2 mb-2">
                    <div class="p-4 w-ful rounded-md text-gray-600">
                        <p class="mb-4 text-md"><i class="fa-solid fa-box"></i> ติดตามสถานะสินค้า</p>

                        <RouterLink to="/order-detail">

                            <div class="w-full h-auto bg-gray-50 rounded-md p-4 shadow-md text-md cursor-pointer mb-4">
                                <div class="flex gap-2">
                                    <p>วันที่</p>
                                    <p class="font-semibold">2024/12/06</p>
                                    <p>เวลา</p>
                                    <p class="font-semibold">09:31</p>
                                </div>

                                <div class="flex items-center gap-4 border p-2 lg:p-4 rounded-md mt-3 mb-3">
                                    <img src="../../assets/image/system/delivery-bike.png" alt=""
                                        class="h-12 w-12 lg:h-16 lg:w-16 object-cover">
                                    <div>
                                        <div class="flex gap-2 mt-1">
                                            <p class="">เลขที่ : </p>
                                            <p class="font-semibold">78945623</p>
                                        </div>

                                        <div class="flex gap-2 mt-1">
                                            <p class="">สถานะ : </p>
                                            <p class="font-semibold">กำลังจัดส่ง</p>
                                        </div>
                                    </div>
                                </div>

                                <div class="lg:flex lg:justify-end gap-4">
                                    <div class="flex gap-2">
                                        <p>จำนวนสินค้า : </p>
                                        <p class="">4 ชิ้น</p>
                                    </div>
                                    <div class="flex gap-2 text-orange-500">
                                        <p>ราคารวม : </p>
                                        <p class="font-semibold">121.00 บาท</p>
                                    </div>

                                </div>
                            </div>
                        </RouterLink>

                        <div class="w-full h-auto bg-gray-50 rounded-md p-4 shadow-md text-md cursor-pointer mb-4">

                            <div class="flex items-center justify-center gap-4 border p-2 lg:p-4 rounded-md mt-3 mb-3">
                                <img src="../../assets/image/system/shopping-basket.png" alt=""
                                    class="h-10 w-10 lg:h-14 lg:w-14 object-cover">
                                <p class="font-semibold text-md lg:text-2xl">ไม่มีรายการสั่งซื้อ</p>
                            </div>

                        </div>

                    </div>
                </div>


            </div>

        </div>
    </div>
</template>