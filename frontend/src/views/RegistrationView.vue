<script>
import {register_user} from "@/services/api";
import RegisterButton from "@/components/buttons/RegisterButton.vue";

export default {
    name: "RegistrationView",
    components: {RegisterButton},
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

<template>
    <div class="box justify-center align-self-center mt10">
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
                class="px8 pt2 pb12">
            <div class="title2 text-center text-bold">Регистрация</div>
            <div class="title4 m2 text-center">Уже есть аккаунт?</div>

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
                    class="my5"
                />
                <w-button
                        text
                        type="reset"
                        @click="form.submitted = form.sent = false"
                        class="my1 mr2">
                    <w-icon>
                        mdi mdi-backspace-outline
                    </w-icon>
                </w-button>
            </w-flex>
        </w-form>
    </w-card>
    </div>
</template>

<style>
.w-card__content {
    max-width: 300px;
}
</style>
