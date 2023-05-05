import {defineStore} from 'pinia'
import {login as apiLogin, refreshUserToken, getProfile} from "@/services/api";
import {useTokenStore} from "@/stores/token";

export const useAuthStore = defineStore('auth', {
    state: () => {
        return {
            user: null,
            token: useTokenStore()
        }
    },
    getters: {
        isAuth() {
            return this.user !== null;
        }
    },
    actions: {
        async login(email, password) {
            try {
                localStorage.removeItem('access')
                localStorage.removeItem('refresh')

                const response = await apiLogin(email, password);
                this.token.setAccess(response.access)
                this.token.setRefresh(response.refresh)

                localStorage.setItem('access', response.access)
                localStorage.setItem('refresh', response.refresh)

                await this.load()
            } catch (e) {
                throw new Error(e.message)
            }
        },
        async load() {
            try {
                this.user = await getProfile()
            } catch(e) {
                throw new Error(e.message)
            }
            if (!this.user) {
                this.logout();
            }
        },
        async refreshToken() {
            if (localStorage.getItem('access')) {
                const access = await refreshUserToken(localStorage.getItem('refresh'))

                this.token.setAccess(access)
                localStorage.setItem('access', access)
            } else {
                console.log('refresh token does not exist')
            }

        },
        logout() {
            localStorage.removeItem('access')
            localStorage.removeItem('refresh')
            this.token.removeAccess()
            this.token.removeRefresh()

            this.user = null
        }
    },
});