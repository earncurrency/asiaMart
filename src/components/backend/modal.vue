<template></template>
<script>
export default {
  methods: {
    showAlertModal({ swlTitle, swlText, swlIcon }) {
      this.$swal
        .fire({
          title: swlTitle,
          text: swlText,
          icon: swlIcon,
          confirmButtonText: "ยืนยัน",
          customClass: {
            confirmButton:
              "bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400",
          },
        })
        .then((result) => {
          if (result.isConfirmed) {
            this.$emit("showFormTable");
          }
        });
    },
    showDeleteModal({ swlTitle, swlText, swlIcon, onConfirm }) {
      this.$swal
        .fire({
          title: swlTitle,
          text: swlText,
          icon: swlIcon,
          showCancelButton: true,
          confirmButtonText: "ยืนยัน",
          cancelButtonText: "ยกเลิก",
          customClass: {
            confirmButton:
              "bg-red-500 text-white px-4 py-2 rounded-md hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-400",
            cancelButton:
              "bg-gray-300 text-black px-4 py-2 rounded-md hover:bg-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-300",
          },
        })
        .then((result) => {
          if (result.isConfirmed) {
            // ถ้าผู้ใช้ยืนยันการลบ จะเรียกใช้ฟังก์ชัน onConfirm
            if (onConfirm) onConfirm();
          }
        });
    },

  },
};
</script>
