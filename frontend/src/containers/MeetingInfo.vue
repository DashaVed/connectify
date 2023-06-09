<script setup>
import formatDate from "@/services/services";
import { default as EnterButton } from "@/components/buttons/OrangeButton.vue";
import ExitButton from "@/components/buttons/ExitButton.vue";
</script>

<template>
  <div class="content mx12 my12" v-if="isLoading">
    <w-flex wrap gap="2" class="justify-space-between">
      <div class="box ml12 xs6">
        <div class="title1 text-bold">{{ meeting.title }}</div>
        <div class="title3 mt4 mb8">
          {{ formatDate(meeting.date, "D MMMM YYYY г. H:mm") }}
        </div>
        <div v-if="meeting.is_online">
          <w-icon color="deep-orange pb1 mr4" lg>mdi mdi-video</w-icon>
          Это онлайн мероприятие
        </div>
        <div class="body" v-if="meeting.location">
          <w-icon color="deep-orange pb1 mr4" lg>mdi mdi-map-marker</w-icon>
          {{ meeting.location }}
        </div>
        <div class="body my8">
          <w-icon color="deep-orange pb1 mr4" lg>mdi mdi-account-group</w-icon>
          Участников - {{ countUsers }}
        </div>
        <div class="title3">Про что встреча?</div>
        <p class="body my4">{{ meeting.description }}</p>
      </div>
      <div class="box mr12 xs3">
        <w-flex class=" mb10 justify-end">
          <EnterButton v-if="!isJoined" @click="addUser">Присоединиться к мероприятию</EnterButton>
          <ExitButton v-else-if="isJoined && user.id!==admin.id"
                      question="Отписаться от мероприятия?"
                      @confirm="exitUser">Вы участник мероприятия
          </ExitButton>
          <EnterButton disabled v-else>Вы организатор</EnterButton>
        </w-flex>
        <div class="title3 mt8  text-right">Группа</div>
        <w-card tile class="my3">
          <div class="title4 mb4">{{ meeting.group.title }}</div>
          <w-flex class="justify-space-between">
            <div>
              <w-icon color="deep-orange pb2">mdi mdi-city</w-icon>
              {{ meeting.group.city }}
            </div>
            <router-link class="body link" :to="{name: 'group',
            params: {id: meeting.group.id}}">Посмотреть
            </router-link>
          </w-flex>
        </w-card>
        <div class="title3 my8 text-right">Организатор</div>
        <router-link :to="{name: 'profile', params: {id: admin.id}}">
          <div class="body link text-right" style="font-size: 16px">{{ admin.name }}</div>
        </router-link>
        <router-link :to="{name: 'chat', params: {id: admin.id}, query: {username: admin.name}}">
          <div class="body link text-right" style="font-size: 16px">Написать</div>
        </router-link>
      </div>
    </w-flex>

  </div>
</template>

<script>
import { addUserToMeeting, deleteUserFromMeeting, getMeeting } from "@/services/meetingApi";
import { mapState } from "pinia";
import { useAuthStore } from "@/stores/auth";

export default {
  name: "MeetingInfo",
  async created() {
    await this.loadMeeting();
  },
  data() {
    return {
      meeting: null,
      isLoading: false
    };
  },
  computed: {
    ...mapState(useAuthStore, ["user"]),
    countUsers() {
      return this.meeting.users.length;
    },
    admin() {
      for (const user of this.meeting.users) {
        if (user.role === "admin") {
          return user.user;
        }
      }
    },
    isJoined() {
      for (const user of this.meeting.users) {
        if (user.user.id === this.user.id) {
          return true;
        }
      }
      return false;
    }
  },
  methods: {
    async loadMeeting() {
      this.isLoading = false;
      this.meeting = await getMeeting(this.$route.params.id);
      this.isLoading = true;
    },
    async addUser() {
      const meeting = {
        users: [
          {
            user_id: this.user.id,
            role: "participant"
          }
        ]
      };
      const responseStatus = await addUserToMeeting(meeting, this.$route.params.id);
      if (responseStatus < 400) {
        await this.loadMeeting();
      } else {
        console.log("error");
      }
    },
    async exitUser() {
      let participantId;
      for (const participant of this.meeting.users) {
        if (participant.user.id === this.user.id) {
          participantId = participant.id;
        }
      }
      const responseStatus = await deleteUserFromMeeting(participantId);
      if (responseStatus < 400) {
        await this.loadMeeting();
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