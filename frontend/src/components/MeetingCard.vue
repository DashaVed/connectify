<script setup>

import formatDate from "../services/services";
</script>

<template>
  <w-card tile v-for="meeting in meetings" :key="meeting.id"
          class="my2" v-if="meetings.length">
    <div class="title4">{{ meeting.title }}</div>
    <w-flex class="justify-space-between">
      <div v-if="meeting.location">
        <w-icon color="deep-orange pb2">mdi mdi-city</w-icon>
        {{ meeting.location }}
      </div>
      <w-tag v-else class="pt10" width="4em"
             height="1.5em">online
      </w-tag>
      <router-link class="body link"
                   :to="{name: 'meeting', params: {id: meeting.id}}">
        Посмотреть
      </router-link>
    </w-flex>
  </w-card>
  <div v-if="!meetings.length" class="body mb8">
    Нет совпадений на {{formatDate(dateInput)}}</div>

</template>

<script>
export default {
  name: "MeetingCard",
  props: ["meetings", "dateInput"]
};
</script>

<style scoped>
.link {
  color: var(--color-text);
}

.link:hover, .link:focus, .link:active {
  color: var(--color-text-active);
}

.link-route {
  text-decoration: underline;
}
</style>