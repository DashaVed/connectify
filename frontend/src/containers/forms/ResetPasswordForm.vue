<script setup>
import {default as SendButton} from "@/components/buttons/OrangeButton.vue"

</script>

<template>
    <w-overlay
            v-model="showOverlay"
            :persistent="true"
            :persistent-no-animation="true"
            :opacity="0.3">
        <w-card bg-color="white" class="pa4 card-overflow">
            <w-icon class="mr2 close-icon" lg @click="$emit('update:modelValue', $event.target.value)">wi-cross</w-icon>
            <div class="title2 text-center">Сбросить пароль</div>
            <div class="body my6">Если вы забыли пароль, то вы можете его сбросить.
                Для этого введите свой e-mail
            </div>
            <div class="message-box">
                <w-transition-fade>
                    <w-alert
                            v-if="form.isSent && form.isSuccess === false"
                            error
                            no-border
                            class="mb4 body text-light">
                        {{ message }}
                    </w-alert>

                    <w-alert
                            v-if="form.isSent && form.isSuccess === true"
                            success
                            no-border
                            class="mb4 body text-light">
                        {{ message }}
                    </w-alert>
                </w-transition-fade>
            </div>

            <w-form>
                <w-input
                        required
                        v-model="form.email"
                        label="Введите e-mail"
                        type="email"
                        class="mb8"
                        :validators="[valids.required]"
                @click="">
                </w-input>
                <w-flex wrap align-center justify-center>
                    <SendButton class="ml4"
                                :disabled="form.email===''"
                                @click="submitForm">Отправить
                    </SendButton>
                </w-flex>
            </w-form>
        </w-card>
    </w-overlay>
</template>

<script>
import {resetPassword} from "@/services/userApi";

export default {
    name: 'ResetPasswordForm',
    data() {
        return {
            message: '',
            form: {
                email: '',
                isSent: false,
                isSuccess: null,
            },
        }
    },
    props: ['valids'],
    methods: {
        async submitForm() {
            const response = await resetPassword(this.form.email)
            this.form.isSent = true
            if (response.status !== 400) {
                this.form.isSuccess = true
                this.message = `На почту ${this.form.email} отправлено сообщение.
                Для сброса пароля следуйте инструкции в сообщении. Если сообщение не пришло,
                то проверьте правильность набранной почты`
            } else {
                this.form.isSuccess = false
                this.message = 'Вы ввели неправильную почту. Попробуйте еще раз.'
            }
        }
    }
}
</script>

<style scoped>
.card-overflow {
    width: 600px;
}

.close-icon:hover, .close-icon:focus, .close-icon:active {
    color: #ff6825;
}
</style>