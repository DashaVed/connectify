import {defineStore} from 'pinia'
import {login as apiLogin, refreshUserToken} from "@/services/api";
import {useTokenStore} from "@/stores/token";

export const useAuthStore = defineStore('auth', {
    state: () => {
        return {
            error: null,
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
            this.error = null;
            try {
                localStorage.removeItem('access')
                localStorage.removeItem('refresh')

                const response = await apiLogin(email, password);
                this.token.setAccess(this.token, response.access)
                this.token.setRefresh(this.token, response.refresh)

                localStorage.setItem('access', response.access)
                localStorage.setItem('refresh', response.refresh)
            } catch (e) {
                throw new Error(e.message)
            }
        },
        async refreshToken() {
            console.log(this.token.access)
            if (this.token.access) {
                const access = await refreshUserToken(this.token.refresh)

                this.token.setAccess(this.token, access)
                localStorage.setItem('access', access)
            }

        },
        logout() {
            localStorage.removeItem('access')
            localStorage.removeItem('refresh')
            this.token.removeAccess(this.token)
            this.token.removeRefresh(this.token)
        }
    },
});