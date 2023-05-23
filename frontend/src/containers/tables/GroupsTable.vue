<script setup>

</script>

<template>
  <w-select
    :items="categories"
    v-model="filterCategories"
    outline
    multiple
    style="width:500px;"
    placeholder="Выберите тип мероприятия"
    label="Тип мероприятия"
    class="my6"></w-select>

  <w-table
    :headers="table.headers"
    no-headers
    :items="filterGroups"
    :loading="loading">
    <template #no-data>
      К сожалению, нет подходящих групп. Попробуйте другой фильтр.
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
        <td :class="py4" :colspan="table.headers.length">
          <w-flex class="px12 py4">
            <div class="box">
              <router-link :to="{name: 'group', params: {id: item.id}}" class="title3 link">
                {{ item.title }}
              </router-link>
              <w-flex class="py2">
                <w-icon color="deep-orange mr2 pt1">mdi mdi-city</w-icon>
                <div>{{ item.city }}</div>
              </w-flex>
            </div>
          </w-flex>
        </td>
      </tr>
    </template>
  </w-table>
</template>

<script>
import { getGroups } from "@/services/groupApi";
import { mapState } from "pinia";
import { useCategoriesStore } from "@/stores/categories";

export default {
  name: "GroupsTable",
  async created() {
    await this.loadGroups();
  },
  data() {
    return {
      filterCategories: [],
      table: {
        headers: [
          { label: "Название", key: "title" },
          { label: "Город", key: "city" }
        ],
        groups: []
      }
    };
  },
  props: ["searchData"],
  computed: {
    filterGroups() {
      return this.table.groups.filter((item) => this.getFilteredItem(item) === true);
    },
    ...mapState(useCategoriesStore, ["categories"])
  },
  methods: {
    async loadGroups() {
      const response = await getGroups();
      this.table.groups = response.data.results;
    },
    getFilteredItem(item) {
      const search = this.searchData.toLowerCase();
      let result = item.title.toLowerCase().includes(search) ||
        item.city.toLowerCase().includes(search);
      if (!result) {
        return result;
      }
      if (this.filterCategories) {
        for (const category of this.filterCategories) {
          result = item.categories.length > 0
          for (const group_category of item.categories) {
            result = category === group_category.id;
            if (result) {
              break;
            }
          }
          if (!result) {
            break;
          }
        }
      }
      return result;
    }
  }
};
</script>

<style scoped>

</style>