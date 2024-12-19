<script setup>


</script>
<template>

    <div class="flex pr-6 pl-6 items-center justify-center min-h-screen bg-gray-100">
        <div class="w-full max-w-md p-12 bg-white rounded-lg shadow-md relative border border-blue-gray-100">

            <div class="p-2.5 mb-8 flex items-center rounded-md justify-center">

                <img class="w-36 h-auto" src="../../assets/image/asia/asiaGray.png">

            </div>

            <!-- <div class="mt-8">
                <label for="email" class="block mb-2 text-md font-medium text-gray-700">ชื่อผู้ใช้</label>
                <input type="text" 
                    class="bg-white border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-gray-300 block w-full pt-2 pl-3"
                    placeholder="ชื่อผู้ใช้" required />
            </div>

            <div class="mt-8">
                <label for="password" class="block mb-2 text-md font-medium text-gray-700">รหัสผ่าน</label>
                <input type="password" 
                    class="bg-white border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-gray-300 block w-full pt-2 pl-3"
                    placeholder="รหัสผ่าน" required />
            </div> -->

            <div class="mt-8">
                <label for="employeeCode" class="block mb-2 text-md font-medium text-gray-700">รหัสพนักงาน</label>
                <input type="text" v-model="code" ref="employeeCode" :class="{
                    'bg-white border border-gray-300 text-gray-900 text-sm rounded-lg block focus:border-gray-300 w-full pt-2 pl-3 ': true,
                    'focus:border-blue-500 focus:ring-2 focus:ring-blue-500 ': !code
                }" placeholder="ใส่รหัสพนักงาน" required />
            </div>


            <div class="flex justify-center mt-12">
                <button @click="BtnLogin"
                    class="w-1/2 px-5 py-2 text-white bg-blue-600 hover:bg-blue-700 border border-blue-600 focus:ring-4 focus:ring-gray-300 font-medium rounded-lg text-md transition shadow-md hover:shadow-lg">
                    เข้าสู่ระบบ
                </button>
            </div>

        </div>
    </div>

</template>

<script>


export default {
    data() {
        return {
            code: '',

        };
    },

    methods: {

        BtnLogin() {
            // if (!this.username || !this.password) {
            if (!this.code) {
                // ถ้ารหัสพนักงานว่าง ให้ focus และทำให้ input มี border สีแดง
                this.isFocus = true;
                this.$refs.employeeCode.focus();  // ให้ focus ไปที่ input
            }
        },
    },
};

</script>
