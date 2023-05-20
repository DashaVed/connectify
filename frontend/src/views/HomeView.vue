<script setup>
import { DatePicker } from "v-calendar";
import "v-calendar/style.css";
import Navbar from "@/containers/Navbar.vue";
import MeetingListInHome from "@/containers/MeetingListInHome.vue";
</script>

<template>
  <Navbar />
  <main class="pa12">
    <div class="title1 px12">Добро пожаловать!</div>
    <w-flex wrap>
      <div class="xs4 pa12">
        <DatePicker :attributes="attributes" :min-date="new Date()"
                    color="orange" v-model="attributes.dates" class="my12" />
      </div>
      <div class="xs8 pa12">
        <MeetingListInHome :date-input="attributes.dates" />
      </div>
    </w-flex>
  </main>
</template>

<script>
export default {
  name: "HomeView",
  data() {
    return {
      attributes: [
        {
          key: "today",
          dates: new Date(),
          highlight: {
            color: "gray",
            fillMode: "outline"
          }
        }
      ]

    };
  }
};
</script>

<style scoped>

</style>