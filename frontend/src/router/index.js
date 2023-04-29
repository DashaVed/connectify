import {createRouter, createWebHistory} from 'vue-router'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'main',
            component: () => import('../views/HomeView.vue')
        },
        {
            path: '/register',
            name: 'registration',
            component: () => import('../views/RegistrationView.vue')
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('../views/LoginView.vue')
        },
        {
            path: '/members/:id(\\d+)',
            name: 'profile',
            component: () => import('../views/ProfileView.vue'),
        },
        {
            path: '/groups/create',
            name: 'create_group',
            component: () => import('../views/GroupCreate.vue'),
        },
    ]
})

export default router
