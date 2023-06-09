<script setup>
import { default as EnterButton } from "@/components/buttons/OrangeButton.vue";
import ExitButton from "@/components/buttons/ExitButton.vue";
import GroupMeetings from "@/containers/GroupMeetings.vue";
</script>

<template>
  <div class="content mx12 my12" v-if="isLoading">
    <w-flex wrap gap="2" class="justify-space-between">
      <div class="box ml12">
        <div class="title1 text-bold mb8">{{ group.title }}</div>
        <div class="body">
          <w-icon color="deep-orange pb1">mdi mdi-city</w-icon>
          {{ group.city }}
        </div>
        <div class="body mb8">
          <w-icon color="deep-orange pb1">mdi mdi-account-group</w-icon>
          Участников - {{ countUsers }}
        </div>
        <div class="categories-content mb8 ">
          <w-tag class="my1 mr2" color="deep-orange" outline
                 v-for="category in group.categories" :key="category.id">
            {{ category.title }}
          </w-tag>
        </div>
        <div class="title3">Про что группа?</div>
        <p class="body my4">{{ group.description }}</p>
      </div>
      <div class="box mr12">
        <EnterButton v-if="!isJoined" @click="addUser">Вступить в группу</EnterButton>
        <ExitButton v-else-if="isJoined && user.id!==admin.id"
                    question="Покинуть группу?"
                    @confirm="exitUser">Вы участник группы
        </ExitButton>
        <EnterButton disabled v-else>Вы администратор</EnterButton>
        <div class="title3 my8 text-right">Организатор</div>
        <router-link :to="{name: 'profile', params: {id: admin.id}}">
          <div class="body link text-right">{{ admin.name }}</div></router-link>
        <router-link :to="{name: 'chat', params: {id: admin.id}, query: {username: admin.name}}">
          <div class="body link text-right">Написать</div>
        </router-link>
        <GroupMeetings />
      </div>
    </w-flex>

  </div>
</template>

<script>
import { addUserToGroup, deleteUserFromGroup, getGroup } from "@/services/groupApi";
import { useAuthStore } from "@/stores/auth";
import { mapState } from "pinia";

export default {
  name: "GroupInfo",
  async created() {
    await this.loadGroup();
  },
  data() {
    return {
      group: null,
      isLoading: false
    };
  },
  computed: {
    ...mapState(useAuthStore, ["user"]),
    countUsers() {
      return this.group.users.length;
    },
    admin() {
      for (const user of this.group.users) {
        if (user.role === "admin") {
          return user.user;
        }
      }
    },
    isJoined() {
      for (const user of this.group.users) {
        if (user.user.id === this.user.id) {
          return true;
        }
      }
      return false;
    }

  },
  methods: {
    async loadGroup() {
      this.isLoading = false;
      this.group = await getGroup(this.$route.params.id);
      this.isLoading = true;
    },
    async addUser() {
      const group = {
        title: this.group.title,
        city: this.group.city,
        description: this.group.description,
        users: [
          {
            user_id: this.user.id,
            role: "participant"
          }
        ]
      };
      const responseStatus = await addUserToGroup(group, this.$route.params.id);
      if (responseStatus < 400) {
        await this.loadGroup();
      } else {
        console.log("error");
      }
    },
    async exitUser() {
      let groupParticipantId;
      for (const participant of this.group.users) {
        if (participant.user.id === this.user.id) {
          groupParticipantId = participant.id;
        }
      }
      const responseStatus = await deleteUserFromGroup(groupParticipantId);
      if (responseStatus < 400) {
        await this.loadGroup();
      }
    }
  }
};
</script>

<style scoped>
.categories-content {
  width: 500px;
}
.link {
  color: var(--color-text);
}

.link:hover, .link:focus, .link:active {
  color: var(--color-text-active);
}
</style>