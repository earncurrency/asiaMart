import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    // vueDevTools(),
  ],
  // base: '/asiaMart/',
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  define: {
    __BASE_URL__: JSON.stringify(
      process.env.NODE_ENV === 'production'
      ?'https://app.asiagroup1999.co.th/asiaMart'
      :'http://localhost/asiaMart'
    ),
    __API_URL__: JSON.stringify(
      process.env.NODE_ENV === 'production'
      ? 'https://app.asiagroup1999.co.th/asiaMart/api/' // Production API URL
      : 'http://127.0.0.1:8000/'   // Development API URL
    ),
  },
})

// export default {
//   mounted() {
//     console.log(__API_BASE_URL__); // Output: "https://api.example.com"
//     console.log(__APP_NAME__);    // Output: "My Awesome App"
//     console.log(__VERSION__);     // Output: "1.0.0"
//   }
// };