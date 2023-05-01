<script setup>
import RegisterButton from "@/components/buttons/RegisterButton.vue";
import ResetButton from "@/components/buttons/ResetButton.vue";
import LoginLink from "@/components/Links/LoginLink.vue";
</script>

<template>
    <w-card content-class="pa0">
        <div class="message-box">
            <w-transition-fade>
                <w-alert
                        v-if="form.isSuccess === true"
                        success
                        no-border
                        class="my0 text-light">
                    {{ message }}
                </w-alert>
                <w-alert
                        v-else-if="form.isSuccess === false"
                        error
                        no-border
                        class="my0 text-light">
                    {{ message }}
                </w-alert>
                <w-alert
                        v-else-if="form.valid === false"
                        error
                        no-border
                        class="my0 text-light">
                    Заполните все поля корректно
                </w-alert>
            </w-transition-fade>
        </div>

        <w-form
                v-model="form.valid"
                v-model:errors-count="form.errorsCount"
                @validate="onValidate"
                @submit.prevent="submitForm"
                class="px8 pt2 pb8">
            <div class="title2 text-center text-bold mb6">Регистрация</div>

            <w-input
                    required
                    label="Имя Фамилия"
                    v-model="form.name"
                    :validators="[validators.required]"
                    class="mb4">
            </w-input>

            <w-input
                    required
                    label="Город проживания"
                    v-model="form.city"
                    :validators="[validators.required]"
                    class="mb4">
            </w-input>

            <w-input
                    required
                    label="Email"
                    type="email"
                    v-model="form.email"
                    :validators="[validators.required]"
                    class="mb4">
            </w-input>

            <w-input
                    required
                    class="mt3"
                    label="Пароль"
                    v-model="form.password"
                    :type="isPassword ? 'password' : 'text'"
                    :inner-icon-right="isPassword ? 'mdi mdi-eye-off' : 'mdi mdi-eye'"
                    @click:inner-icon-right="isPassword = !isPassword">
            </w-input>

            <w-input
                    required
                    class="mt3"
                    label="Повторите пароль"
                    v-model="form.re_password"
                    :type="isPassword ? 'password' : 'text'"
                    :inner-icon-right="isPassword ? 'mdi mdi-eye-off' : 'mdi mdi-eye'"
                    :validators="[validators.passwordsAccess]"
                    @click:inner-icon-right="isPassword = !isPassword">
            </w-input>

            <w-flex wrap align-center justify-center class="mt4">
                <RegisterButton
                        :disabled="form.valid === false"
                        class="my5 pa4 "
                />
                <ResetButton @click="form.submitted = form.sent = false"/>
            </w-flex>
            <w-flex wrap align-center justify-center class="m2 mt3 text-center">
                <span class="body mr2">Уже есть аккаунт?</span>
                <LoginLink class="body deep-orange-dark3"/>
            </w-flex>
        </w-form>
    </w-card>
</template>

<script>
import {registerUser} from "@/services/api";

export default {
    name: "RegistrationForm",
    data() {
        return {
            isPassword: true,
            message: '',
            form: {
                name: '',
                city: '',
                email: '',
                password: null,
                re_password: null,
                valid: null,
                submitted: null,
                sent: false,
                isSuccess: null,
                errorsCount: 0
            },
            validators: {
                required: value => !!value || 'Поле обязательно для заполнения',
                passwordsAccess: (value) => this.form.password === value || 'Пароли не совпадают',
            }
        }
    },

    methods: {
        onValidate() {
            this.form.sent = false
            this.form.submitted = this.form.errorsCount === 0
        },
        async submitForm() {
            const formData = {
                name: this.form.name,
                city: this.form.city,
                email: this.form.email,
                password: this.form.password,
                re_password: this.form.re_password,
            };
            try {
                await registerUser(formData)
                this.form.isSuccess = true;
                this.message = 'Вы успешно зарегистрировались!'
                setTimeout(this.$router.push, 1500, {name: "login"})
            } catch (e) {
                this.form.isSuccess = false;
                this.message = e.message
            }
        }
    }
}
</script>

<style scoped>
.message-box {
    min-height: 35px;
    max-width: 400px;
}
</style>