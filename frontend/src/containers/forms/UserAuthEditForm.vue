<script setup>
import {default as SaveButton} from "@/components/buttons/OrangeButton.vue"
</script>

<template>
    <div class="box pa4" v-if="isLoading">
        <span class="title4">Управление учетной записью</span>

        <w-alert
                v-if="formEmail.isSuccess === true"
                success
                no-border
                class="my3 text-light">
            {{ formEmail.message }}
        </w-alert>
        <w-alert
                v-if="formEmail.isSuccess === false"
                error
                no-border
                class="my3 text-light">
            {{ formEmail.message }}
        </w-alert>

        <w-form method="post" class="my5"
                v-model="formEmail.valid"
                @submit.prevent="submitEmailForm">
            <w-input
                    type="email"
                    class="my4"
                    label="Email"
                    v-model="user.email"
                    :validators="[validators.required]"
                    outline>
            </w-input>
            <SaveButton class="mt2 mb4" :disabled="formEmail.valid === false">Сохранить</SaveButton>
        </w-form>

        <span class="title4 mt6">Смена пароля</span>

        <w-alert
                v-if="formPassword.isSuccess === true"
                success
                no-border
                class="my3 text-light">
            {{ formPassword.message }}
        </w-alert>
        <w-alert
                v-if="formPassword.isSuccess === false"
                error
                no-border
                class="my3 text-light">
            {{ formPassword.message }}
        </w-alert>

        <w-form class="my5"
                v-model="formPassword.valid"
                @submit.prevent="submitPasswordForm">
            <w-input
                    required outline
                    label="Старый пароль"
                    :type="isPassword ? 'password' : 'text'"
                    :inner-icon-right="isPassword ? 'mdi mdi-eye-off' : 'mdi mdi-eye'"
                    @click:inner-icon-right="isPassword = !isPassword"
                    :validators="[validators.required]"
                    v-model="formPassword.old_password"
            >
            </w-input>
            <w-input
                    required outline
                    class="mt4"
                    label="Новый пароль"
                    :type="isPassword ? 'password' : 'text'"
                    :inner-icon-right="isPassword ? 'mdi mdi-eye-off' : 'mdi mdi-eye'"
                    @click:inner-icon-right="isPassword = !isPassword"
                    :validators="[validators.required]"
                    v-model="formPassword.new_password"

            >
            </w-input>
            <w-input
                    required outline
                    class="mt4"
                    label="Повторите пароль"
                    :type="isPassword ? 'password' : 'text'"
                    :inner-icon-right="isPassword ? 'mdi mdi-eye-off' : 'mdi mdi-eye'"
                    @click:inner-icon-right="isPassword = !isPassword"
                    :validators="[validators.passwordsAccess]"
                    v-model="formPassword.re_new_password"
            >
            </w-input>
            <SaveButton class="mt6" :disabled="formPassword.valid === false">Сменить пароль</SaveButton>
        </w-form>
    </div>
</template>

<script>
import {changePassword, getUser, updateUser} from "@/services/api";

export default {
    name: "UserAuthEditForm",
    async created() {
        await this.load();
    },
    data() {
        return {
            user: null,
            formEmail: {
                valid: null,
                isSuccess: null,
                message: '',
            },
            formPassword: {
                old_password: "",
                new_password: "",
                re_new_password: "",
                valid: null,
                isSuccess: null,
                message: '',
            },
            isLoading: false,
            isPassword: true,
            validators: {
                required: value => !!value || 'Поле обязательно для заполнения',
                passwordsAccess: (value) => this.formPassword.new_password === value || 'Пароли не совпадают',
            }
        }
    },
    methods: {
        async load() {
            this.isLoading = false;
            this.user = await getUser();
            this.isLoading = true;
        },
        async submitEmailForm() {
            try {
                await updateUser({email: this.user.email});
                this.formEmail.message = 'Email успешно обновлен.'
                this.formEmail.isSuccess = true;
            } catch (e) {
                this.formEmail.message = 'Неправильно заполнено поле. Попробуйте еще раз.';
                this.formEmail.isSuccess = false;
            }
        },
        async submitPasswordForm() {
            if (this.formPassword.new_password !== this.formPassword.re_new_password) {
                return
            }
            const formData = {
                old_password: this.formPassword.old_password,
                new_password: this.formPassword.new_password,
            }
            try {
                await changePassword(formData)
                this.formPassword.message = 'Пароль успешно обновлен.'
                this.formPassword.isSuccess = true;
            }
            catch (e) {
                this.formPassword.message = e;
                this.formPassword.isSuccess = false;
            }
        },
    }
}
</script>

<style scoped>
.label {
    color: #234781;
}
</style>