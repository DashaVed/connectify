<script setup>

import formatDate from "@/services/services";
</script>

<template>
  <w-flex wrap class="filter-panel my6">
     <w-input
    type="date"
    v-model="filterDate"
    class="xs2"
    outline
    :validators="[validators.dateValidate]">
  </w-input>
  </w-flex>

  <w-table
    :headers="table.headers"
    no-headers
    :items="filterMeetings"
    :loading="loading">
    <template #no-data>
      К сожалению, нет подходящих мероприятий. Попробуйте другой фильтр.
    </template>
    <template #item="{ item, index, classes }">
      <tr
        :class="{
        ...classes,
        'lime-light6--bg': index % 2 ,
        'grey-light6--bg': !(index % 2)
      }"
        @click="select">
        <th :colspan="table.headers.length"></th>
        <td class="pa4" :colspan="table.headers.length">
          <div class="box">
            <w-flex class="align-center">
              <router-link :to="{name: 'meeting', params: {id: item.id}}" class="title3 link">
                {{ item.title }}
              </router-link>
              <w-tag v-if="item.is_online" class="ml6 pt10" width="4em"
                     height="1.5em">online
              </w-tag>
            </w-flex>
            <div class="mt2">{{ formatDate(item.date, "D MMMM YYYY г. h:mm") }}</div>
          </div>
        </td>
      </tr>
    </template>
  </w-table>
</template>

<script>
import { getMeetings } from "@/services/meetingApi";

export default {
  name: "MeetingsTable",
  async created() {
    await this.loadMeetings();
  },
  data() {
    return {
      filterDate: "",
      table: {
        headers: [
          { label: "Название", key: "title" },
          { label: "Дата и время проведения", key: "date" },
          { label: "Онлайн", key: "is_online" }
        ],
        meetings: []
      },
      validators: {
                dateValidate: (value) => this.dateIsValid(value) === true ||
                    'Нeправильная дата. Она должна быть формата mm-dd-yyyy',
            }
    };
  },
  props: ["searchData"],
  computed: {
    filterMeetings() {
      return this.table.meetings.filter((item) =>
        item.title.toLowerCase().includes(this.searchData.toLowerCase()) ||
        item.location.toLowerCase().includes(this.searchData.toLowerCase())
      );
    }
  },
  methods: {
    async loadMeetings() {
      const response = await getMeetings();
      this.table.meetings = response.data.results;
    },
    dateIsValid(dateStr) {
      const regex = /^\d{4}-\d{2}-\d{2}$/;
      if (dateStr.match(regex) === null) {
        this.form.valid = false;
        return false;
      }
      return true;
    }
  }
};
</script>

<style scoped>

</style>