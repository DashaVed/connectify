<script setup>

</script>

<template>
  <div class="title2 pb8">Участник</div>
  <w-table
      :headers="table.headers"
      no-headers
      :items="table.groupsParticipant"
      :loading="loading">
    <template #no-data>
      Вы не состоите ни в одной из групп
    </template>
    <template #item="{ item, index, classes }">
      <tr
          :class="{
        ...classes,
        'yellow-light6--border': index,
        'body': index,
        'yellow-light6--bg': index % 2,
        'grey-light6--bg': !(index % 2)
      }"
          @click="select">
        <th :colspan="table.headers.length"></th>
        <td :class="py4" :colspan="table.headers.length">
          <w-flex class="px12 py4">
            <div class="box">
              <router-link :to="{name: 'group', params: {id: item.group}}" class="title3 link">
                {{ item.group_info.title }}
              </router-link>
              <w-flex class="py2">
                <w-icon color="deep-orange mr2 pt1">mdi mdi-city</w-icon>
                <div>{{ item.group_info.city }}</div>
              </w-flex>
            </div>
          </w-flex>
        </td>
      </tr>
    </template>
  </w-table>
  <div class="title2 py8">Организатор</div>
  <w-table
      :headers="table.headers"
      no-headers
      :items="table.groupsAdmin"
      :loading="loading">
    <template #no-data>
      <w-flex column>
        <div class="body mb4">Пока вы не организовали ни одной группы</div>
        <router-link :to="{name: 'create_group'}" class="link link-route">Создайте свою первую группу</router-link>
      </w-flex>

    </template>
    <template #item="{ item, index, classes }">
      <tr
          :class="{
        ...classes,
        'yellow-light6--border': index,
        'body': index,
        'yellow-light6--bg': index % 2,
        'grey-light6--bg': !(index % 2)
      }">
        <th :colspan="table.headers.length"></th>
        <td :class="py4" :colspan="table.headers.length">
          <w-flex class="px12 py4 justify-space-between">
            <div class="box">
              <router-link :to="{name: 'group', params: {id: item.group}}" class="title3 link">
                {{ item.group_info.title }}
              </router-link>
              <w-flex class="py2">
                <w-icon color="deep-orange mr2 pt1">mdi mdi-city</w-icon>
                <div>{{ item.group_info.city }}</div>
              </w-flex>
            </div>
            <div class="pt6">
              <router-link :to="{name: 'create_meetings', query: {group: item.group}}" class="body link mr12">
                Добавить мероприятие
              </router-link>
              <w-icon color="indigo-deep6 mr6 pt1" md>mdi mdi-square-edit-outline</w-icon>
              <w-confirm color="indigo-deep6 mr2 pt1" icon="mdi mdi-trash-can"
                         question="Вы уверены, что хотите удалить группу?"
                         cancel="Нет" confirm="Да" @confirm="delGroup(item.group, index)">
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
import {deleteGroup, getUserGroup} from "@/services/groupApi";
import {useAuthStore} from "@/stores/auth";
import {mapState} from "pinia";

export default {
  name: "UserGroupsTable",
  async created() {
    await this.loadGroup();
  },
  data: () => ({
    table: {
      headers: [
        {label: 'Название', key: 'title'},
        {label: 'Город', key: 'city'},
      ],
      groupsParticipant: [],
      groupsAdmin: [],
    },
    loading: true,
  }),
  computed: {
    ...mapState(useAuthStore, ['user']),
  },
  methods: {
    async loadGroup() {
      this.loading = true;
      const response = await getUserGroup(this.user.id)
      for (const group of response) {
        if (group['role'] === 'admin') {
          this.table.groupsAdmin.push(group)
        } else {
          this.table.groupsParticipant.push(group)
        }
      }
      this.loading = false;
    },
    async delGroup(group_id, index) {
      const statusCode = await deleteGroup(group_id);
      if (statusCode === 204) {
        this.table.groupsAdmin.splice(index - 1, 1)
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

.link-route {
  text-decoration: underline;
}
</style>