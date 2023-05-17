<script setup>

import Navbar from "@/containers/Navbar.vue";
import MeetingForm from "@/containers/forms/MeetingCreateForm.vue";
</script>

<template>
    <Navbar/>
    <main class="mt4 pa6">
        <div class="title2 mb4 text-center">Создайте собственную встречу для
            <router-link :to="{name:'group', params:{id: groupId}}" class="link">группы</router-link>!</div>
        <div class="mb4">Для того, чтобы создать встречу, заполните форму ниже
            <w-icon color="deep-orange">mdi mdi-arrow-down-right</w-icon>
        </div>
        <MeetingForm/>
    </main>
</template>

<script>
export default {
    name: "MeetingCreateView",
    computed: {
        groupId() {
            return parseInt(this.$route.query.group)
        }
    }
}
</script>

<style scoped>
.link {
    color: var(--color-text);
    text-decoration: underline;
}

.link:hover, .link:focus, .link:active {
    color: var(--color-text-active);
}
</style>