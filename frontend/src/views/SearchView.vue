<script setup>

import Navbar from "@/containers/Navbar.vue";
import MeetingsTable from "@/containers/tables/MeetingsTable.vue";
</script>

<template>
  <Navbar />
  <main class="grow pa4 mt4">
    <w-tabs :items="tabs">
      <template #item-title="{ item }">
        <span class="title4">{{ item.title }}</span>
      </template>
      <template #item-content.1="{ item }">
        <MeetingsTable :search-data="queryParams" class="ma3" />
      </template>
      <template #item-content.2="{ item }">
      </template>
    </w-tabs>
  </main>
</template>

<script>
export default {
  name: "SearchView",
  data() {
    return {
      tabs: [
        { title: "Мероприятия" },
        { title: "Группы" }
      ]
    };
  },
  computed: {
    queryParams() {
      return this.$route.query.search || "";
    }
  },


};
</script>

<style scoped>

</style>