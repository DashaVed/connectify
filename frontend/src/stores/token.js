import {defineStore} from 'pinia'

export const useTokenStore = defineStore('token', {
    state: () => {
        return {
            access: '',
            refresh: '',
        }
    },
    actions: {
        initializeTokenStore(state) {
            if (localStorage.getItem('access')) {
                state.access = localStorage.getItem('access');
                state.refresh = localStorage.getItem('refresh')
            } else {
                state.access = '';
            }
        },
        setAccess(state, access) {
            state.access = access;
        },
        setRefresh(state, refresh) {
            state.refresh = refresh
        },
        removeAccess(state) {
            state.access = '';
        },
        removeRefresh(state) {
            state.refresh = ''
        },
    }
})