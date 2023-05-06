<script setup>
import HeaderOnlyWithTitle from "@/components/HeaderOnlyWithTitle.vue";
import LoginLink from "@/components/Links/LoginLink.vue";
import RegisterButton from "@/components/buttons/OrangeButton.vue";
</script>

<template>
    <header>
        <HeaderOnlyWithTitle>
            <div v-if="!isAuth">
                <LoginLink/>
                <RegisterButton route="/register">Зарегистрироваться</RegisterButton>
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
                                color="deep-orange"
                                class="pb1">mdi mdi-chevron-up
                        </w-icon>
                    </template>
                    <w-toolbar shadow content-class="pa10">
                        <w-grid columns="1">
                            <router-link to="/" class="menu-link">Ваши мероприятия</router-link>
                            <router-link to="/" class="menu-link">Ваши группы</router-link>
                            <w-divider class="ma3"/>
                            <router-link :to="{name: 'profile', params: {id: user.id}}" class="menu-link">Посмотреть профиль</router-link>
                            <router-link :to="{name: 'account'}" class="menu-link">Настройки</router-link>
                            <w-divider class="ma3"/>
                            <router-link to="/" class="menu-link">Выйти</router-link>
                        </w-grid>
                    </w-toolbar>
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