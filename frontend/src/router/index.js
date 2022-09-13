import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/about',
            name: 'about',
            component: () => import('../views/AboutView.vue')
        },
        {
            path: '/user_login',
            name: 'userLogin',
            component: () => import('../views/UserLogin.vue')
        },
        {
            path: '/user_home',
            name: 'userHome',
            component: () => import('../views/UserHome.vue'),
            meta: {requiresAuth: true}
        },
        {
            path: '/user_qr',
            name: 'userQR',
            component: () => import('../views/UserQR.vue'),
            meta: {requiresAuth: true}
        },
        {
            path: '/authority_login',
            name: 'authorityLogin',
            component: () => import('../views/AuthorityLogin.vue')
        },
        {
            path: '/authority_home',
            name: 'authorityHome',
            component: () => import('../views/AuthorityHome.vue'),
            meta: {requiresAuth: true}
        },
        {
            path: '/authority_scanner',
            name: 'authorityScanner',
            component: () => import('../views/AuthorityScanner.vue'),
            meta: {requiresAuth: true}
        },
    ]
})

export default router
