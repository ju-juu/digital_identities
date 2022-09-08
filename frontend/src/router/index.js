import { createRouter, createWebHistory } from 'vue-router'
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
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/user_login',
      name: 'userLogin',
      component: () => import('../views/UserLogin.vue')
    },
    {
      path: '/authority_login',
      name: 'authorityLogin',
      component: () => import('../views/AuthorityLogin.vue')
    },
  ]
})

export default router
