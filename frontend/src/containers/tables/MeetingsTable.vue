<script setup>
import formatDate from "@/services/services";
</script>

<template>
  <w-flex wrap gap="2" class="filter-panel my6">
    <w-input
      type="date"
      label="Дата проведения"
      v-model="filterDate"
      class="xs2"
      outline>
    </w-input>
    <w-select
      :items="selectItems"
      v-model="filterType"
      outline
      placeholder="Выберите тип мероприятия"
      label="Тип мероприятия"
      class="xs2"></w-select>
    <div class="xs6"></div>
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
        <td class="px12 py4" :colspan="table.headers.length">
          <div class="box">
            <w-flex class="align-center">
              <router-link :to="{name: 'meeting', params: {id: item.id}}" class="title3 link">
                {{ item.title }}
              </router-link>
              <w-tag v-if="item.is_online" class="ml6 pt10" width="4em"
                     height="1.5em">online
              </w-tag>
            </w-flex>
            <div class="mt2">{{ formatDate(item.date, "D MMMM YYYY г. H:mm") }}</div>

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
      selectItems: [
        { label: "Все", value: "all" },
        { label: "Только онлайн", value: true },
        { label: "Только очно", value: false }
      ],
      filterDate: "",
      filterType: "all",
      table: {
        headers: [
          { label: "Название", key: "title" },
          { label: "Дата и время проведения", key: "date" },
          { label: "Онлайн", key: "is_online" }
        ],
        meetings: []
      }
    };
  },
  props: ["searchData"],
  computed: {
    filterMeetings() {
      return this.table.meetings.filter((item) => this.getFilteredItem(item) === true);
    }
  },
  methods: {
    async loadMeetings() {
      const response = await getMeetings();
      this.table.meetings = response.data.results;
    },
    getFilteredItem(item) {
      const search = this.searchData.toLowerCase();
      let result = item.title.toLowerCase().includes(search) ||
        item.location.toLowerCase().includes(search);
      if (result) {
        if (this.filterDate) {
          const date = new Date(item.date).setHours(0, 0, 0, 0);
          const filterDate = new Date(this.filterDate).setHours(0, 0, 0, 0);
          result = date === filterDate;
        }
        if (result) {
          if (this.filterType !== "all") {
            result = item.is_online === this.filterType;
          }
        }
      }
      return result;
    }
  }
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