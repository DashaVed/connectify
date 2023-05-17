import {createRouter, createWebHistory} from 'vue-router'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'main',
            component: () => import('../views/MainView.vue'),
            meta: {unauthorizedAccess: true}
        },
        {
            path: '/register',
            name: 'registration',
            component: () => import('../views/RegistrationView.vue'),
            meta: {unauthorizedAccess: true}
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('../views/LoginView.vue'),
            meta: {unauthorizedAccess: true}
        },
        {
            path: '/members/:id(\\d+)',
            name: 'profile',
            component: () => import('../views/ProfileView.vue'),
        },
        {
            path: '/account',
            name: 'account',
            component: () => import('../views/AccountSettingsView.vue'),
        },
        {
            path: '/your-groups',
            name: 'user_groups',
            component: () => import('../views/ListGroupsOfUserView.vue'),
        },
        {
            path: '/groups/create',
            name: 'create_group',
            component: () => import('../views/GroupCreateView.vue'),
        },
        {
            path: '/password/reset/confirm/:uid/:token',
            name: 'password_reset',
            component: () => import('../views/ResetPasswordView.vue'),
            meta: {unauthorizedAccess: true}
        },
        {
            path: '/groups/:id(\\d+)',
            name: 'group',
            component: () => import('../views/GroupView.vue'),
        },
        {
            path: '/meetings/create',
            name: 'create_meetings',
            component: () => import('../views/MeetingCreateView.vue'),
            beforeEnter: (to, from, next) => {
                if (from.name !== 'user_groups') {
                    return next({name: from.name})
                }
                return next(true)
            }
        }
    ]
})

router.beforeEach((to, from) => {
    const isUnauthorizedAccessAllowed = to.meta?.unauthorizedAccess === true;
    if (!localStorage.getItem('access') && !isUnauthorizedAccessAllowed) {
        return {name: 'login'}
    }
})

export default router
