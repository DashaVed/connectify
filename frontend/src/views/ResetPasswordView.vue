<script setup>
import Navbar from "@/containers/Navbar.vue"
import {default as SaveButton} from "@/components/buttons/OrangeButton.vue"
</script>

<template>
    <Navbar/>
    <div class="box justify-center align-self-center mt12">
        <w-card content-class="pa0">
            <w-alert
                    v-if="message"
                    error
                    no-border
                    class="my0 text-light">
                {{ message }}
            </w-alert>
            <w-form v-model="form.valid"
                @submit.prevent="submitForm"
                    class="px8 pt2 pb8">
                <div class="title2 text-center text-bold mt4 mb8">Сбросить пароль</div>
                <w-input
                        required
                        v-model="form.password"
                        class="mt4"
                        label="Новый пароль"
                        :type="isPassword ? 'password' : 'text'"
                        :inner-icon-right="isPassword ? 'mdi mdi-eye-off' : 'mdi mdi-eye'"
                        @click:inner-icon-right="isPassword = !isPassword">
                </w-input>
                <w-input
                        required
                        v-model="form.password2"
                        class="mt4"
                        label="Повторите пароль"
                        :type="isPassword ? 'password' : 'text'"
                        :inner-icon-right="isPassword ? 'mdi mdi-eye-off' : 'mdi mdi-eye'"
                        :validators="[validators.passwordsAccess]"
                        @click:inner-icon-right="isPassword = !isPassword">
                </w-input>
                <w-flex justify-center class="mt4">
                    <SaveButton class="mt6">Сменить пароль</SaveButton>
                </w-flex>
            </w-form>
        </w-card>
    </div>
</template>

<script>
import {resetPasswordConfirm} from "@/services/userApi";

export default {
    name: "ResetPasswordView",
    data() {
        return {
            message: null,
            isPassword: true,
            form: {
                valid: null,
                password: '',
                password2: '',
            },
            validators: {
                passwordsAccess: (value) => this.form.password === value || 'Пароли не совпадают',
            }
        }
    },
    methods: {
        async submitForm() {
            const formData = {
                uid: this.$route.params.uid,
                token: this.$route.params.token,
                new_password: this.form.password,
                re_new_password: this.form.password2,
            }
            const response = resetPasswordConfirm(formData)
            if (response.status === 400) {
                this.message = 'Попробуйте еще раз.'
            } else {
                this.$router.push({name: 'login'})
            }
        }
    }
}
</script>

<style scoped>
.box {
    max-width: 800px;
}
</style>