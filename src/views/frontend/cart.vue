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
                        <p class="mb-6 text-3xl font-semibold pt-4 pr-8 pl-8">ตระกร้า</p>

                        <div class="lg:flex lg:gap-8 w-full">

                            <div
                                class="lg:w-3/4 w-full z-40 pr-8 pl-8 pt-2 lg:h-auto h-[calc(100vh-480px)] overflow-y-auto no-scrollbar">

                                <!-- product -->
                                <div
                                    class="relative w-full h-auto bg-gray-50 rounded-md shadow-md text-md cursor-pointer mb-4">
                                    <div class="flex gap-4 lg:gap-6 p-2 lg:p-4 rounded-md">
                                        <img src="../../assets/image/product/food3.jpg" alt=""
                                            class="h-28 w-28 lg:h-32 lg:w-48 object-cover rounded-md">
                                        <div class="flex flex-col w-full">
                                            <div class="flex justify-between items-center mb-1 lg:mb-2">
                                                <p class="text-mb ">ข้าวมันไก่ทอด</p>
                                                <button
                                                    class="absolute -right-2 -top-2 bg-red-500 text-white w-10 h-10 rounded-full justify-center text-md">
                                                    <i class="fa-solid fa-trash-can"></i>
                                                </button>
                                            </div>
                                            <p class="font-semibold text-mb  text-orange-500 mb-2 lg:mb-3">150 บาท
                                            </p>
                                            <div class="flex items-center bottom-0">
                                                <!-- ปุ่มลดจำนวน -->
                                                <button
                                                    class="bg-gray-300 text-gray-600 hover:bg-gray-200 p-2 pr-3 pl-3 focus:outline-none transition rounded-l-md">
                                                    -
                                                </button>

                                                <!-- ช่องกรอกจำนวนสินค้า -->
                                                <input type="text"
                                                    class="w-14 text-center border-none focus:outline-none p-2 pr-3 pl-3"
                                                    value="1" />

                                                <!-- ปุ่มเพิ่มจำนวน -->
                                                <button
                                                    class="bg-gray-300 text-gray-600 hover:bg-gray-200 p-2 pr-3 pl-3 focus:outline-none transition rounded-r-md">
                                                    +
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <div
                                    class="relative w-full h-auto bg-gray-50 rounded-md shadow-md text-md cursor-pointer mb-4">
                                    <div class="flex gap-4 lg:gap-6 p-2 lg:p-4 rounded-md">
                                        <img src="../../assets/image/product/food3.jpg" alt=""
                                            class="h-28 w-28 lg:h-32 lg:w-48 object-cover rounded-md">
                                        <div class="flex flex-col w-full">
                                            <div class="flex justify-between items-center mb-1 lg:mb-2">
                                                <p class="text-mb ">ข้าวมันไก่ทอด</p>
                                                <button
                                                    class="absolute -right-2 -top-2 bg-red-500 text-white w-10 h-10 rounded-full justify-center text-md">
                                                    <i class="fa-solid fa-trash-can"></i>
                                                </button>
                                            </div>
                                            <p class="font-semibold text-mb  text-orange-500 mb-2 lg:mb-3">150 บาท
                                            </p>
                                            <div class="flex items-center bottom-0">
                                                <!-- ปุ่มลดจำนวน -->
                                                <button
                                                    class="bg-gray-300 text-gray-600 hover:bg-gray-200 p-2 pr-3 pl-3 focus:outline-none transition rounded-l-md">
                                                    -
                                                </button>

                                                <!-- ช่องกรอกจำนวนสินค้า -->
                                                <input type="text"
                                                    class="w-14 text-center border-none focus:outline-none p-2 pr-3 pl-3"
                                                    value="1" />

                                                <!-- ปุ่มเพิ่มจำนวน -->
                                                <button
                                                    class="bg-gray-300 text-gray-600 hover:bg-gray-200 p-2 pr-3 pl-3 focus:outline-none transition rounded-r-md">
                                                    +
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <div
                                    class="relative w-full h-auto bg-gray-50 rounded-md shadow-md text-md cursor-pointer mb-4">
                                    <div class="flex gap-4 lg:gap-6 p-2 lg:p-4 rounded-md">
                                        <img src="../../assets/image/product/food3.jpg" alt=""
                                            class="h-28 w-28 lg:h-32 lg:w-48 object-cover rounded-md">
                                        <div class="flex flex-col w-full">
                                            <div class="flex justify-between items-center mb-1 lg:mb-2">
                                                <p class="text-mb ">ข้าวมันไก่ทอด</p>
                                                <button
                                                    class="absolute -right-2 -top-2 bg-red-500 text-white w-10 h-10 rounded-full justify-center text-md">
                                                    <i class="fa-solid fa-trash-can"></i>
                                                </button>
                                            </div>
                                            <p class="font-semibold text-mb  text-orange-500 mb-2 lg:mb-3">150 บาท
                                            </p>
                                            <div class="flex items-center bottom-0">
                                                <!-- ปุ่มลดจำนวน -->
                                                <button
                                                    class="bg-gray-300 text-gray-600 hover:bg-gray-200 p-2 pr-3 pl-3 focus:outline-none transition rounded-l-md">
                                                    -
                                                </button>

                                                <!-- ช่องกรอกจำนวนสินค้า -->
                                                <input type="text"
                                                    class="w-14 text-center border-none focus:outline-none p-2 pr-3 pl-3"
                                                    value="1" />

                                                <!-- ปุ่มเพิ่มจำนวน -->
                                                <button
                                                    class="bg-gray-300 text-gray-600 hover:bg-gray-200 p-2 pr-3 pl-3 focus:outline-none transition rounded-r-md">
                                                    +
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <div
                                    class="relative w-full h-auto bg-gray-50 rounded-md shadow-md text-md cursor-pointer mb-4">
                                    <div class="flex gap-4 lg:gap-6 p-2 lg:p-4 rounded-md">
                                        <img src="../../assets/image/product/food3.jpg" alt=""
                                            class="h-28 w-28 lg:h-32 lg:w-48 object-cover rounded-md">
                                        <div class="flex flex-col w-full">
                                            <div class="flex justify-between items-center mb-1 lg:mb-2">
                                                <p class="text-mb ">ข้าวมันไก่ทอด</p>
                                                <button
                                                    class="absolute -right-2 -top-2 bg-red-500 text-white w-10 h-10 rounded-full justify-center text-md">
                                                    <i class="fa-solid fa-trash-can"></i>
                                                </button>
                                            </div>
                                            <p class="font-semibold text-mb  text-orange-500 mb-2 lg:mb-3">150 บาท
                                            </p>
                                            <div class="flex items-center bottom-0">
                                                <!-- ปุ่มลดจำนวน -->
                                                <button
                                                    class="bg-gray-300 text-gray-600 hover:bg-gray-200 p-2 pr-3 pl-3 focus:outline-none transition rounded-l-md">
                                                    -
                                                </button>

                                                <!-- ช่องกรอกจำนวนสินค้า -->
                                                <input type="text"
                                                    class="w-14 text-center border-none focus:outline-none p-2 pr-3 pl-3"
                                                    value="1" />

                                                <!-- ปุ่มเพิ่มจำนวน -->
                                                <button
                                                    class="bg-gray-300 text-gray-600 hover:bg-gray-200 p-2 pr-3 pl-3 focus:outline-none transition rounded-r-md">
                                                    +
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                            </div>

                            <!--สรุปคำสั่งซื้อ-->
                            <div
                                class="w-full lg:w-1/4 bg-gray-100 rounded-md lg:rounded-t-md shadow-md p-8 text-md cursor-pointer h-60 z-50">
                                <p class="text-xl font-semibold text-gray-600">รวมทั้งหมด</p>

                                <hr class="my-2 text-gray-600">

                                <p class="text-mb text-gray-600 mt-4">จำนวน<span class="mr-2 ml-2">4</span>รายการ</p>

                                <div class="flex justify-between text-mb font-semibold text-orange-500">
                                    <p class="mb-8">ราคารวม</p>
                                    <div class="flex">
                                        <span class="">600</span>
                                        <span class="ml-2">บาท</span>
                                    </div>
                                </div>

                                <RouterLink to="/confirm-order">
                                    <button
                                        class="bg-gray-800 text-white p-2 w-full rounded-md">ยืนยันรายการสินค้า</button>
                                </RouterLink>

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