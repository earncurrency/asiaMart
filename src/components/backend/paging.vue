<script setup>
import { last } from "lodash";

const normalClass =
  "flex items-center justify-center px-2 lg:px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 transition";
const activeClass =
  "flex items-center justify-center px-2 lg:px-3 h-8 leading-tight text-gray-700 bg-gray-300 border border-gray-300 hover:bg-gray-100 hover:text-gray-700 transition";
</script>

<template>
  <!-- Pagination -->
  <nav
    class="flex items-center justify-center flex-wrap md:flex-row lg:justify-between pt-4 p-2"
    aria-label="Table navigation"
  >
    <span
      class="text-sm font-normal text-gray-500 mb-4 md:mb-0 w-full md:inline md:w-auto text-center md:text-left"
    >
      เเสดง
      <span class="font-semibold text-gray-900"
        >{{ firstRowNumber }} - {{ lastRowNumber }}</span
      >
      จาก <span class="font-semibold text-gray-900">{{ totalList }}</span>
    </span>

    <ul class="inline-flex -space-x-px rtl:space-x-reverse text-sm h-8">
      <li @click="prev()">
        <a
          href="#"
          class="flex items-center justify-center px-2 lg:px-3 h-8 ms-0 leading-tight text-gray-500 bg-white border border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700"
        >
          <i class="fa-solid fa-angle-left"></i>
        </a>
      </li>

      <li
        v-for="(index, idx) in pagination"
        :key="idx"
        @click="clickPage(index)"
      >
        <a href="#" :class="index == currentPage ? activeClass : normalClass">{{
          index
        }}</a>
      </li>

      <li @click="next()">
        <a
          href="#"
          class="flex items-center justify-center px-2 lg:px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 rounded-e-lg hover:bg-gray-100 hover:text-gray-700"
        >
          <i class="fa-solid fa-angle-right"></i>
        </a>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  props: {
    pageSize: {
      type: Number,
      required: false,
    },
    totalList: {
      required: false,
      default: 1,
    },
    currentNum: {
      type: Number,
      required: false,
    },
  },
  data() {
    return {
      currentPage: 1,
      // pageList: [10, 20, 50, 100, 200],
      firstRowNumber: 1,
      lastRowNumber: null,
    };
  },
  mounted() {
    // this.changeLastrow();
  },
  watch: {
    pageSize(newPageSize) {
      this.currentPage = 1;
      this.changeShowRowNumber();
    },
    currentNum(NewcurrentNum) {
      this.currentPage = 1;
      this.changeShowRowNumber();
    },
  },
  computed: {
    // คำนวณจำนวนหน้าทั้งหมด
    totalPagination() {
      return Math.ceil(this.totalList / this.pageSize);
    },
    //ตัวเลขใน pagination
    pagination() {
      let pages = [];
      let ellipsis = "...";

      if (this.totalList < this.pageSize) {
        this.lastRowNumber = this.totalList;
      } else {
        this.lastRowNumber = this.pageSize;
      }

      if (this.totalPagination <= 10) {
        // ถ้ามีจำนวนหน้าทั้งหมดไม่เกิน 10 หน้า จะแสดงหน้าทั้งหมด
        pages = Array.from({ length: this.totalPagination }, (_, i) => i + 1);
      } else {
        // จะแสดงหน้าแรกเสมอ
        pages.push(1);

        // ถ้าหน้าปัจจุบันมากกว่า 4 จะแสดง '...' ก่อนหน้า
        if (this.currentPage > 4) {
          pages.push(ellipsis);
        }

        // จะแสดงหน้ารอบๆ หน้าปัจจุบัน เช่น หน้าปัจจุบัน - 2 ถึง หน้าปัจจุบัน + 2
        for (
          let i = Math.max(2, this.currentPage - 2);
          i <= Math.min(this.totalPagination - 1, this.currentPage + 2);
          i++
        ) {
          pages.push(i);
        }

        // ถ้าหน้าปัจจุบันห่างจากหน้าสุดท้ายมากเกินไป จะมีการแสดง '...' ก่อนหน้านั้น
        if (this.currentPage < this.totalPagination - 4) {
          pages.push(ellipsis);
        }

        // จะแสดงหน้าสุดท้ายเสมอ
        pages.push(this.totalPagination);
      }

      return pages;
    },
  },
  methods: {
    // changeLastrow() {
    //   if (this.totalList < 10) {
    //     this.lastRowNumber = this.totalList;
    //   }
    // },
    // ฟังก์ชั่นที่ทำงานเมื่อผู้ใช้คลิกที่หมายเลขหน้า
    clickPage(pageNo) {
      if (pageNo === "..." || pageNo < 1 || pageNo > this.totalPagination)
        return;
      this.currentPage = pageNo;
      // this.offset = (pageNo - 1) * this.pageSize;
      this.$emit("reloadData", pageNo);
      this.changeShowRowNumber();
    },
    changeShowRowNumber() {
      if (this.currentPage > this.totalPagination) {
        this.currentPage = this.totalPagination;
      }

      this.firstRowNumber = (this.currentPage - 1) * this.pageSize + 1;
      this.lastRowNumber = this.currentPage * this.pageSize;

      if (this.lastRowNumber > this.totalList) {
        this.lastRowNumber = this.totalList;
      }

      // console.log("currentPage",currentPage)
    },
    prev() {
      if (this.currentPage > 1) {
        this.currentPage--;
        this.clickPage(this.currentPage);
      }
    },
    next() {
      if (this.currentPage < this.totalPagination) {
        this.currentPage++;
        this.clickPage(this.currentPage);
      }
    },
  },
};
</script>
