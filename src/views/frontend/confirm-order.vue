<script setup>
    import frontend_navbar from '../../components/frontend/navbar.vue';
</script>

<template>
    <frontend_navbar />

    <div class="flex justify-center pt-24">
        <div class="w-full max-w-screen-2xl lg:p-12 lg:border border-gray-200 rounded-lg lg:mb-4 bg-white z-40">
            <div>

                <!-- content -->

                <div class="mt-2 mb-2">
                    <div class="w-full rounded-md text-gray-600 ">
                        <p class="mb-6 text-3xl font-semibold pt-4 pr-8 pl-8">ยืนยันรายการสินค้า</p>

                        <div class="lg:flex lg:gap-8 w-full">

                            <div
                                class="lg:w-3/4 w-full z-40 pr-8 pl-8 pt-2 lg:h-auto h-[calc(100vh-480px)] overflow-y-auto no-scrollbar">

                                <!--ข้อมูลลูกค้า-->
                                <div class="mb-8">
                                    <p class="mb-2 text-xl font-semibold">ข้อมูลลูกค้า</p>
                                    <div class="p-4 text-md text-gray-600 rounded-lg bg-gray-50 shadow-md">
                                        <div class="mb-5">
                                            <label
                                                class="block text-md font-medium text-gray-900 mb-3">ชื่อผู้รับสินค้า</label>
                                            <input type="text"
                                                class="bg-gray-50 border border-gray-300 text-orange-500 text-md rounded-lg focus:border-gray-300 block w-full p-2"
                                                value="เจษฎากร หวานสนิท" disabled />
                                        </div>
                                        <div class="mb-5">
                                            <div class="flex justify-between mb-2 items-center">
                                                <label class="block text-md font-medium text-gray-900">เบอร์โทร</label>
                                                <button class="py-1 px-2 bg-white shadow-md rounded-md text-orange-500">
                                                    <i class="fa-regular fa-pen-to-square"></i>
                                                </button>
                                            </div>
                                            <input type="text"
                                                class="bg-gray-50 border border-gray-300 text-orange-500 text-md rounded-lg focus:border-gray-300 block w-full p-2"
                                                value="0xx xxx xxxx" disabled />
                                        </div>
                                    </div>
                                </div>
                                <!--ที่อยู่จัดส่ง-->
                                <div class="mb-8">
                                    <p class="mb-2 text-xl font-semibold">ที่อยู่จัดส่ง</p>
                                    <div class="p-4 text-md text-gray-600 rounded-lg bg-gray-50 shadow-md">
                                        <label class="flex items-center space-x-2">
                                            <input type="radio" name="deliveryOption" value="asiaMart"
                                                class="h-4 w-4 text-gray-600 border-gray-300 focus:ring-gray-500 cursor-pointer">
                                            <span class="text-gray-700">รับที่ Asia Mart</span>
                                        </label>
                                        <div class="flex justify-between pt-4 items-center">
                                            <label class="flex items-center space-x-2">
                                                <input type="radio" name="deliveryOption" value="address"
                                                    class="h-4 w-4 text-gray-600 border-gray-300 focus:ring-gray-500 cursor-pointer">
                                                <span class="text-gray-700">ที่อยู่ในการจัดส่ง</span>
                                            </label>
                                            <button class="py-1 px-2 bg-white shadow-md rounded-md text-orange-500">
                                                <i class="fa-regular fa-pen-to-square"></i>
                                            </button>
                                        </div>
                                        <textarea rows="4"
                                            class="block p-2 w-full text-md text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:border-gray-300 mt-2"
                                            placeholder="ใส่ที่อยู่ในการจัดส่ง"></textarea>
                                    </div>
                                </div>
                                <!--รายการสินค้า-->
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

                            </div>

                            <!--สรุปคำสั่งซื้อ-->
                            <div
                                class="w-full lg:w-1/4 bg-gray-100 rounded-md lg:rounded-t-md shadow-md p-8 text-md cursor-pointer h-60 z-50">
                                <p class="text-xl font-semibold text-gray-600">สรุปคำสั่งซื้อ</p>

                                <hr class="my-2 text-gray-600">

                                <p class="text-mb text-gray-600 mt-4">จำนวน<span class="mr-2 ml-2">4</span>รายการ</p>

                                <div class="flex justify-between text-mb font-semibold text-orange-500">
                                    <p class="mb-8">ราคารวม</p>
                                    <div class="flex">
                                        <span class="">600</span>
                                        <span class="ml-2">บาท</span>
                                    </div>
                                </div>


                                <button class="bg-gray-800 text-white p-2 w-full rounded-md">สั่งซื้อ</button>


                            </div>
                        </div>

                    </div>

                </div>
            </div>

        </div>
    </div>

</template>

<style scoped>
/* ใช้สำหรับซ่อนแถบเลื่อน */
.no-scrollbar::-webkit-scrollbar {
    display: none;
}

.no-scrollbar {
    -ms-overflow-style: none;
    /* Internet Explorer 10+ */
    scrollbar-width: none;
    /* Firefox */
}
</style>