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
          }
        });
    },
    showSuccessModal({ swlTitle, swlText, swlIcon }) {
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
            this.$emit("clearLocalStorage");
            this.$router.push("/");
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

    showPhoneModal({ swlTitle, swlIcon }) {
      this.$swal
        .fire({
          title: swlTitle,
          icon: swlIcon,
          html: `
        <input
          id="phone"
          type="text"
          class="bg-white border border-gray-300 text-gray-900 text-sm rounded-lg block focus:border-gray-300 w-full p-2 focus:border-blue-500 focus:ring-2 focus:ring-blue-500"
          placeholder="กรอกเบอร์โทรศัพท์"
          required
        />
      `,
          showCancelButton: true,
          confirmButtonText: "ยืนยัน",
          cancelButtonText: "ยกเลิก",
          customClass: {
            confirmButton:
              "bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400",
            cancelButton:
              "bg-gray-300 text-black px-4 py-2 rounded-md hover:bg-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-400",
          },
          didOpen: () => {
            const phoneInput = document.getElementById("phone");
            phoneInput.focus();
          },
          preConfirm: () => {
            const phoneInput = document.getElementById("phone");
            const phone = phoneInput.value;
            const phoneRegex = /^[0-9]{10}$/;

            if (!phone || !phoneRegex.test(phone)) {
              phoneInput.focus();
              this.$swal.showValidationMessage(
                "กรุณากรอกเบอร์โทรศัพท์ที่ถูกต้อง"
              );
              return false;
            }
            return phone;
          },
        })
        .then((result) => {
          if (result.isConfirmed) {
            const phone = result.value;
            console.log("เบอร์โทรศัพท์ที่กรอก: ", phone);
            this.$emit("setPhone", phone);
          }
        });
    },
  },
};
</script>
