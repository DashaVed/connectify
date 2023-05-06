<script setup>
import {default as SaveButton} from "@/components/buttons/OrangeButton.vue"
</script>

<template>
    <div class="box pa4" v-if="isLoading">
        <span class="title4">Управление учетной записью</span>
        <form method="post" class="my5">
            <w-input
                    type="email"
                    class="my4"
                    label="Email"
                    outline>
            </w-input>
            <SaveButton class="mt2 mb4">Сохранить</SaveButton>
        </form>
        <span class="title4 mt6">Смена пароля</span>
        <form method="post" class="my5">
            <w-input
                    required outline
                    label="Старый пароль"
                    :type="isPassword ? 'password' : 'text'"
                    :inner-icon-right="isPassword ? 'mdi mdi-eye-off' : 'mdi mdi-eye'"
                    @click:inner-icon-right="isPassword = !isPassword">
            </w-input>
            <w-input
                    required outline
                    class="mt4"
                    label="Новый пароль"
                    :type="isPassword ? 'password' : 'text'"
                    :inner-icon-right="isPassword ? 'mdi mdi-eye-off' : 'mdi mdi-eye'"
                    @click:inner-icon-right="isPassword = !isPassword">
            </w-input>
            <w-input
                    required outline
                    class="mt4"
                    label="Повторите пароль"
                    :type="isPassword ? 'password' : 'text'"
                    :inner-icon-right="isPassword ? 'mdi mdi-eye-off' : 'mdi mdi-eye'"
                    @click:inner-icon-right="isPassword = !isPassword">
            </w-input>
            <SaveButton class="mt6">Сменить пароль</SaveButton>
        </form>
    </div>
</template>

<script>
import {getUser} from "@/services/api";
import {BASE_URL} from "@/services/consts";
import {mapState} from "pinia";
import {useAuthStore} from "@/stores/auth";

export default {
    name: "UserAuthEditForm",
    async created() {
        await this.load();
    },
    data() {
        return {
            user: null,
            isLoading: false,
            isPassword: true,
        }
    },
    methods: {
        async load() {
            this.isLoading = false;
            this.user = await getUser();
            this.isLoading = true;
        },
    }
}
</script>

<style scoped>
.label {
    color: #234781;
}
</style>