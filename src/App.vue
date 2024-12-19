<script setup>
import { useRoute } from 'vue-router';
import { RouterView } from 'vue-router';
const route = useRoute(); // ใช้ useRoute เพื่อเข้าถึง route ปัจจุบัน
</script>

<template>

  <div class="flex flex-col min-h-screen">
    <div class="flex-grow">
      <RouterView />
    </div>
  </div>


</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@400;700&display=swap');

body {
  font-family: 'Prompt', sans-serif;
}
</style>
