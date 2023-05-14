<script setup>
import ResetButton from "@/components/buttons/ResetButton.vue";
import {default as CreateButton} from "@/components/buttons/OrangeButton.vue"
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
        <w-form
                v-model="form.valid"
                v-model:errors-count="form.errorsCount"
                @validate="onValidate"
                @submit.prevent="submitForm">
            <w-input
                    label="Название"
                    class="mb5"
                    v-model="form.title"
                    :validators="[validators.required]">
            </w-input>
            <w-input
                    label="Город проведения мероприятий группы"
                    class="mb5"
                    v-model="form.city"
                    :validators="[validators.required]">
            </w-input>
            <div class="body mb2">Темы для группы</div>
            <div class="checkbox-content">
                <w-checkboxes color="deep-orange" v-model="form.categories" :items="categories" round
                              inline></w-checkboxes>
            </div>
            <w-textarea
                    rows="4"
                    no-autogrow
                    resizable
                    label="Описание"
                    class="my5"
                    v-model="form.description"
            >
            </w-textarea>

            <w-flex wrap align-center>
                <CreateButton>Создать</CreateButton>
                <ResetButton @click="form.submitted = form.sent = false"/>
            </w-flex>
        </w-form>
    </w-card>


</template>

<script>
import {createGroup, getCategories} from "@/services/groupApi";
import {mapState} from "pinia";
import {useAuthStore} from "@/stores/auth";

export default {
    name: "GroupCreateForm",
    created() {
        this.loadCategories()
    },
    data() {
        return {
            categories: [],
            message: '',
            form: {
                title: '',
                city: '',
                description: '',
                categories: [],
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
    computed: {
        ...mapState(useAuthStore, ['user']),
    },
    methods: {
        onValidate() {
            this.form.sent = false
            this.form.submitted = this.form.errorsCount === 0
        },
        async loadCategories() {
            let response = await getCategories()
            response = response.data.results
            for (let i = 0; i < response.length; i++) {
                this.categories.push({label: response[i].title, value: response[i].id})
            }
        },
        async submitForm() {
            const formData = {
                title: this.form.title,
                city: this.form.city,
                description: this.form.description,
                categories: this.form.categories,
                users: [{
                    user_id: this.user.id,
                    role: 'admin'
                }],
            };
            const response = await createGroup(formData);
            if (response) {
                console.log(response.id)
                this.message = `Группа успешно создана.
                Сейчас вы будете перенаправлены на страницу группы ${response.title}`
                setTimeout(this.$router.push, 2000, {name: "group", params: {id: response.id}})
            }
        }
    }
}
</script>

<style scoped>
.checkbox-content {
    width: 500px;
}
</style>