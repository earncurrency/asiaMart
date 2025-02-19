<script setup>
import { data } from "autoprefixer";
import axios from "axios";
import Modal from "@/components/frontend/modal.vue";
</script>
<template>
  <Modal ref="modal" />
  <div
    class="flex pr-6 pl-6 items-center justify-center min-h-screen bg-gray-100"
  >
    <div
      class="w-full max-w-md p-12 bg-white rounded-lg shadow-md relative border border-blue-gray-100"
    >
      <div class="p-2.5 mb-8 flex items-center rounded-md justify-center">
        <img class="w-36 h-auto" src="../../assets/image/asia/asiaGray.png" />
      </div>

      <div class="mt-8">
        <label
          for="employeeCode"
          class="block mb-2 text-md font-medium text-gray-700"
          >รหัสพนักงาน</label
        >
        <input
          type="text"
          v-model="code"
          ref="employeeCode"
          :class="{
            'bg-white border border-gray-300 text-gray-900 text-sm rounded-lg block focus:border-gray-300 w-full p-2 ': true,
            'focus:border-blue-500 focus:ring-2 focus:ring-blue-500 ': !code,
          }"
          placeholder="ใส่รหัสพนักงาน"
          required
        />
      </div>

      <div class="flex justify-center mt-12">
        <button
          @click="BtnLogin"
          class="w-1/2 px-5 py-2 text-white bg-blue-600 hover:bg-blue-700 border border-blue-600 focus:ring-4 focus:ring-gray-300 font-medium rounded-lg text-md transition shadow-md hover:shadow-lg"
        >
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
      apiUrl: __API_URL__,
      authUrl: __AUTH_URL__,
      code: "",     
      member: {
        code: "",
        name: "",
      },
      isFocus: false,
    };
  },

  methods: {
    BtnLogin() {
      if (!this.code) {
        this.isFocus = true;
        this.$refs.employeeCode.focus();
      } else {
        const postData = {
          code: this.code,
        };
        axios
          .post(this.authUrl + "action=mrsLogin", postData)
          .then((response) => {
            if (response.data.success) {
              localStorage.setItem("hash", response.data.hash);
              localStorage.setItem("fullname", response.data.fullname);
              this.$router.push("/");

              // const idNumber = response.data.hash.split("-")[0];
              this.member.code = response.data.hash.split("-")[1];
              this.member.name = response.data.fullname;

              const member = {
                code: this.member.code,
                name: this.member.name,
                status: "active",
              };

              axios.post(`${this.apiUrl}members/`, member);
     
            } else {
              this.$refs.modal.showAlertModal({
                swlIcon: "warning",
                swlTitle: "ไม่พบพนักงาน",
                swlText: "ไม่พบข้อมูลพนักงานในระบบ",
              });
              return;
            }
          })
          .catch((error) => {
            if (error.response) {
              this.$refs.modal.showAlertModal({
                swlIcon: "warning",
                swlTitle: "เกิดข้อผิดพลาด",
                swlText: "เกิดข้อผิดพลาดในการเข้าสู่ระบบ",
              });
              return;
            } else {
              this.$refs.modal.showAlertModal({
                swlIcon: "warning",
                swlTitle: "เกิดข้อผิดพลาด",
                swlText: "เกิดข้อผิดพลาดในการเชื่อมต่อกับเซิร์ฟเวอร์",
              });
              return;
            }
          });
      }
    },
  },
};
</script>
