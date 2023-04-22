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
            <div class="title2 text-center text-bold mb3">Регистрация</div>

            <w-input
                    required
                    label="Имя"
                    v-model="form.first_name"
                    :validators="[validators.required]">
            </w-input>

            <w-input
                    required
                    label="Фамилия"
                    v-model="form.last_name"
                    :validators="[validators.required]"
                    class="mt3">
            </w-input>

            <w-input
                    required
                    label="Город проживания"
                    v-model="form.city"
                    :validators="[validators.required]"
                    class="mt3">
            </w-input>

            <w-input
                    required
                    label="Email"
                    type="email"
                    v-model="form.email"
                    :validators="[validators.required]"
                    class="mt3">
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

            <w-flex wrap align-center justify-end class="mt4">
                <RegisterButton
                    :disabled="form.valid === false"
                    class="my5 pa4"
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
import {register_user} from "@/services/api";

export default {
    name: "RegistrationForm",
    data() {
        return {
            isPassword: true,
            message: '',
            form: {
                first_name: '',
                last_name: '',
                city: '',
                email: '',
                password: null,
                valid: null,
                submitted: null,
                sent: false,
                isSuccess: null,
                errorsCount: 0
            },
            validators: {
                required: value => !!value || 'Поле обязательно для заполнения',
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
                first_name: this.form.first_name,
                last_name: this.form.last_name,
                city: this.form.city,
                email: this.form.email,
                password: this.form.password,
            };
            const response = await register_user(formData);
            this.message = response.message;
            if (response.status === 'ok') {
                this.form.isSuccess = true;
                setTimeout(this.$router.push, 1500, {name: "login"})
            } else {
                this.form.isSuccess = false;
            }
        }
    }
}
</script>

<style scoped>
.message-box {
    min-height: 35px;
}
.w-card__content {
    max-width: 300px;
}
</style>