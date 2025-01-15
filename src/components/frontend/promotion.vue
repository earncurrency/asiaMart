<template>

    <div class="overflow-x-auto py-6 no-scrollbar">
        <div
            class="grid grid-flow-col auto-cols-[16rem] gap-4 min-w-max sm:grid-cols-1 lg:grid-cols-3 lg:grid-flow-row lg:auto-cols-[26rem]">
            <!-- Card 1 -->
            <div class="bg-white rounded-lg">
                <img src="../../assets/image/asia/placeholder-image.webp" alt="Promotion Image"
                    class="w-full h-48 object-cover rounded-t-lg">
                <div class="p-4">
                    <h3 class="text-lg font-semibold text-gray-800">โปรโมชั่น 1</h3>
                    <p class="text-sm text-gray-600">ลดราคา 10% สำหรับสินค้าทุกชิ้น</p>
                </div>
            </div>

            <!-- Card 2 -->
            <div class="bg-white rounded-lg">
                <img src="../../assets/image/asia/placeholder-image.webp" alt="Promotion Image"
                    class="w-full h-48 object-cover rounded-t-lg">
                <div class="p-4">
                    <h3 class="text-lg font-semibold text-gray-800">โปรโมชั่น 2</h3>
                    <p class="text-sm text-gray-600">รับส่วนลด 20% เมื่อช็อปครบ 500 บาท</p>
                </div>
            </div>

            <!-- Card 3 -->
            <div class="bg-white rounded-lg">
                <img src="../../assets/image/asia/placeholder-image.webp" alt="Promotion Image"
                    class="w-full h-48 object-cover rounded-t-lg">
                <div class="p-4">
                    <h3 class="text-lg font-semibold text-gray-800">โปรโมชั่น 3</h3>
                    <p class="text-sm text-gray-600">ซื้อ 1 เเถม 1</p>
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