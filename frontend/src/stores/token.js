import {defineStore} from 'pinia'

export const useTokenStore = defineStore('token', {
    state: () => {
        return {
            access: '',
            refresh: '',
        }
    },
    actions: {
        initializeTokenStore() {
            if (localStorage.getItem('access')) {
                this.access = localStorage.getItem('access');
                this.refresh = localStorage.getItem('refresh')
            } else {
                this.access = '';
            }
        },
        setAccess(access) {
            this.access = access;
        },
        setRefresh(refresh) {
            this.refresh = refresh
        },
        removeAccess() {
            this.access = '';
        },
        removeRefresh() {
            this.refresh = ''
        },
    }
})