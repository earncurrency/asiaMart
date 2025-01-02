<script setup>
import backend_navbar from '@/components/backend/navbar.vue';
import Modal from '@/components/backend/modal.vue';
import axios from 'axios'
</script>

<template class="">

    <backend_navbar @showFormTable="showFormTable" />
    <Modal ref="modal" @showFormTable="showFormTable" />

    <div class="p-4 lg:pr-24 lg:pl-24 pt-6 sm:ml-64">
        <div class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-14">


            <div class="mt-2 mb-2">
                <div class=" lg:p-4 w-full rounded-md text-gray-600">

                    <div v-if="formTable">

                        <!-- title -->
                        <div class="flex justify-between items-center mb-2">
                            <p class="text-3xl font-semibold">รายการสินค้า</p>
                            <button @click="showFormAdd"
                                class="block py-2 px-6 bg-green-500 hover:bg-green-600 text-white rounded-md transition">
                                <i class="fa-solid fa-plus"></i></button>
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

                            <!-- เลือกสถานะ-->
                            <div class="flex gap-2 justify-center pt-4 lg:pt-0">

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
                                                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">อาหาร</a>
                                            </li>
                                            <li>
                                                <a href="#" @click="DropdownStatus(1)"
                                                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">เครื่องดื่ม</a>
                                            </li>
                                            <li>
                                                <a href="#" @click="DropdownStatus(2)"
                                                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">ของทานเล่น</a>
                                            </li>
                                            <li>
                                                <a href="#" @click="DropdownStatus(3)"
                                                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">ของใช้ทั่วไป</a>
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
                                            ราคาทุน
                                        </th>
                                        <th scope="col" class="px-6 py-4 whitespace-nowrap">
                                            ราคาขาย
                                        </th>
                                        <th scope="col" class="px-6 py-4 whitespace-nowrap">
                                            สถานะ
                                        </th>
                                        <th scope="col" class="px-6 py-4 whitespace-nowrap">

                                        </th>
                                    </tr>
                                </thead>

                                <tbody>
                                    <tr v-for="(product, index) in products" :key="index"
                                        @click="showFormEdit(product.id)"
                                        class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 cursor-pointer hover:bg-gray-100 transition">
                                        <th scope="row" class="px-6 py-4">
                                            <div class="w-24 h-24 lg:w-24 lg:h-24 ">
                                                <img class="w-full h-full rounded-md object-cover ring-4 ring-gray-300 shadow-md"
                                                    src="../../assets/image/product/product.png">
                                            </div>
                                        </th>

                                        <td class="px-6 py-4 whitespace-nowrap font-semibold">
                                            {{ product.code }}
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            {{ product.name }}
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            {{ product.cost }}
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            {{ product.sell }}
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            <span class="font-semibold text-green-500 p-1 bg-green-100 rounded-md">{{
                                                product.status }}</span>
                                        </td>
                                        <td class="px-6 py-4">
                                            <button @click.stop="btnDelete"
                                                class="bg-red-500 text-white px-4 py-2 rounded-md">
                                                <i class="fa-solid fa-trash-can"></i></button>
                                        </td>

                                    </tr>

                                </tbody>
                            </table>
                        </div>
                    </div>

                    <div v-if="formAdd">
                        <!-- title -->
                        <div class="flex gap-2 items-center mb-2">
                            <p class="text-3xl font-semibold">เพิ่มสินค้า</p>
                        </div>

                        <div class="flex w-full gap-2 mb-2 pt-1 mt-4">
                            <div class="w-full lg:w-1/4">
                                <input type="text" v-model="codeProduct" ref="inputCodeProduct" :class="{
                                    'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                    'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !codeProduct
                                }" placeholder="รหัสสินค้า" required />
                            </div>
                            <div class="w-full lg:w-3/4">
                                <input type="text" v-model="nameProduct" ref="inputNameProduct" :class="{
                                    'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                    'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !nameProduct
                                }" placeholder="ใส่ชื่อสินค้า" required />
                            </div>
                        </div>

                        <div class="md:flex w-full gap-2 mb-2 pt-1 mt-4">

                            <div class="flex gap-2 w-full">
                                <div class="lg:w-1/2 w-full">
                                    <input type="text" v-model="costPriceProduct" ref="inputCostPriceProduct" :class="{
                                        'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                        'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !costPriceProduct
                                    }" placeholder="ราคาทุน" required />
                                </div>

                                <div class="lg:w-1/2 w-full">
                                    <input type="text" v-model="sellPriceProduct" ref="inputSellPriceProduct" :class="{
                                        'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                        'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !sellPriceProduct
                                    }" placeholder="ราคาขาย" required />
                                </div>
                            </div>

                            <div class="flex gap-2 w-full pt-1 mt-4 lg:pt-0 lg:mt-0">
                                <div class="lg:w-1/2 w-full">
                                    <select v-model="typeProduct" ref="inputTypeProduct" :class="{
                                        'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                        'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !typeProduct
                                    }" required>
                                        <option value="" disabled selected>ประเภท</option>
                                        <option value="อาหาร">อาหาร</option>
                                        <option value="เครื่องดื่ม">เครื่องดื่ม</option>
                                        <option value="ของทานเล่น">ของทานเล่น</option>
                                        <option value="ของใช้ทั่วไป">ของใช้ทั่วไป</option>
                                    </select>
                                </div>

                                <div class="lg:w-1/2 w-full">
                                    <select v-model="statusProduct" ref="inputStatusProduct" :class="{
                                        'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                        'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !statusProduct
                                    }" required>
                                        <option value="" disabled selected>สถานะ</option>
                                        <option value="เเสดง">เเสดง</option>
                                        <option value="ไม่เเสดง">ไม่เเสดง</option>
                                    </select>
                                </div>
                            </div>

                        </div>

                        <div class="md:flex w-full gap-2 mb-2 pt-1 mt-4">
                            <div class="flex gap-2 w-full">
                                <div class="w-full">
                                    <textarea type="text" v-model="detailProduct" ref="inputDetailProduct" rows="4"
                                        :class="{
                                            'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                            'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !detailProduct
                                        }" placeholder="รายละเอียดสินค้า" required />
                                </div>
                            </div>
                        </div>


                        <div class="md:flex w-full gap-2 mb-2 pt-1 mt-4">
                            <!-- Input สำหรับเลือกรูปภาพหลายๆ รูป -->
                            <input type="file" id="fileInput" @change="inputImage" accept="image/*" multiple hidden>
                            <label for="fileInput"
                                class="cursor-pointer bg-gray-100 border border-gray-300 text-gray-500 px-4 py-2 rounded-md hover:bg-gray-50 transition">
                                เลือกรูปภาพ
                            </label>
                        </div>
                        <div class="md:flex w-full gap-2 mb-4 pt-1 mt-5">
                            <!-- แสดงภาพตัวอย่างที่เลือก -->
                            <div v-if="previewImages.length > 0"
                                class="image-preview grid grid-cols-2 lg:grid-cols-5 gap-8">
                                <div v-for="(image, imageIndex) in previewImages" :key="imageIndex"
                                    class="preview-item relative">
                                    <img :src="image" alt="Image preview"
                                        class="w-32 h-32 lg:w-64 lg:h-48 object-cover rounded-md">
                                    <!-- ปุ่มลบภาพ -->
                                    <button @click="removeImage(imageIndex)"
                                        class="absolute text-white bg-red-500 font-medium rounded-lg text-md text-center inline-flex items-center -top-2 -right-3 px-4 py-2.5">
                                        <i class="fa-solid fa-trash-can"></i>
                                    </button>
                                </div>
                            </div>

                        </div>

                        <hr class="my-2 text-gray-600">

                        <div class="flex gap-2 justify-center mt-4 md:mt-4">
                            <button @click="btnAdd"
                                class="text-white bg-blue-500 border border-blue-500 font-medium rounded-lg text-sm px-3 py-2.5 text-center inline-flex items-center h-full">
                                ยืนยัน
                            </button>
                            <button @click="showFormTable"
                                class="text-black bg-gray-200 border border-gray-400 font-medium rounded-lg text-sm px-3 py-2.5 text-center inline-flex items-center h-full">
                                ยกเลิก
                            </button>
                        </div>

                    </div>

                    <div v-if="formEdit">
                        <!-- title -->
                        <div class="flex justify-between items-center mb-2">
                            <p class="text-3xl font-semibold">เเก้ไขข้อมูลสินค้า</p>
                            <button @click.stop="btnDelete" class="bg-red-500 text-white px-4 py-1.5 rounded-md">
                                <i class="fa-solid fa-trash-can"></i>
                            </button>
                        </div>

                        <div class="flex w-full gap-2 mb-2 pt-1 mt-4">
                            <div class="w-full lg:w-1/4">
                                <input type="text" v-model="codeProduct" ref="inputCodeProduct" :class="{
                                    'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                    'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !codeProduct
                                }" placeholder="รหัสสินค้า" required />
                            </div>
                            <div class="w-full lg:w-3/4">
                                <input type="text" v-model="nameProduct" ref="inputNameProduct" :class="{
                                    'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                    'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !nameProduct
                                }" placeholder="ใส่ชื่อสินค้า" required />
                            </div>
                        </div>

                        <div class="md:flex w-full gap-2 mb-2 pt-1 mt-4">

                            <div class="flex gap-2 w-full">
                                <div class="lg:w-1/2 w-full">
                                    <input type="text" v-model="costPriceProduct" ref="inputCostPriceProduct" :class="{
                                        'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                        'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !costPriceProduct
                                    }" placeholder="ราคาทุน" required />
                                </div>

                                <div class="lg:w-1/2 w-full">
                                    <input type="text" v-model="sellPriceProduct" ref="inputSellPriceProduct" :class="{
                                        'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                        'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !sellPriceProduct
                                    }" placeholder="ราคาขาย" required />
                                </div>
                            </div>

                            <div class="flex gap-2 w-full pt-1 mt-4 lg:pt-0 lg:mt-0">
                                <div class="lg:w-1/2 w-full">
                                    <select v-model="typeProduct" ref="inputTypeProduct" :class="{
                                        'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                        'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !typeProduct
                                    }" required>
                                        <option value="" disabled selected>ประเภท</option>
                                        <option value="อาหาร">อาหาร</option>
                                        <option value="เครื่องดื่ม">เครื่องดื่ม</option>
                                        <option value="ของทานเล่น">ของทานเล่น</option>
                                        <option value="ของใช้ทั่วไป">ของใช้ทั่วไป</option>
                                    </select>
                                </div>

                                <div class="lg:w-1/2 w-full">
                                    <select v-model="statusProduct" ref="inputStatusProduct" :class="{
                                        'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                        'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !statusProduct
                                    }" required>
                                        <option value="" disabled selected>สถานะ</option>
                                        <option value="เเสดง">เเสดง</option>
                                        <option value="ไม่เเสดง">ไม่เเสดง</option>
                                    </select>
                                </div>
                            </div>

                        </div>

                        <div class="md:flex w-full gap-2 mb-2 pt-1 mt-4">
                            <div class="flex gap-2 w-full">
                                <div class="w-full">
                                    <textarea type="text" v-model="detailProduct" ref="inputDetailProduct" rows="4"
                                        :class="{
                                            'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full py-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                                            'focus:border-blue-300 focus:ring-2 focus:ring-blue-300': !detailProduct
                                        }" placeholder="รายละเอียดสินค้า" required />
                                </div>
                            </div>
                        </div>

                        <div class="md:flex w-full gap-2 mb-2 pt-1 mt-4">
                            <!-- Input สำหรับเลือกรูปภาพหลายๆ รูป -->
                            <input type="file" id="fileInput" @change="inputImage" accept="image/*" multiple hidden>
                            <label for="fileInput"
                                class="cursor-pointer bg-gray-100 border border-gray-300 text-gray-500 px-4 py-2 rounded-md hover:bg-gray-50 transition">
                                เลือกรูปภาพ
                            </label>
                        </div>
                        <div class="md:flex w-full gap-2 mb-4 pt-1 mt-5">
                            <!-- แสดงภาพตัวอย่างที่เลือก -->
                            <div v-if="previewImages.length > 0"
                                class="image-preview grid grid-cols-2 lg:grid-cols-5 gap-8">
                                <div v-for="(image, imageIndex) in previewImages" :key="imageIndex"
                                    class="preview-item relative">
                                    <img :src="image" alt="Image preview"
                                        class="w-32 h-32 lg:w-64 lg:h-48 object-cover rounded-md">
                                    <!-- ปุ่มลบภาพ -->
                                    <button @click="removeImage(imageIndex)"
                                        class="absolute text-white bg-red-500 font-medium rounded-lg text-md text-center inline-flex items-center -top-2 -right-3 px-4 py-2.5">
                                        <i class="fa-solid fa-trash-can"></i>
                                    </button>
                                </div>
                            </div>

                        </div>

                        <hr class="my-2 text-gray-600">

                        <div class="flex gap-2 justify-center mt-4 md:mt-6">
                            <button @click="btnEdit"
                                class="text-white bg-blue-500 border border-blue-500 font-medium rounded-lg text-sm px-3 py-2.5 text-center inline-flex items-center h-full">
                                ยืนยัน
                            </button>
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
            apiUrl: 'http://127.0.0.1:8000/',
            products: [],

            isFocus: false,

            productId: '',
            codeProduct: '',
            nameProduct: '',
            costPriceProduct: '',
            sellPriceProduct: '',
            typeProduct: '',
            statusProduct: '',
            detailProduct: '',
            previewImages: [],

            formTable: true,
            formAdd: false,
            formEdit: false,

            DropdownStatusOpen: false,
            pageSizeOpen: false,
        };
    },
    mounted() {
        this.getListProduct();


        document.addEventListener('click', this.closeDropdownStatus);
        document.addEventListener('click', this.closeDropdown);

    },

    methods: {

        showFormAdd() {
            this.formTable = false;
            this.formAdd = true;
            this.formEdit = false;
        },
        showFormTable() {
            this.formTable = true;
            this.formAdd = false;
            this.formEdit = false;

            this.getListProduct();
        },

        //เเสดงข้อมูลสมาชิกบนตาราง
        async getListProduct() {

            await axios.get(`${this.apiUrl}products`)
                .then(response => {
                    const data = response.data;
                    this.products = data.rows;
                    console.log(this.products)

                })
                .catch(error => {
                    console.error('There was an error fetching the data:', error);
                });
        },

        async showFormEdit(productId) {

            // เปิดฟอร์มแก้ไข
            this.formTable = false;
            this.formAdd = false;
            this.formEdit = true;

            try {
                // เรียก API เพื่อดึงข้อมูลสมาชิกที่ระบุ
                const response = await axios.get(`${this.apiUrl}products/${productId}`);

                if (response.status === 200) {
                    const product = response.data.row;

                    if (product) {
                        this.productId = productId;
                        this.codeProduct = product.code;
                        this.nameProduct = product.name;
                        this.costPriceProduct = product.cost;
                        this.sellPriceProduct = product.sell;
                        this.typeProduct = product.type;
                        this.statusProduct = product.status;
                        this.detailProduct = product.detail;
                    } else {
                        alert("ไม่พบข้อมูลสมาชิกที่ต้องการแก้ไข");
                    }
                }
            } catch (error) {
                console.error("เกิดข้อผิดพลาดในการดึงข้อมูลสมาชิก:", error.response?.data?.detail || error.message);
                this.$refs.modal.showAlertModal({
                    swlIcon: 'error',
                    swlTitle: 'ล้มเหลว',
                    swlText: "เกิดข้อผิดพลาด",
                });
            }
        },

        async btnAdd() {
            if (!this.codeProduct) {
                this.isFocus = true;
                this.$refs.inputCodeProduct.focus();
            } else if (!this.nameProduct) {
                this.isFocus = true;
                this.$refs.inputNameProduct.focus();
            } else if (!this.costPriceProduct) {
                this.isFocus = true;
                this.$refs.inputCostPriceProduct.focus();
            } else if (!this.sellPriceProduct) {
                this.isFocus = true;
                this.$refs.inputSellPriceProduct.focus();
            } else if (!this.typeProduct) {
                this.isFocus = true;
                this.$refs.inputTypeProduct.focus();
            } else if (!this.statusProduct) {
                this.isFocus = true;
                this.$refs.inputStatusProduct.focus();
            } else if (!this.detailProduct) {
                this.isFocus = true;
                this.$refs.inputDetailProduct.focus();
            } else {
                try {
                    const dataProduct = {
                        code: this.codeProduct,
                        name: this.nameProduct,
                        cost: this.costPriceProduct,
                        sell: this.sellPriceProduct,
                        status: this.statusProduct,
                        type: this.typeProduct,
                        detail: this.detailProduct,
                    };

                    const response = await axios.post(`${this.apiUrl}products/${this.productId}`, dataProduct);

                    if (response.status === 200) {
                        this.$refs.modal.showAlertModal({
                            swlIcon: 'success',
                            swlTitle: 'สำเร็จ',
                            swlText: response.data.message,
                        });
                    }
                } catch (error) {
                    this.$refs.modal.showAlertModal({
                        swlIcon: 'error',
                        swlTitle: 'ล้มเหลว',
                        swlText: "เกิดข้อผิดพลาด",
                    });
                }
            }
        },

        async btnEdit() {
            if (!this.codeProduct) {
                this.isFocus = true;
                this.$refs.inputCodeProduct.focus();
            } else if (!this.nameProduct) {
                this.isFocus = true;
                this.$refs.inputNameProduct.focus();
            } else if (!this.costPriceProduct) {
                this.isFocus = true;
                this.$refs.inputCostPriceProduct.focus();
            } else if (!this.sellPriceProduct) {
                this.isFocus = true;
                this.$refs.inputSellPriceProduct.focus();
            } else if (!this.typeProduct) {
                this.isFocus = true;
                this.$refs.inputTypeProduct.focus();
            } else if (!this.statusProduct) {
                this.isFocus = true;
                this.$refs.inputStatusProduct.focus();
            } else if (!this.detailProduct) {
                this.isFocus = true;
                this.$refs.inputDetailProduct.focus();
            } else {
                try {
                    const dataProduct = {
                        code: this.codeProduct,
                        name: this.nameProduct,
                        cost: this.costPriceProduct,
                        sell: this.sellPriceProduct,
                        status: this.statusProduct,
                        type: this.typeProduct,
                        detail: this.detailProduct,
                    };

                    const response = await axios.put(`${this.apiUrl}products/${this.productId}`, dataProduct);

                    if (response.status === 200) {
                        this.$refs.modal.showAlertModal({
                            swlIcon: 'success',
                            swlTitle: 'สำเร็จ',
                            swlText: response.data.message,
                        });
                    }
                } catch (error) {
                    this.$refs.modal.showAlertModal({
                        swlIcon: 'error',
                        swlTitle: 'ล้มเหลว',
                        swlText: "เกิดข้อผิดพลาด",
                    });
                }
            }
        },
        inputImage(event) {
            const files = event.target.files;
            this.previewImages = [];

            for (let i = 0; i < files.length; i++) {
                const file = files[i];
                if (file && file.type.startsWith('image')) {
                    const reader = new FileReader();
                    reader.onload = (e) => {
                        const imageURL = e.target.result;
                        this.previewImages.push(imageURL);
                        console.log('Image URL:', imageURL);
                    };
                    reader.readAsDataURL(file);
                }
            }
            console.log(this.previewImages)
        },
        //ลบภาพจาก array previewImages
        removeImage(imageIndex) {
            this.previewImages.splice(imageIndex, 1);
        },
        btnDelete() {
            this.$refs.modal.showDeleteModal({
                swlIcon: 'warning',
                swlTitle: 'เเจ้งเตือน',
                swlText: 'คุณต้องการลบสินค้านี้หรือไม่!',
            })
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