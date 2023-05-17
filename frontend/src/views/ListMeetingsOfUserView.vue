<script setup>
import Navbar from "@/containers/Navbar.vue";
import UserMeetingsTable from "@/containers/tables/UserMeetingsTable.vue";
</script>

<template>
    <Navbar/>
    <div class="box py10 px12">
        <div class="title1 mb10">Ваши встречи</div>
        <UserMeetingsTable/>
    </div>
</template>

<style scoped>

</style>