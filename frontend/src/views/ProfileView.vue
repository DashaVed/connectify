<script setup>
import Navbar from "@/containers/Navbar.vue";
import UserInfo from "@/containers/UserInfo.vue"
import UserGroups from "@/containers/UserGroups.vue"
</script>

<template>
    <Navbar/>
    <w-flex wrap gap="2">
    <UserInfo/>
    <UserGroups/>
    </w-flex>

</template>

<script>
export default {
    name: "ProfileView",
}
</script>

<style scoped>

</style>