<script setup>
import {default as SaveButton} from "@/components/buttons/OrangeButton.vue"
</script>

<template>
    <div class="box pa4" v-if="isLoading">
        <w-form method="post" class="my5"
                v-model="form.valid"
                v-model:errors-count="form.errorsCount"
                @validate="onValidate"
                @submit.prevent="submitForm">
            <w-flex align-center>
                <w-image :src="user.image" height="160" width="160" class="mr12"></w-image>
                <w-flex column>
                    <label class="my3">Загрузите изображение</label>
                    <w-input
                            v-model="userImage"
                            type="file"
                            accept=".jpg, .jpeg, .png, .gif, .svg" outline shadow
                    @change="onImageSelect">
                    </w-input>
                </w-flex>
            </w-flex>

            <w-input
                    class="mt8 mb4"
                    label="Имя"
                    v-model="user.name"
                    :validators="[validators.required]"
                    outline>
            </w-input>
            <w-input
                    class="mb4"
                    label="Город"
                    v-model="user.city"
                    :validators="[validators.required]"
                    outline>
            </w-input>
            <w-textarea
                    rows="4"
                    no-autogrow
                    label="Напишите пару слов о себе"
                    class="mb5"
                    v-model="user.description"
                    outline>
            </w-textarea>

            <span class="title4">Дополнительная информация</span>
            <div class="mt3 ml2 label body">Пол</div>
            <w-radios
                    color="deep-orange"
                    class="mb9 ml2"
                    v-model="user.gender"
                    :items="genders">
            </w-radios>
            <w-input
                    type="date"
                    label="Дата рождения"
                    v-model="user.birthday"
                    outline
                    :validators="[validators.dateValidate]">
            </w-input>
            <SaveButton class="mt6"
                        :disabled="form.valid === false">Сохранить
            </SaveButton>
        </w-form>
        <w-alert
                v-if="form.isSuccess === true"
                success
                no-border
                class="my0 text-light">
            {{ message }}
        </w-alert>

    </div>
</template>

<script>
import {getUser, updateUser} from "@/services/api";

export default {
    name: "UserEditForm",
    async created() {
        await this.load();
    },
    data() {
        return {
            user: null,
            userImage: '',
            isLoading: false,
            message: '',
            genders: [
                {label: 'Не указывать', value: ''},
                {label: 'Женский', value: 'f'},
                {label: 'Мужской', value: 'm'},
            ],
            form: {
                isSuccess: null,
                errorsCount: 0,
                valid: null,
            },
            validators: {
                required: value => !!value || 'Поле обязательно для заполнения',
                dateValidate: (value) => this.dateIsValid(value) === true ||
                    'Нeправильная дата. Она должна быть формата mm-dd-yyyy',
            }
        }
    },
    methods: {
        onValidate() {
            this.form.sent = false
            this.form.submitted = this.form.errorsCount === 0
        },
        onImageSelect(event) {
            this.userImage = event.target.files[0];
        },
        dateIsValid(dateStr) {
            const regex = /^\d{4}-\d{2}-\d{2}$/;
            if (dateStr.match(regex) === null) {
                this.form.valid = false;
                return false;
            }
            return true;
        },
        async load() {
            this.isLoading = false;
            this.user = await getUser();
            this.isLoading = true;
        },
        async submitForm() {
            const userData = new FormData()
            userData.append('name', this.user.name)
            userData.append('city', this.user.city)
            userData.append('description', this.user.description)
            userData.append('gender', this.user.gender)
            userData.append('birthday', this.user.birthday)
            if (this.userImage) {
                userData.append('image', this.userImage)
            }
            try {
                await updateUser(userData);
                this.message = 'Данные успешно обновлены.'
                this.userImage = ''
                this.form.isSuccess = true;
            } catch (e) {
                this.message = 'Неправильно заполнены поля( Попробуйте еще раз.';
                this.form.isSuccess = false;
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