<script setup>
import backend_navbar from '@/components/backend/navbar.vue';
</script>

<template class="">

    <backend_navbar @showFormTable="showFormTable" />

    <div class="p-4 lg:pr-24 lg:pl-24 pt-6 sm:ml-64">
        <div class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-14">


            <div class="mt-2 mb-2">
                <div class=" lg:p-4 w-full rounded-md text-gray-600">

                    <div v-if="formTable">

                        <!-- title  -->
                        <div class="flex justify-between items-center mb-2">
                            <p class="text-3xl font-semibold">จัดการออร์เดอร์</p>
                        </div>

                        <!-- sort -->
                        <div class="lg:flex lg:justify-between mb-4 mt-4 items-center">

                            <!-- ช่องค้นหา -->
                            <div class="bg-white lg:justify-start">
                                <div class="relative mt-1">
                                    <div
                                        class="absolute inset-y-0 rtl:inset-r-0 start-0 flex items-center ps-3 pointer-events-none">
                                        <svg class="w-4 h-4 text-gray-500" aria-hidden="true"
                                            xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                                stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
                                        </svg>
                                    </div>
                                    <input type="text"
                                        class="block ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-full lg:w-80 bg-white focus:border-gray-300 h-full py-2.5"
                                        placeholder="ค้นหา">
                                </div>
                            </div>

                            <div class="flex gap-2 justify-center pt-4 lg:pt-0">
                                <!-- เลือกสถานะ-->
                                <div class="relative">
                                    <!-- ปุ่มเลือกสถานะ-->
                                    <button
                                        class="border border-gray-300 bg-gray-50 font-medium rounded-lg text-sm px-16 py-2.5 text-center inline-flex items-center"
                                        type="button" @click="dropdownStatus">
                                        <span class="mr-2">
                                            <span>ทั้งหมด</span>

                                        </span>
                                        <i class="fa-solid fa-angle-down"></i>
                                    </button>
                                    <!-- เมนูสถานะ -->
                                    <div v-show="DropdownStatusOpen" ref="statusMenu"
                                        class="z-50 absolute right-0 mt-2 text-base list-none w-full bg-white divide-y divide-gray-100 rounded-lg shadow border border-gray-300">
                                        <ul class="py-2">
                                            <li>
                                                <a href="#" @click="DropdownStatus('')"
                                                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">ทั้งหมด</a>
                                            </li>
                                            <li>
                                                <a href="#" @click="DropdownStatus(0)"
                                                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">รายการใหม่</a>
                                            </li>
                                            <li>
                                                <a href="#" @click="DropdownStatus(1)"
                                                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">เตรียมสินค้า</a>
                                            </li>
                                            <li>
                                                <a href="#" @click="DropdownStatus(2)"
                                                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">กำลังจัดส่ง</a>
                                            </li>
                                            <li>
                                                <a href="#" @click="DropdownStatus(3)"
                                                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">ส่งสำเร็จ</a>
                                            </li>
                                        </ul>
                                    </div>

                                </div>
                                <!-- เลือกขนาดเเถวในตาราง -->
                                <div class="relative">
                                    <!-- ปุ่มเลือกขนาดเเถวในตาราง -->
                                    <button
                                        class="border border-gray-300 bg-gray-50 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center"
                                        type="button" @click="togglePageSize">
                                        <span class="mr-2">10</span><i class="fa-solid fa-angle-down"></i>
                                    </button>
                                    <!-- เมนูขนาดเเถวในตาราง -->
                                    <div v-show="pageSizeOpen" ref="pageSizeMenu"
                                        class="z-50 absolute right-0 mt-2 text-base list-none w-full bg-white divide-y divide-gray-100 rounded-lg shadow border border-gray-300">
                                        <ul class="py-2">
                                            <li>
                                                <a href="#" @click="DropdownPageSize(10)"
                                                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">10</a>
                                            </li>
                                            <li>
                                                <a href="#" @click="DropdownPageSize(20)"
                                                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">20</a>
                                            </li>
                                            <li>
                                                <a href="#" @click="DropdownPageSize(50)"
                                                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">50</a>
                                            </li>
                                            <li>
                                                <a href="#" @click="DropdownPageSize(100)"
                                                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">100</a>
                                            </li>
                                        </ul>
                                    </div>

                                </div>
                            </div>
                        </div>

                        <!-- ตาราง -->
                        <div class="relative overflow-x-auto rounded-lg border border-gray-200">
                            <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                <thead
                                    class="text-sm text-gray-100 uppercase bg-gray-800 dark:bg-gray-700 dark:text-gray-400">
                                    <tr>
                                        <th scope="col" class="px-6 py-4 whitespace-nowrap">
                                            วันที่ / เวลา
                                        </th>
                                        <th scope="col" class="px-6 py-4 whitespace-nowrap">
                                            เลขที่
                                        </th>
                                        <th scope="col" class="px-6 py-4 whitespace-nowrap">
                                            สถานที่
                                        </th>
                                        <th scope="col" class="px-6 py-4 whitespace-nowrap">
                                            สถานะ
                                        </th>
                                        <th scope="col" class="px-6 py-4 whitespace-nowrap">
                                            จำนวน / ยอดรวม
                                        </th>

                                    </tr>
                                </thead>
                                <tbody>
                                    <tr @click="showFormEdit"
                                        class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 cursor-pointer hover:bg-gray-100 transition">
                                        <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap dark:text-white">
                                            <span class="font-semibold">วันที่</span> 2024/12/06
                                            <span class="font-semibold">เวลา</span> 9:31
                                        </th>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            78945623
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            มหาชัย
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            <span class="font-semibold mr-2 text-pink-500">รายการใหม่</span>
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            <span class="font-semibold mr-2">4ชิ้น</span>
                                            <span class="font-semibold text-orange-500">รวม 600 บาท</span>
                                        </td>

                                    </tr>
                                    <tr @click="showFormEdit"
                                        class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 cursor-pointer hover:bg-gray-100 transition">
                                        <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap dark:text-white">
                                            <span class="font-semibold">วันที่</span> 2024/12/06
                                            <span class="font-semibold">เวลา</span> 9:31
                                        </th>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            78945623
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            มหาชัย
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            <span class="font-semibold mr-2 text-amber-500">เตรียมสินค้า</span>
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            <span class="font-semibold mr-2">4ชิ้น</span>
                                            <span class="font-semibold text-orange-500">รวม 600 บาท</span>
                                        </td>

                                    </tr>
                                    <tr @click="showFormEdit"
                                        class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 cursor-pointer hover:bg-gray-100 transition">
                                        <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap dark:text-white">
                                            <span class="font-semibold">วันที่</span> 2024/12/06
                                            <span class="font-semibold">เวลา</span> 9:31
                                        </th>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            78945623
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            มหาชัย
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            <span class="font-semibold mr-2 text-blue-500">กำลังจัดส่ง</span>
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            <span class="font-semibold mr-2">4ชิ้น</span>
                                            <span class="font-semibold text-orange-500">รวม 600 บาท</span>
                                        </td>

                                    </tr>
                                    <tr @click="showFormEdit"
                                        class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 cursor-pointer hover:bg-gray-100 transition">
                                        <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap dark:text-white">
                                            <span class="font-semibold">วันที่</span> 2024/12/06
                                            <span class="font-semibold">เวลา</span> 9:31
                                        </th>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            78945623
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            มหาชัย
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            <span class="font-semibold mr-2 text-green-500">ส่งสำเร็จ</span>
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            <span class="font-semibold mr-2">4ชิ้น</span>
                                            <span class="font-semibold text-orange-500">รวม 600 บาท</span>
                                        </td>

                                    </tr>
                                    <tr @click="showFormEdit"
                                        class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 cursor-pointer hover:bg-gray-100 transition">
                                        <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap dark:text-white">
                                            <span class="font-semibold">วันที่</span> 2024/12/06
                                            <span class="font-semibold">เวลา</span> 9:31
                                        </th>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            78945623
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            มหาชัย
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            <span class="font-semibold mr-2 text-green-500">ส่งสำเร็จ</span>
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            <span class="font-semibold mr-2">4ชิ้น</span>
                                            <span class="font-semibold text-orange-500">รวม 600 บาท</span>
                                        </td>

                                    </tr>
                                    <tr @click="showFormEdit"
                                        class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 cursor-pointer hover:bg-gray-100 transition">
                                        <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap dark:text-white">
                                            <span class="font-semibold">วันที่</span> 2024/12/06
                                            <span class="font-semibold">เวลา</span> 9:31
                                        </th>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            78945623
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            มหาชัย
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            <span class="font-semibold mr-2 text-green-500">ส่งสำเร็จ</span>
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            <span class="font-semibold mr-2">4ชิ้น</span>
                                            <span class="font-semibold text-orange-500">รวม 600 บาท</span>
                                        </td>

                                    </tr>

                                </tbody>
                            </table>
                        </div>

                    </div>

                    <div v-if="formEdit">

                        <!-- title -->
                        <div class="flex justify-between items-center mb-2">
                            <p class="text-3xl font-semibold">ข้อมูลออเดอร์</p>
                        </div>

                        <div class="md:flex w-full gap-2 mb-2 pt-1 mt-4">

                            <div class="flex gap-2 w-full">
                                <div class="lg:w-1/2 w-full">
                                    <input type="text" v-model="codeOrder" ref="inputCodeOrder" :class="{
                                        'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                        'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !codeOrder
                                    }" placeholder="รหัสคำสั่งซื้อ" disabled />
                                </div>

                                <div class="lg:w-1/2 w-full">
                                    <input type="text" v-model="dayTimeOrder" ref="inputDayTimeOrder" :class="{
                                        'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                        'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !dayTimeOrder
                                    }" placeholder="วันที่ เวลา" disabled />
                                </div>

                                <div class="lg:w-1/2 w-full">
                                    <input type="text" v-model="statusOrder" ref="inputStatusOrder" :class="{
                                        'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                        'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !statusOrder
                                    }" placeholder="สถานะ" disabled />
                                </div>
                            </div>

                        </div>

                        <div class="flex justify-between items-center mb-2 mt-8">
                            <p class="text-xl font-semibold">ข้อมูลลูกค้า</p>
                        </div>

                        <div class="sm:block lg:flex w-full gap-2 mb-2 pt-1 mt-4">

                            <div class="flex gap-2 w-full">
                                <div class="lg:w-1/2 w-full">
                                    <input type="text" v-model="nameMemberOrder" ref="inputNameMemberOrder" :class="{
                                        'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                        'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !nameMemberOrder
                                    }" placeholder="ชื่อผู้รับ" disabled />
                                </div>

                                <div class="lg:w-1/2 w-full">
                                    <input type="text" v-model="phoneMemberOrder" ref="inputPhoneMemberOrder" :class="{
                                        'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                        'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !phoneMemberOrder
                                    }" placeholder="เบอร์โทร" disabled />
                                </div>

                            </div>

                        </div>
                        <div class="w-full mb-4 pt-1 mt-4">
                            <textarea type="text" v-model="addressOrder" ref="inputAddressOrder" rows="4" :class="{
                                'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !addressOrder
                            }" placeholder="ที่อยู่การจัดส่ง" disabled />
                        </div>

                        <div class="mb-4 mt-8">
                            <p class="text-xl font-semibold">รายการสินค้า</p>
                        </div>

                        <!-- ตาราง -->
                        <div class="relative overflow-x-auto rounded-lg border border-gray-200">
                            <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                <thead
                                    class="text-sm text-gray-100 uppercase bg-gray-800 dark:bg-gray-700 dark:text-gray-400">
                                    <tr>
                                        <th scope="col" class="px-6 py-4 whitespace-nowrap">
                                            รูป
                                        </th>
                                        <th scope="col" class="px-6 py-4 whitespace-nowrap">
                                            รหัส
                                        </th>
                                        <th scope="col" class="px-6 py-4 whitespace-nowrap">
                                            ชื่อ
                                        </th>
                                        <th scope="col" class="px-6 py-4 whitespace-nowrap">
                                            จำนวน
                                        </th>
                                        <th scope="col" class="px-6 py-4 whitespace-nowrap">
                                            ราคา
                                        </th>
                                    </tr>
                                </thead>

                                <tbody>
                                    <tr
                                        class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 cursor-pointer hover:bg-gray-100 transition">
                                        <th scope="row" class="px-6 py-4">
                                            <div class="w-24 h-14 lg:w-36 lg:h-24">
                                                <img class="w-full h-full rounded-md object-cover ring-4 ring-gray-300 shadow-md"
                                                    src="../../assets/image/product/food1.jpg">
                                            </div>
                                        </th>

                                        <td class="px-6 py-4 whitespace-nowrap font-semibold">
                                            78945623
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            สินค้าทดสอบ 01
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            1
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            150 บาท
                                        </td>
                                    </tr>
                                    <tr
                                        class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 cursor-pointer hover:bg-gray-100 transition">
                                        <th scope="row" class="px-6 py-4">
                                            <div class="w-24 h-14 lg:w-36 lg:h-24">
                                                <img class="w-full h-full rounded-md object-cover ring-4 ring-gray-300 shadow-md"
                                                    src="../../assets/image/product/food2.jpg">
                                            </div>
                                        </th>

                                        <td class="px-6 py-4 whitespace-nowrap font-semibold">
                                            78945623
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            สินค้าทดสอบ 02
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            1
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            150 บาท
                                        </td>
                                    </tr>
                                    <tr
                                        class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 cursor-pointer hover:bg-gray-100 transition">
                                        <th scope="row" class="px-6 py-4">
                                            <div class="w-24 h-14 lg:w-36 lg:h-24">
                                                <img class="w-full h-full rounded-md object-cover ring-4 ring-gray-300 shadow-md"
                                                    src="../../assets/image/product/food3.jpg">
                                            </div>
                                        </th>
                                        <td class="px-6 py-4 whitespace-nowrap font-semibold">
                                            78945623
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            สินค้าทดสอบ 03
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            1
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            150 บาท
                                        </td>
                                    </tr>
                                    <tr
                                        class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 cursor-pointer hover:bg-gray-100 transition">
                                        <th scope="row" class="px-6 py-4">
                                            <div class="w-24 h-14 lg:w-36 lg:h-24">
                                                <img class="w-full h-full rounded-md object-cover ring-4 ring-gray-300 shadow-md"
                                                    src="../../assets/image/product/food4.jpg">
                                            </div>
                                        </th>

                                        <td class="px-6 py-4 whitespace-nowrap font-semibold">
                                            78945623
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            สินค้าทดสอบ 04
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            1
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            150 บาท
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

                        <div class="flex gap-2 justify-end mb-4 mt-6 text-2xl font-semibold">
                            <span class="">ยอดรวม :</span>
                            <span class="text-orange-500">600บาท</span>
                        </div>

                        <hr class="my-2 text-gray-600">

                        <div class="w-full mb-4 pt-1 mt-4">
                            <textarea type="text" v-model="infoOrder" ref="inputInfoOrder" rows="4" :class="{
                                'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !infoOrder
                            }" placeholder="หมายเหตุ" />
                        </div>

                        <div class="flex gap-2 justify-center mt-4 md:mt-4 ">
                            <button
                                class="text-white bg-blue-500 border border-blue-500 font-medium rounded-lg text-sm px-3 py-2.5 text-center inline-flex items-center h-full">
                                เตรียมสินค้า
                            </button>
                            <button @click="showFormTable"
                                class="text-black bg-gray-200 border border-gray-400 font-medium rounded-lg text-sm px-3 py-2.5 text-center inline-flex items-center h-full">
                                ยกเลิก
                            </button>
                            <button
                                class="text-white bg-red-500 border border-red-500 font-medium rounded-lg text-sm px-3 py-2.5 text-center inline-flex items-center h-full">
                                ยกเลิกคำสั่งซื้อ
                            </button>
                        </div>
                    </div>
                </div>
            </div>


        </div>
    </div>

</template>

<script>
export default {
    data() {
        return {

            codeOrder: '',
            dayTimeOrder: '',
            statusOrder: '',
            nameMemberOrder: '',
            phoneMemberOrder: '',
            addressOrder: '',
            infoOrder: '',

            formTable: true,
            formEdit: false,

            DropdownStatusOpen: false,
            pageSizeOpen: false,
        };
    },
    mounted() {
        document.addEventListener('click', this.closeDropdownStatus);
        document.addEventListener('click', this.closeDropdown);

    },

    methods: {

        showFormTable() {
            this.formTable = true;
            this.formEdit = false;
        },
        showFormEdit() {
            this.formTable = false;
            this.formEdit = true;
        },

        DropdownStatus(statusName) {
            this.pageSizeOpen = false;

        },
        dropdownStatus(event) {
            // ป้องกันการคลิกบนปุ่มที่ทำให้ event ไปถึง listener ของ document
            event.stopPropagation();
            this.DropdownStatusOpen = !this.DropdownStatusOpen;
        },
        closeDropdownStatus(event) {
            // ตรวจสอบว่าคลิกภายนอกปุ่มและ dropdown หรือไม่
            const dropdown = this.$refs.statusMenu;
            if (dropdown && !dropdown.contains(event.target)) {
                this.DropdownStatusOpen = false;
            }
        },


        DropdownPageSize(size) {
            this.pageSizeOpen = false;
        },
        togglePageSize(event) {
            // ป้องกันการคลิกบนปุ่มที่ทำให้ event ไปถึง listener ของ document
            event.stopPropagation();
            this.pageSizeOpen = !this.pageSizeOpen;
        },
        closeDropdown(event) {
            // ตรวจสอบว่าคลิกภายนอกปุ่มและ dropdown หรือไม่
            const dropdown = this.$refs.pageSizeMenu;
            if (dropdown && !dropdown.contains(event.target)) {
                this.pageSizeOpen = false;
            }
        },

    },
};
</script>