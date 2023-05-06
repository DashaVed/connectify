<script setup>
import Navbar from "@/containers/Navbar.vue";
import UserEditForm from "@/containers/forms/UserEditForm.vue";
import UserAuthEditForm from "@/containers/forms/UserAuthEditForm.vue";
</script>

<template>
    <Navbar/>
    <main class="grow pa4">
        <w-tabs :items="tabs">
            <template #item-title="{ item }">
                <span class="title4">{{ item.title }}</span>
            </template>
            <template #item-content.1="{ item }">
                <UserEditForm/>
            </template>
            <template #item-content.2="{ item }">
                <UserAuthEditForm/>
            </template>
        </w-tabs>
    </main>
</template>

<script>
export default {
    name: "AccountSettingsView",
    data() {
        return {
            tabs: [
                {title: 'Редактирование профиля'},
                {title: 'Управление аккаунтом'},
            ]
        }
    }
}
</script>

<style scoped>

</style>