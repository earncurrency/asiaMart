<template>
    <ul
        class="flex flex-wrap justify-center text-md font-medium text-center mt-4 lg:mt-0 text-gray-500 dark:text-gray-400">
        <!-- ใช้ v-for กับ <li> โดยที่ RouterLink จะครอบ <li> -->
        <li v-for="(productType, index) in typeName" :key="index" class="me-2">
            <RouterLink :to="`/product-type/${productType}`" >
                <a href="#"
                    class="inline-block px-4 py-3 rounded-lg hover:text-gray-900 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-white">{{ productType }}</a>
            </RouterLink>
        </li>
    </ul>
</template>

<script>
export default {
    data() {
        return {
            typeName: ['ทั้งหมด', 'อาหาร', 'เครื่องดื่ม', 'ของทานเล่น', 'ของใช้ทั่วไป'],
        };
    },
};
</script>
