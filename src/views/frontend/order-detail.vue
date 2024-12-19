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
                        <p class="mb-6 text-3xl font-semibold">รายละเอียดคำสั่งซื้อ</p>

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
                                    <div class="flex gap-2 mt-1 ">
                                        <p class="">เลขที่ : </p>
                                        <p class="font-semibold">78945623</p>
                                    </div>

                                    <div class="flex gap-2 mt-1">
                                        <p class="">สถานะ : </p>
                                        <p class="font-semibold">กำลังจัดส่ง</p>
                                    </div>
                                </div>
                            </div>

                        </div>

                        <!--ข้อมูลลูกค้า-->
                        <div class="mb-8">

                            <div class="p-4 text-md text-gray-600 rounded-lg bg-gray-50 shadow-md">
                                <div class="mb-5">
                                    <label class="block text-md font-medium text-gray-900 mb-3">ชื่อผู้รับสินค้า</label>
                                    <input type="text"
                                        class="bg-gray-50 border border-gray-300 text-orange-500 text-md rounded-lg focus:border-gray-300 block w-full p-2"
                                        value="เจษฎากร หวานสนิท" disabled />
                                </div>
                                <div class="mb-5">
                                    <label class="block text-md font-medium text-gray-900 mb-2">เบอร์โทร</label>
                                    <input type="text"
                                        class="bg-gray-50 border border-gray-300 text-orange-500 text-md rounded-lg focus:border-gray-300 block w-full p-2"
                                        value="0xx xxx xxxx" disabled />
                                </div>
                                <div class="mb-5">

                                    <span class="text-gray-700">ที่อยู่ในการจัดส่ง</span>
                                    <label class="flex items-center space-x-2 mt-4">
                                        <input checked type="radio" name="deliveryOption" value="0"
                                            class="h-4 w-4 text-gray-600 border-gray-300 focus:ring-gray-500 cursor-pointer">
                                        <span class="text-gray-700">รับที่ Asia Mart</span>
                                    </label>
                                </div>

                            </div>
                        </div>

                        <div class="mb-8">
                            <p class="mb-2 text-xl font-semibold">รายการสินค้า</p>
                            <div class="bg-gray-50 shadow-md p-4 rounded-md grid grid-rows-auto gap-4">

                                <!-- สินค้า -->
                                <div class="w-full h-auto rounded-md text-md cursor-pointer border bg-gray-50">
                                    <div class="flex gap-4 lg:gap-6 p-2 lg:p-4 rounded-md">
                                        <img src="../../assets/image/product/food3.jpg" alt=""
                                            class="h-20 w-48 object-cover rounded-md">
                                        <div class="w-full">
                                            <div class="flex justify-between">
                                                <p class="text-mb mb-1 lg:mb-2">ข้าวมันไก่ทอด</p>
                                                <p class="font-semibold text-mb text-orange-500 mb-2 lg:mb-3">
                                                    150 บาท
                                                </p>
                                            </div>
                                            <div class="flex justify-end">
                                                <p class="text-mb mb-2 lg:mb-3">จำนวน X1</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <div class="w-full h-auto rounded-md text-md cursor-pointer border bg-gray-50">
                                    <div class="flex gap-4 lg:gap-6 p-2 lg:p-4 rounded-md">
                                        <img src="../../assets/image/product/food3.jpg" alt=""
                                            class="h-20 w-48 object-cover rounded-md">
                                        <div class="w-full">
                                            <div class="flex justify-between">
                                                <p class="text-mb mb-1 lg:mb-2">ข้าวมันไก่ทอด</p>
                                                <p class="font-semibold text-mb text-orange-500 mb-2 lg:mb-3">
                                                    150 บาท
                                                </p>
                                            </div>
                                            <div class="flex justify-end">
                                                <p class="text-mb mb-2 lg:mb-3">จำนวน X1</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <div class="w-full h-auto rounded-md text-md cursor-pointer border bg-gray-50">
                                    <div class="flex gap-4 lg:gap-6 p-2 lg:p-4 rounded-md">
                                        <img src="../../assets/image/product/food3.jpg" alt=""
                                            class="h-20 w-48 object-cover rounded-md">
                                        <div class="w-full">
                                            <div class="flex justify-between">
                                                <p class="text-mb mb-1 lg:mb-2">ข้าวมันไก่ทอด</p>
                                                <p class="font-semibold text-mb text-orange-500 mb-2 lg:mb-3">
                                                    150 บาท
                                                </p>
                                            </div>
                                            <div class="flex justify-end">
                                                <p class="text-mb mb-2 lg:mb-3">จำนวน X1</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <div class="w-full h-auto rounded-md text-md cursor-pointer border bg-gray-50">
                                    <div class="flex gap-4 lg:gap-6 p-2 lg:p-4 rounded-md">
                                        <img src="../../assets/image/product/food3.jpg" alt=""
                                            class="h-20 w-48 object-cover rounded-md">
                                        <div class="w-full">
                                            <div class="flex justify-between">
                                                <p class="text-mb mb-1 lg:mb-2">ข้าวมันไก่ทอด</p>
                                                <p class="font-semibold text-mb text-orange-500 mb-2 lg:mb-3">
                                                    150 บาท
                                                </p>
                                            </div>
                                            <div class="flex justify-end">
                                                <p class="text-mb mb-2 lg:mb-3">จำนวน X1</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                            </div>


                        </div>

                        <!--สรุปคำสั่งซื้อ-->
                        <p class="mb-2 text-xl font-semibold">สรุปคำสั่งซื้อ</p>
                        <div class="w-full bg-gray-50 rounded-md lg:rounded-t-md shadow-md p-4 text-md cursor-pointer ">


                            <p class="text-mb text-gray-600 mt-2">จำนวน<span class="mr-2 ml-2">4</span>รายการ</p>

                            <div class="flex justify-between text-mb font-semibold text-orange-500 text-2xl">
                                <p class="mb-2">ยอดชำระ</p>
                                <div class="flex ">
                                    <span class="">600</span>
                                    <span class="ml-2">บาท</span>
                                </div>
                            </div>


                        </div>

                    </div>
                </div>
            </div>

        </div>
    </div>
</template>