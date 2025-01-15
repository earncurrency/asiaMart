import { createRouter, createWebHistory } from 'vue-router';

import '../assets/tailwind.css';

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/login',
            name: 'login',
            component: () => import('../views/frontend/login.vue'),
        },
        {
            path: '/',
            name: 'home',
            component: () => import('../views/frontend/home.vue'),
        },
        {
            path: '/cart',
            name: 'carts',
            component: () => import('../views/frontend/cart.vue'),
        },
        {
            path: '/alert',
            name: 'alert',
            component: () => import('../views/frontend/alert.vue'),
        },
        {
            path: '/profile',
            name: 'profile',
            component: () => import('../views/frontend/profile.vue'),
        },
        {
            path: '/confirm-order',
            name: 'confirm-order',
            component: () => import('../views/frontend/confirm-order.vue'),
        },
        {
            path: '/order-detail',
            name: 'order-detail',
            component: () => import('../views/frontend/order-detail.vue'),
        },
        {
            path: '/product-detail',
            name: 'product-detail',
            component: () => import('../views/frontend/product-detail.vue'),
        },
        {
            path: '/category/:category',
            name: 'category',
            component: () => import('../views/frontend/category.vue'),
            props: true,
        },
        {
            path: '/history',
            name: 'history',
            component: () => import('../views/frontend/history.vue'),
        },

        //////////////////////////////////backend/////////////////////////////////////////    
        {
            path: '/backend/dashboard',
            name: 'backend/dashboard',
            component: () => import('../views/backend/dashboard.vue'),
        },
        {
            path: '/backend/manage-category',
            name: 'backend/manage-category',
            component: () => import('../views/backend/manage-category.vue'),
        },
        {
            path: '/backend/manage-product',
            name: 'backend/manage-product',
            component: () => import('../views/backend/manage-product.vue'),
        },
        {
            path: '/backend/manage-member',
            name: 'backend/manage-member',
            component: () => import('../views/backend/manage-member.vue'),
        },
        {
            path: '/backend/manage-order',
            name: 'backend/manage-order',
            component: () => import('../views/backend/manage-order.vue'),
        },
        {
            path: '/backend/manage-inventory',
            name: 'backend/manage-inventory',
            component: () => import('../views/backend/manage-inventory.vue'),
        },
        {
            path: '/backend/report',
            name: 'backend/report',
            component: () => import('../views/backend/report.vue'),
        },
    ]
});



export default router;
