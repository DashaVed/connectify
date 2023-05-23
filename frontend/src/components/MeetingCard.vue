<script setup>

import formatDate from "../services/services";
</script>

<template>
  <w-card tile v-for="meeting in meetings" :key="meeting.id"
          class="my2" v-if="meetings.length">
    <w-flex class="align-center">
      <div class="title4">{{ meeting.meeting_info.title }}</div>
      <w-tag v-if="meeting.meeting_info.is_online" class="ml4 pt10" width="4em"
             height="1.5em">online
      </w-tag>
    </w-flex>
    <div class="mt2 mb4">
      {{ formatDate(meeting.meeting_info.date, "D MMMM YYYY г. H:mm") }}
    </div>
    <w-flex class="justify-space-between">
      <div v-if="meeting.meeting_info.location">
        <w-icon color="deep-orange pb2">mdi mdi-city</w-icon>
        {{ meeting.meeting_info.location }}
      </div>
      <div v-else></div>
      <router-link class="body link"
                   :to="{name: 'meeting', params: {id: meeting.meeting}}">
        Посмотреть
      </router-link>
    </w-flex>
  </w-card>
  <div v-if="!meetings.length" class="body mb8">
    Нет совпадений
  </div>

</template>

<script>
export default {
  name: "MeetingCard",
  props: ["meetings"]
};
</script>

<style scoped>
.link {
  color: var(--color-text);
}

.link:hover, .link:focus, .link:active {
  color: var(--color-text-active);
}

</style>