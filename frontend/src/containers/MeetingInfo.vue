<script setup>
import {default as EnterButton} from '@/components/buttons/OrangeButton.vue'
</script>

<template>
    <div class="content mx12 my12" v-if="isLoading">
        <w-flex wrap gap="2" class="justify-space-between">
            <div class="box ml12 xs6">
                <div class="title1 text-bold">{{ meeting.title }}</div>
                <div class="title3 mt4 mb8">
                    {{ formatDate }}
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
                    <EnterButton>Посетить мероприятие</EnterButton>
                </w-flex>
                <div class="title3 mt8  text-right">Группа</div>
                <w-card tile class="my3">
                    <div class="title4 mb4">{{ meeting.group.title }}</div>
                    <w-flex class="justify-space-between">
                        <div>
                            <w-icon color="deep-orange pb2">mdi mdi-city</w-icon>
                            {{ meeting.group.city }}
                        </div>
                        <router-link class="body link" :to="{name: 'group', params: {id: meeting.group.id}}">Посмотреть
                        </router-link>
                    </w-flex>
                </w-card>
                <div class="title3 my8 text-right">Организатор</div>
                <div class="body">{{ admin }}</div>
                <div class="title3 my8 text-right">Участники ({{ countUsers }})</div>
            </div>
        </w-flex>

    </div>
</template>

<script>
import {getMeeting} from "@/services/meetingApi";
import 'dayjs/locale/ru'
import dayjs from "dayjs";

export default {
    name: "MeetingInfo",
    async created() {
        await this.loadMeeting()
    },
    data() {
        return {
            meeting: null,
            isLoading: false,
        }
    },
    computed: {
        countUsers() {
            return this.meeting.users.length
        },
        admin() {
            for (const user of this.meeting.users) {
                if (user.role === "admin") {
                    return user.user
                }
            }
        },
        formatDate() {
            dayjs.locale('ru')
            return dayjs(this.meeting.date).format('ddd, D MMMM YYYY г. h:mm');
        }
    },
    methods: {
        async loadMeeting() {
            this.isLoading = false;
            this.meeting = await getMeeting(this.$route.params.id);
            this.isLoading = true;
        }
    }
}
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