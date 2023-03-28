import { createRouter, createWebHashHistory } from 'vue-router'
import page1 from '../views/page1.vue'
import page3 from '../views/page3.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: page1
  },
  {
    path: '/page1',
    name: 'page1',
    component: page1
  },
  {
    path: '/page2',
    name: 'page2',
    component: page1
  },
  {
    path: '/page3',
    name: 'page3',
    component: page3
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
