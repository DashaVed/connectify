<script setup>
import ResetButton from "@/components/buttons/ResetButton.vue";
</script>

<template>
    <w-card content-class="pa0">
        <div class="message-box">
            <w-transition-fade>
                <w-alert
                        v-if="form.submitted"
                        success
                        no-border
                        class="my0 text-light body">
                    Все поля заполнены
                </w-alert>

                <w-alert
                        v-else-if="form.valid === false"
                        error
                        no-border
                        class="my0 text-light">
                    Заполните все поля корректно!
                </w-alert>
            </w-transition-fade>
        </div>

        <w-form
                v-model="form.valid"
                v-model:errors-count="form.errorsCount"
                @validate="onValidate"
                @submit.prevent="submitForm"
                class="px8 pt2 pb8">
            <div class="title2 text-center text-bold mb8">Авторизация</div>

            <w-input
                    required
                    v-model="form.email"
                    label="Email"
                    type="email"
                    :validators="[validators.required]"
                    class="mb8">
            </w-input>

            <w-input
                    required
                    class="mt3"
                    v-model="form.password"
                    label="Пароль"
                    :type="isPassword ? 'password' : 'text'"
                    :inner-icon-right="isPassword ? 'mdi mdi-eye-off' : 'mdi mdi-eye'"
                    @click:inner-icon-right="isPassword = !isPassword">
            </w-input>

            <w-flex wrap align-center justify-center class="mt4">

                <w-button md
                          color="white"
                          bg-color="deep-orange"
                          type="submit"
                          :disabled="form.valid === false"
                          class="title3 my5 ml3 pa3 pl6 pr6">
                    Войти
                </w-button>
                <ResetButton @click="form.submitted = form.sent = false"/>
            </w-flex>
            <w-flex wrap align-center justify-center class="m2 mt3 text-center">
                <span class="body mr2">Еще нет аккаунта?</span>
                <a href="/register" class="sign-up-link body deep-orange-dark3">
                    Создать</a>
            </w-flex>
        </w-form>
    </w-card>
</template>

<script>
import {useAuthStore} from "@/stores/auth";
import {mapActions} from "pinia";
import {nextTick} from "vue";

export default {
    name: "RegistrationForm",
    data: () => ({
        isPassword: true,
        form: {
            email: '',
            password: '',
            valid: null,
            submitted: false,
            sent: false,
            errorsCount: 0
        },
        validators: {
            required: value => !!value || 'Поле обязательно для заполнения',
        }
    }),

    methods: {
        ...mapActions(useAuthStore, ['login']),
        onValidate() {
            this.form.sent = false
            this.form.submitted = this.form.errorsCount === 0
        },
        async submitForm() {
            await this.login(this.form.email, this.form.password)
            await nextTick()
            // this.$router.push({name: "main"})
        }
    }
}
</script>

<style scoped>
.message-box {
    min-height: 35px;
}

.sign-up-link:hover {
    text-decoration: underline;
}
</style>