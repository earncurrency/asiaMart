<script setup>

import frontend_navbar from '@/components/frontend/navbar.vue';
import imageBanner from '@/components/frontend/image-banner.vue';
import tabsCategory from '@/components/frontend/tabs-category.vue';
import productList from '@/components/frontend/product-list.vue';
import promotion from '@/components/frontend/promotion.vue';


</script>
<template>

    <frontend_navbar />


    <imageBanner />

    <div class="flex justify-center pt-18 p-4 ">
        <div class="w-full max-w-screen-2xl lg:p-12 lg:border border-gray-200 rounded-lg mb-16 lg:mb-4 bg-white z-40">
            <div>
                <!-- Title -->
                <div class="title-content lg:flex items-center justify-between font-medium mt-4 gap-4 p-4 lg:p-0">
                    <div class="flex justify-center">
                        <p class="text-3xl font-semibold ">Asia Mart</p>
                    </div>

                    <!-- tabs menu -->
                    <tabsCategory />

                </div>

                <hr class="my-2 text-gray-600">

                <div class="flex justify-center">
                    <p class="text-3xl font-semibold mt-8 mb-2">โปรโมชั่น</p>
                </div>

                <promotion />


                <div class="flex justify-center">
                    <p class="text-3xl font-semibold mt-8 mb-2">สินค้าเเนะนำ</p>
                </div>

<!-- 
                <productList /> -->

                <div class="flex justify-center mt-8 mb-4">
                    <button class="bg-gray-400 text-gray-900 p-2 pl-6 pr-6 rounded-md">ดูเพิ่มเติม</button>
                </div>

            </div>

        </div>
    </div>



</template>

