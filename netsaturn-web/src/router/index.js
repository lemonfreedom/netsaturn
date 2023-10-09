import { createRouter, createWebHashHistory } from "vue-router"

const isAuthenticated = true // 是否登录

const routes = [
  {
    path: '/', name: 'Home',
    component: () => import("@/layouts/HomeLayout/index.vue"),
    redirect: 'home',
    children: [
      {
        path: 'home',
        component: () => import("@/views/Home/index.vue"),
      },
    ]
  },
  { path: '/login', name: 'Login', component: () => import("@/views/Login/index.vue") }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

router.beforeEach((to, from) => {
  if (!isAuthenticated && to.name !== 'Login') {
    return { name: 'Login' }
  }
})

export default router
