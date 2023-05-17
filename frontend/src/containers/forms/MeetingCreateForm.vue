<script setup>
import {default as CreateButton} from "@/components/buttons/OrangeButton.vue";
import ResetButton from "@/components/buttons/ResetButton.vue";
</script>

<template>
    <w-card class="pa8">
        <div class="message-box">
            <w-transition-fade>
                <w-alert sm
                         v-if="message"
                         success
                         no-border
                         class="text-light mb8">
                    {{ message }}
                </w-alert>
            </w-transition-fade>
        </div>
        <div>{{ param1 }}</div>
        <w-form
                v-model="form.valid"
                v-model:errors-count="form.errorsCount"
                @validate="onValidate"
                @submit.prevent="submitForm">
            <w-input
                    label="Заголовок"
                    class="mb5"
                    v-model="form.title"
                    :validators="[validators.required]">
            </w-input>
            <w-flex class="my5">
                <div class="body mr4">Это онлайн мероприятие?</div>
                <w-switch class="mr6" color="deep-orange" thin v-model="form.is_online"></w-switch>
            </w-flex>
            <w-input v-if="!form.is_online"
                    label="Место проведения мероприятия"
                    class="mb5"
                    v-model="form.location"
                    :validators="[validators.required]"/>
            <w-input v-if="form.is_online"
                     label="Место проведения мероприятия"
                     class="mb5"
                     v-model="form.location"
                     disabled/>
            <w-textarea
                    rows="4"
                    no-autogrow
                    resizable
                    label="Описание"
                    class="my5"
                    v-model="form.description"
            >
            </w-textarea>
            <div class="body mt5">Дата и время проведения</div>
            <w-input
                    type="datetime-local"
                    v-model="form.date"
                    class="mb5"
                    :validators="[validators.required]">
            </w-input>

            <w-flex wrap align-center>
                <CreateButton>Создать</CreateButton>
                <ResetButton @click="form.submitted = form.sent = false"/>
            </w-flex>
        </w-form>
    </w-card>
</template>

<script>
import {mapState} from "pinia";
import {useAuthStore} from "@/stores/auth";
import {createMeeting} from "@/services/meetingApi";

export default {
    name: 'MeetingForm',
    data() {
        return {
            message: '',
            form: {
                title: '',
                location: '',
                description: '',
                is_online: false,
                date: '',
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
    props: ['param1'],
    computed: {
        ...mapState(useAuthStore, ['user']),
        groupId() {
            return parseInt(this.$route.query.group)
        },
    },
    methods: {
        onValidate() {
            this.form.sent = false
            this.form.submitted = this.form.errorsCount === 0
        },
        async submitForm() {
            if (this.form.is_online) {
                this.form.location = "";
            }
            const formData = {
                title: this.form.title,
                location: this.form.location,
                description: this.form.description,
                is_online: this.form.is_online,
                date: this.form.date,
                users: [{
                    user_id: this.user.id,
                    role: 'admin'
                }],
                group_id: this.groupId
            };
            const response = await createMeeting(formData);
            if (response) {
                this.message = `Встреча успешно создана.
                Сейчас вы будете перенаправлены на её страницу ${response.title}`
                setTimeout(this.$router.push, 2000, {name: "meeting", params: {id: response.id}})
            }
        },
    }
}
</script>

<style scoped>

</style>