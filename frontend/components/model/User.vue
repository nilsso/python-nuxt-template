<script lang="ts" setup>
import { CompleteUser } from '@/prisma/zod';

defineProps<{
  user: CompleteUser,
}>();
</script>

<template>
  <Card
    class="shadow"
    header-bg-color="bg-blue-500"
  >
    <template #header>
      <div class="flex text-blue-200 space-x-2 items-center">
        <span>{{ user.name }}</span>
        <span class="px-2 py-1 leading-none border border-blue-200 rounded-full">
          ID {{ user.id }}
        </span>
      </div>
    </template>
    <div>
      <div
        class="text-lg font-bold"
        role="button"
        :class="{
          'disabled cursor-default text-gray-400': !(user.posts && user.posts.length > 0),
        }"
      >
        Posts
      </div>
      <div
        v-if="user.posts && user.posts.length > 0"
        class="mt-2"
      >
        <ModelPost
          v-for="post in user.posts"
          :key="post.id"
          :post="post"
        />
      </div>
    </div>
  </Card>
</template>
