<script lang="ts" setup>
import { CompletePost } from '@/prisma/zod';
import { Method, modelRequest } from '@/common';

const props = defineProps<{
  post: CompletePost,
}>();

const emit = defineEmits<{
  (e: 'delete', id: number): void,
  (e: 'refresh'): void,
}>();

const hasTags = computed(() => props.post.tags && props.post.tags.length > 0);
</script>

<template>
  <Card
    class="shadow"
  >
    <template #header>
      <div class="flex text-gray-200 space-x-2 items-center">
        <div class="flex space-x-2 items-center">
          <span>{{ post.title }}</span>
          <span class="px-2 py-1 leading-none border border-gray-200 rounded-full">
            ID {{ post.id }}
          </span>
        </div>
        <span class="flex-1" />
        <span class="flex-1" />
        <div
          role="button"
          class="transition hover:text-red-300"
          @click.prevent="emit('delete', post.id)"
        >
          <i class="icon-close-o" />
        </div>
      </div>
    </template>
    <div class="max-w-150">
      Lorem
    </div>
    <div
      v-if="post.tags && post.tags.length > 0"
      class="flex text-gray-400 text-sm space-x-2"
    >
      <div
        v-if="hasTags"
        class="mt-2 flex space-x-2 items-center"
      >
        <span>Tags:</span>
        <div
          v-for="tag in post.tags"
          :key="tag.tag"
          class="px-2 py-1 border rounded-full"
        >
          {{ tag.tag }}
        </div>
      </div>
    </div>
  </Card>
</template>
