import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import './assets/tailwind.css'
import '@fortawesome/fontawesome-free/css/all.css'
import Swal from 'sweetalert2';

const app = createApp(App)

// เพิ่ม SweetAlert2 เป็น global property
app.config.globalProperties.$swal = Swal;

app.use(router)

app.mount('#app')



