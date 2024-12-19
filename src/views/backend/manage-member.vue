<script setup>
import backend_navbar from '@/components/backend/navbar.vue';
import Modal from '@/components/backend/modal.vue';
</script>

<template class="">

    <backend_navbar @showFormTable="showFormTable" />
    <Modal ref="modal" @showFormTable="showFormTable" />

    <div class="p-4 lg:pr-64 lg:pl-64 pt-6 sm:ml-64">
        <div class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-14">


            <div class="mt-2 mb-2">
                <div class=" lg:p-4 w-full rounded-md text-gray-600">

                    <div v-if="formTable">
                        <!-- title -->
                        <div class="flex justify-between items-center mb-2">
                            <p class="text-3xl font-semibold">รายการลูกค้า</p>
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
                                        class="border border-gray-300 bg-gray-50 font-medium rounded-lg text-sm px-16 py-2.5 text-center inline-flex items-center h-full"
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
                                                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">เเสดง</a>
                                            </li>
                                            <li>
                                                <a href="#" @click="DropdownStatus(1)"
                                                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">ไม่เเสดง</a>
                                            </li>
                                        </ul>
                                    </div>

                                </div>
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
                                            เบอร์
                                        </th>
                                        <th scope="col" class="px-6 py-4 whitespace-nowrap">
                                            สถานะ
                                        </th>

                                    </tr>
                                </thead>
                                <tbody>
                                    <tr @click="showFormEdit"
                                        class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 cursor-pointer hover:bg-gray-100 transition">
                                        <th scope="row" class="px-6 py-4">
                                            <div class="w-20 h-20">
                                                <img class="w-full h-full rounded-full object-cover ring-4 ring-gray-300 shadow-md"
                                                    src="../../assets/image/system/cathothead.jpg">
                                            </div>
                                        </th>

                                        <td class="px-6 py-4 whitespace-nowrap font-semibold">
                                            1670525
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            เจษฎากร หวานสนิท
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            0xx xxx xxxx
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            <span
                                                class="font-semibold text-green-500 p-1 bg-green-100 rounded-md">ใช้งาน</span>
                                        </td>

                                    </tr>
                                    <tr @click="showFormEdit"
                                        class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 cursor-pointer hover:bg-gray-100 transition">
                                        <th scope="row" class="px-6 py-4">
                                            <div class="w-20 h-20">
                                                <img class="w-full h-full rounded-full object-cover ring-4 ring-gray-300 shadow-md"
                                                    src="../../assets/image/system/dogcoloruser.jpg">
                                            </div>
                                        </th>

                                        <td class="px-6 py-4 whitespace-nowrap font-semibold">
                                            1670580
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            สมหมา จนจัด
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            0xx xxx xxxx
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            <span
                                                class="font-semibold text-green-500 p-1 bg-green-100 rounded-md">ใช้งาน</span>
                                        </td>

                                    </tr>
                                    <tr @click="showFormEdit"
                                        class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 cursor-pointer hover:bg-gray-100 transition">
                                        <th scope="row" class="px-6 py-4">
                                            <div class="w-20 h-20">
                                                <img class="w-full h-full rounded-full object-cover ring-4 ring-gray-300 shadow-md"
                                                    src="../../assets/image/system/catuser.jpg">
                                            </div>
                                        </th>

                                        <td class="px-6 py-4 whitespace-nowrap font-semibold">
                                            1670580
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            เเมวเป้า ปลาทูนึ่ง
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            0xx xxx xxxx
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            <span
                                                class="font-semibold text-green-500 p-1 bg-green-100 rounded-md">ใช้งาน</span>
                                        </td>

                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <div v-if="formEdit">
                        <!-- title -->
                        <div class="flex justify-between items-center mb-2">
                            <p class="text-3xl font-semibold">ข้อมูลลูกค้า</p>
                        </div>

                        <div class="flex justify-center w-full">
                            <div class="w-28 h-28 lg:w-44 lg:h-44 mt-4 mb-2 ">
                                <img class="w-full h-full rounded-full object-cover ring-4 ring-gray-300 shadow-md"
                                    src="../../assets/image/system/cathothead.jpg">
                            </div>
                        </div>


                        <div class="md:flex w-full gap-2 mb-2 pt-1 mt-4">

                            <div class="flex gap-2 w-full">
                                <div class="lg:w-1/2 w-full">
                                    <input type="text" v-model="codeMember" ref="inputCodeMember" :class="{
                                        'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                        'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !codeMember
                                    }" placeholder="รหัส" disabled />
                                </div>

                                <div class="lg:w-1/2 w-full">
                                    <input type="text" v-model="nameMember" ref="inputNameMember" :class="{
                                        'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                        'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !nameMember
                                    }" placeholder="ชื่อลูกค้า" disabled />
                                </div>
                            </div>

                            <div class="flex gap-2 w-full pt-1 mt-4 lg:pt-0 lg:mt-0">
                                <div class="lg:w-1/2 w-full">
                                    <input type="text" v-model="phoneMember" ref="inputPhoneMember" :class="{
                                        'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                        'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !phoneMember
                                    }" placeholder="เบอร์" disabled />
                                </div>

                                <div class="lg:w-1/2 w-full">
                                    <select v-model="statusMember" ref="inputStatusMember" :class="{
                                        'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-200 h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                        'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !statusMember
                                    }" disabled>
                                        <option value="" disabled selected>สถานะ</option>
                                        <option value="เเสดง">เเสดง</option>
                                        <option value="ไม่เเสดง">ไม่เเสดง</option>
                                    </select>
                                </div>
                            </div>

                        </div>

                        <!-- <div class="w-full mb-2 pt-1 mt-4">
                            <textarea type="text" v-model="addressMember" ref="inputAddressMember" rows="4" :class="{
                                'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !addressMember
                            }" placeholder="ที่อยู่" disabled />
                        </div> -->

                        <div class="flex gap-2 items-center mb-4 mt-8 text-2xl font-semibold">
                            <span class="">ยอดรวมคำสั่งซื้อทั้งหมด :</span>
                            <span class="text-orange-500">600บาท</span>
                        </div>

                        <hr class="my-2 text-gray-600">

                        <div class="flex gap-2 justify-center mt-4 md:mt-4">
                            <!-- <button @click="btnEdit"
                                class="text-white bg-blue-500 border border-blue-500 font-medium rounded-lg text-sm px-3 py-2.5 text-center inline-flex items-center h-full">
                                ยืนยัน
                            </button> -->
                            <button @click="showFormTable"
                                class="text-black bg-gray-200 border border-gray-400 font-medium rounded-lg text-sm px-3 py-2.5 text-center inline-flex items-center h-full">
                                ยกเลิก
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
            isFocus: false,
            codeMember: '',
            nameMember: '',
            phoneMember: '',
            statusMember: '',
            // addressMember: '',

            formTable: true,
            formAdd: false,
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
            this.formAdd = false;
            this.formEdit = false;
            this.nameMember = '';
            this.phoneMember = '';
            this.statusMember = '';
            this.addressMember = '';
        },
        showFormEdit() {
            this.formTable = false;
            this.formAdd = false;
            this.formEdit = true;
        },
        // btnEdit() {
        //     if (!this.statusMember) {
        //         this.isFocus = true;
        //         this.$refs.inputStatusMember.focus();
        //     } else {
        //         this.$refs.modal.showAlertModal({
        //             swlIcon: 'success',
        //             swlTitle: 'สำเร็จ',
        //             swlText: 'เเก้ไขข้อมูลลูกค้าสำเร็จ!',
        //         });
        //     }
        // },

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