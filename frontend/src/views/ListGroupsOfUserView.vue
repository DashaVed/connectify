<script setup>
import Navbar from "@/containers/Navbar.vue";
import {default as CreateButton} from "@/components/buttons/OrangeButton.vue"
import UserGroupsTable from "@/containers/tables/UserGroupsTable.vue";
</script>

<template>
    <Navbar/>
    <div class="box py10 px12">
        <w-flex class="justify-space-between mb10">
            <div class="title1">Ваши группы</div>
            <CreateButton @click="$router.push('/groups/create')">Создать собственную группу</CreateButton>
        </w-flex>
        <UserGroupsTable/>
    </div>

</template>

<script>
export default {
    name: "ListGroupsOfUserView",
}
</script>

<style scoped>

</style>