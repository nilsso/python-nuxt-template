<script lang="ts" setup>
import { CompletePost } from '@/prisma/zod';

defineProps<{
  post: CompletePost,
}>();
</script>

<template>
  <Card
    class="shadow"
  >
    <template #header>
      <div class="flex text-gray-200 space-x-2 items-center">
        <span>{{ post.title }}</span>
        <span class="px-2 py-1 leading-none border border-gray-200 rounded-full">
          ID {{ post.id }}
        </span>
      </div>
    </template>
    <div
      v-if="post.tags && post.tags.length > 0"
      class="flex space-x-2"
    >
      <div
        v-for="tag in post.tags"
        :key="tag.tag"
      >
        {{ tag }}
      </div>
    </div>
    <div class="max-w-150">
      Lorem
    </div>
  </Card>
</template>
