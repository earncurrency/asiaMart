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
  base: process.env.NODE_ENV === 'production'?'/asiaMart/':'',
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  define: {
    __BASE_URL__: JSON.stringify(
      process.env.NODE_ENV === 'production'
      ?'https://www.asg1999.com/asiaMart'
      :''
    ),
    __API_URL__: JSON.stringify(
      process.env.NODE_ENV === 'production'
      ? 'https://app.asiagroup1999.co.th/asiaMart/middleware.php?endpoint='
      : 'http://localhost/asiaMart/middleware.php?endpoint='
      // : 'http://127.0.0.1:8000/'
    ),
    __AUTH_URL__: JSON.stringify(
      process.env.NODE_ENV === "production"
      ? "https://app.asiagroup1999.co.th/app/hr/employee?"
      : "https://app.asiagroup1999.co.th/app/hr/employee?"
    ),
  },
})
