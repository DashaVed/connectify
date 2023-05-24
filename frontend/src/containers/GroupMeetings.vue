<script setup>

import formatDate from "../services/services";
</script>

<template>
  <div class="title3 my8 text-right">Текущие мероприятия</div>
  <w-flex v-if="meetings.length !== 0" column>
    <w-card tile v-for="meeting in meetings" class="meetings-content my3">
      <div class="title4 mb2">{{ meeting.title }}</div>
      <div>{{formatDate(meeting.date, "D MMMM YYYY г. H:mm")}}</div>
      <w-flex class="justify-space-between">
        <div v-if="meeting.location">
          <w-icon color="deep-orange pb2">mdi mdi-city</w-icon>
          {{ meeting.location }}
        </div>
        <div v-else></div>
        <router-link class="body link" :to="{name: 'meeting', params: {id: meeting.id}}">Посмотреть
        </router-link>
      </w-flex>
    </w-card>
  </w-flex>
  <div class="body pl5" style="width:300px;" v-else>На данный момент в этой группу нет мероприятий</div>

</template>

<script>
import { getGroupMeeting } from "@/services/meetingApi";

export default {
  name: "GroupMeetings",
  async created() {
    await this.getMeetings();
  },
  data() {
    return {
      meetings: []
    };
  },
  methods: {
    async getMeetings() {
      const response = await getGroupMeeting(this.$route.params.id);
      if (response.results) {
        this.meetings = response.results;
      }
    }
  }
};
</script>

<style scoped>


.link {
    color: var(--color-text);
    font-size: 12px;
}

.link:hover, .link:focus, .link:active {
    color: var(--color-text-active);
}
</style>