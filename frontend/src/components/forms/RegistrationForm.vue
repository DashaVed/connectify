<template>
    <w-card content-class="pa0">
        <div class="message-box">
            <w-transition-fade>
                <w-alert
                        v-if="form.submitted"
                        success
                        no-border
                        class="my0 text-light">
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
                @success="onSuccess"
                class="px8 pt2 pb12">
            <div class="title2 text-center text-bold">Регистрация</div>
            <div class="title4 m2 text-center">Уже есть аккаунт?</div>

            <w-input
                    required
                    label="Имя"
                    :validators="[validators.required]">
            </w-input>

            <w-input
                    required
                    label="Фамилия"
                    :validators="[validators.required]"
                    class="mt3">
            </w-input>

            <w-input
                    required
                    label="Email"
                    type="email"
                    :validators="[validators.required]"
                    class="mt3">
            </w-input>

            <w-input
                    required
                    class="mt3"
                    label="Пароль"
                    :type="isPassword ? 'password' : 'text'"
                    :inner-icon-right="isPassword ? 'mdi mdi-eye-off' : 'mdi mdi-eye'"
                    @click:inner-icon-right="isPassword = !isPassword">
            </w-input>

            <w-flex wrap align-center justify-end class="mt4">

                <w-button md
                    color="white"
                    bg-color="indigo-dark6"
                        type="submit"
                        :disabled="form.valid === false"
                        :loading="form.submitted && !form.sent"
                        class="my5">
                    Зарегистрироваться
                </w-button>

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

        <w-notification
                class="mt3"
                v-model="form.sent"
                success
                transition="bounce"
                absolute
                plain
                bottom>
            Вы успешно зарегистрированы!
        </w-notification>
    </w-card>
</template>

<script>
export default {
    name: "RegistrationForm",
    data: () => ({
        isPassword: true,
        form: {
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
        onSuccess() {
            setTimeout(() => (this.form.sent = true), 2000)
        },
        onValidate() {
            this.form.sent = false
            this.form.submitted = this.form.errorsCount === 0
        }
    }
}
</script>

<style scoped>
.message-box {
    min-height: 35px;
}
</style>