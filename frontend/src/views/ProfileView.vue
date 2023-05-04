<script setup>
import Navbar from "@/containers/Navbar.vue";
import UserInfo from "@/containers/UserInfo.vue"
import UserGroups from "@/containers/UserGroups.vue"
</script>

<template>
    <Navbar/>
    <w-button @click="logout">
        logout
    </w-button>
    <w-flex wrap gap="2">
    <UserInfo/>
    <UserGroups/>
    </w-flex>

</template>

<script>
import {useAuthStore} from "@/stores/auth";
import {mapActions} from "pinia";

export default {
    name: "ProfileView",
    methods: {
        ...mapActions(useAuthStore, ['logout']),
    }
}
</script>

<style scoped>

</style>