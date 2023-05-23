<script setup>
import formatDate from "@/services/services"
</script>

<template>
  <div class="title2 pb8">Участник</div>
  <w-table
      :headers="table.headers"
      no-headers
      :items="table.meetingsParticipant"
      :loading="loading">
    <template #no-data>
      Вы не зарегистрировались для участия в каком-либо мероприятии
    </template>
    <template #item="{ item, index, classes }">
      <tr
          :class="{
        ...classes,
        'yellow-light6--bg': index % 2,
        'grey-light6--bg': !(index % 2)
      }"
          @click="select">
        <th :colspan="table.headers.length"></th>
        <td class="px12 py4" :colspan="table.headers.length">
          <div class="box">
            <w-flex class="align-center">
              <router-link :to="{name: 'meeting', params: {id: item.meeting}}" class="title3 link">
                {{ item.meeting_info.title }}
              </router-link>
              <w-tag v-if="item.meeting_info.is_online" class="ml6 pt10" width="4em"
                     height="1.5em">online
              </w-tag>
            </w-flex>
            <div class="mt2">{{ formatDate(item.meeting_info.date, "D MMMM YYYY г. H:mm") }}</div>
            <w-flex v-if="item.meeting_info.location" class="py2">
                <w-icon color="deep-orange mr2 pt1">mdi mdi-city</w-icon>
                <div>{{ item.meeting_info.location }}</div>
              </w-flex>
          </div>
        </td>
      </tr>
    </template>
  </w-table>
  <div class="title2 py8">Организатор</div>
  <w-table
      :headers="table.headers"
      no-headers
      :items="table.meetingsAdmin"
      :loading="loading">
    <template #no-data>
      Пока вы не организовали ни одной встречи
    </template>
    <template #item="{ item, index, classes }">
      <tr
          :class="{
        ...classes,
        'yellow-light6--bg': index % 2,
        'grey-light6--bg': !(index % 2)
      }">
        <th :colspan="table.headers.length"></th>
        <td :class="py4" :colspan="table.headers.length">
          <w-flex class="px12 py4 justify-space-between">
            <div class="box">
              <w-flex class="align-center">
                <router-link :to="{name: 'meeting', params: {id: item.meeting}}" class="title3 link">
                  {{ item.meeting_info.title }}
                </router-link>
                <w-tag v-if="item.meeting_info.is_online" class="ml6 pt10" width="4em"
                       height="1.5em">online
                </w-tag>
              </w-flex>
              <div class="mt2">{{ formatDate(item.meeting_info.date, "D MMMM YYYY г. H:mm") }}</div>
              <w-flex v-if="item.meeting_info.location" class="py2">
                <w-icon color="deep-orange mr2 pt1">mdi mdi-city</w-icon>
                <div>{{ item.meeting_info.location }}</div>
              </w-flex>
            </div>
            <div class="pt6">
              <w-icon color="indigo-deep6 mr6 pt1" md>mdi mdi-square-edit-outline</w-icon>
              <w-confirm color="indigo-deep6 mr2 pt1" icon="mdi mdi-trash-can"
                         question="Вы уверены, что хотите отменить встречу?"
                         cancel="Нет" confirm="Да" @confirm="delMeeting(item.meeting, index)">
                Delete
              </w-confirm>
            </div>
          </w-flex>
        </td>
      </tr>
    </template>
  </w-table>
</template>

<script>
import {mapState} from "pinia";
import {useAuthStore} from "@/stores/auth";
import {deleteMeeting, getUserMeeting} from "@/services/meetingApi";
import dayjs from "dayjs";
import 'dayjs/locale/ru'

export default {
  name: "UserMeetingsTable",
  async created() {
    await this.loadMeeting();
  },
  data: () => ({
    table: {
      headers: [
        {label: 'Название', key: 'title'},
        {label: 'Дата и время проведения', key: 'date'},
        {label: 'Онлайн', key: 'is_online'},
      ],
      meetingsParticipant: [],
      meetingsAdmin: [],
    },
    loading: true,
  }),
  computed: {
    ...mapState(useAuthStore, ['user']),
  },
  methods: {
    async loadMeeting() {
      this.loading = true;
      const response = await getUserMeeting(this.user.id)
      console.log(response)
      for (const meeting of response) {
        if (!meeting["meeting_info"]) {
          continue;
        }
        if (meeting['role'] === 'admin') {
          this.table.meetingsAdmin.push(meeting)
        } else {
          this.table.meetingsParticipant.push(meeting)
        }
      }
      this.loading = false;
    },
    async delMeeting(meeting_id, index) {
      const statusCode = await deleteMeeting(meeting_id);
      if (statusCode === 204) {
        this.table.meetingsAdmin.splice(index - 1, 1)
      }
    }
  }
}
</script>

<style scoped>
.link {
  color: var(--color-text);
}

.link:hover, .link:focus, .link:active {
  color: var(--color-text-active);
}
</style>