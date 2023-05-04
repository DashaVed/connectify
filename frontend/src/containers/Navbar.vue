<script setup>
import HeaderOnlyWithTitle from "@/components/HeaderOnlyWithTitle.vue";
import LoginLink from "@/components/Links/LoginLink.vue";
import RegisterButton from "@/components/buttons/RegisterButton.vue";
</script>

<template>
    <header>
        <HeaderOnlyWithTitle>
            <div v-if="!isAuth">
                <LoginLink/>
                <RegisterButton md route="/register" class="pa4"/>
            </div>
            <div v-if="isAuth">
                <w-menu persistent align-right shadow custom class="mt6">
                    <template #activator="{ on }">
                        <span v-on="on"
                              @click="isMenuShow = !isMenuShow"
                              class="title3 mr2">{{ user.name }}</span>
                        <w-icon xl
                                v-on="on"
                                v-if="!isMenuShow"
                                @click="isMenuShow = !isMenuShow"
                                class="pb1">mdi mdi-chevron-down
                        </w-icon>
                        <w-icon xl
                                v-if="isMenuShow"
                                @click="isMenuShow = !isMenuShow"
                                class="pb1">mdi mdi-chevron-up
                        </w-icon>
                    </template>
                    <w-card content-class="pa4">
                        <w-grid columns="1">
                            <router-link to="/" class="menu-link">Ваши мероприятия</router-link>
                            <router-link to="/" class="menu-link">Ваши группы</router-link>
                            <w-divider class="ma3"/>
                            <router-link to="/" class="menu-link">Посмотреть профиль</router-link>
                            <router-link to="/" class="menu-link">Настройки</router-link>
                            <w-divider class="ma3"/>
                            <router-link to="/" class="menu-link">Выйти</router-link>
                        </w-grid>
                    </w-card>
                </w-menu>
            </div>
        </HeaderOnlyWithTitle>

    </header>
</template>

<script>
import {useAuthStore} from "@/stores/auth";
import {mapState} from "pinia";

export default {
    name: "Navbar",
    data() {
        return {
            isMenuShow: false,
        }
    },
    computed: {
        ...mapState(useAuthStore, ['user', 'isAuth']),
    }
}
</script>

<style scoped>
@import '@/assets/base.css';

.menu-link {
    color: var(--color-text);
}
.menu-link:hover, .menu-link:focus, .menu-link:active {
    color: var(--color-text-active);
}
</style>