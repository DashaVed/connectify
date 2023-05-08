<script setup>
import GroupForm from '@/containers/forms/GroupCreateForm.vue'
import Navbar from '@/containers/Navbar.vue'
</script>

<template>
    <Navbar/>
    <main class="mt4 pa6">
        <div class="title2 mb4 text-center">Создайте собственную группу!</div>
        <div class="mb4">Для того, чтобы создать группу, заполните форму ниже
            <w-icon color="deep-orange">mdi mdi-arrow-down-right</w-icon></div>
        <GroupForm/>
    </main>
</template>

<script>
export default {
    name: "GroupCreateView"
}
</script>

<style scoped>

</style>