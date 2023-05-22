<script setup>
import formatDate from "@/services/services";
import MeetingCard from "@/components/MeetingCard.vue";
</script>

<template>

  <div class="title2 text-center">Мероприятия групп</div>
  <div v-if="isLoading">
    <div class="box today" v-if="!dateInput || dateInput === new Date()">
      <div class="title3 my4">Сегодня</div>
      <MeetingCard :meetings="todayMeetings" :date-input="dateInput" />
      <div class="box days">
        <div class="title3 my4">Ближайшие дни</div>
        <MeetingCard :meetings="meetings" :date-input="dateInput" />
      </div>
    </div>

    <div class="box next-days" v-else>
      <div class="title3 my4">{{ formatDate(dateInput) }}</div>
      <MeetingCard :meetings="getDayMeeting()" :date-input="dateInput" />
    </div>


  </div>
</template>

<script>
import { getUserMeeting } from "@/services/meetingApi";
import { mapState } from "pinia";
import { useAuthStore } from "@/stores/auth";

export default {
  name: "MeetingListInHome",
  async created() {
    await this.getListOfMeetings();
  },
  props: ["dateInput"],
  data() {
    return {
      meetings: [],
      isLoading: false,
      todayMeetings: []
    };
  },
  computed: {
    ...mapState(useAuthStore, ["user"])
  },
  methods: {
    getDayMeeting() {
      let meetings = [];
      for (const meeting of this.meetings) {
        const date = new Date(meeting.date).setHours(0, 0, 0, 0);
        if (date === this.dateInput.setHours(0, 0, 0, 0)) {
          meetings.push(meeting);
        }
      }
      return meetings;
    },
    async getListOfMeetings() {
      this.isLoading = false;
      const response = await getUserMeeting(this.user.id);
      const today = new Date().setHours(0, 0, 0, 0);
      if (response.data) {
        for (const meeting of response.data.results) {
          const date = new Date(meeting.date).setHours(0, 0, 0, 0);
          if (date === today) {
            this.todayMeetings.push(meeting);
          } else {
            this.meetings.push(meeting);
          }
        }
      }
      this.isLoading = true;
    }
  }


};
</script>

<style scoped>

</style>