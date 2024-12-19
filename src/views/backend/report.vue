<script setup>
import backend_navbar from '@/components/backend/navbar.vue';
</script>

<template class="">

    <backend_navbar />

    <div class="p-4 pt-6 sm:ml-64">
        <div class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-14">


            <div class="mt-2 mb-2">
                <div class=" lg:p-4 w-full rounded-md text-gray-600">
                    <!-- title -->
                    <p class="mb-6 text-3xl font-semibold">ยอดขาย</p>

                    <!-- content -->

                    <!-- sort -->
                    <div class="lg:flex lg:justify-between items-center mb-6">

                        <!-- ช่องค้นหา -->
                        <div class="bg-white flex justify-center lg:justify-start">
                            <label for="table-search" class="sr-only">Search</label>
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
                                    class="block ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-60 lg:w-80 bg-gray-50 focus:border-gray-300 h-full py-2.5"
                                    placeholder="ค้นหา">
                            </div>
                        </div>

                        <div class="flex gap-2 justify-center pt-4">
                            <!-- เลือกสถานะ-->
                            <!-- <div class="relative">

                                <button
                                    class="border border-gray-300 bg-gray-50 font-medium rounded-lg text-sm px-16 py-2.5 text-center inline-flex items-center h-full"
                                    type="button" @click="dropdownStatus">
                                    <span class="mr-2">
                                        <span>ทั้งหมด</span>

                                    </span>
                                    <i class="fa-solid fa-angle-down"></i>
                                </button>

                                <div v-show="DropdownStatusOpen" ref="statusMenu"
                                    class="z-50 absolute right-0 mt-2 text-base list-none w-full bg-white divide-y divide-gray-100 rounded-lg shadow border border-gray-300">
                                    <ul class="py-2">
                                        <li>
                                            <a href="#" @click="DropdownStatus('')"
                                                class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">ทั้งหมด</a>
                                        </li>
                                        <li>
                                            <a href="#" @click="DropdownStatus(0)"
                                                class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">ขายดีสุด</a>
                                        </li>
                                        <li>
                                            <a href="#" @click="DropdownStatus(1)"
                                                class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">กำไรมากสุด</a>
                                        </li>
                                        <li>
                                            <a href="#" @click="DropdownStatus(1)"
                                                class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">เเพงสุด</a>
                                        </li>

                                    </ul>
                                </div>

                            </div> -->
                            
                            <!-- เลือกขนาดเเถวในตาราง -->
                            <div class="relative">
                                <!-- ปุ่มเลือกขนาดเเถวในตาราง -->
                                <button
                                    class="border border-gray-300 bg-gray-50 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center h-full"
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
                                        รูป
                                    </th>
                                    <th scope="col" class="px-6 py-4 whitespace-nowrap">
                                        รหัส
                                    </th>
                                    <th scope="col" class="px-6 py-4 whitespace-nowrap">
                                        ชื่อ
                                    </th>
                                    <th scope="col" class="px-6 py-4 whitespace-nowrap">
                                        ราคาทุน
                                    </th>
                                    <th scope="col" class="px-6 py-4 whitespace-nowrap">
                                        ราคาขาย
                                    </th>
                                    <th scope="col" class="px-6 py-4 whitespace-nowrap">
                                        จำนวนที่ขายได้
                                    </th>
                                    <th scope="col" class="px-6 py-4 whitespace-nowrap">
                                        กำไร
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
                                        145
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        150
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        1
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap font-semibold text-green-500">
                                        5
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
                                        145
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        150
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        1
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap font-semibold text-green-500">
                                        5
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
                                        145
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        150
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        1
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap font-semibold text-green-500">
                                        5
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
                                        145
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        150
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        1
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap font-semibold text-green-500">
                                        5
                                    </td>
                                </tr>
                                <tr
                                    class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 cursor-pointer hover:bg-gray-100 transition">
                                    <th scope="row" class="px-6 py-4">
                                        <div class="w-24 h-14 lg:w-36 lg:h-24">
                                            <img class="w-full h-full rounded-md object-cover ring-4 ring-gray-300 shadow-md"
                                                src="../../assets/image/product/food5.jpg">
                                        </div>
                                    </th>
                                    <td class="px-6 py-4 whitespace-nowrap font-semibold">
                                        78945623
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        สินค้าทดสอบ 05
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        145
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        150
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        1
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap font-semibold text-green-500">
                                        5
                                    </td>
                                </tr>

                            </tbody>
                        </table>
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
            DropdownStatusOpen: false,
            pageSizeOpen: false,
        };
    },
    mounted() {
        document.addEventListener('click', this.closeDropdownStatus);
        document.addEventListener('click', this.closeDropdown);

    },

    methods: {

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