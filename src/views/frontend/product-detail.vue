<script setup>
    import frontend_navbar from '../../components/frontend/navbar.vue';
    import axios from "axios";
</script>


<template>
    <frontend_navbar />
    
    <div class="flex justify-center pt-24 p-4 ">
        <div class="w-full max-w-screen-2xl lg:p-12 lg:border border-gray-200 rounded-lg mb-16 lg:mb-4 bg-white z-40">
            <div>
                <!-- Title -->
                <!-- เปุ่มนี้เสดงเมื่อจอเล็ก -->
                <div class="flex items-center gap-4 lg:hidden">
                    <RouterLink to="/">
                        <button class="px-2 py-1 bg-gray-800 rounded-md text-white text-sm"><i
                                class="fa-solid fa-arrow-left"></i></button>
                    </RouterLink>
                    <!-- <p class="text-xl">อาหาร</p> -->
                </div>
                <div class="lg:flex items-center justify-between font-medium p-2 lg:p-0">
                    <!-- เปุ่มนี้เสดงเมื่อจอใหญ่ -->
                    <div class="flex justify-center gap-4">
                        <div class="hidden lg:flex items-center gap-4">
                            <RouterLink to="/">
                                <button
                                    class="px-2 py-1 bg-gray-800 rounded-md text-white text-sm hover:bg-gray-600 transition"><i
                                        class="fa-solid fa-arrow-left"></i></button>
                            </RouterLink>
                            <!-- <p class="text-xl">อาหาร</p> -->
                        </div>
                        <!-- <p class="text-xl">กลับ</p> -->
                    </div>

                </div>

                <hr class="my-2 text-gray-600">

                <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 gap-4 lg:gap-8 mt-8">
                    <div>
                        <!-- รูปใหญ่ด้านบนที่จะแสดงภาพที่เลือก -->
                        <div class="lg:h-96 h-60 w-full cursor-pointer">
                            <img :src="selectedImage" alt="Selected Food" class="h-full w-full object-cover rounded-md">
                        </div>

                        <!-- กริดของภาพ -->
                        <div class="grid grid-cols-4 gap-2 lg:gap-4 pt-2 lg:pt-4">
                            <div class="w-full lg:h-28 h-20 cursor-pointer"
                                @click="selectImage('https://images.deliveryhero.io/image/fd-th/LH/ws9f-listing.jpg')">
                                <img src="https://images.deliveryhero.io/image/fd-th/LH/ws9f-listing.jpg" alt="Food 1"
                                    class="h-full w-full object-cover rounded-md">
                            </div>
                            <div class="w-full lg:h-28 h-20 cursor-pointer"
                                @click="selectImage('https://images.deliveryhero.io/image/fd-th/LH/e4gw-listing.jpg')">
                                <img src="https://images.deliveryhero.io/image/fd-th/LH/e4gw-listing.jpg" alt="Food 2"
                                    class="h-full w-full object-cover rounded-md">
                            </div>
                            <div class="w-full lg:h-28 h-20 cursor-pointer"
                                @click="selectImage('https://shopee.co.th/blog/wp-content/uploads/2020/10/%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%A1%E0%B8%B1%E0%B8%99%E0%B9%84%E0%B8%81%E0%B9%88.jpg')">
                                <img src="https://shopee.co.th/blog/wp-content/uploads/2020/10/%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%A1%E0%B8%B1%E0%B8%99%E0%B9%84%E0%B8%81%E0%B9%88.jpg"
                                    alt="Food 3" class="h-full w-full object-cover rounded-md">
                            </div>
                            <div class="w-full lg:h-28 h-20 cursor-pointer"
                                @click="selectImage('https://img-global.cpcdn.com/recipes/8d36694f728a8620/1200x630cq70/photo.jpg')">
                                <img src="https://img-global.cpcdn.com/recipes/8d36694f728a8620/1200x630cq70/photo.jpg"
                                    alt="Food 4" class="h-full w-full object-cover rounded-md">
                            </div>
                        </div>
                    </div>

                    <div class="p-8 bg-gray-100 rounded-md text-gray-600">
                        <p class="text-2xl lg:text-3xl font-semibold mb-2">ข้าวกระเพราหมู+ไข่ดาว</p>
                        <p class="text-md">Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                            Nostrum, sint. Itaque, quisquam aliquid. Optio cumque a, iure blanditiis dolorem modi natus
                        </p>
                        <div class="flex gap-4 items-center mt-8 justify-center lg:justify-start">
                            <p class="text-2xl font-semibold">ราคา</p>
                            <p class="text-2xl font-semibold text-orange-500">45 บาท</p>
                        </div>
                        <div class="flex gap-4 items-center mt-4 justify-center lg:justify-start">
                            <div class="flex items-center">
                                <!-- ปุ่มลดจำนวน -->
                                <button
                                    class="bg-gray-300 text-gray-600 hover:bg-gray-200 p-2 pr-3 pl-3 focus:outline-none transition rounded-l-md">
                                    -
                                </button>

                                <!-- ช่องกรอกจำนวนสินค้า -->
                                <input type="text" class="w-14 text-center border-none focus:outline-none p-2 pr-3 pl-3" value="1" />

                                <!-- ปุ่มเพิ่มจำนวน -->
                                <button
                                    class="bg-gray-300 text-gray-600 hover:bg-gray-200 p-2 pr-3 pl-3 focus:outline-none transition rounded-r-md">
                                    +
                                </button>
                            </div>
                        </div>

                        <div class="flex justify-center lg:justify-start">
                            <button
                                class="p-2 pr-4 pl-4 rounded-lg bg-gray-800 text-white mt-6 hover:bg-gray-600 transition">
                                <i class="fa-solid fa-cart-plus text-md"></i> เพิ่มลงตระกร้า
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
            // กำหนดภาพเริ่มต้นที่จะแสดง
            selectedImage: 'https://images.deliveryhero.io/image/fd-th/LH/ws9f-listing.jpg',
        };
    },
    methods: {
        // ฟังก์ชันในการเปลี่ยนภาพเมื่อคลิก
        selectImage(imageUrl) {
            this.selectedImage = imageUrl;
        },
    },
};
</script>
