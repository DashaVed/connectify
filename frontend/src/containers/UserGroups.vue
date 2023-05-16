<template>

    <w-flex column class="mx12">
        <div class="title3 text-center pt8 pb4">Группы, в которых я состою:</div>
        <w-card tile v-for="group in groups" :key="group.id"
                class="ma3">
            <div class="title4">{{ group.group_info.title }}</div>
            <w-flex class="justify-space-between">
                <div>
                    <w-icon color="deep-orange pb2">mdi mdi-city</w-icon>
                    {{ group.group_info.city }}</div>
                <router-link class="body link" :to="{name: 'group', params: {id: group.group}}">Посмотреть</router-link>
            </w-flex>
        </w-card>
    </w-flex>

</template>

<script>
import {getUserGroup} from "@/services/groupApi";

export default {
    name: "UserGroups",
    async created() {
        await this.loadGroup();
    },
    data() {
        return {
            groups: [],
        }
    },
    methods: {
        async loadGroup() {
            this.groups = await getUserGroup(this.$route.params.id)
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